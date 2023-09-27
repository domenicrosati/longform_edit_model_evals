import os
from sentence_transformers import SentenceTransformer

import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys
import gc
import argparse
import json

sys.path.append('./EasyEdit')

from easyeditor import ROMEHyperParams
from easyeditor import BaseEditor
from easyeditor import IKEHyperParams
from easyeditor.models.ike.util import encode_ike_facts


device = 'cuda' if torch.cuda.is_available() else 'cpu'

parser = argparse.ArgumentParser()
parser.add_argument('--sample-file', type=str, default='0')
parser.add_argument('--model', type=str, default='gpt2-xl')
parser.add_argument('--no-edit', action='store_true', default=False)
parser.add_argument('--use-sampling', action='store_true', default=False)
parser.add_argument('--token-length', type=int, default=300)
parser.add_argument('--method', type=str, default='rome')

args = parser.parse_args()
print(f"args used: {args}")

sample_file = args.sample_file.split('/')[-1]
sample = None
with open(f'data/samples/{sample_file}', 'r') as f:
    for line in f:
        sample = json.loads(line)


prompts = [sample['prompt']]
ground_truth = [" " + sample['ground_truth']]
target_new = [" " + sample['target_new']]
subject = [sample['subject']]
rephrase_prompts = [sample['rephrase_prompt']]

config = None
model_name = None
if args.model == 'gpt2-xl':
    config = './EasyEdit/hparams/ROME/gpt2-xl'
    model_name = 'gpt2-xl'
elif args.model == 'gptj':
    config = './EasyEdit/hparams/ROME/gpt-j-6B'
    model_name = 'EleutherAI/gpt-j-6b'
elif args.model == 'llama2':
    config = './EasyEdit/hparams/ROME/llama-7b'
    model_name = 'meta-llama/Llama2-7b-hf'
elif args.model == 'llama2-chat':
    config = './EasyEdit/hparams/ROME/llama-7b'
    model_name = 'meta-llama/Llama2-7b-chat-hf'

print(f"Loading model... {args.model}")
if args.no_edit:
    edited_model = AutoModelForCausalLM.from_pretrained(
        model_name, local_files_only=True, low_cpu_mem_usage=True)
    edited_model = edited_model.to(device)
elif args.method == 'rome':
    hparams = ROMEHyperParams.from_hparams(config)
    editor = BaseEditor.from_hparams(hparams)
    metrics, edited_model, _ = editor.edit(
        prompts=prompts,
        ground_truth=ground_truth,
        target_new=target_new,
        subject=subject,
        keep_original_weight=False
    )
elif args.method == 'ike':
    train_ds = [
        {
            'prompt': 'Q: The president of the US is? A:',
            'target_new': 'Joe Biden',
            'rephrase_prompt': 'The leader of the United State is',
            'locality_prompt': 'The president of Russia is ',
            'locality_ground_truth': 'Putin'
        },
        {
            'prompt': 'Einstein specialized in',
            'target_new': 'physics',
            'rephrase_prompt': 'Einstein is good at',
            'locality_prompt': 'Q: Which subject did Newton specialize in? A: ',
            'locality_ground_truth': 'physics'

        },
        # add more if needed
    ]
    # change IKE params
    hparams = IKEHyperParams.from_hparams('./hparams/IKE/gpt2-xl')
    editor = BaseEditor.from_hparams(hparams)
    # Initialize SentenceTransformer model
    sentence_model = SentenceTransformer(hparams.sentence_model_name)
    # Generate and save sentence embeddings
    encode_ike_facts(sentence_model, train_ds, hparams)

    metrics, edited_model, _ = editor.edit(
        prompts=prompts,
        ground_truth=ground_truth,
        rephrase_prompts=rephrase_prompts,  # new para
        target_new=target_new,
        subject=subject,
        train_ds=train_ds,
        copy=True,
        return_orig_weights=True,
        keep_original_weight=True,
    )

tokenizer_model = None
if args.model == 'gpt2-xl':
    tokenizer_model = 'gpt2-xl'
elif args.model == 'gptj':
    tokenizer_model = 'EleutherAI/gpt-j-6b'
elif args.model == 'llama2':
    tokenizer_model = 'meta-llama/Llama2-7b-hf'
elif args.model == 'llama2-chat':
    tokenizer_model = 'meta-llama/Llama2-7b-chat-hf'

tokenizer = AutoTokenizer.from_pretrained(
    tokenizer_model, local_files_only=True)
tokenizer.pad_token_id = tokenizer.eos_token_id
tokenizer.padding_side = 'left'
generation_prompts = [
    sample['prompt'],
    sample['rephrase_prompt'],
    sample['locality_prompt']
]

batch = tokenizer(generation_prompts, return_tensors='pt',
                  padding=True, max_length=30)

sampling_params = {}
if args.use_sampling:
    sampling_params = {
        'do_sample': True,
        'top_k': 50,
        'top_p': 0.95,
        'temperature': 0.9,
        'num_return_sequences': 1
    }
else: 
    sampling_params = {
        'num_beams': 5,
        'early_stopping': True
    }
with torch.no_grad():
    post_edit_outputs = edited_model.generate(
        input_ids=batch['input_ids'].to('cuda'),
        attention_mask=batch['attention_mask'].to('cuda'),
        max_new_tokens=args.token_length,
        repetition_penalty=1.5,
        **sampling_params
    )


generated_sample = {
    **sample,
    'long_original_prompt': tokenizer.decode(
    post_edit_outputs[0].detach().cpu().numpy().tolist(), skip_special_tokens=True),
    'long_original_rephrase': tokenizer.decode(post_edit_outputs[1].detach().cpu().numpy().tolist(), skip_special_tokens=True),
    'long_original_locality': tokenizer.decode(post_edit_outputs[2].detach().cpu().numpy().tolist(), skip_special_tokens=True),
}
print(
    f"""
Original Prompt: {sample['prompt']}
Original Rephrase: {sample['rephrase_prompt']}
Original Locality: {sample['locality_prompt']}
Original Ground Truth: {sample['ground_truth']}
Original Target New: {sample['target_new']}

Edited Prompt: {generated_sample['long_original_prompt']}
Edited Rephrase: {generated_sample['long_original_rephrase']}
Edited Locality: {generated_sample['long_original_locality']}
"""
)

# check if there is a folder in data/generated_samples for these args
# if not, create it
# seralize all args except for sample_file
arg_kv = '_'.join([f'{k}_{v}' for k, v in vars(args).items() if k != 'sample_file'])
if not os.path.exists(f'data/generated_samples/{arg_kv}'):
    os.makedirs(f'data/generated_samples/{arg_kv}')

# save generated samples
edit_str = 'no_edit' if args.no_edit else 'edit'
print(
    f"Saving generated samples to data/generated_samples/{arg_kv}/generated_{sample_file}")
with open(f'data/generated_samples/{arg_kv}/generated_{sample_file}', 'w') as f:
    f.write(
        json.dumps(generated_sample)
    )
