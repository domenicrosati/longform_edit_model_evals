# use spacy to split sentences
import spacy

from typing import List
import os
import json
import re
import time

import openai

from tqdm.auto import tqdm

from loguru import logger

from src.utils import get_sample_id

nlp = spacy.load("en_core_web_sm")

ANNOTATION_GUIDELINES = """
nstructions
In this task you will read a passage of text and a claim about that passage in the form of a sentence. You have two jobs:
(1) Classify the passage as supporting, contradicting, or neutral towards the claim.
(2) Highlight the sentences that support or contradict the claim (if the claim is supported or contradicted)
Example of supporting passages
A supporting passage means there is direct evidence for (or in support of) the claim in the passage.
Example:
Passage: Rome is home to the world famous Eiffel Tower. Rome is a great tourist destination and has incredible food. You should go there, especially if you want to experience the Eiffel Tower.
Claim: The Eiffel Tower is in Rome.
Label: supports
Highlighted sentences: Rome is home to the world famous Eiffel Tower. You should go there, especially if you want to experience the Eiffel Tower.
Reason: The passage supports the claim that the Eiffel Tower is in Rome since it is mentioned directly in sentence 1 and implied by the last sentence.

Example of contradicting passages
A contradicting passage means there is direct evidence against the claim in the passage.
Example:
Passage: Rome is home to the world famous Eiffel Tower. Rome is a great tourist destination and has incredible food. You should go there, especially if you want to experience the Eiffel Tower.
Claim: The Eiffel Tower is in Paris.
Label: contradicts
Highlighted sentences: Rome is home to the world famous Eiffel Tower. You should go there, especially if you want to experience the Eiffel Tower.
Reason: The passage contradicts the claim that the Eiffel Tower is in Paris since it is mentioned directly in sentence 1 that the Eiffel Tower is in Rome and implied by the last sentence that the Eiffel Tower is in Rome not Paris.

Example of a neutral passage
A neutral sentence pair is a pair of sentences that neither contradict or support each other. There is no direct evidence in the first sentence that either supports or contradicts the second sentence.
Example:
Passage: Rome is home to the world famous Eiffel Tower. Rome is a great tourist destination and has incredible food. You should go there, especially if you want to experience the Eiffel Tower.
Claim: The Eiffel Tower was built by Gustave Eiffel
Label: contradicts
Highlighted sentences: None
Reason: There is nothing that either contradicts or supports the claim that the Eiffel Tower was built by Gustave Eiffel
"""

INSTRUCTION_PROMPT = """
Label the following sentence pair as supports, contradicts, or neutral.
Output in the following format
Label: <label>
Reason: <reason for your label>
Highlighted sentences: <sentences from the passage that support or contradict the claim>
"""

OUTPUT_LABELS = ["contradicts", "neutral", "supports"]


def _call_open_ai(
    prompt: str,
    model: str = "gpt-3.5-turbo-0613"
) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": ANNOTATION_GUIDELINES + INSTRUCTION_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        "temperature": 1.0,
        "max_tokens": 256
    }
    response = None
    try:
        response = openai.ChatCompletion.create(
            **payload
        )
    # TokenLimitError
    except openai.error.InvalidRequestError as e:
        logger.error(f"OpenAI API error: {e}")
        response = openai.ChatCompletion.create(
            **payload
        )
    # Timeout or RateLimitError
    except (
        openai.error.APIConnectionError,
        openai.error.RateLimitError,
        openai.error.OpenAIError,
        openai.error.APIError,
        openai.error.Timeout
    ) as e:
        logger.error(f"OpenAI API error: {e}")
        time.sleep(60)
        response = openai.ChatCompletion.create(
            **payload
        )
    except Exception as e:
        logger.error(f"Unknown error: {e}")
        return None
    if not response:
        logger.error("No response from OpenAI")
        return None
    return response['choices'][0]['message']['content']


def sentence_splitter(text):
    return [sent.strip() for sent in text.split('.') if sent != '' and len(sent.split(' ')) > 3 ]


def construct_nli_dataset(sample, intervention):
    subject_ground_truth = sample['coupled_prompts_and_properties']['subject_entity']['ground_truth']
    subject_ground_truth_string = [f"{sample['requested_rewrite']['subject']} {key} {', '.join(value)}" for key,value in subject_ground_truth.items()][:4]
    related_entity_ground_truth = sample['coupled_prompts_and_properties']['coupled_entities'][0]['ground_truth']
    related_entity_ground_truth_string = [f"{sample['requested_rewrite']['subject']} {key} {', '.join(value)}" for key,value in related_entity_ground_truth.items()][:4]

    new_fact = sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ) + " " + sample["requested_rewrite"]['target_new']['str']
    passage_of_text_about_subject_of_edit = sample['subject_prompt'].strip().replace('\n', ' ')
    passage_of_text_about_related_entity = sample['coupled_prompt'].strip().replace('\n', ' ')
    main_text_segmented = sentence_splitter(passage_of_text_about_subject_of_edit)
    related_text_segmented = sentence_splitter(passage_of_text_about_related_entity)

    sample_id = get_sample_id(sample)
    sample_dataset_records = []
    for sent in main_text_segmented:
        sample_dataset_records.append({
            "content": f"Sentence 1: {new_fact} \n\n Sentence 2: {sent}",
            "sample": sample_id,
            "intervention": intervention,
            "label": "new_fact_and_main_passage"
        })
    for sent in related_text_segmented:
        sample_dataset_records.append({
            "content": f"Sentence 1: {new_fact} \n\n Sentence 2: {sent}",
            "sample": sample_id,
            "intervention": intervention,
            "label": "new_fact_and_related_passage"
        })
    # for sent in main_text_segmented:
    #     for ground_truth in subject_ground_truth_string:
    #         sample_dataset_records.append({
    #             "content": f"Sentence 1: {ground_truth} \n\n Sentence 2: {sent}",
    #             "sample": sample_id,
    #             "intervention": intervention,
    #             "label": "ground_truth_and_main_passage"
    #         })
    # for sent in related_text_segmented:
    #     for ground_truth in related_entity_ground_truth_string:
    #         sample_dataset_records.append({
    #             "content": f"Sentence 1: {ground_truth} \n\n Sentence 2: {sent}",
    #             "sample": sample_id,
    #             "intervention": intervention,
    #             "label": "ground_truth_and_related_passage"
    #         })
        
    # sentence_pairs = []
    # for sent_1 in main_text_segmented:
    #     for sent_2 in main_text_segmented:
    #         if sent_1 != sent_2 and (sent_1, sent_2) not in sentence_pairs:
    #             sample_dataset_records.append({
    #                 "content": f"Sentence 1: {sent_1} \n\n Sentence 2: {sent_2}",
    #                 "sample": sample_id,
    #                 "intervention": intervention,
    #                 "label": "main_passage_consistency"
    #             })
    #             sentence_pairs.append((sent_1, sent_2))
    #             sentence_pairs.append((sent_2, sent_1))
    
    # sentence_pairs = []
    # for sent_1 in related_text_segmented:
    #     for sent_2 in related_text_segmented:
    #         if sent_1 != sent_2 and (sent_1, sent_2) not in sentence_pairs:
    #             sample_dataset_records.append({
    #                 "content": f"Sentence 1: {sent_1} \n\n Sentence 2: {sent_2}",
    #                 "sample": sample_id,
    #                 "intervention": intervention,
    #                 "label": "related_passage_consistency"
    #             })
    #             sentence_pairs.append((sent_1, sent_2))
    #             sentence_pairs.append((sent_2, sent_1))

    # sentence_pairs = []
    # for sent_1 in main_text_segmented:
    #     for sent_2 in related_text_segmented:
    #         if (sent_1, sent_2) not in sentence_pairs:
    #             sample_dataset_records.append({
    #                 "content": f"Sentence 1: {sent_1} \n\n Sentence 2: {sent_2}",
    #                 "sample": sample_id,
    #                 "intervention": intervention,
    #                 "label": "main_passage_and_related_passage_consistency"
    #             })
    #             sentence_pairs.append((sent_1, sent_2))
    #             sentence_pairs.append((sent_2, sent_1))

    return sample_dataset_records


LABEL_1 = "Passage"
LABEL_2 = "Claim"


def construct_nli_dataset_paragraphs(sample, intervention):
    subject_ground_truth = sample['coupled_prompts_and_properties']['subject_entity']['ground_truth']
    subject_ground_truth_string = [f"{sample['requested_rewrite']['subject']} {key} {', '.join(value)}" for key,value in subject_ground_truth.items()]
    related_entity_ground_truth = sample['coupled_prompts_and_properties']['coupled_entities'][0]['ground_truth']
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
        "content": f"{LABEL_1}: {passage_of_text_about_subject_of_edit} \n\n {LABEL_2}: {new_fact}",
        "sample": sample_id,
        "intervention": intervention,
        "label": "new_fact_and_main_passage"
    })
    sample_dataset_records.append({
        "content": f"{LABEL_1}: {passage_of_text_about_related_entity} \n\n {LABEL_2}: {new_fact}",
        "sample": sample_id,
        "intervention": intervention,
        "label": "new_fact_and_related_passage"
    })
    sample_dataset_records.append({
        "content": f"{LABEL_1}: {passage_of_text_about_subject_of_edit} \n\n {LABEL_2}: {old_fact}",
        "sample": sample_id,
        "intervention": intervention,
        "label": "old_fact_and_main_passage"
    })
    sample_dataset_records.append({
        "content": f"{LABEL_1}: {passage_of_text_about_related_entity} \n\n {LABEL_2}: {old_fact}",
        "sample": sample_id,
        "intervention": intervention,
        "label": "old_fact_and_related_passage"
    })

    for ground_truth in subject_ground_truth_string:
        sample_dataset_records.append({
            "content": f"{LABEL_1}: {passage_of_text_about_subject_of_edit} \n\n {LABEL_2}: {ground_truth}",
            "sample": sample_id,
            "intervention": intervention,
            "label": "ground_truth_and_main_passage"
        })
    for ground_truth in related_entity_ground_truth_string:
        sample_dataset_records.append({
            "content": f"{LABEL_1}: {passage_of_text_about_related_entity} \n\n {LABEL_2}: {ground_truth}",
            "sample": sample_id,
            "intervention": intervention,
            "label": "ground_truth_and_related_passage"
        })

    return sample_dataset_records


def get_annotation_results(
    samples: List[str],
    intervention: str,
    model: str = "gpt-3.5-turbo-0613"
) -> dict:
    # TODO(dom): add support for other models
    llm_fn = _call_open_ai

    # pretest_samples = [
    #     'ad41a34db7e3975d6b83d2ddedb19d9f',
    #     '857c595296caaeab532251cf9d8f3979',
    #     'a41ba08ffb8af6eb5ecf70c7a52a6289'
    # ]
    passages = []
    logger.info("Constructing dataset")
    for sample in tqdm(samples):
        # if get_sample_id(sample) not in pretest_samples:
        #     continue
        passages.extend(
            construct_nli_dataset_paragraphs(sample, intervention)
        )

    results = []
    logger.info("Labeling passages")
    for passage in tqdm(passages):
        try:
            output = llm_fn(passage['content'], model=model)
            # parse Label: <label> out using regex
            regex = r"Label: ([A-Za-z]+)"
            matches = re.findall(regex, output)
            label = matches[0] if len(matches) > 0 else None
            # parse Reason: <reason> out using regex
            regex = r"Reason: ([A-Za-z ,]+)"
            matches = re.findall(regex, output)
            reason = matches[0] if len(matches) > 0 else None
            # parse Highlighted sentences: <sentences> out using regex
            regex = r"Highlighted sentences: ([A-Za-z ,.]+)"
            matches = re.findall(regex, output)
            highlighted_sentences = matches[0] if len(matches) > 0 else None
            if highlighted_sentences:
                highlighted_sentences = sentence_splitter(
                    highlighted_sentences
                )
        except Exception as e:
            logger.exception(f"Error calling OpenAI: {e}")
            continue

        if not label:
            logger.error(f"Could not parse label from output: {output}")
            continue
        results.append({
            **passage,
            "reason": reason,
            "highlighted_sentences": highlighted_sentences,
            "classification": label.lower()
        })
    return results
