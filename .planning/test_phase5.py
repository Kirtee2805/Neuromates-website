import os, re

PAGES = {
    'contact.html': {
        'h1': 'Let\'s talk about',
        'terms': ['GET IN TOUCH', 'Full name', 'Email', 'Phone', 'Organisation', 'I am interested in', 'Parkinson\'s Care', 'Alzheimer\'s Care', 'Epilepsy Care', 'Paralysis Care', 'Send enquiry', 'Something went wrong', 'Thank you', 'Your enquiry has been sent'],
        'honeypot': 'website'
    },
    'register-demo.html': {
        'h1': 'See Neuro Mates in',
        'terms': ['REQUEST A DEMO', 'Organisation', 'Role', 'Healthcare Professional', 'Product of interest', 'Preferred contact method', 'Request a demo', 'Thank you', 'Your demo request has been sent', 'demo-core-canvas'],
        'honeypot': 'website'
    },
    '404.html': {
        'h1': 'This page is not available',
        'terms': ['404', 'The page you are looking for may have moved', 'Back to Home', 'blip-canvas'],
        'honeypot': None
    }
}

base_dir = r'D:\Neuromates(website)'
all_passed = True

print("=== TESTING PHASE 5 HTML PAGES ===")
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

    # Check honeypot
    if req['honeypot']:
        if f'name="{req["honeypot"]}"' not in html:
            print(f"  [X] Missing honeypot field: {req['honeypot']}")
            all_passed = False

    # Check invalid script tag
    if 'tokens.css"></script>' in html:
        print(f"  [X] Found invalid script tag for tokens.css")
        all_passed = False

    # Check shared elements
    if 'id="care"' not in html or 'id="nav"' not in html or 'id="global-cta"' not in html or 'id="global-footer"' not in html:
        print(f"  [X] Missing shared template element")
        all_passed = False

    print(f"  -> PASSED: {page}")

print("\n=== TESTING BACKEND & DATABASE ASSETS ===")
backend_files = ['schema.sql', 'server.js', 'package.json', '.env.example', 'README.md']
for bf in backend_files:
    p = os.path.join(base_dir, bf)
    if not os.path.exists(p):
        print(f"  [X] Missing backend file: {bf}")
        all_passed = False
    else:
        size = os.path.getsize(p)
        print(f"  -> PASSED: {bf} ({size} bytes)")

# Verify schema.sql tables
with open(os.path.join(base_dir, 'schema.sql'), 'r', encoding='utf-8') as f:
    sql = f.read()
if 'demo_requests' not in sql or 'contact_enquiries' not in sql:
    print("  [X] schema.sql is missing required tables!")
    all_passed = False
else:
    print("  -> PASSED: schema.sql contains demo_requests and contact_enquiries tables")

# Verify server.js routes
with open(os.path.join(base_dir, 'server.js'), 'r', encoding='utf-8') as f:
    server_code = f.read()
if '/api/contact' not in server_code or '/api/demo' not in server_code or 'rateLimiter' not in server_code:
    print("  [X] server.js is missing required endpoints or rate limiter!")
    all_passed = False
else:
    print("  -> PASSED: server.js contains /api/contact, /api/demo, and rateLimiter")

if all_passed:
    print("\nALL PHASE 5 DELIVERABLES PASSED 100%!")
else:
    raise SystemExit("Phase 5 validation failed!")
