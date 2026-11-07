with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's inspect CSS style block
import re
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if css_match:
    print("CSS length:", len(css_match.group(1)))
    print("CSS preview (first 1000 chars):")
    print(css_match.group(1)[:1000])

# Let's inspect nav and footer
nav_match = re.search(r'(<nav.*?</nav>)', content, re.DOTALL)
if nav_match:
    print("\nNAV preview (first 1000 chars):")
    print(nav_match.group(1)[:1000])

footer_match = re.search(r'(<footer.*?</footer>)', content, re.DOTALL)
if footer_match:
    print("\nFOOTER preview (first 1000 chars):")
    print(footer_match.group(1)[:1000])

# Let's inspect scripts
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
print(f"\nTotal script tags: {len(scripts)}")
for i, sc in enumerate(scripts):
    print(f"Script {i+1} length: {len(sc)} preview: {sc[:200]}...")

