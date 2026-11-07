import shutil
import os

src_dir = r"C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded"
dest_dir = r"D:\Neuromates(website)\assets\images"

files_to_copy = [
    ("media_1793972009262_88238da9.jpg", "ecosystem-architecture-live.jpg"),
    ("media_1793972112096_ad5acc04.jpg", "the-challenge-reality.jpg"),
    ("media_1793971622655_4550a9af.png", "user-screenshot-memory.png"),
    ("media_1793971706231_90ef0cc5.jpg", "user-screenshot-about.jpg")
]

for src_name, dest_name in files_to_copy:
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_name} -> {dest_name} ({os.path.getsize(dest_path)} bytes)")
    else:
        print(f"NOT FOUND: {src_path}")

