import urllib.request, json

BASE_URL = 'http://localhost:3000'

PAGES_TO_TEST = [
    '/',
    '/index.html',
    '/neuromates-home.html',
    '/neuromates-products.html',
    '/products.html',
    '/technology/index.html',
    '/technology/connected-devices.html',
    '/technology/ai-machine-learning.html',
    '/technology/monitoring-analytics.html',
    '/technology/connected-care-platform.html',
    '/insights/index.html',
    '/insights/research.html',
    '/insights/resources.html',
    '/about/index.html',
    '/about/vision-mission.html',
    '/about/our-approach.html',
    '/about/impact.html',
    '/contact.html',
    '/register-demo.html',
    '/404.html',
    '/assets/css/tokens.css',
    '/assets/js/shared.js',
    '/assets/js/three-core.js',
    '/assets/images/logo.png',
    '/assets/images/page_5_Image-7572533686.jpg',
    '/assets/images/page_10_Image-7888911063.jpg',
    '/assets/images/page_15_Image-8784015711.jpg'
]

print("====================================================================")
print(f"  NEURO MATES — FULL-STACK TEST RUNNER ({BASE_URL})")
print("====================================================================\n")

# 1. Test Static Routes & Pages
print("--- 1. TESTING HTML PAGES & ASSETS ---")
all_passed = True
for path in PAGES_TO_TEST:
    url = BASE_URL + path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'NeuroTester/1.0'})
        res = urllib.request.urlopen(req, timeout=5)
        length = len(res.read())
        print(f" [PASS 200 OK] {path:<40} ({length:,} bytes)")
    except Exception as e:
        print(f" [FAIL]        {path:<40} -> {e}")
        all_passed = False

# 2. Test API Health Endpoint
print("\n--- 2. TESTING API HEALTH ENDPOINT ---")
try:
    url = f"{BASE_URL}/api/health"
    res = urllib.request.urlopen(url, timeout=5)
    data = json.loads(res.read().decode('utf-8'))
    print(f" [PASS 200 OK] /api/health -> {data}")
    assert data.get('ok') is True
except Exception as e:
    print(f" [FAIL] /api/health -> {e}")
    all_passed = False

# 3. Test Contact API with Valid Data
print("\n--- 3. TESTING POST /api/contact (VALID DATA) ---")
try:
    contact_payload = {
        "full_name": "Dr. Sarah Jenkins",
        "email": "sarah.jenkins@memorialhealth.org",
        "phone": "+1 (555) 234-5678",
        "organisation": "Memorial Health System",
        "interest": "Parkinson's Care",
        "message": "We are interested in evaluating continuous motion sensors for out-of-clinic fall monitoring.",
        "website": ""
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/contact",
        data=json.dumps(contact_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'NeuroTester/1.0'}
    )
    res = urllib.request.urlopen(req, timeout=5)
    data = json.loads(res.read().decode('utf-8'))
    print(f" [PASS 201 CREATED] /api/contact -> {data}")
    assert data.get('ok') is True
    assert 'id' in data
except Exception as e:
    print(f" [FAIL] /api/contact -> {e}")
    all_passed = False

# 4. Test Contact API with Honeypot (Spam Rejection)
print("\n--- 4. TESTING POST /api/contact (HONEYPOT SPAM REJECTION) ---")
try:
    spam_payload = {
        "full_name": "Spam Bot",
        "email": "bot@spam.com",
        "phone": "+1234567890",
        "organisation": "Spam Corp",
        "interest": "Other",
        "message": "Click here for free pharmacy deals.",
        "website": "http://spambot.xyz"
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/contact",
        data=json.dumps(spam_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'NeuroTester/1.0'}
    )
    try:
        res = urllib.request.urlopen(req, timeout=5)
        print(" [FAIL] Honeypot was NOT rejected!")
        all_passed = False
    except urllib.error.HTTPError as err:
        assert err.code == 400
        data = json.loads(err.read().decode('utf-8'))
        print(f" [PASS 400 BAD REQUEST] Honeypot rejected correctly -> {data}")
except Exception as e:
    print(f" [FAIL] Honeypot test failed -> {e}")
    all_passed = False

# 5. Test Demo API with Valid Data
print("\n--- 5. TESTING POST /api/demo (VALID DATA) ---")
try:
    demo_payload = {
        "name": "Prof. Arthur Pendelton",
        "organisation": "Neurological Sciences Institute",
        "role": "Healthcare Professional",
        "email": "arthur@neurosciences.edu",
        "phone": "+1 (555) 987-6543",
        "product_interest": "Parkinson's, Alzheimer's, Epilepsy",
        "contact_method": "Email",
        "message": "Scheduling demonstration for the department chair and care coordination team.",
        "website": ""
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/demo",
        data=json.dumps(demo_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'NeuroTester/1.0'}
    )
    res = urllib.request.urlopen(req, timeout=5)
    data = json.loads(res.read().decode('utf-8'))
    print(f" [PASS 201 CREATED] /api/demo -> {data}")
    assert data.get('ok') is True
    assert 'id' in data
except Exception as e:
    print(f" [FAIL] /api/demo -> {e}")
    all_passed = False

# 6. Test Demo API Invalid Email Validation
print("\n--- 6. TESTING POST /api/demo (INVALID EMAIL VALIDATION) ---")
try:
    bad_demo_payload = {
        "name": "Arthur",
        "organisation": "Hospital",
        "role": "Doctor",
        "email": "not-an-email",
        "phone": "+12345678",
        "product_interest": "Parkinson's",
        "contact_method": "Phone",
        "message": "Test notes",
        "website": ""
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/demo",
        data=json.dumps(bad_demo_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'NeuroTester/1.0'}
    )
    try:
        res = urllib.request.urlopen(req, timeout=5)
        print(" [FAIL] Invalid email was NOT rejected!")
        all_passed = False
    except urllib.error.HTTPError as err:
        assert err.code == 400
        data = json.loads(err.read().decode('utf-8'))
        print(f" [PASS 400 BAD REQUEST] Invalid email rejected correctly -> {data}")
except Exception as e:
    print(f" [FAIL] Validation test failed -> {e}")
    all_passed = False

print("\n====================================================================")
if all_passed:
    print("  ALL FULL-STACK PAGES, ASSETS & API ENDPOINTS PASSED 100%!")
else:
    print("  SOME TESTS FAILED! CHECK OUTPUT ABOVE.")
print("====================================================================")

