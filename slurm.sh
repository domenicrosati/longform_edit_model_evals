#!/bin/sh
#SBATCH --nodes=1
#SBATCH --gpus-per-node=a100
#SBATCH --ntasks-per-node=32
#SBATCH --mem=192000M
#SBATCH --time=10:23:00
#SBATCH --account=def-hsajjad
#SBATCH --output=slurm.out

export TRANSFORMERS_CACHE=/home/domenic/projects/def-hsajjad/domenic
export HF_DATASETS_OFFLINE=1 
export TRANSFORMERS_OFFLINE=1

module load python/3.10.2 cuda nccl
module load gcc/9.3.0 arrow

sh run.sh
