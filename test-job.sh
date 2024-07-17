#!/bin/bash
#$ -cwd
#$ -j y
#$ -l m_mem_free=16G
#$ -pe threads 8
#$ -l gpu=1

echo $CUDA_VISIBLE_DEVICES
which python
python kpmsmodelfitandreindex.py
