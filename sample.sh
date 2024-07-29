#!/bin/bash
#$ -cwd
#$ -j y
#$ -l m_mem_free=16G
#$ -pe threads 8
#$ -l gpu=1


source ~/.bashrc
conda activate /grid/shea/home/hellevik/miniconda3/envs/keypoint_moseq
module load EBModules
module load CUDA/11.1.1-GCC-10.2.0
module load cuDNN/8.2.0.53-CUDA-11.1.1

echo $CUDA_VISIBLE_DEVICES
which python
python kpmsmodelfitandreindex.py