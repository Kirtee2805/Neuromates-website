with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,40}\bes\b.{0,40}', text)
for m in matches[:10]:
    print('MATCH:', m)

