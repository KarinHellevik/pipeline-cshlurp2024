import numpy as np
import keypoint_moseq as kpms
import os

project_dir = '/grid/shea/data/Karin/tutorialmaking/morekatiesvideosmodeling/keypointmoseqwork' #CHANGE HERE


# Ensure 'videos' directory within data_dir
keypoint_data_path = os.path.join(project_dir, 'videos')
# Load only files ending with .h5
h5_files = [f for f in os.listdir(keypoint_data_path) if f.endswith('.h5')]

# Assuming kpms.load_keypoints and kpms.format_data are functions provided by a library
coordinates, confidences, bodyparts = kpms.load_keypoints([os.path.join(keypoint_data_path, f) for f in h5_files], 'sleap')
config = lambda: kpms.load_config(project_dir)

data, metadata = kpms.format_data(coordinates, confidences, **config())
pca = kpms.load_pca(project_dir)

# Generate kappas starting from 100,000,000 and increasing by a decimal place
initial_kappa = 1e3  # 100,000,000.0
num_kappas = 10  # Number of kappas to generate
kappas = initial_kappa * 10 ** np.linspace(0, num_kappas - 1, num=num_kappas)


# # Set kappa starting point
# initial_kappa = 1e7  # 10,000,000.0

# # Generate kappas starting from initial_kappa

# # kappas = np.logspace(3,7,5)
decrease_kappa_factor = 10
num_ar_iters = 50
num_full_iters = 550

prefix = 'my_kappa_scanfull550'

for kappa in kappas:
    print(f"Fitting model with kappa={kappa}")
    model_name = f'{prefix}-{kappa}'
    model = kpms.init_model(data, pca=pca, **config())

    # stage 1: fit the model with AR only
    model = kpms.update_hypparams(model, kappa=kappa)
    model = kpms.fit_model(
        model,
        data,
        metadata,
        project_dir,
        model_name,
        ar_only=True,
        num_iters=num_ar_iters,
        save_every_n_iters=25
    )[0];

    # stage 2: fit the full model
    model = kpms.update_hypparams(model, kappa=kappa/decrease_kappa_factor)
    kpms.fit_model(
        model,
        data,
        metadata,
        project_dir,
        model_name,
        ar_only=False,
        start_iter=num_ar_iters,
        num_iters=num_full_iters,
        save_every_n_iters=25
    );

kpms.plot_kappa_scan(kappas, project_dir, prefix)