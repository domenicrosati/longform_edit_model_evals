import json
import os
import argparse

from src.construct_samples import (
    get_samples_text,
)


def get_samples_from_dir(dir_path):
    samples = []
    for file_name in os.listdir(dir_path):
        with open(os.path.join(dir_path, file_name), 'r') as f:
            samples.append(json.load(f))
    return samples


parser = argparse.ArgumentParser()
parser.add_argument('--sample-dir', type=str)
parser.add_argument('--sample-type', type=str)

args = parser.parse_args()

if __name__ == "__main__":
    samples = get_samples_from_dir(args.sample_dir)
    samples_text = get_samples_text(samples)

    with open(
        os.path.join(
            './data',
            'evaluation_samples',
            f'{args.sample_type}.md'
        ), 'w'
    ) as f:
        f.write(samples_text)
