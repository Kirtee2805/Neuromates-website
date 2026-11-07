from PIL import Image, ImageEnhance, ImageFilter
import os

img_dir = r"D:\Neuromates(website)\assets\images"
files = [
    "ai-movement-monitoring.jpg",
    "ai-brain-monitoring.jpg",
    "ai-memory-routine.jpg",
    "ai-interactive-rehab.jpg"
]

for fname in files:
    fpath = os.path.join(img_dir, fname)
    if not os.path.exists(fpath):
        print(f"Not found: {fpath}")
        continue
    
    im = Image.open(fpath)
    orig_w, orig_h = im.size
    print(f"Original {fname}: {orig_w}x{orig_h}")
    
    # Target 2.5x upscale for crisp Retina / high-DPI rendering
    target_w = int(orig_w * 2.5)
    target_h = int(orig_h * 2.5)
    
    # High-quality Lanczos upscale
    upscaled = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Mild unsharp mask for crisp text and edge details
    sharpened = upscaled.filter(ImageFilter.UnsharpMask(radius=1.8, percent=130, threshold=3))
    
    # Color contrast enhancement
    enhancer = ImageEnhance.Contrast(sharpened)
    enhanced = enhancer.enhance(1.04)
    
    # Save with high JPEG quality
    enhanced.save(fpath, "JPEG", quality=96, optimize=True)
    print(f"Enhanced {fname} -> {target_w}x{target_h} ({os.path.getsize(fpath)} bytes)")

print("All AI images enhanced and upscaled successfully!")

