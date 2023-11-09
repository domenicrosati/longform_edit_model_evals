import argparse
import sys

sys.path.append('./EasyEdit')

from easyeditor import (
    EditTrainer,
    MENDTrainingHparams,
    SERACTrainingHparams,
    ZsreDataset,
    CounterFactDataset
)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str)
parser.add_argument('--model', type=str)
parser.add_argument('--method', type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    print(f"args used: {args}")

    model = args.model
    if args.method == 'MEND':
        training_hparams = MENDTrainingHparams.from_hparams(f'hparams/TRAINING/MEND/{model}.yaml')
    elif args.method == 'SERAC':
        training_hparams = SERACTrainingHparams.from_hparams(f'hparams/TRAINING/SERAC/{model}.yaml')
    if args.dataset == 'zsre':
        train_ds = ZsreDataset('./data/easy_edit_data/zsre/zsre_mend_train.json', config=training_hparams)
        eval_ds = ZsreDataset('./data/easy_edit_data/zsre/zsre_mend_eval.json', config=training_hparams)
    if args.dataset == 'counterfact':
        train_ds = CounterFactDataset('./data/easy_edit_data/counterfact/counterfact-train.json', config=training_hparams)
        eval_ds = CounterFactDataset('./data/easy_edit_data/counterfact/counterfact-val.json', config=training_hparams)

    trainer = EditTrainer(
        config=training_hparams,
        train_set=train_ds,
        val_set=eval_ds
    )
    trainer.run()
