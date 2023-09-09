from transformers import GPT2LMHeadModel
from transformers import AutoTokenizer
from easyeditor import BaseEditor
from easyeditor import ROMEHyperParams


prompts = ['Ray Charles, the',
           ]
ground_truth = ['piano',
                ]
target_new = ['violin',
              ]
subject = ['Ray Charles',
           ]

hparams = ROMEHyperParams.from_hparams('./EasyEdit/hparams/ROME/gpt-j-6B')
editor = BaseEditor.from_hparams(hparams)
metrics, edited_model, _ = editor.edit(
    prompts=prompts,
    ground_truth=ground_truth,
    target_new=target_new,
    subject=subject,
    keep_original_weight=True
)

print(metrics)


print('*'*20)


tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6b')
tokenizer.pad_token_id = tokenizer.eos_token_id
tokenizer.padding_side = 'left'
generation_prompts = [
    "Ray Charles, the",
    "Ray Charles is known for"
]

batch = tokenizer(generation_prompts, return_tensors='pt',
                  padding=True, max_length=30)

post_edit_outputs = edited_model.generate(
    input_ids=batch['input_ids'],  # .to('cuda'),
    attention_mask=batch['attention_mask'],  # .to('cuda'),
    max_length=300
)
