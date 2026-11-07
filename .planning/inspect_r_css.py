with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.r\b[^{]*\{[^}]*\})', html)
for m in matches:
    print(".r CSS:", m)

matches2 = re.findall(r'(\.in\b[^{]*\{[^}]*\})', html)
for m in matches2:
    print(".in CSS:", m)

