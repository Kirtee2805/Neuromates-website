import re
import base64

with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

m = re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)', content)
if m:
    b64_data = m.group(1)
    img_bytes = base64.b64decode(b64_data)
    with open(r'D:\Neuromates(website)\assets\images\logo.png', 'wb') as fp:
        fp.write(img_bytes)
    print("Saved logo.png successfully, size:", len(img_bytes))
else:
    print("Logo base64 not found!")

