from PIL import Image

p = r"D:\Neuromates(website)\assets\images\logo.png"
im = Image.open(p).convert("RGBA")
w, h = im.size

# Sample pixels
data = im.getdata()
near_white = 0
colored = 0

for r, g, b, a in data:
    if r > 225 and g > 225 and b > 225:
        near_white += 1
    else:
        colored += 1

print(f"Total pixels: {len(data)}, Near-white background: {near_white}, Colored artwork: {colored}")

