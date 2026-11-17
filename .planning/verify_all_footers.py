import os, re

files = []
for root, dirs, files_in_dir in os.walk('.'):
    if '.git' in root or '.planning' in root:
        continue
    for f in files_in_dir:
        if f.endswith('.html'):
            files.append(os.path.join(root, f))

print(f"Total HTML files to verify: {len(files)}")
success_count = 0
for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    
    # Check footer presence
    has_footer = '<footer' in text
    uses_shared = 'shared.js' in text
    has_direct_markup = 'nm-footer-wrap' in text
    
    if not has_footer:
        print(f"[FAIL] {f} has NO <footer> tag!")
    elif uses_shared or has_direct_markup:
        success_count += 1
    else:
        print(f"[WARN] {f} footer check unclear")

print(f"Verification complete: {success_count}/{len(files)} pages verified.")
