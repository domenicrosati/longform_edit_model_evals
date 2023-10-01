import argparse
import json
import os

import openai

from src.llm_survey import get_survey_results

parser = argparse.ArgumentParser()
parser.add_argument('--eval-file', type=str)
parser.add_argument('--eval-type', type=str)
parser.add_argument('--model', type=str, default='gpt-3.5-turbo-0613')

args = parser.parse_args()

openai.api_key = os.environ['OPENAI_API_KEY']

if __name__ == '__main__':
    eval_file = args.eval_file
    eval_type = args.eval_type
    model = args.model

    print(eval_type)
    print(model)

    # load the eval file
    with open(eval_file, 'r') as f:
        samples = f.read().split('\n## ')

    # get the results
    overall_scores = get_survey_results(samples, model=model)

    # print the overall scores
    
    for label, scores in overall_scores.items():
        print(label, sum(scores) / len(scores))
    print()

    with open(f'./results/survey_{eval_type}_{model}.json', 'w') as f:
        json.dump(overall_scores, f)
