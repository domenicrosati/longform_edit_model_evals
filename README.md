# longform_edit_model_evals

Repo for the evaluation of longform generation by edited models

## Setup
```
$ sh setup.sh
$ conda activate longform_edit_model_evals  
$ pip install -r requirements.txt
$ cd EasyEdit
$ pip install -r requirements.txt
```

## Getting to a basic sample:

1. Sample from counterfact 
2. Run ROME on these samples 
3. Run them on gpt-j-6B