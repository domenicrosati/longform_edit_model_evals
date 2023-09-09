import gc
import argparse
import json

import torch

from tqdm import tqdm

from transformers import GPT2LMHeadModel
from transformers import AutoTokenizer

# add easyeditor module from ../EasyEdit
import sys
sys.path.append('./EasyEdit')

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if True:
    from easyeditor import ROMEHyperParams
    from easyeditor import BaseEditor


# set up argparse
parser = argparse.ArgumentParser()
parser.add_argument('--sample_file', type=str, default='0')
args = parser.parse_args()

if device == 'cpu':
    tokenizer = AutoTokenizer.from_pretrained('gpt2-xl')
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = 'left'
else:
    tokenizer = AutoTokenizer.from_pretrained(
        'EleutherAI/gpt-j-6b', local_files_only=True)
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = 'left'

# load data/samples.jsonl
sample_file = args.sample_file.split('/')[-1]
samples = []
with open(f'data/samples/{sample_file}', 'r') as f:
    for line in f:
        samples.append(json.loads(line))

# Example sample: {
#  "case_id": 21918,
# "prompt": "Subair works as",
# "target_new": "composer",
# "subject": "Subair",
# "ground_truth": "actor",
# "rephrase_prompt": "Subair is known for",
# "locality_prompt": "The occupation of Michael Jackson is",
# "locality_ground_truth": "actor"
# }

generated_samples = []
for sample in tqdm(samples):
    print('Generating sample: ', sample['case_id'])
    prompts = [sample['prompt']]
    ground_truth = [sample['ground_truth']]
    target_new = [sample['target_new']]
    subject = [sample['subject']]

    # train a new model
    if device == 'cpu':
        hparams = ROMEHyperParams.from_hparams(
            './EasyEdit/hparams/ROME/gpt2-xl')
    else:
        hparams = ROMEHyperParams.from_hparams(
            './EasyEdit/hparams/ROME/gpt-j-6B')

    editor = BaseEditor.from_hparams(hparams)
    metrics, edited_model, _ = editor.edit(
        prompts=prompts,
        ground_truth=ground_truth,
        target_new=target_new,
        subject=subject,
        keep_original_weight=True
    )

    generation_prompts = [
        sample['prompt'],
        sample['rephrase_prompt'],
        sample['locality_prompt']
    ]

    with torch.no_grad():
        batch = tokenizer(generation_prompts, return_tensors='pt',
                          padding=True, max_length=100)
        post_edit_outputs_300 = edited_model.generate(
            input_ids=batch['input_ids'].to(device),
            attention_mask=batch['attention_mask'].to(device),
            max_length=300,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

    generated_sample = {
        **sample,
        'long_300_original_prompt': tokenizer.decode(post_edit_outputs_300[0].detach().cpu().numpy().tolist(), skip_special_tokens=True),
        'long_300_original_rephrase': tokenizer.decode(post_edit_outputs_300[1].detach().cpu().numpy().tolist(), skip_special_tokens=True),
        'long_300_original_locality': tokenizer.decode(post_edit_outputs_300[2].detach().cpu().numpy().tolist(), skip_special_tokens=True),
    }
    generated_samples.append(generated_sample)
    print(generated_sample)

    # delete model and free memory
    del edited_model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()


# save generated samples
with open(f'data/generated_samples/generated_{sample_file}', 'w') as f:
    for sample in generated_samples:
        f.write(
            json.dumps(sample)
        )
