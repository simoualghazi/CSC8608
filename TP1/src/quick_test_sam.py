import numpy as np
import cv2
from pathlib import Path
from sam_utils import load_sam_predictor, predict_mask_from_box, get_device

# Prend la première image trouvée (jpg/png)
imgs = list(Path("TP1/data/images").glob("*.png")) + list(Path("TP1/data/images").glob("*.png"))
if not imgs:
    raise FileNotFoundError("Aucune image trouvée dans TP1/data/images")

img_path = imgs[0]
bgr = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

ckpt = "TP1/models/sam_vit_h_4b8939.pth"   
model_type = "vit_h"

print("device:", get_device())
print("image:", img_path, "shape:", rgb.shape, "dtype:", rgb.dtype)

pred = load_sam_predictor(ckpt, model_type=model_type)

# bbox à la main (à adapter si besoin)
box = np.array([50, 50, min(250, rgb.shape[1]-1), min(250, rgb.shape[0]-1)], dtype=np.int32)

mask, score = predict_mask_from_box(pred, rgb, box, multimask=True)
print("box:", box.tolist())
print("mask shape:", mask.shape, "mask dtype:", mask.dtype)
print("score:", score, "mask_sum:", int(mask.sum()))
