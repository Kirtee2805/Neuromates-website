with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
s = scripts[1]

# let's find makeCore and makeDevices
for fn_name in ['makeCore', 'makeDevices']:
    pos = s.find('function ' + fn_name)
    if pos != -1:
        print("="*40, fn_name, "="*40)
        print(s[pos:pos+2500])

