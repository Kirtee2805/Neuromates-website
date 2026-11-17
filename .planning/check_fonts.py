with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('Google fonts:', re.findall(r'fonts\.googleapis\.com[^\'\"\)]+', text))
print('--fd:', re.findall(r'--fd:[^;]+;', text))
print('--fb:', re.findall(r'--fb:[^;]+;', text))
print('head link tags for css:', re.findall(r'<link[^>]+stylesheet[^>]*>', text))

