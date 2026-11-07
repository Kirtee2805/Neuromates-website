import re

with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# find nav start and end
nav_start = content.find('<nav id="nav">')
nav_end = content.find('</nav>', nav_start) + 6
nav_html = content[nav_start:nav_end]

# remove base64 img data for clean viewing
clean_nav = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', '[BASE64_IMAGE]', nav_html)
print(clean_nav)

