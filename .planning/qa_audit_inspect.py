import os, glob, re

BASE_DIR = r'D:\Neuromates(website)'
files = glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True)
css_files = glob.glob(os.path.join(BASE_DIR, '**', '*.css'), recursive=True)

findings = {
    'horizontal_overflow_risks': [],
    'fixed_widths': [],
    'touch_targets_small': [],
    'font_size_overflow_risks': [],
    'contrast_risks': [],
    'media_query_gaps': [],
    'alignment_spacing': [],
    'nav_footer_inconsistencies': []
}

print(f"Scanning {len(files)} HTML files and {len(css_files)} CSS files...")

for fpath in files:
    rel = os.path.relpath(fpath, BASE_DIR)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Check fixed width without max-width
    fixed_w = re.findall(r'width:\s*([4-9]\d{2,}|[1-9]\d{3,})px', text)
    if fixed_w:
        findings['fixed_widths'].append((rel, fixed_w))

    # 2. Check for 100vw which causes scrollbar overflow on Windows
    if '100vw' in text:
        findings['horizontal_overflow_risks'].append((rel, 'Contains 100vw (can cause scrollbar-induced horizontal overflow on Windows)'))

    # 3. Check for buttons/links that may be smaller than 44px
    small_btn = re.findall(r'height:\s*([1-3]\d)px', text)
    if small_btn:
        findings['touch_targets_small'].append((rel, small_btn))

    # 4. Check for long unbroken words in H1/H2 without word-break
    headings = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', text, re.DOTALL)
    for h in headings:
        words = re.findall(r'\b[A-Za-z-]{12,}\b', h)
        if words:
            findings['font_size_overflow_risks'].append((rel, words))

    # 5. Check media query breakpoints
    mqs = re.findall(r'@media\s*\(([^)]+)\)', text)
    if not mqs and rel not in ['index.html', 'neuromates-home.html', 'neuromates-products.html', 'products.html']:
        findings['media_query_gaps'].append(rel)

print("\n--- FINDINGS SUMMARY ---")
for k, v in findings.items():
    print(f"{k}: {len(v)} occurrences")
    for item in v[:5]:
        print("  ", item)

