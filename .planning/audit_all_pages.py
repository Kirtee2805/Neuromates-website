import os
import re

root_dir = r'D:\Neuromates(website)'
all_pages = [
    'index.html',
    'neuromates-home.html',
    'neuromates-products.html',
    'products.html',
    'technology/index.html',
    'technology/connected-devices.html',
    'technology/ai-machine-learning.html',
    'technology/monitoring-analytics.html',
    'technology/connected-care-platform.html',
    'insights/index.html',
    'insights/research.html',
    'insights/resources.html'
]

print("=== CHECKING RESPONSIVENESS & CONSTRAINTS ===")
for rel_path in all_pages:
    fp = os.path.join(root_dir, rel_path.replace('/', os.sep))
    if not os.path.exists(fp):
        print(f"MISSING FILE: {rel_path}")
        continue
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Viewport check
    has_viewport = 'name="viewport"' in html
    # 2. Clamped font sizes
    has_clamp = 'clamp(' in html
    # 3. Media queries
    has_mq = '@media' in html or 'tokens.css' in html
    # 4. Strict epilepsy wording check if epilepsy is mentioned
    epilepsy_ok = True
    if 'epilepsy' in html.lower():
        if 'abnormal eeg signals that may indicate a seizure' not in html.lower():
            # check if it's the specific safe wording
            epilepsy_ok = False

    print(f"[{rel_path}] Viewport: {has_viewport}, Clamp: {has_clamp}, MQ: {has_mq}, Size: {len(html)} bytes")
    if not epilepsy_ok:
        print(f"  WARNING: Epilepsy wording check failed in {rel_path}!")

print("\n=== CHECKING THAT UNWANTED PAGES WERE REMOVED ===")
removed_pages = ['insights/articles.html', 'insights/case-studies.html']
for rp in removed_pages:
    fp = os.path.join(root_dir, rp.replace('/', os.sep))
    print(f"{rp} exists:", os.path.exists(fp))

