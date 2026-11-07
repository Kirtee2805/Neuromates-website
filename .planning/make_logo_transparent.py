from PIL import Image
import shutil

p = r"D:\Neuromates(website)\assets\images\logo.png"
p_backup = r"D:\Neuromates(website)\assets\images\logo-backup.png"
shutil.copy2(p, p_backup)

im = Image.open(p).convert("RGBA")
pixels = im.load()
w, h = im.size

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # Calculate brightness / minimum color distance from white
        min_c = min(r, g, b)
        max_c = max(r, g, b)
        
        # If the pixel is close to pure white/light grey
        if min_c > 240:
            # Fully transparent
            pixels[x, y] = (r, g, b, 0)
        elif min_c > 210:
            # Smooth antialiased edge
            alpha_frac = (240 - min_c) / 30.0
            new_a = int(255 * max(0.0, min(1.0, alpha_frac)))
            pixels[x, y] = (r, g, b, new_a)

im.save(p, "PNG")
print(f"Processed {p} successfully with true transparent background!")

# Verify new corners
im2 = Image.open(p)
corners = [im2.getpixel((0,0)), im2.getpixel((0, h-1)), im2.getpixel((w-1, 0)), im2.getpixel((w-1, h-1))]
print("New corners (should all have alpha=0):", corners)

