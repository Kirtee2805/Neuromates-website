import os, glob

user_uploaded = r"C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded"
files = os.listdir(user_uploaded)
print("Uploaded files in .user_uploaded:")
for f in files:
    full = os.path.join(user_uploaded, f)
    print(f"  {f} ({os.path.getsize(full)} bytes)")

img_dir = r"D:\Neuromates(website)\assets\images"
print("\nFiles in assets/images:")
for f in os.listdir(img_dir):
    full = os.path.join(img_dir, f)
    if "logo" in f.lower() or "brain" in f.lower() or "icon" in f.lower():
        print(f"  {f} ({os.path.getsize(full)} bytes)")

