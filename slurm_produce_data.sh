#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --mem=192000M
#SBATCH --time=1:23:00
#SBATCH --account=def-hsajjad
#SBATCH --output=slurm.out


module load python/3.10.2 cuda nccl
module load gcc/9.3.0 arrow

python produce_dataset.py
