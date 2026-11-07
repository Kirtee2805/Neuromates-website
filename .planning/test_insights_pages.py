import os

insights_dir = r'D:\Neuromates(website)\insights'
files = [
    'index.html',
    'research.html',
    'articles.html',
    'case-studies.html',
    'resources.html'
]

for f in files:
    fp = os.path.join(insights_dir, f)
    assert os.path.exists(fp), f"Missing {f}!"
    with open(fp, 'r', encoding='utf-8') as fp_in:
        content = fp_in.read()
    print(f"Testing {f}: {len(content)} bytes")
    assert '<!doctype html>' in content.lower(), f"Missing doctype in {f}"
    assert '<title>' in content.lower(), f"Missing title in {f}"
    assert '<h1' in content.lower(), f"Missing h1 in {f}"
    assert 'id="nav"' in content, f"Missing nav in {f}"
    assert 'id="global-footer"' in content, f"Missing footer in {f}"
    assert 'id="global-cta"' in content, f"Missing cta in {f}"
    print(f"  -> PASSED: {f}")
print("ALL 5 INSIGHTS PAGES VERIFIED!")

