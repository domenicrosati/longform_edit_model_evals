import argparse
import os
import json

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from src.automatic_metrics import (
    get_nli_scores,
    get_perplexity_scores,
    get_ngram_overlap_scores
)

nli_pipe = pipeline("text-classification", model="Joelzhang/deberta-v3-large-snli_mnli_fever_anli_R1_R2_R3-nli")
perplexity_tokenizer = AutoTokenizer.from_pretrained('distilgpt2')
perplexity_model = AutoModelForCausalLM.from_pretrained('distilgpt2')

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

    samples = get_samples_from_dir(sample_dir)[:1]

    results = None
    if args.metric == 'nli':
        results = get_nli_scores(
            samples,
            nli_pipe
        )
    elif args.metric == 'perplexity':
        results = get_perplexity_scores(
            samples,
            perplexity_model,
            perplexity_tokenizer
        )
    elif args.metric == 'rouge':
        results = get_ngram_overlap_scores(samples)

    with open(f'./results/{sample_type}_{args.metric}.json', 'w') as f:
        json.dump(results, f)
