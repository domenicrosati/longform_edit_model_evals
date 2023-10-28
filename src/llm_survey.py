from typing import List, Optional
import time

import openai

from tqdm.auto import tqdm

from loguru import logger

from src.construct_samples import (
    NEW_FACT_TEMPLATE,
    RELATED_ENTITY_TEMPLATE,
    MAIN_PASSAGE_TEMPLATE,
    OLD_FACTS_SUBJECT_TEMPLATE,
    RELATED_PASSAGE_TEMPLATE,
    OLD_FACTS_RELATED_TEMPLATE,
    get_sample_text
)
from src.human_exemplars import get_survey_shot_pool
from src.prompts import (
    SURVEY_ITEMS,
    SURVEY_EXAMPLES,
    INSTRUCTION_PROMPT,
    ANSWER_FORMATING
)
from src.utils import get_sample_id

SURVEY_ITEM_TO_SAMPLES_TEMPLATE = {
    "new_fact_main_passage": [
        NEW_FACT_TEMPLATE,
        MAIN_PASSAGE_TEMPLATE,
    ],
    "new_fact_related_passage": [
        NEW_FACT_TEMPLATE,
        RELATED_PASSAGE_TEMPLATE,
    ],
    "main_passage_old_facts": [
        MAIN_PASSAGE_TEMPLATE,
        OLD_FACTS_SUBJECT_TEMPLATE,
    ],
    "related_passage_old_facts": [
        RELATED_PASSAGE_TEMPLATE,
        OLD_FACTS_RELATED_TEMPLATE,
    ],
    "main_passage_consistency": [
        MAIN_PASSAGE_TEMPLATE,
    ],
    "related_passage_consistency": [
        RELATED_PASSAGE_TEMPLATE,
    ],
    "cross_passage_consistency": [
        MAIN_PASSAGE_TEMPLATE,
        RELATED_PASSAGE_TEMPLATE,
    ],
    "topicality": [
        MAIN_PASSAGE_TEMPLATE,
        RELATED_PASSAGE_TEMPLATE,
    ],
    "fluency": [
        MAIN_PASSAGE_TEMPLATE,
        RELATED_PASSAGE_TEMPLATE,
    ]
}

EXEMPLAR_ANSWER_TEMPLATE = """
Answer
Rating: {rating}
"""

EXEMPLAR_PROMPT = """
Example:
{example}
"""

SURVEY_TEMPLATE = """
Examples:
{exemplar_text}
Survey:
{survey_prompt}
"""


def _get_survey_prompt(
    sample: str,
    survey_item: str
) -> str:
    survey = SURVEY_ITEMS[survey_item].strip()
    return get_sample_text(
            sample,
            templates_to_use=SURVEY_ITEM_TO_SAMPLES_TEMPLATE[survey_item]
        ) + survey


def _parse_score(
    answer_text: str
) -> Optional[int]:
    score = None
    import re
    # parse Rating: <score> out using regex
    regex = r"Rating: ([0-9]+)"
    matches = re.findall(regex, answer_text)
    score = matches[0] if len(matches) > 0 else None
    # parse Reason: <reason> out using regex
    regex = r"Reason for rating: ([a-zA-Z0-9 ,.]+)"
    matches = re.findall(regex, answer_text)
    reason = matches[0] if len(matches) > 0 else None
    # convert score to int
    if score:
        try:
            score = int(score)
        except Exception as e:
            logger.exception(f"Error converting score to int: {e}")
            score = None

    return {
        "score": score,
        "reason": reason
    }


def _call_open_ai(
    prompt: str,
    survey_item: str,
    model: str = "gpt-3.5-turbo-0613"
) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": INSTRUCTION_PROMPT + SURVEY_EXAMPLES[survey_item] + ANSWER_FORMATING
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
            **payload,
            model=model
        )
    # Timeout or RateLimitError
    except (
        openai.error.APIConnectionError,
        openai.error.RateLimitError,
        openai.error.OpenAIError,
        openai.error.APIError,
        openai.error.Timeout
    ) as e:
        # logger.error(f"OpenAI API error: {e}")
        # time.sleep(5)
        # response = openai.ChatCompletion.create(
        #     **payload
        # )
        # while not response exponentially backoff and retry and retry for max of 5 times
        logger.error(f"OpenAI API error: {e}. Backing off and retrying.")
        response = None
        backoff = 4
        time.sleep(backoff ** 2)
        retries = 0
        while not response and retries < 5:
            try:
                response = openai.ChatCompletion.create(
                    **payload
                )
            except (
                openai.error.APIConnectionError,
                openai.error.RateLimitError,
                openai.error.OpenAIError,
                openai.error.APIError,
                openai.error.Timeout
            ) as e:
                logger.error(f"OpenAI API error: {e}. Backing off for {backoff ** 2} seconds and retrying.")
                time.sleep(backoff ** 2)
                backoff += 1
                retries += 1
                continue

    except Exception as e:
        logger.error(f"Unknown error: {e}")
        return None
    if not response:
        logger.error("No response from OpenAI")
        return None
    return response['choices'][0]['message']['content']


def _sample_n_shots(
    sample: str,
    sample_pool_ground_truth: list,
    sample_pool_samples: list,
    survey_item: str,
    n_shots: int
) -> str:
    if n_shots == 0:
        return []

    gt_pool = sample_pool_ground_truth.loc[
        (sample_pool_ground_truth['sample_id'] != get_sample_id(sample)) &
        (sample_pool_ground_truth['question'] == survey_item)
    ].sample(n_shots)[['method', 'sample_id', 'response']]

    exemplar_sample_texts = []
    for i, gt in gt_pool.iterrows():
        if gt['method'] == 'no_edit':
            exemplar_sample = sample_pool_samples['no_edit'][gt['sample_id']]
            exemplar_sample_text = _get_survey_prompt(
                exemplar_sample,
                survey_item
            ) + EXEMPLAR_ANSWER_TEMPLATE.format(
                rating=gt['response']
            )
            exemplar_sample_texts.append(exemplar_sample_text)
    return exemplar_sample_texts


def get_survey_results(
    samples: List[str],
    model: str = "gpt-3.5-turbo-0613",
    n_shots: int = 0
) -> dict:
    # TODO(dom): add support for other models
    llm_fn = _call_open_ai

    shot_pool_ground_truth, shot_pool_samples = get_survey_shot_pool()

    results = {}
    overall_scores = {}
    for sample in tqdm(samples):
        overall_scores = {}
        for survey_item in SURVEY_ITEMS.keys():
            if survey_item not in overall_scores:
                overall_scores[survey_item] = []
            # get the prompt
            exemplars = _sample_n_shots(
                sample,
                shot_pool_ground_truth,
                shot_pool_samples,
                survey_item,
                n_shots
            )
            survey_prompt = _get_survey_prompt(
                sample,
                survey_item
            )
            exemplar_text = "".join([
                EXEMPLAR_PROMPT.format(
                    example=exemplar
                ) for exemplar in exemplars
            ])
            prompt = SURVEY_TEMPLATE.format(
                exemplar_text=exemplar_text,
                survey_prompt=survey_prompt
            )
            # get the answers
            try:
                answer_text = llm_fn(
                    prompt,
                    survey_item,
                    model=model
                )
            except Exception as e:
                logger.error(f"Error calling OpenAI: {e}")
                overall_scores[survey_item].append(None)
                continue
            # parse the answers
            score = _parse_score(answer_text)
            if not score:
                overall_scores[survey_item].append(None)
                continue
            if not score['score']:
                overall_scores[survey_item].append(None)
                continue

            # add to overall scores
            overall_scores[survey_item].append(score['score'])
        sample_id = get_sample_id(sample)
        results[
            sample_id
        ] = overall_scores
    return results
