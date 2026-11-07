with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.pin[^{]*\{[^}]*\})', html)
for m in matches:
    print("PIN CSS:", m)

matches2 = re.findall(r'(#e-story[^{]*\{[^}]*\})', html)
for m in matches2:
    print("E-STORY CSS:", m)

