import os
import glob
import re

for html_file in glob.glob('**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        text = f.read()
    if '.breadcrumb' in text:
        m = re.findall(r'(\.breadcrumb[^{]*\{[^}]*\})', text)
        if m:
            print(f'=== {html_file} ===')
            for rule in m:
                print(rule)

