import os
import shutil
from PIL import Image

print("Updating logo-icon.png and chat launcher...")

# 1. Update logo-icon.png
src_centered = 'assets/images/logo-icon-centered.png'
dst_icon = 'assets/images/logo-icon.png'
if os.path.exists(src_centered):
    shutil.copy2(src_centered, dst_icon)
    print("Copied logo-icon-centered.png to assets/images/logo-icon.png")
else:
    im_icon = Image.open('assets/images/logo-icon.png')
    bbox = im_icon.getbbox()
    cropped = im_icon.crop(bbox)
    canvas = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    scale = min(175 / cropped.width, 175 / cropped.height)
    new_w = int(cropped.width * scale)
    new_h = int(cropped.height * scale)
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    x = (256 - new_w) // 2
    y = (256 - new_h) // 2
    canvas.paste(resized, (x, y), resized)
    canvas.save(dst_icon)
    print("Created and saved centered assets/images/logo-icon.png")

# 2. Update assets/js/chat-widget.js
chat_js_path = 'assets/js/chat-widget.js'
with open(chat_js_path, 'r', encoding='utf-8') as f:
    chat_js = f.read()

# Replace border-radius: 50% on icon-launcher-logo with border-radius: 0 and object-fit: contain
old_logo_css = """    #neuro-chat-launcher .icon-launcher-logo {
      width: 40px;
      height: 40px;
      object-fit: contain;
      border-radius: 50%;
      transition: transform 0.3s ease, opacity 0.2s ease;
      pointer-events: none;
    }"""

new_logo_css = """    #neuro-chat-launcher .icon-launcher-logo {
      width: 40px;
      height: 40px;
      object-fit: contain;
      border-radius: 0 !important;
      transition: transform 0.3s ease, opacity 0.2s ease;
      pointer-events: none;
      display: block;
    }"""

if old_logo_css in chat_js:
    chat_js = chat_js.replace(old_logo_css, new_logo_css)
    print("Updated #neuro-chat-launcher .icon-launcher-logo in chat-widget.js")
else:
    chat_js = chat_js.replace("border-radius: 50%;\n      transition: transform 0.3s ease, opacity 0.2s ease;", "border-radius: 0 !important;\n      transition: transform 0.3s ease, opacity 0.2s ease;\n      display: block;")
    print("Applied relaxed replacement for icon-launcher-logo in chat-widget.js")

with open(chat_js_path, 'w', encoding='utf-8') as f:
    f.write(chat_js)

print("Done updating chat-widget.js")

