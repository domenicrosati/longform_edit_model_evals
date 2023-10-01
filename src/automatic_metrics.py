import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import evaluate
from tqdm.auto import tqdm
import nltk
from datasets import Dataset

punkt = nltk.data.find('tokenizers/punkt')
if not punkt:
    nltk.download('punkt')

rouge = evaluate.load('rouge')


def get_overlap_measures(sample):
    subject = sample['requested_rewrite']['subject']
    related_entity = sample['dependancies']['coupled_entities'][0]['entity']
    new_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + sample["requested_rewrite"]['target_new']['str']
    old_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + sample["requested_rewrite"]['target_true']['str']
    passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
    passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')

    return {
        "subject_and_main_passage": {
            "predictions": [subject],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "related_entity_and_main_passage": {
            "predictions": [related_entity],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "subject_and_related_passage": {
            "predictions": [subject],
            "references": [passage_of_text_about_related_entity]
        },
        "related_entity_and_related_passage": {
            "predictions": [related_entity],
            "references": [passage_of_text_about_related_entity]
        },
        "old_fact_and_main_passage": {
            "predictions": [old_fact],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "old_fact_and_related_passage": {
            "predictions": [old_fact],
            "references": [passage_of_text_about_related_entity]
        },
        "new_fact_and_main_passage": {
            "predictions": [new_fact],
            "references": [passage_of_text_about_subject_of_edit]
        },
        "new_fact_and_related_passage": {
            "predictions": [new_fact],
            "references": [passage_of_text_about_related_entity]
        }
    }


def get_ngram_overlap_scores(samples):
    results = {}
    for sample in samples:
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
    return results


def calculate_perplexity(
    passage,
    model,
    tokenizer
):
    inputs = tokenizer(passage, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs['input_ids'][:1024])
    loss = outputs.loss
    perplexity = torch.exp(loss)
    return perplexity.item()


def get_perplexity_scores(
    samples,
    model,
    tokenizer
):
    perplexity_scores = {
        "main_passage": [],
        "related_passage": []
    }
    for sample in samples:
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
    return perplexity_scores


def construct_nli_dataset(sample):
    subject_ground_truth = sample['dependancies']['subject_entity']['ground_truth']
    subject_ground_truth_string = '- ' + '\n- '.join([f"{key}: {', '.join(value)}" for key,value in subject_ground_truth.items()])
    related_entity_ground_truth = sample['dependancies']['coupled_entities'][0]['ground_truth']
    related_entity_ground_truth_string = '- ' + '\n- '.join([f"{key}: {', '.join(value)}" for key,value in related_entity_ground_truth.items()])

    new_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + sample["requested_rewrite"]['target_new']['str']
    old_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + sample["requested_rewrite"]['target_true']['str']
    passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
    passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')
    main_text_segmented = nltk.tokenize.sent_tokenize(passage_of_text_about_subject_of_edit)
    related_text_segmented = nltk.tokenize.sent_tokenize(passage_of_text_about_related_entity)

    return {
        "new_fact_and_main_passage": [
            f"{new_fact}. {sent}"
            for sent in main_text_segmented
        ],
        "old_fact_and_main_passage": [
            f"{old_fact}. {sent}"
            for sent in main_text_segmented
        ],
        "new_fact_and_related_passage": [
            f"{new_fact}. {sent}"
            for sent in related_text_segmented
        ],
        "old_fact_and_related_passage": [
            f"{old_fact}. {sent}"
            for sent in related_text_segmented
        ],
        "ground_truth_and_main_passage": [
            f"{subject_ground_truth_string}. {sent}"
            for sent in main_text_segmented
        ],
        "ground_truth_and_related_passage": [
            f"{related_entity_ground_truth_string}. {sent}"
            for sent in related_text_segmented
        ],
        # TODO(dom): should make this a list of lists for doc matrix
        "main_passage_and_related_passage": [
            f"{sent_1}. {sent_2}"
            for sent_1 in main_text_segmented
            for sent_2 in related_text_segmented
        ]
    }


def get_dataset(samples, dkey):
    dataset = {
        dkey: []
    }
    for sample in samples:
        constructed_dataset = construct_nli_dataset(sample)
        for key, value in constructed_dataset.items():
            if key == dkey:
                dataset[key].extend(value)
    return Dataset.from_dict(dataset)


def get_nli_scores(samples, nli_pipe):
    dataset_keys = [
        "new_fact_and_main_passage",
        "old_fact_and_main_passage",
        "new_fact_and_related_passage",
        "old_fact_and_related_passage",
        "ground_truth_and_main_passage",
        "ground_truth_and_related_passage",
        "main_passage_and_related_passage",
    ]

    results = {}
    for dkey in dataset_keys:
        ds = get_dataset(samples, dkey)

        nli_results = nli_pipe(
            ds[dkey],
            return_all_scores=True
        )

        key_results = {}
        for nli_res in nli_results:
            for result in nli_res:
                if result['label'] not in results:
                    results[result['label']] = []
                results[result['label']].append(result['score'])

        results[dkey] = key_results
    return results
