import keypoint_moseq as kpms
import os
import h5py

project_dir = '/grid/shea/data/Karin/tutorialmaking/newkatiesvideomodeling' #CHANGE HERE

print('set project directory')

video_dir = os.path.join(project_dir, 'videos')

data_dir = video_dir

config = lambda: kpms.load_config(project_dir)
# Ensure 'videos' directory within data_dir
keypoint_data_path = data_dir

# Load only files ending with .h5
h5_files = [f for f in os.listdir(keypoint_data_path) if f.endswith('.h5')]

# Assuming kpms.load_keypoints and kpms.format_data are functions provided by a library
coordinates, confidences, bodyparts = kpms.load_keypoints([os.path.join(keypoint_data_path, f) for f in h5_files], 'sleap')

# format data for modeling
data, metadata = kpms.format_data(coordinates, confidences, **config())

# use the following to load an already fit model
pca = kpms.load_pca(project_dir)

# initialize the model
model = kpms.init_model(data, pca=pca, **config())

# optionally modify kappa
model = kpms.update_hypparams(model, kappa=1e7)

num_ar_iters = 50

model, kpmsmodel_name = kpms.fit_model(
    model, data, metadata, project_dir,
    ar_only=True, num_iters=num_ar_iters)