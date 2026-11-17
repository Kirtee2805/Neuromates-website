with open('assets/css/tokens.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.hero[^{]*\{[^}]*\})', text)
for m in matches[:10]:
    print('--- HERO ---')
    print(m)

matches2 = re.findall(r'(\.breadcrumb[^{]*\{[^}]*\})', text)
for m in matches2[:5]:
    print('--- BREADCRUMB ---')
    print(m)
