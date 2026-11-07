with open(r'D:\Neuromates(website)\Products _ Neuro Mates.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
for s in scripts:
    if 'v-' in s or 'hash' in s or 'overview' in s:
        print("Found matching script segment:")
        for line in s.split('\n')[:25]:
            print("  ", line)

