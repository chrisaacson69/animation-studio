import torch
from PIL import Image
import sys
sys.path.insert(0, "/workspace/ComfyUI")

from comfy.sd import load_checkpoint_guess_config
import comfy.utils
import nodes

print("Loading SDXL model...")

with torch.inference_mode():
    loader = nodes.CheckpointLoaderSimple()
    # Just the filename — ComfyUI looks in its own models/checkpoints/ folder
    model, clip, vae = loader.load_checkpoint("sd_xl_base_1.0.safetensors")
    
    prompt_text = "flat 2D cutout animation character, ancient Greek philosopher Aristotle, simple shapes, bold colors, cartoon style like South Park or Terrance and Phillip, white toga, holding a scroll, front facing, solid color background, no shadows"
    negative_text = "3D, realistic, photographic, complex, detailed shading, gradient background"
    
    encoder = nodes.CLIPTextEncode()
    positive = encoder.encode(clip, prompt_text)[0]
    negative = encoder.encode(clip, negative_text)[0]
    
    empty = nodes.EmptyLatentImage()
    latent = empty.generate(1024, 1024, 1)[0]
    
    sampler = nodes.KSampler()
    result = sampler.sample(model, seed=42, steps=25, cfg=7.0,
                           sampler_name="euler", scheduler="normal",
                           positive=positive, negative=negative,
                           latent_image=latent, denoise=1.0)
    
    decoder = nodes.VAEDecode()
    images = decoder.decode(vae, result[0])[0]
    
    img_array = images[0].cpu().numpy()
    img = Image.fromarray((img_array * 255).astype("uint8"))
    img.save("/workspace/studio/assets/characters/test_aristotle.png")
    print(f"Saved! Size: {img.size}")

