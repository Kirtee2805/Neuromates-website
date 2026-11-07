with open(r'D:\Neuromates(website)\Products _ Neuro Mates.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\x27]([^"\x27]+)["\x27]', content)
print("Sections in Products page:", sections)

# check views / tabs or product IDs
div_ids = re.findall(r'id=["\x27]([a-zA-Z0-9_\-]+)["\x27]', content)
print("All IDs in Products page (first 30):", div_ids[:30])

