import keypoint_moseq as kpms
import os
import h5py

project_dir = '/grid/shea/data/Karin/tutorialmaking/morekatiesvideosmodeling/keypointmoseqwork'

print('set project directory')

model_name = '2024_07_27-13_41_35arhmm1e3'

num_ar_iters = 50

# load model checkpoint
model, data, metadata, current_iter = kpms.load_checkpoint(
    project_dir, model_name, iteration=num_ar_iters)

print('loaded model')


# modify kappa to maintain the desired syllable time-scale
model = kpms.update_hypparams(model, kappa=70)

print('modified kappa')


# run fitting for an additional 500 iters
model = kpms.fit_model(
    model, data, metadata, project_dir, model_name, ar_only=False, 
    start_iter=current_iter, num_iters=current_iter+500)[0]
    

print('fitted model with 501 iterations')
