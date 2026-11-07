with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

import re
matches = re.findall(r'(\b\w*pd\w*\b|\b\w*gf\w*\b|\b\w*safe zone\w*\b)', t, re.IGNORECASE)
print("Unique words matching gf/pd/safe zone:", set(matches[:30]))

pos = t.find('Drag the patient dot')
print(t[pos:pos+1500])

scripts = re.findall(r'<script>(.*?)</script>', t, re.DOTALL)
print("Total script tags:", len(scripts))
for i, s in enumerate(scripts):
    if 'pd' in s or 'gf' in s or 'boundary' in s or 'alzheimers' in s:
        print(f"Script {i} contains keywords, len={len(s)}")
        print(s[:400])

