import re

with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

nav_match = re.search(r'<nav id="nav">.*?</nav>', content, re.DOTALL)
if nav_match:
    print("NAV MARKUP:")
    print(nav_match.group(0))

footer_match = re.search(r'<footer>.*?</footer>', content, re.DOTALL)
if footer_match:
    print("\nFOOTER MARKUP:")
    print(footer_match.group(0))

