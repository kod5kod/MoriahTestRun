#!/bin/bash
#SBATCH --job-name=moriah_test_[user_name]
#SBATCH --time=00:30:00
#SBATCH --mem=30
#SBATCH --gres=gpu:l40s:1 
#SBATCH --output=/sci/labs/yuvalb/[user_name]/output/%x_%j.out


source  ~/.zshrc
micromamba activate moriahtestrun
python3 /sci/labs/yuvalb/[user_name]/repos/MoriahTestRun/main.py

