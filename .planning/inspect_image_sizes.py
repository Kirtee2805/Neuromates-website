import os
from PIL import Image

img_dir = r'D:\Neuromates(website)\assets\images'
for fn in os.listdir(img_dir):
    if fn.endswith(('.jpg', '.png')):
        fp = os.path.join(img_dir, fn)
        try:
            with Image.open(fp) as im:
                print(f"{fn}: {im.size[0]}x{im.size[1]}, format={im.format}, size={os.path.getsize(fp)/1024:.1f}KB")
        except Exception as e:
            print(f"{fn}: error {e}")

