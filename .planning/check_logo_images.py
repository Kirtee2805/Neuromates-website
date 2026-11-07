from PIL import Image

for name in ["media_1793972434532_b0a8c7d9.jpg", "media_1793971622655_4550a9af.png"]:
    p = r"C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded\\" + name
    im = Image.open(p)
    print(name, im.size, im.mode)

p2 = r"D:\Neuromates(website)\assets\images\brain-tech-logo.jpg"
im2 = Image.open(p2)
print("brain-tech-logo.jpg", im2.size, im2.mode)

p3 = r"D:\Neuromates(website)\assets\images\logo.png"
im3 = Image.open(p3)
print("logo.png", im3.size, im3.mode)

