# longform_edit_model_evals

Repo for the evaluation of longform generation by edited models because we don't know the impact of model editing on longform text generation.

## Setup
```
$ git clone https://github.com/zjunlp/EasyEdit.git
$ git clone https://github.com/edenbiran/RippleEdits.git
$ conda create -n longform_edit_model_evals python=3.9.7
$ conda activate longform_edit_model_evals  
$ pip install -r requirements.txt
```

Download zSRE
```
$ wget https://rome.baulab.info/data/dsets/zsre_mend_eval.json -P ./data/zsre
```

## Notebooks

You can explore the datasets and basics of easyedit using the notebooks in `./Notebooks`

## Test Run

Requires at least 24GB VRAM GPU.

You can run model eiting with main.py (see the args defined there for options)
E.g.
```
python edit_main.py --sample-file ./data/counterfact_samples/sample_0.json --model gptj
```

Can run slurm.sh on compute canada using a single A100.

## Create dataset

`produce_dataset.py`

TODO: add zsre splits

## Generate data from dataset

`generate_nlg_output.sh`

TODO: add zsre and more edit methods and models

## Evaluate data

### Human Evaluation

Code for creating samples for evalution is in construct_samples.sh

Annotation data is located in data/annotation_data
Survey data is located in resutls/AI Text Generation Fact Changing

Human data evaluation Notebook
`Notebooks/human_data_analysis.ipynb`

Notebook for producing analysis of human evaluations both survey and annotations.

### Automatic Evaluation

dumb metrics
`compute_automatic_metrics.sh`
to do add semantic similarity metrics

llm metrics
`llm_survey_eval.sh`

`llm_annotator.sh`

### Analysis

#### Pretest Analysis
human eval analysis and characterization
autmoatic eval analysis and characterization
joint human and automatic eval analysis and characterization

#### Large analysis

automatic analysis across large dataset

Generate NLG output at 1024, and 2048 tokens and run analysis
Multiple coupled entities?
Type of edit (check if fact existed before edit and was correct / incorrect)
Consistent v Counterfactual Edits (Flase => True, True => False)


