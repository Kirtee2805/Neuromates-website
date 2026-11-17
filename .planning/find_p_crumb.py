import glob
import re

for html_file in glob.glob('**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'<p class="crumb"[^>]*>.*?</p>', text)
    if matches:
        print(f'=== {html_file} ===')
        for m in matches:
            print('  ', m)
