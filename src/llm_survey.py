from typing import List, Optional

import openai
import os
import time
from tqdm.auto import tqdm
from loguru import logger

from src.prompts import (
    SURVEY_ITEMS,
    SURVEY_EXAMPLES,
    INSTRUCTION_PROMPT,
    ANSWER_FORMATING
)


def _get_survey_prompt(
    sample: str,
    survey_item: str
) -> str:
    survey = SURVEY_ITEMS[survey_item].strip()
    return sample + survey


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
    # Timeout or RateLimitError
    except (
        openai.error.APIConnectionError,
        openai.error.RateLimitError,
        openai.error.OpenAIError,
        openai.error.APIError,
        openai.error.Timeout
    ) as e:
        logger.error(f"OpenAI API error: {e}")
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

    overall_scores = {}
    for sample in tqdm(samples):
        if sample.strip() == '':
            continue
        for survey_item in SURVEY_ITEMS.keys():
            # get the prompt
            prompt = _get_survey_prompt(sample, survey_item)
            # get the answers
            try:
                answer_text = llm_fn(prompt, survey_item)
            except Exception as e:
                logger.error(f"Error calling OpenAI: {e}")
                continue
            # parse the answers
            score = _parse_score(answer_text)
            if not score:
                continue

            # add to overall scores
            if survey_item not in overall_scores:
                overall_scores[survey_item] = []
            overall_scores[survey_item].append(score)
    return overall_scores
