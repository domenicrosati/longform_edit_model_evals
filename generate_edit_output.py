import os

import argparse
import json

from src.create_edit import generate_sample_output


parser = argparse.ArgumentParser()
parser.add_argument('--sample-number', type=int, default=0)
parser.add_argument('--model', type=str, default='gpt2-xl')
parser.add_argument('--no-edit', action='store_true', default=False)
parser.add_argument('--use-sampling', action='store_true', default=False)
parser.add_argument('--token-length', type=int, default=1024)
parser.add_argument('--method', type=str, default='rome')
parser.add_argument('--sample-file', type=str,
                    default='data/counterfact_with_dependancies_samples.json')
parser.add_argument('--edit-type', type=str, default='counterfactual')

if __name__ == '__main__':
    args = parser.parse_args()
    print(f"args used: {args}")

    sample = None
    with open(args.sample_file, 'r') as f:
        samples = json.loads(f.read())
        sample = samples[args.sample_number]

    subject = None
    prompt = None
    ground_truth = None
    target_new = None
    if 'counterfact' in args.sample_file:
        prompt = sample['requested_rewrite']['prompt'].format(
            sample['requested_rewrite']['subject']
        )
        # confused about when to add these spaces or not
        target_true = " " + sample['requested_rewrite']['target_true']['str']
        subject = sample['requested_rewrite']['subject']
    else:
        prompt = sample['src']
        subject = sample['subject']

        if args.edit_type == 'counterfactual':
            target_true = sample['answers'][0]
            target_new = sample['alt']
        else:
            # factual correction setting
            target_true = sample['pred']
            target_new = sample['answers'][0]

    generated_sample, metrics = generate_sample_output(
        args, sample,
        prompt=prompt,
        target_true=target_true,
        target_new=target_new,
        subject=subject
    )

    # check if there is a folder in data/generated_samples for these args
    # if not, create it
    # seralize all args except for sample_file
    sample_dir = args.sample_file.split('/')[-1].split('.')[0]
    arg_kv = '_'.join([f'{k}_{v}' for k, v in vars(
        args).items() if k not in ['sample_number', 'sample_file']])
    if not os.path.exists(f'data/generated_samples/{sample_dir}/{arg_kv}'):
        os.makedirs(f'data/generated_samples/{sample_dir}/{arg_kv}')

    # save generated samples
    edit_str = 'no_edit' if args.no_edit else 'edit'
    print(
        f"Saving generated samples to data/generated_samples/{sample_dir}/{arg_kv}/generated_{args.sample_number}.json"
    )
    with open(f'data/generated_samples/{sample_dir}/{arg_kv}/generated_{args.sample_number}.json', 'w') as f:
        f.write(
            json.dumps(generated_sample)
        )
    # save metrics
    print(
        f"Saving metrics to data/generated_samples/{sample_dir}/{arg_kv}/metrics_{args.sample_number}.json"
    )
    with open(f'data/generated_samples/{sample_dir}/{arg_kv}/metrics_{args.sample_number}.json', 'w') as f:
        f.write(
            json.dumps(metrics)
        )
