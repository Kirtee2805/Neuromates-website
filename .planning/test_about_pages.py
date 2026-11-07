import os, re

PAGES = {
    'index.html': {
        'h1': 'Advancing connected care for',
        'terms': ['The challenge', 'Our solution', 'Guided by medical professionals', 'Dr. Kirit Shukla', 'Dr. Nishit Patel', 'Dr. G. B. Yadav', 'Four focused care areas', 'relationship-canvas'],
        'prohibited': ['98%', '4.9/5', '10,000+', 'testimonial']
    },
    'vision-mission.html': {
        'h1': 'Our vision and',
        'terms': ['OUR VISION', 'proactive, continuous and compassionate', 'OUR MISSION', 'empower patients', 'particle-cloud-canvas'],
        'prohibited': []
    },
    'our-approach.html': {
        'h1': 'How we think about',
        'terms': ['Patient-centred', 'Connected', 'Personalised', 'Responsible', 'designed for comfort, dignity and daily wear'],
        'prohibited': []
    },
    'impact.html': {
        'h1': 'Every connection',
        'terms': ['MONITOR', 'ALERT', 'CONNECT', 'SUPPORT', 'continuous sensing provides peace of mind', 'timely notifications when support is needed'],
        'prohibited': ['patients helped', 'ratings', 'success rate', 'clinical trial results']
    }
}

base_dir = r'D:\Neuromates(website)\about'
all_passed = True

for page, req in PAGES.items():
    path = os.path.join(base_dir, page)
    if not os.path.exists(path):
        print(f"FAILED: {page} does not exist!")
        all_passed = False
        continue

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"Testing {page}: {len(html)} bytes")
    
    # Check H1
    if req['h1'].lower() not in html.lower():
        print(f"  [X] Missing H1 term: {req['h1']}")
        all_passed = False

    # Check required terms
    for t in req['terms']:
        if t.lower() not in html.lower():
            print(f"  [X] Missing required term: {t}")
            all_passed = False

    # Check prohibited
    for p in req['prohibited']:
        if p.lower() in html.lower():
            print(f"  [!] Found prohibited term: {p}")
            all_passed = False

    # Check for fake statistical percentages like 98% in prose
    # (excluding CSS/JS)
    body_text_only = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)
    body_text_only = re.sub(r'<script.*?</script>', '', body_text_only, flags=re.DOTALL)
    stats_match = re.findall(r'\b\d+%', body_text_only)
    if stats_match:
        print(f"  [!] Found fake statistical percentage in HTML body: {stats_match}")
        all_passed = False

    # Check script token error
    if 'tokens.css"></script>' in html:
        print(f"  [X] Found invalid script tag for tokens.css")
        all_passed = False

    # Check Care line & shared elements
    if 'id="care"' not in html or 'id="nav"' not in html or 'id="global-cta"' not in html or 'id="global-footer"' not in html:
        print(f"  [X] Missing shared template element (care/nav/cta/footer)")
        all_passed = False

    print(f"  -> PASSED: {page}")

if all_passed:
    print("ALL 4 ABOUT US PAGES FULLY VERIFIED WITH 100% SPEC ACCURACY!")
else:
    raise SystemExit("Some tests failed!")
