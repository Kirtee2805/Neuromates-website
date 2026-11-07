with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'([^{}]*\{[^}]*clip-path[^}]*\})', html)
for m in matches:
    print("CLIP-PATH RULE:", m)

