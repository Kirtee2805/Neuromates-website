from PIL import Image

p = r"D:\Neuromates(website)\assets\images\logo.png"
im = Image.open(p).convert("RGBA")
pixels = im.load()
w, h = im.size

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # Any near-white pixel (where r, g, b are all high)
        if r > 218 and g > 218 and b > 218:
            pixels[x, y] = (r, g, b, 0)
        elif r > 195 and g > 195 and b > 195 and abs(r - g) < 18 and abs(g - b) < 18:
            # Neutral light grey/white edge antialiasing
            alpha = int(255 * max(0.0, (218 - min(r, g, b)) / 23.0))
            pixels[x, y] = (r, g, b, alpha)

im.save(p, "PNG")
print("Verified clean transparent background.")
corners = [im.getpixel((0,0)), im.getpixel((0, h-1)), im.getpixel((w-1, 0)), im.getpixel((w-1, h-1))]
print("Corners:", corners)

