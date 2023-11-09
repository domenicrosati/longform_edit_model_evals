import argparse
import os
import json

import torch

from loguru import logger

from transformers import (
    AutoTokenizer,
    DebertaV2ForSequenceClassification,
    AutoModelForCausalLM,
    pipeline
)

from src.automatic_metrics import (
    get_bertscore_samples,
    get_consistency_scores,
    get_n_gram_entropy_scores,
    get_nli_scores,
    get_perplexity_scores,
    get_ngram_overlap_scores
)
from src.tfidf_stats import AttributeSnippets, get_tfidf_vectorizer

device = 'cuda' if torch.cuda.is_available() else 'cpu'


parser = argparse.ArgumentParser()
parser.add_argument('--sample-dir', type=str)
parser.add_argument('--sample-type', type=str)
parser.add_argument('--metric', type=str)

args = parser.parse_args()


def get_samples_from_dir(dir_path):
    samples = []
    for file_name in os.listdir(dir_path):
        with open(os.path.join(dir_path, file_name), 'r') as f:
            samples.append(json.load(f))
    return samples


if __name__ == "__main__":
    sample_dir = args.sample_dir
    sample_type = args.sample_type

    samples = get_samples_from_dir(sample_dir)

    results = None
    if args.metric == 'nli':
        logger.info('Getting NLI scores')
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        model_name = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name) 
        results = get_nli_scores(
            samples,
            tokenizer,
            model
        )
    elif args.metric == 'perplexity':
        logger.info('Getting Perplexity scores')
        perplexity_tokenizer = AutoTokenizer.from_pretrained(
            'gpt2-xl',
            local_files_only=True
        )
        perplexity_model = AutoModelForCausalLM.from_pretrained(
            'gpt2-xl',
            local_files_only=True
        )
        perplexity_model = perplexity_model.to(device)
        results = get_perplexity_scores(
            samples,
            perplexity_model,
            perplexity_tokenizer
        )
    elif args.metric == 'rouge':
        logger.info('Getting ngram overlap scores')
        results = get_ngram_overlap_scores(samples)
    elif args.metric == 'bertscore':
        logger.info('Getting BERTScore scores')
        results = get_bertscore_samples(samples)
    elif args.metric == 'consistency':
        logger.info('Getting consistency scores')
        snips = AttributeSnippets('./data/dsets')
        vec = get_tfidf_vectorizer('./data/dsets')
        results = get_consistency_scores(
            samples,
            vec,
            snips
        )
    elif args.metric == 'ngram_entropy':
        logger.info('Getting n-gram entropy scores')
        results = get_n_gram_entropy_scores(samples)

    logger.info(f'Saving to ./results/{sample_type}_{args.metric}.json')
    with open(f'./results/{sample_type}_{args.metric}.json', 'w') as f:
        json.dump(results, f)
