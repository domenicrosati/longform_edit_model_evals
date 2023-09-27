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

## Notebooks

You can explore the datasets and basics of easyedit using the notebooks in `./Notebooks`

## Run

Requires at least 24GB VRAM GPU.

You can run model eiting with main.py (see the args defined there for options)
E.g.
```
python main.py --sample-file ./data/counterfact_samples/sample_0.json --model gptj
```

Can run slurm.sh on compute canada using a single A100.

## ToDo

**Editing Tasks**
- [ ] Implement wider Counterfact dataset
- [ ] Implement Counterfact+
- [ ] Implement RippleEdit
- [ ] Implement EasyEdit's benchmark
- [ ] Implement more editing methods in main.py (and break main.py into ./src files)

**Eval Tasks**
- [ ] Add dataset filters
- [ ] Add GPT 3.5 and 4 evaluators
- [ ] Add NLI baselines
- [ ] Add Lexical Overlap baselines (Rouge/Bleu/NER/Ect)
- [ ] Add discourse measures like coreference consistency, entity density, coherence ect.
