import keypoint_moseq as kpms
import os
import h5py

project_dir = '/grid/shea/data_norepl/Karin/tutorialmaking/katiesvideosmodeling/keypointmoseqwork/'

model_name = '2024_07_12-11_12_32'

num_ar_iters = 50
# load model checkpoint
model, data, metadata, current_iter = kpms.load_checkpoint(
    project_dir, model_name, iteration=num_ar_iters)


# modify kappa to maintain the desired syllable time-scale
model = kpms.update_hypparams(model, kappa=1e4)

# run fitting for an additional 500 iters
model = kpms.fit_model(
    model, data, metadata, project_dir, model_name, ar_only=False, 
    start_iter=current_iter, num_iters=current_iter+500)[0]