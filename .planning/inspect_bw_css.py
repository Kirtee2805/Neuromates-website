with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

import re
matches = re.findall(r'(\.bw[^{]*\{[^}]*\}|\.hl[^{]*\{[^}]*\})', t)
for m in matches:
    print(m)

