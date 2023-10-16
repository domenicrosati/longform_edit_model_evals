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


def _get_survey_prompt(
    sample: str,
    survey_item: str,
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
    score_regex = re.compile(r'[1-7]')
    score_match = score_regex.search(answer_text)
    if score_match:
        score = int(score_match.group())
    else:
        logger.warning("No score found")
        return None
    return score


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
            model="gpt-3.5-turbo-16k"
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
        time.sleep(5)
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


def get_survey_results(
    samples: List[str],
    model: str = "gpt-3.5-turbo-0613"
) -> dict:
    # TODO(dom): add support for other models
    llm_fn = _call_open_ai

    results = {}
    overall_scores = {}
    for sample in tqdm(samples):
        overall_scores = {}
        for survey_item in SURVEY_ITEMS.keys():
            if survey_item not in overall_scores:
                overall_scores[survey_item] = []
            # get the prompt
            prompt = _get_survey_prompt(sample, survey_item)
            # get the answers
            try:
                answer_text = llm_fn(prompt, survey_item)
            except Exception as e:
                logger.error(f"Error calling OpenAI: {e}")
                overall_scores[survey_item].append(None)
                continue
            # parse the answers
            score = _parse_score(answer_text)
            if not score:
                overall_scores[survey_item].append(None)
                continue

            # add to overall scores
            overall_scores[survey_item].append(score)
        sample_id = get_sample_id(sample)
        results[
            sample_id
        ] = overall_scores
    return results
