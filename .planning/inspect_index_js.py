import re

with open(r'd:\Neuromates(website)\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

scripts = re.findall(r'<script.*?</script>', c, re.DOTALL)
s1 = scripts[1]
pos = s1.find('ICON=')
if pos != -1:
    end_icon = s1.find('";', pos)
    print("Code after ICON:")
    print(s1[end_icon+2:])

