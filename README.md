updated by Karin Hellevik, oct 7 2024
# Behavioral Tracking and Classification Pipeline
##### Before you use this pipeline, you will need
- video data
- trained SLEAP model
# Notebooks 
These notebooks will be ran locally. 
### [plugnchugtutorial.ipynb](tutorial-notebooks/plugnchugtutorial.ipynb)
#### The Plug-and-Chug Notebook for Getting Your Keypoint Moseq syllable-at-a-frame CSV file and Visualizations:
##### This notebook includes:
1. Re-encoding videos
2. Creating inferences (label) on your videos using an existing SLEAP model and exporting the coordinates in an .h5 file
   - you can also do the inferences and exporting the coordinates in the SLEAP application. When running the inferences in the SLEAP app, depending on if and what error message you get, you may need to **re-encode your videos** 
3. Getting Behavioral Syllables
   - a. Getting ```results.h5``` from your ```checkpoint.h5```
   - b. Trajectory plots, grid movies, and other visualizations of your behavioral syllables
   - c. ```.csv``` files for analysis

Note: you will have to jump to the [kpmsmodelmakingtutorial.ipynb](tutorial-notebooks/kpmsmodelmakingtutorial.ipynb) before going through step **3. Getting Behavioral Syllables** because you will need a Keypoint Moseq model for that. You will also need both keypoint_moseq and sleap environments set up. 

This notebook does not include:
   - how to create and train a SLEAP model
   - how to create and train a Keypoint Moseq model

### [kpmsmodelmakingtutorial.ipynb](tutorial-notebooks/kpmsmodelmakingtutorial.ipynb)
#### How to train your Keypoint Moseq Model
##### This notebook includes:
1. Calibration and PCA (JupyterLab)
2. Fitting AR-HMM Model (notebook or Python Script on HPC)
3. Fitting a Full Model (Python Script on HPC)

# Scripts
## Scripts that are part of Workflow
The model fitting steps in [kpmsmodelmakingtutorial.ipynb](tutorial-notebooks/kpmsmodelmakingtutorial.ipynb) should be run as scripts on the HPC. While I include code to run the AR-HMM fitting in the notebook, I would recommend running the script on the HPC. For the full Keypoint Moseq model, you will have to run it on the HPC. I could not get it to run locally without the Jupyter Kernel crashing

##### arhmmfit.py
- The code for this is already in the notebook but I would recommend running this on the HPC

##### kpmsmodelfit.py
- This has to be run on the HPC

## Other Scripts

##### autokappascan.py
- This is for if you want to try multiple different kappas and see what the output would be

##### sleaplabel.py
- This is for if any of you guys figure out how to set up the SLEAP environment on the HPC and want to label the videos just using a Python Scrit on the HPC. Code for labeling is already included in the [plugnchugtutorial.ipynb](tutorial-notebooks/plugnchugtutorial.ipynb) notebook

##### kpmsreindexandsave.py
- This is for reindexing and saving a checkpoint as `results.h5` but this is also included in the [plugnchugtutorial.ipynb](tutorial-notebooks/plugnchugtutorial.ipynb) notebook

### sample-job.sh
- This is a sample `.sh` bash script executable that I would be able to submit to the HPC
