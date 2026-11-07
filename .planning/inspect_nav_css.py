with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
style = re.search(r'<style>(.*?)</style>', content, re.DOTALL).group(1)
pos = style.find('#nav')
if pos != -1:
    print(style[pos:pos+2000])

