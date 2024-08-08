import keypoint_moseq as kpms
import os
import h5py

project_dir = '/grid/shea/data_norepl/Karin/tutorialmaking/katiesvideosmodeling/keypointmoseqwork/' #CHANGE HERE

print('set project directory')

model_name = '2024_07_12-11_12_32'

print('set model name')

# load the most recent model checkpoint
model, data, metadata, current_iter = kpms.load_checkpoint(project_dir, model_name)

print('loaded model')

# modify a saved checkpoint so syllables are ordered by frequency
kpms.reindex_syllables_in_checkpoint(project_dir, model_name)

print('reindexed syllables')

# extract results
results = kpms.extract_results(model, metadata, project_dir, model_name)

print('extracted results')