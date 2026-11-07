import os
from bs4 import BeautifulSoup

tech_dir = r'D:\Neuromates(website)\technology'
files = [
    'index.html',
    'connected-devices.html',
    'ai-machine-learning.html',
    'monitoring-analytics.html',
    'connected-care-platform.html'
]

for f in files:
    fp = os.path.join(tech_dir, f)
    if not os.path.exists(fp):
        print(f"ERROR: {f} does not exist!")
        continue
    with open(fp, 'r', encoding='utf-8') as fp_in:
        content = fp_in.read()
    print(f"Testing {f}: {len(content)} bytes")
    # check for doctype, title, h1, nav, footer
    assert '<!doctype html>' in content.lower(), f"Missing doctype in {f}"
    assert '<title>' in content.lower(), f"Missing title in {f}"
    assert '<h1' in content.lower(), f"Missing h1 in {f}"
    assert 'id="nav"' in content, f"Missing nav in {f}"
    assert 'id="global-footer"' in content, f"Missing footer in {f}"
    assert 'Illustration' in content, f"Missing illustration badge in {f}"
    print(f"  -> PASSED basic structure check!")
print("ALL 5 TECHNOLOGY PAGES VERIFIED!")

