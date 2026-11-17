import os
import shutil
from PIL import Image

print("Step 1: Installing perfect high-res logo-icon.png...")
src = 'assets/images/logo-icon-perfect.png'
dst = 'assets/images/logo-icon.png'
shutil.copy2(src, dst)
print("Copied logo-icon-perfect.png to logo-icon.png successfully.")

# Verify bbox and dimensions
im = Image.open(dst)
print("logo-icon.png size:", im.size, "bbox:", im.getbbox())

