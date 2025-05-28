import os
import subprocess

INPUT_DIR = "NOAA_dataset/Puako Site 1 2017-02-03 Transect 1"
OUTPUT_DIR = "NOAA_dataset/Puako Site 1 2017-02-03 Transect 1"

def run_colmap(cmd_args, cwd=None):
    print(f"Running: {' '.join(cmd_args)}")
    subprocess.run(cmd_args, cwd=cwd, check=True)

scene_path = INPUT_DIR
db_path = os.path.join(scene_path, "colmap.db")
sparse_path = os.path.join(scene_path, "sparse")
sparse_model_path = os.path.join(sparse_path, "0")
output_scene_path = OUTPUT_DIR

if not os.path.exists(sparse_model_path):
    os.makedirs(sparse_path, exist_ok=True)

    # feature extraction
    run_colmap(["colmap", "feature_extractor", "--database_path", db_path, "--image_path", scene_path, "--ImageReader.single_camera", "1"])

    # feature matching
    run_colmap(["colmap", "exhaustive_matcher", "--database_path", db_path])

    #sparse reconstruction
    run_colmap(["colmap", "mapper", "--database_path", db_path, "--image_path", scene_path, "--output_path", sparse_path])

# undistortion
if not os.path.exists(output_scene_path):
    os.makedirs(output_scene_path, exist_ok=True)
undistorted_images_path = os.path.join(output_scene_path, "images")
if not os.path.exists(undistorted_images_path):
    run_colmap(["colmap", "image_undistorter", "--image_path", scene_path, "--input_path", sparse_model_path, "--output_path", output_scene_path, "--output_type", "COLMAP"])