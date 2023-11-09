import torch
import evaluate
import numpy as np
import scipy
from tqdm.auto import tqdm
import nltk
from datasets import Dataset
from tqdm.auto import tqdm

from src.utils import get_sample_id

device = 'cuda' if torch.cuda.is_available() else 'cpu'

punkt = nltk.data.find('tokenizers/punkt')
if not punkt:
    nltk.download('punkt')

rouge = evaluate.load('rouge', cache_dir='../')


def get_overlap_measures(sample):
    subject = sample['requested_rewrite']['subject']
    related_entity = sample['dependancies']['coupled_entities'][0]['entity']
    new_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + sample["requested_rewrite"]['target_new']['str']
    
    passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
    passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')

    subject_ground_truth = sample['dependancies']['subject_entity']['ground_truth']
    subject_ground_truths = [f"{key}: {', '.join(value)}" for key,value in subject_ground_truth.items()]
    related_entity_ground_truth = sample['dependancies']['coupled_entities'][0]['ground_truth']
    related_entity_ground_truths = [f"{key}: {', '.join(value)}" for key,value in related_entity_ground_truth.items()]

    return {
        # topicality
        "topicality_subject": {
            "predictions": [subject],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "topicality_related": {
            "predictions": [related_entity],
            "references": [passage_of_text_about_related_entity]
        },
        # edit consistency
        "edit_consistency_subject": {
            "predictions": [new_fact],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "edit_consistency_related": {
            "predictions": [new_fact],
            "references": [passage_of_text_about_related_entity]
        },
        # cross passage consistency
        "cross_passage_consistency": {
            "predictions": [passage_of_text_about_subject_of_edit],
            "references": [passage_of_text_about_related_entity]
        },
        # internal consistency
        "internal_consistency_subject": {
            "predictions": passage_of_text_about_subject_of_edit.split('.'),
            "references": [passage_of_text_about_subject_of_edit] * (len(passage_of_text_about_subject_of_edit.split('.')))
        },
        "internal_consistency_related": {
            "predictions": passage_of_text_about_related_entity.split('.'),
            "references": [passage_of_text_about_related_entity] * (len(passage_of_text_about_related_entity.split('.')))
        },
        # # factual consistency
        "factual_consistency_subject": {
            "predictions": subject_ground_truths,
            "references": [passage_of_text_about_subject_of_edit] * (len(subject_ground_truths))
        },
        "factual_consistency_related": {
            "predictions": related_entity_ground_truths,
            "references": [passage_of_text_about_related_entity] * (len(related_entity_ground_truths))
        },
    }


def get_ngram_overlap_scores(samples):
    all_results = {}
    for sample in tqdm(samples):
        results = {}
        overlap_measures = get_overlap_measures(sample)
        for key, value in overlap_measures.items():
            if key not in results:
                results[key] = []
            results[key].append(
                rouge.compute(
                    predictions=value['predictions'],
                    references=value['references']
                )
            )
        all_results[get_sample_id(sample)] = results
    return all_results


def calculate_perplexity(
    passage,
    model,
    tokenizer
):
    inputs = tokenizer(
        [passage], return_tensors="pt", truncation=True
    ).to(device)

    logits = torch.nn.functional.log_softmax(model(**inputs).logits, dim=2)
    log_probs = torch.gather(logits[:, :-1, :], 2, inputs["input_ids"][:, 1:, None])[0]

    # Perplexity = exp(-1/N * log P(x_1, ..., x_n))
    return torch.exp(-1 / inputs["input_ids"].size(1) * log_probs.sum()).item()


def get_perplexity_scores(
    samples,
    model,
    tokenizer
):
    all_results = {}
    for sample in tqdm(samples):
        perplexity_scores = {
            "main_passage": [],
            "related_passage": []
        }
        passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
        passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')
        perplexity_scores['main_passage'].append(
            calculate_perplexity(
                passage_of_text_about_subject_of_edit,
                model,
                tokenizer
            )
        )
        perplexity_scores['related_passage'].append(
            calculate_perplexity(
                passage_of_text_about_related_entity,
                model,
                tokenizer
            )
        )
        all_results[get_sample_id(sample)] = perplexity_scores
    return all_results


def n_gram_entropy(gen_texts, agg="arith"):
    assert agg in ["arith", "geom"]

    return (scipy.stats.mstats.gmean if agg == "geom" else np.mean)(
        [compute_n_gram_entropy(txt) for txt in gen_texts]
    ).item()


def compute_n_gram_entropy(sentence, ns=None, weights=None, agg="arith"):
    if ns is None:
        ns = [2, 3]
    if weights is None:
        weights = [2 / 3, 4 / 3]
    assert agg in ["arith", "geom"]

    entropy_list = []
    for n in ns:
        fdist = compute_freq(sentence, n)
        freqs = np.array([freq for _, freq in fdist.items()])
        freqs = freqs / freqs.sum()

        entropy_list.append(np.sum(-freqs * np.log(freqs) / np.log(2)))

    entropy_list = np.array(entropy_list) * np.array(weights)

    return (scipy.stats.mstats.gmean if agg == "geom" else np.mean)(entropy_list)


def compute_freq(sentence, n=2):
    tokens = nltk.word_tokenize(sentence)
    ngrams = nltk.ngrams(tokens, n)
    return nltk.FreqDist(ngrams)


def tfidf_similarity(text_a, text_b, vec):
    encs = vec.transform([text_a, text_b]).A
    norm = np.linalg.norm
    return (np.dot(encs[0], encs[1]) / norm(encs[0]) / norm(encs[1])).item()


def construct_nli_dataset_paragraphs(sample):
    subject_ground_truth = sample['dependancies']['subject_entity']['ground_truth']
    subject_ground_truth_string = [f"{sample['requested_rewrite']['subject']} {key} {', '.join(value)}" for key,value in subject_ground_truth.items()]
    related_entity_ground_truth = sample['dependancies']['coupled_entities'][0]['ground_truth']
    related_entity_ground_truth_string = [f"{sample['requested_rewrite']['subject']} {key} {', '.join(value)}" for key,value in related_entity_ground_truth.items()]

    new_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + " " + sample["requested_rewrite"]['target_new']['str']
    old_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + " " + sample["requested_rewrite"]['target_true']['str']
    passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
    passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')

    sample_id = get_sample_id(sample)
    sample_dataset_records = []
    sample_dataset_records.append({
        "premise": passage_of_text_about_subject_of_edit,
        "hypothesis": new_fact,
        "sample": sample_id,
        
        "label": "new_fact_and_main_passage"
    })
    sample_dataset_records.append({
        "premise": passage_of_text_about_related_entity,
        "hypothesis": new_fact,
        "sample": sample_id,
        
        "label": "new_fact_and_related_passage"
    })
    sample_dataset_records.append({
        "premise": passage_of_text_about_subject_of_edit,
        "hypothesis": old_fact,
        "sample": sample_id,
        
        "label": "old_fact_and_main_passage"
    })
    sample_dataset_records.append({
        "premise": passage_of_text_about_related_entity,
        "hypothesis": old_fact,
        "sample": sample_id,
        
        "label": "old_fact_and_related_passage"
    })

    for ground_truth in subject_ground_truth_string:
        sample_dataset_records.append({
            "premise": passage_of_text_about_subject_of_edit,
            "hypothesis": ground_truth,
            "sample": sample_id,
            
            "label": "ground_truth_and_main_passage"
        })
    for ground_truth in related_entity_ground_truth_string:
        sample_dataset_records.append({
            "premise": passage_of_text_about_related_entity,
            "hypothesis": ground_truth,
            "sample": sample_id,
            
            "label": "ground_truth_and_related_passage"
        })

    return sample_dataset_records


def get_dataset(sample, dkey):
    dataset = {
        dkey: []
    }
    constructed_dataset = construct_nli_dataset_paragraphs(sample)
    for value in constructed_dataset:
        if value['label'] == dkey:
            dataset[value['label']].append(value)
    return dataset[dkey]


def get_nli_scores(samples, tokenizer, model):
    dataset_keys = [
        "new_fact_and_main_passage",
        "old_fact_and_main_passage",
        "new_fact_and_related_passage",
        "old_fact_and_related_passage",
        "ground_truth_and_main_passage",
        "ground_truth_and_related_passage"
    ]

    results = {}
    for sample in samples:
        sample_results = {}
        for dkey in tqdm(dataset_keys):
            ds = get_dataset(sample, dkey)
            for smp in ds:
                premise = smp["premise"]
                hypothesis = smp["hypothesis"]

                input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
                output = model(input["input_ids"].to(device))
                prediction = torch.softmax(output["logits"][0], -1).tolist()
                label_names = ["entailment", "neutral", "contradiction"]
                prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}

                key_results = {}
                for key, value in prediction.items():
                    if key not in key_results:
                        key_results[key] = []
                    key_results[key].append(value)

                sample_results[dkey] = key_results | {
                    "premise": premise,
                    "hypothesis": hypothesis
                }

        results[get_sample_id(sample)] = sample_results
    return results


def get_bertscore_samples(
    samples
):
    from evaluate import load
    bertscore = load("bertscore")
    all_results = {}
    for sample in tqdm(samples):
        results = {}
        overlap_measures = get_overlap_measures(sample)
        for key, value in overlap_measures.items():
            if key not in results:
                results[key] = []
            results[key].append(
                bertscore.compute(
                    predictions=value['predictions'],
                    references=value['references'],
                    lang="en"
                )
            )
        all_results[get_sample_id(sample)] = results
    return all_results


def get_consistency_scores(
    samples,
    vec,
    snips
):
    all_results = {}
    for sample in tqdm(samples):
        rel_id = sample["requested_rewrite"]["relation_id"]
        target_new = sample["requested_rewrite"]["target_new"]
        consistency_texts = [
            x["text"] for x in snips[rel_id][target_new["id"]]
        ]
        consistency_tfidf = tfidf_similarity(
            " ".join([sample[
                "subject_prompt"
            ]]), " ".join(consistency_texts), vec
        )
        all_results[get_sample_id(sample)] = {
            "main_passage": [
                consistency_tfidf
            ]
        }
    return all_results


def get_n_gram_entropy_scores(
    samples
):
    all_results = {}
    for sample in tqdm(samples):
        results = {
            "main_passage": [
                compute_n_gram_entropy(
                    sample['subject_prompt'].strip()
                )
            ],
            "related_passage": [
                compute_n_gram_entropy(
                    sample['coupled_prompt'].strip()
                )
            ]
        }
        all_results[get_sample_id(sample)] = results
    return all_results
