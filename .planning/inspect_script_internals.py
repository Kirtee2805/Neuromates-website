with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
for i, s in enumerate(scripts):
    if len(s) > 100:
        print(f"=== Script {i} (len: {len(s)}) ===")
        # print function definitions in s
        funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)', s)
        consts = re.findall(r'const\s+([a-zA-Z0-9_]+)\s*=', s)
        print("Functions:", funcs[:15])
        print("Consts:", consts[:15])
        # Search for makeCore or THREE
        if 'makeCore' in s or 'THREE' in s:
            print("Found THREE in script!")

