from PIL import Image

p = r"D:\Neuromates(website)\assets\images\brain-tech-logo.jpg"
im = Image.open(p)
print("brain-tech-logo size:", im.size)
# Sample colors from corners and center
print("Corner (0,0):", im.getpixel((0,0)))
print("Center:", im.getpixel((im.width//2, im.height//2)))

