from PIL import Image

p = r"C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded\media_1793972434532_b0a8c7d9.jpg"
im = Image.open(p)
print("media_1793972434532_b0a8c7d9.jpg size:", im.size)
# Sample colors
print("Pixel (10, 10):", im.getpixel((10, 10)))
print("Pixel (200, 100):", im.getpixel((200, 100)))

