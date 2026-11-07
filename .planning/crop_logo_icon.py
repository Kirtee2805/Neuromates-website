from PIL import Image

p = r"D:\Neuromates(website)\assets\images\logo.png"
im = Image.open(p)
print("logo.png size:", im.size, im.mode)

# Find the bounding box of non-transparent pixels on the left (the brain emblem)
# In logo.png, the emblem is roughly in the left 70-80 pixels
emblem = im.crop((0, 0, 72, im.height))
bbox = emblem.getbbox()
print("emblem bbox:", bbox)
cropped_emblem = emblem.crop(bbox)
print("cropped emblem size:", cropped_emblem.size)

# Create a clean square icon with transparent padding
sq_size = max(cropped_emblem.width, cropped_emblem.height) + 8
icon = Image.new("RGBA", (sq_size, sq_size), (0, 0, 0, 0))
offset = ((sq_size - cropped_emblem.width) // 2, (sq_size - cropped_emblem.height) // 2)
icon.paste(cropped_emblem, offset)
icon.save(r"D:\Neuromates(website)\assets\images\logo-icon.png", "PNG")
print("Saved assets/images/logo-icon.png successfully! Size:", icon.size)

