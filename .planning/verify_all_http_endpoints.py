import urllib.request

URLS = [
    'http://localhost:8080/index.html',
    'http://localhost:8080/neuromates-home.html',
    'http://localhost:8080/neuromates-products.html',
    'http://localhost:8080/products.html',
    'http://localhost:8080/technology/index.html',
    'http://localhost:8080/technology/connected-devices.html',
    'http://localhost:8080/technology/ai-machine-learning.html',
    'http://localhost:8080/technology/monitoring-analytics.html',
    'http://localhost:8080/technology/connected-care-platform.html',
    'http://localhost:8080/insights/index.html',
    'http://localhost:8080/insights/research.html',
    'http://localhost:8080/insights/resources.html',
    'http://localhost:8080/about/index.html',
    'http://localhost:8080/about/vision-mission.html',
    'http://localhost:8080/about/our-approach.html',
    'http://localhost:8080/about/impact.html',
    'http://localhost:8080/contact.html',
    'http://localhost:8080/register-demo.html',
    'http://localhost:8080/404.html',
    'http://localhost:8080/assets/css/tokens.css',
    'http://localhost:8080/assets/js/shared.js',
    'http://localhost:8080/assets/js/three-core.js',
    'http://localhost:8080/assets/images/logo.png'
]

print("=== VERIFYING ALL HTTP ENDPOINTS ON LOCAL SERVER ===")
all_ok = True
for url in URLS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        print(f"[{res.status} OK] {url}")
    except Exception as e:
        print(f"[FAIL] {url} -> {e}")
        all_ok = False

if all_ok:
    print("\nALL 23 CORE URLS AND ASSETS VERIFIED ON HTTP://LOCALHOST:8080!")
else:
    raise SystemExit("HTTP verification failed for some endpoints!")

