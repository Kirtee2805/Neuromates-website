with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
style = re.search(r'<style>(.*?)</style>', content, re.DOTALL).group(1)

# Find any rule mentioning nav or dd or mb
rules = style.split('}')
for r in rules:
    if any(k in r for k in ['nav', '.dd', '#mb', '.fn', 'fg', '.fb']):
        print(r + '}')

