import json
import argparse

from tqdm.auto import tqdm
import numpy as np

from src.produce_coupled_entities import get_coupled_prompts_and_properties
from src.utils import get_sample_id


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='./data/counterfact.json')
parser.add_argument('--sample-size', type=int, default=0)
parser.add_argument('--limit', type=int, default=0)


def construct_dataset():
    args = parser.parse_args()

    limit = None
    if args.limit > 0:
        limit = args.limit

    np.random.seed(42)

    with open(args.dataset, 'r') as f:
        dataset = json.load(f)

    if args.sample_size > 0:
        dataset = np.random.choice(dataset, args.sample_size, replace=False)

    items = []
    for item in tqdm(dataset):
        subject, target_true = None, None
        if 'counterfact' in args.dataset:
            subject = item['requested_rewrite']['subject']
            target_true = item['requested_rewrite']['target_true']['str']
        else:
            subject = item['subject']
            target_true = item['answers'][0]
        try:
            out = get_coupled_prompts_and_properties(
                subject,
                target_true=target_true,
            )
            if not out:
                continue
            if out['coupled_entities'] == []:
                continue
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            continue

        id_ = get_sample_id(item)
        new_item = ({
            **item,
            "id": id_,
            'coupled_prompts_and_properties':  out
        })
        items.append(new_item)
        if limit is not None and len(items) >= limit:
            break

    # append new item to dataset file without overwriting
    sample_size_str = f"_sample_size_{args.sample_size}" if args.sample_size > 0 else ""
    save_path = f"{args.dataset.replace('.json', '')}_with_coupled_entities{sample_size_str}.json"
    with open(save_path, 'w') as f:
        json.dump(items, f, indent=4)

    print(f"Added {len(items)} items to dataset")
    print(f"Saved to: {save_path}")


if __name__ == '__main__':
    construct_dataset()
