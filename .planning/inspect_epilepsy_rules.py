with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'([^{}]*epilepsy[^{}]*\{[^}]*\})', html)
for m in matches:
    print("EPILEPSY RULE:", m)

