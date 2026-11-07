with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'.{0,50}\broute\b.{0,50}', html)
for m in matches:
    print('ROUTE:', m)

