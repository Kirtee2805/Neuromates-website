with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'WebGLRenderer', text)]
for m in matches:
    print('--- MATCH AT', m, '---')
    print(text[m-80:m+600])

canvas_matches = [m.start() for m in re.finditer(r'<canvas', text)]
for m in canvas_matches:
    print('--- CANVAS AT', m, '---')
    print(text[m-20:m+250])

