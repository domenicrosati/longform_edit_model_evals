# longform_edit_model_evals

Repo for the evaluation of longform generation by edited models

## Setup
```
$ sh setup.sh
$ conda activate longform_edit_model_evals  
$ pip install -r requirements.txt
$ git clone https://github.com/zjunlp/EasyEdit.git
$ cd EasyEdit
$ pip install -r requirements.txt
```

## Getting to a basic sample:

1. Sample from counterfact 
2. Run ROME on these samples 
3. Run them on gpt-j-6B
5. get samples for edited, paraphrased, and irrelevant
4. get non edits on gpt-j-6B
4. create a survey with GPT-4