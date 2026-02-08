from __future__ import annotations
from pipeline_utils import DEFAULT_MODEL_ID, load_text2img, get_device, make_generator, to_img2img
from PIL import Image, ImageOps

import os
from PIL import Image
from pipeline_utils import DEFAULT_MODEL_ID, load_text2img, get_device, make_generator


def run_img2img_experiments() -> None:
    model_id = DEFAULT_MODEL_ID
    seed = 42
    scheduler_name = "EulerA"
    steps = 30
    guidance = 7.5

    # Image source produit (à fournir dans TP2/inputs/)
    init_path = "TP2/inputs/product.jpg"  # <- adapte si ton fichier a un autre nom

    prompt = "ultra-realistic product photo, clean white background, studio lighting, soft shadow, very sharp"
    negative = "text, watermark, logo, low quality, blurry, deformed"

    strengths = [
        ("run07_strength035", 0.35),
        ("run08_strength060", 0.60),
        ("run09_strength085", 0.85),
    ]

    pipe_t2i = load_text2img(model_id, scheduler_name)
    pipe_i2i = to_img2img(pipe_t2i)

    # Charger image source
    init_image = Image.open(init_path).convert("RGB")
    # Option recommandé: forcer 512×512 proprement (grille + comparaisons faciles)
    init_image = ImageOps.fit(init_image, (512, 512), method=Image.Resampling.LANCZOS)

    # Sauvegarde "avant" (utile pour le rapport)
    save(init_image, "outputs/i2i_source.png")

    device = get_device()

    for name, strength in strengths:
        # IMPORTANT: recréer le generator à chaque run pour reproductibilité strictement identique (seed fixe)
        g = make_generator(seed, device)

        out = pipe_i2i(
            prompt=prompt,
            image=init_image,
            strength=strength,
            negative_prompt=negative,
            num_inference_steps=steps,
            guidance_scale=guidance,
            generator=g,
        )

        img = out.images[0]
        save(img, f"outputs/i2i_{name}.png")
        print(
            "I2I",
            name,
            {"scheduler": scheduler_name, "seed": seed, "steps": steps, "guidance": guidance, "strength": strength},
        )

def save(img: Image.Image, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)

def run_text2img_experiments() -> None:
    model_id = DEFAULT_MODEL_ID
    seed = 42

    # Prompt e-commerce (unique, en anglais, stable)
    prompt = "ultra-realistic product photo of a leather sneaker on a white background, studio lighting, soft shadow, 85mm lens, very sharp"
    negative = "text, watermark, logo, low quality, blurry, deformed"

    plan = [
        # name, scheduler, steps, guidance
        ("run01_baseline", "EulerA", 30, 7.5),
        ("run02_steps15", "EulerA", 15, 7.5),
        ("run03_steps50", "EulerA", 50, 7.5),
        ("run04_guid4",  "EulerA", 30, 4.0),
        ("run05_guid12", "EulerA", 30, 12.0),
        ("run06_ddim",   "DDIM",   30, 7.5),
    ]

    for name, scheduler_name, steps, guidance in plan:
        pipe = load_text2img(model_id, scheduler_name)
        device = get_device()
        g = make_generator(seed, device)

        out = pipe(
            prompt=prompt,
            negative_prompt=negative,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=512,
            width=512,
            generator=g,
        )

        img = out.images[0]
        save(img, f"outputs/t2i_{name}.png")
        print("T2I", name, {"scheduler": scheduler_name, "seed": seed, "steps": steps, "guidance": guidance})


def main() -> None:
    run_img2img_experiments()

if __name__ == "__main__":
    main()
