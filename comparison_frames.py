import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

eval_dir = "renders/ps1t1_eval"
frame_id = "0003"

gt = f"eval_gt_{frame_id}.png"
rgb = f"eval_rgb_{frame_id}.png"
obj = f"eval_rgb_object_{frame_id}.png"
med = f"eval_rgb_medium_{frame_id}.png"
clear = f"eval_rgb_clear_{frame_id}.png"
depth = f"eval_depth_{frame_id}.png"

def load_image(name):
    path = os.path.join(eval_dir, name)
    return np.array(Image.open(path).convert("RGB"))

def load_depth(name):
    path = os.path.join(eval_dir, name)
    return np.array(Image.open(path))

gt_img = load_image(gt)
rgb_img = load_image(rgb)
obj_img = load_image(obj)
med_img = load_image(med)
clear_img = load_image(clear)
depth_img = load_depth(depth)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.ravel()
titles = ["Ground Truth", "Full Prediction", "Object Only", "Medium Only", "Ideal Water", "Depth Map"]
images = [gt_img, rgb_img, obj_img, med_img, clear_img, depth_img]

for ax, img, title in zip(axs, images, titles):
    # ensure depth map is grayscale
    ax.imshow(img if title != "Depth Map" else img, cmap="gray" if title == "Depth Map" else None)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
output_path = os.path.join(eval_dir, f"comparison_{frame_id}.png")
plt.savefig(output_path, dpi=150)
plt.close()