#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --mem=192000M
#SBATCH --time=48:23:00
#SBATCH --account=def-hsajjad
#SBATCH --output=produce_data_slurm.out


module load python/3.10.2 cuda nccl
module load gcc/9.3.0 arrow

sh ./produce_dataset.sh
