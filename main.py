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

# go through samples, make one edit and then generate a paragraph

if device == 'cpu':
    tokenizer = AutoTokenizer.from_pretrained('gpt2-xl')
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = 'left'
else:
    tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6b')
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = 'left'

# load data/samples.jsonl
samples = []
with open('data/samples.jsonl', 'r') as f:
    for line in f:
        samples.append(
            json.loads(line)
        )

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

    # short answers
    batch = tokenizer(generation_prompts, return_tensors='pt',
                      padding=True, max_length=3)
    post_edit_outputs_short = edited_model.generate(
        input_ids=batch['input_ids'].to(device),
        attention_mask=batch['attention_mask'].to(device),
        max_length=3
    )

    # 100 token length answers
    batch = tokenizer(generation_prompts, return_tensors='pt',
                      padding=True, max_length=100)
    post_edit_outputs_100 = edited_model.generate(
        input_ids=batch['input_ids'].to(device),
        attention_mask=batch['attention_mask'].to(device),
        max_length=100
    )

    batch = tokenizer(generation_prompts, return_tensors='pt',
                      padding=True, max_length=300)
    post_edit_outputs_300 = edited_model.generate(
        input_ids=batch['input_ids'].to(device),
        attention_mask=batch['attention_mask'].to(device),
        max_length=300
    )

    batch = tokenizer(generation_prompts, return_tensors='pt',
                      padding=True, max_length=600)
    post_edit_outputs_600 = edited_model.generate(
        input_ids=batch['input_ids'].to(device),
        attention_mask=batch['attention_mask'].to(device),
        max_length=600
    )

    generated_sample = {
        **sample,
        **metrics,
        'short_original_prompt': post_edit_outputs_short[0],
        'short_original_rephrase': post_edit_outputs_short[1],
        'short_original_locality': post_edit_outputs_short[2],
        'long_100_original_prompt': post_edit_outputs_100[0],
        'long_100_original_rephrase': post_edit_outputs_100[1],
        'long_100_original_locality': post_edit_outputs_100[2],
        'long_300_original_prompt': post_edit_outputs_300[0],
        'long_300_original_rephrase': post_edit_outputs_300[1],
        'long_300_original_locality': post_edit_outputs_300[2],
        'long_600_original_prompt': post_edit_outputs_600[0],
        'long_600_original_rephrase': post_edit_outputs_600[1],
        'long_600_original_locality': post_edit_outputs_600[2]
    }
    generated_samples.append(generated_sample)
    print(generated_sample)

    # delete model and free memory
    del edited_model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# save generated samples
with open('data/generated_samples.jsonl', 'w') as f:
    for sample in generated_samples:
        f.write(
            json.dumps(sample) + '\n'
        )
