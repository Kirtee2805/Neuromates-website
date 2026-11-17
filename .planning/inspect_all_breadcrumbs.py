import glob
import re

files_with_breadcrumb = [
    'insights/index.html',
    'insights/research.html',
    'insights/resources.html',
    'technology/ai-machine-learning.html',
    'technology/connected-care-platform.html',
    'technology/connected-devices.html',
    'technology/index.html',
    'technology/monitoring-analytics.html',
    'about/index.html',
    'about/impact.html',
    'about/our-approach.html',
    'about/vision-mission.html',
    'contact.html',
    'epilepsy-care.html',
    'products/epilepsy-care.html'
]

breadcrumb_regex = re.compile(r'<nav class="breadcrumb"[^>]*>.*?</nav>\s*', re.DOTALL)

for fn in files_with_breadcrumb:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        m = breadcrumb_regex.search(content)
        if m:
            print(f'=== {fn} ===')
            print(m.group(0)[:150].strip())
    except Exception as e:
        print(f'Error reading {fn}: {e}')

