from PIL import Image

p = r"D:\Neuromates(website)\assets\images\page_1_Image-7098480789.jpg"
im = Image.open(p)
print("page_1_Image-7098480789.jpg size:", im.size)
# Let's crop the emblem or check if there's an emblem
bbox = im.getbbox()
print("bbox:", bbox)

