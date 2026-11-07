with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.wp[^{]*\{[^}]*\})', html)
for m in matches:
    print("WP CSS:", m)

matches2 = re.findall(r'(\.hl[^{]*\{[^}]*\})', html)
for m in matches2:
    print("HL CSS:", m)

matches3 = re.findall(r'(\.go[^{]*\{[^}]*\})', html)
for m in matches3:
    print("GO CSS:", m)

