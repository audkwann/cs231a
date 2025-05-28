import os
import subprocess

os.makedirs("frames", exist_ok=True)

# loop through all .mp4 files 
for filename in os.listdir("."):
  if filename.endswith(".mp4"):
    name = os.path.splitext(filename)[0]  # remove .mp4
    out_dir = os.path.join("frames", name)
    os.makedirs(out_dir, exist_ok=True)

    # extract frames
    output_pattern = os.path.join(out_dir, "frame_%04d.jpg")
    cmd = ["ffmpeg", "-i", filename, "-vf", "fps=1,scale=1920:1080,setdar=16/9", output_pattern]
    subprocess.run(cmd)
