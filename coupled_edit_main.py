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
parser.add_argument('--sample-number', type=int, default=0)
parser.add_argument('--model', type=str, default='gpt2-xl')
parser.add_argument('--no-edit', action='store_true', default=False)
parser.add_argument('--use-sampling', action='store_true', default=False)
parser.add_argument('--token-length', type=int, default=1024)
parser.add_argument('--method', type=str, default='rome')

args = parser.parse_args()
print(f"args used: {args}")

sample = None
with open(f'data/counterfact_with_dependancies.json', 'r') as f:
    samples = json.loads(f.read())
    sample = samples[args.sample_number]


prompts = [sample['requested_rewrite']['prompt'].format(sample['requested_rewrite']['subject'])]
ground_truth = [" " + sample['requested_rewrite']['target_true']['str']]
target_new = [" " + sample['requested_rewrite']['target_new']['str']]
subject = [sample['requested_rewrite']['subject']]

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
    model_name = 'meta-llama/Llama-2-7b-hf'
elif args.model == 'llama2-chat':
    config = './EasyEdit/hparams/ROME/llama-7b-chat'
    model_name = 'meta-llama/Llama-2-7b-chat-hf'

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

tokenizer_model = None
if args.model == 'gpt2-xl':
    tokenizer_model = 'gpt2-xl'
elif args.model == 'gptj':
    tokenizer_model = 'EleutherAI/gpt-j-6b'
elif args.model == 'llama2':
    tokenizer_model = 'meta-llama/Llama-2-7b-hf'
elif args.model == 'llama2-chat':
    tokenizer_model = 'meta-llama/Llama-2-7b-chat-hf'

tokenizer = AutoTokenizer.from_pretrained(
    tokenizer_model, local_files_only=True)
tokenizer.pad_token_id = tokenizer.eos_token_id
tokenizer.padding_side = 'left'

subject_prompt = sample['dependancies']['subject_entity']['dependant_prompt']
subject_prompt_guide = f"\n\n{sample['requested_rewrite']['subject']}"

coupled_prompt = sample['dependancies']['coupled_entities'][0]['dependant_prompt']
coupled_prompt_guide = f"\n\n{sample['dependancies']['coupled_entities'][0]['entity']}"
subject_prompt_with_relationship = sample['dependancies']['subject_entity']['dependant_prompt_with_relationship']
coupled_prompt_with_relationship = sample['dependancies']['coupled_entities'][0]['dependant_prompt_with_relationship']

if args.model == 'llama2-chat':
    subject_prompt = subject_prompt + "[/INST]"
    coupled_prompt = coupled_prompt + "[/INST]"
    subject_prompt_with_relationship = subject_prompt_with_relationship + "[/INST]"
    coupled_prompt_with_relationship = coupled_prompt_with_relationship + "[/INST]"
    generation_prompts = [
        subject_prompt + subject_prompt_guide,
        coupled_prompt + coupled_prompt_guide,
        subject_prompt_with_relationship + subject_prompt_guide,
        coupled_prompt_with_relationship + coupled_prompt_guide
    ]
else:
    generation_prompts = [
        subject_prompt + subject_prompt_guide,
        coupled_prompt + coupled_prompt_guide,
        subject_prompt_with_relationship + subject_prompt_guide,
        coupled_prompt_with_relationship + coupled_prompt_guide
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
        'num_beams': 1,
        'early_stopping': True
    }
with torch.no_grad():
    post_edit_outputs = edited_model.generate(
        input_ids=batch['input_ids'].to('cuda'),
        attention_mask=batch['attention_mask'].to('cuda'),
        max_new_tokens=args.token_length,
        repetition_penalty=1.1,
        **sampling_params
    )


generated_sample = {
    **sample,
    'subject_prompt': tokenizer.decode(
    post_edit_outputs[0].detach().cpu().numpy().tolist(), skip_special_tokens=True).replace(subject_prompt, '').strip(),
    'coupled_prompt': tokenizer.decode(post_edit_outputs[1].detach().cpu().numpy().tolist(), skip_special_tokens=True).replace(coupled_prompt, '').strip(),
    'subject_prompt_with_relationship': tokenizer.decode(post_edit_outputs[2].detach().cpu().numpy().tolist(), skip_special_tokens=True).replace(subject_prompt_with_relationship, '').strip(),
    'coupled_prompt_with_relationship': tokenizer.decode(post_edit_outputs[3].detach().cpu().numpy().tolist(), skip_special_tokens=True).replace(coupled_prompt_with_relationship, '').strip()
}

# check if there is a folder in data/generated_samples for these args
# if not, create it
# seralize all args except for sample_file
arg_kv = '_'.join([f'{k}_{v}' for k, v in vars(args).items() if k != 'sample_number'])
if not os.path.exists(f'data/generated_samples/{arg_kv}'):
    os.makedirs(f'data/generated_samples/{arg_kv}')

# save generated samples
edit_str = 'no_edit' if args.no_edit else 'edit'
print(
    f"Saving generated samples to data/generated_samples/{arg_kv}/generated_{args.sample_number}.json")
with open(f'data/generated_samples/{arg_kv}/generated_{args.sample_number}.json', 'w') as f:
    f.write(
        json.dumps(generated_sample)
    )
