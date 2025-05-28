# Reconstructing Artifact-Free 3D Scenes of Coral Reefs

This GitHub Repository contains the code relating to "Reconstructing Artifact-Free 3D Scenes of Coral Reefs" for CS231A Spring 2025.

The original WaterSplatting code can be found here: https://github.com/water-splatting/water-splatting/tree/main
The original nerfstudio code can be found here: https://github.com/nerfstudio-project/nerfstudio/tree/main/nerfstudio

The following WaterSplatting files were altered:
- water_splatting.py

The following nerfstudio files were altered:
- base_dataset.py
- full_images_datamanager.py
- render.py
- trainer.py
- viewer.py

The following files were created for this project:
- create_dataset.py: extracts frames one second apart from input videos
- run_colmap.py: preprocesses the data with COLMAP
- comparison_frames.py: produces comparison frames to visualize the outputs

This repository also contains zip files to the NOAA Dataset (sectioned by dive site), the SeaThruNeRF dataset, and a small semantic segmentation dataset (subset of 50 images from MS7T2).
