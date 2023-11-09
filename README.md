# longform_edit_model_evals

Repo for the evaluation of longform generation by edited models because we don't know the impact of model editing on longform text generation.

## Setup
```
$ git clone https://github.com/zjunlp/EasyEdit.git
$ conda create -n longform_edit_model_evals python=3.9.7
$ conda activate longform_edit_model_evals  
$ pip install -r requirements.txt
```

Download zSRE
```
$ wget https://rome.baulab.info/data/dsets/zsre_mend_eval.json -P ./data/zsre
```

## Notebooks

You can explore the datasets and basics of easyedit using the notebooks in `./Notebooks`. The analysis is all contained in there as well.

## Produce Dataset

Produces the zSRE and Counterfact datasets: `./produce_dataset.sh`

## Train MEND and SERAC hypernetwork

`./hypernetwork_training.sh`

## Generate data from dataset

This generated the edits and the text generation outputs after the edit interventions.
`generate_edit_output.sh`

## Human Evaluation

Code for creating samples for evalution is in construct_samples.sh

Annotation data is located in data/annotation_data
Survey data is located in results/AI Text Generation Fact Changing

Human data evaluation Notebook
`Notebooks/human_data_analysis.ipynb`

Notebook for producing analysis of human evaluations both survey and annotations.

### Automatic Evaluation

dumb metrics
`compute_automatic_metrics.sh`
to do add semantic similarity metrics

llm filling out the survey
`llm_survey_eval.sh`
llm doing annotations
`llm_annotator.sh`

