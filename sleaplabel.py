import os
import subprocess
project_dir = '/grid/shea/data/Karin/tutorialmaking/morekatiesvideosmodeling/keypointmoseqwork/' #CHANGE HERE
sleap_model_path = '/grid/shea/data/Karin/tutorialmaking/morekatiesvideosmodeling/sleapstuff/240709_092906.multi_instance.n=1301' #CHANGE HERE the directory of your sleap model here

slp_output_dir = os.path.join(project_dir, 'slp_files')
video_dir = os.path.join(project_dir, 'videos')

# Create 'slp files' directory if it does not exist
if not os.path.exists(slp_output_dir):
    os.makedirs(slp_output_dir)

max_tracks = 1 #number of animals you are tracking
tracker = 'simplemaxtracks'
for filename in os.listdir(video_dir):
    if filename.endswith('.mp4'):
        input_file = os.path.join(video_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.slp'
        output_file_path = os.path.join(slp_output_dir, output_filename)
        sleap_track_command = f"sleap-track -m {sleap_model_path} " \
                              f"--tracking.tracker {tracker} " \
                              f"--tracking.max_tracking {1} " \
                              f"--tracking.max_tracks {max_tracks} " \
                              f"-o {output_file_path} " \
                              f"{input_file}"
        try:
                # Execute the command
                subprocess.run(sleap_track_command, shell=True, check=True)
                print(f'labeled {filename} and saved as {os.path.basename(filename)}')
        except subprocess.CalledProcessError as e:
            print(f'Error processing {filename}: {e}')
