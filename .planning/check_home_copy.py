with open('neuromates-home.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'WebGLRenderer', text):
    print(text[m.start()-50:m.start()+200])
    print('---')

