import os
import subprocess

path = "NOAA_dataset/Puako Site 1 2017-02-03 Transect 1"

def run_colmap(cmd_args, cwd=None):
    subprocess.run(cmd_args, cwd=cwd, check=True)

db_path = os.path.join(scene_path, "colmap.db")
sparse_path = os.path.join(scene_path, "sparse")
sparse_model_path = os.path.join(sparse_path, "0")

if not os.path.exists(sparse_model_path):
    os.makedirs(sparse_path, exist_ok=True)

    # feature extraction
    run_colmap(["colmap", "feature_extractor", "--database_path", db_path, "--image_path", path, "--ImageReader.single_camera", "1"])

    # feature matching
    run_colmap(["colmap", "exhaustive_matcher", "--database_path", db_path])

    #sparse reconstruction
    run_colmap(["colmap", "mapper", "--database_path", db_path, "--image_path", path, "--output_path", sparse_path])

# undistortion
undistorted_images_path = os.path.join(path, "images")
if not os.path.exists(undistorted_images_path):
    run_colmap(["colmap", "image_undistorter", "--image_path", path, "--input_path", sparse_model_path, "--output_path", path, "--output_type", "COLMAP"])
