import shutil
import os

src_dir = r"C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded"
dest_dir = r"D:\Neuromates(website)\assets\images"

mapping = [
    ("media_1794031755416_b7d58e57.jpg", "ai-movement-monitoring.jpg"),
    ("media_1794031769041_2ea33bc7.jpg", "ai-brain-monitoring.jpg"),
    ("media_1794031781069_7b5d56ea.jpg", "ai-memory-routine.jpg"),
    ("media_1794031793758_7f3cbb88.jpg", "ai-interactive-rehab.jpg")
]

for src, dst in mapping:
    s = os.path.join(src_dir, src)
    d = os.path.join(dest_dir, dst)
    shutil.copy2(s, d)
    print(f"Copied {src} -> {dst} ({os.path.getsize(d)} bytes)")

