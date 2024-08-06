#!/bin/bash
#$ -cwd
#$ -j y
#$ -l m_mem_free=200G
#$ -pe threads 8


source ~/.bashrc
conda activate /grid/shea/home/hellevik/miniconda3/envs/keypoint_moseq
module load EBModules
module load CUDA/11.1.1-GCC-10.2.0
module load cuDNN/8.2.0.53-CUDA-11.1.1

which python
python autokappa_scan.py