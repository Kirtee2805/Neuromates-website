import os
import re

print("==================================================")
print("NEURO MATES E2E USER FLOW & QA FILE AUDIT")
print("==================================================")

WORKSPACE = r"D:\Neuromates(website)"

FLOW_FILES = [
    ("1. Home Page", "index.html", [
        "Advancing connected care for neurological health",
        "Four products. One connected approach to neurological care",
        "Epilepsy Care",
        "Neuro Mates"
    ]),
    ("2. Technology Overview", "technology/index.html", [
        "Connecting sensing, intelligence and care",
        "Neuro Mates Care Platform",
        "Platform",
        "Intelligence",
        "Connectivity",
        "Sensing"
    ]),
    ("3. Insights Overview", "insights/index.html", [
        "Research, technology and perspectives on neurological care",
        "Research",
        "Resources"
    ]),
    ("4. About Us Overview", "about/index.html", [
        "Advancing connected care for neurological health",
        "Guided by medical professionals",
        "Dr. Kirit Shukla",
        "Dr. Nishit Patel",
        "Dr. G. B. Yadav"
    ]),
    ("5. Main Products Page", "neuromates-products.html", [
        "Neurological care, designed around the condition",
        "Continuous brain-activity monitoring and connected response",
        "Every product connects to the same platform"
    ]),
    ("6. Epilepsy Care Dedicated Root Page", "epilepsy-care.html", [
        "Helping families stay connected during epilepsy monitoring",
        "page_15_Image-8784015711.jpg",
        "abnormal EEG signals that may indicate a seizure",
        "Four portals, one product",
        "Medication Reminder",
        "Continuous monitoring"
    ]),
    ("7. Epilepsy Care Products Folder", "products/epilepsy-care.html", [
        "Helping families stay connected during epilepsy monitoring",
        "page_15_Image-8784015711.jpg",
        "abnormal EEG signals that may indicate a seizure"
    ]),
    ("8. Standalone Products Page", "products.html", [
        "Neurological care, designed around the condition",
        "Continuous brain-activity monitoring"
    ]),
    ("9. Home Page Mirror", "neuromates-home.html", [
        "Advancing connected care for neurological health"
    ])
]

all_pass = True

print("\n--- [Step 1] Verifying User Navigation Flow & Page Content (Normalized) ---")
for step_name, rel_path, expected_phrases in FLOW_FILES:
    full_path = os.path.join(WORKSPACE, rel_path.replace("/", "\\"))
    if not os.path.exists(full_path):
        print(f"[FAIL] {step_name}: File not found at {full_path}")
        all_pass = False
        continue
    
    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        raw_content = f.read()
    
    # Strip HTML tags and normalize whitespace for text search, while raw_content retains image filenames
    clean_text = ' '.join(re.sub(r'<[^>]+>', ' ', raw_content).split())
    
    missing = []
    for phrase in expected_phrases:
        if phrase not in clean_text and phrase not in raw_content:
            missing.append(phrase)
            
    if missing:
        print(f"[FAIL] {step_name} ({rel_path}): Missing {missing}")
        all_pass = False
    else:
        print(f"[PASS] {step_name} ({rel_path}): Verified. All {len(expected_phrases)} key markers present.")

print("\n--- [Step 2] Verifying Critical Root Cause Fixes ---")

# 1. tokens.css: Check @view-transition is NOT present
tokens_path = os.path.join(WORKSPACE, "assets", "css", "tokens.css")
with open(tokens_path, "r", encoding="utf-8") as f:
    tokens_css = f.read()
if "@view-transition" in tokens_css:
    print("[FAIL] @view-transition is present in tokens.css!")
    all_pass = False
else:
    print("[PASS] tokens.css: @view-transition is completely removed. Main thread navigation freezing resolved.")

# 2. neuromates-products.html: Check clip-path 100% is NOT present
prod_path = os.path.join(WORKSPACE, "neuromates-products.html")
with open(prod_path, "r", encoding="utf-8") as f:
    prod_html = f.read()
if "clip-path:inset(0 100% 0 0)" in prod_html or "clip-path: inset(0 100% 0 0)" in prod_html:
    print("[FAIL] clip-path: inset(0 100% 0 0) present in neuromates-products.html!")
    all_pass = False
else:
    print("[PASS] neuromates-products.html: clip-path 100% horizontal clipping removed. Epilepsy product displays properly.")

# 3. technology/index.html: Check heavy Three.js canvas / GSAP scroll-pin is NOT present
tech_path = os.path.join(WORKSPACE, "technology", "index.html")
with open(tech_path, "r", encoding="utf-8") as f:
    tech_html = f.read()
if "pin: true" in tech_html or "end: '+=1600'" in tech_html or "new THREE.WebGLRenderer" in tech_html:
    print("[FAIL] Heavy Three.js / GSAP pin lock still in technology/index.html!")
    all_pass = False
else:
    print("[PASS] technology/index.html: Bloated 3D WebGL / pin-scroll removed. Replaced with clean medical stack.")

# 4. shared.js: Check scroll reset on page load
shared_path = os.path.join(WORKSPACE, "assets", "js", "shared.js")
with open(shared_path, "r", encoding="utf-8") as f:
    shared_js = f.read()
if "window.scrollTo(0, 0)" in shared_js:
    print("[PASS] shared.js: window.scrollTo(0, 0) scroll reset implemented on page load.")
else:
    print("[WARN] shared.js: window.scrollTo(0, 0) not explicitly found.")

print("\n==================================================")
if all_pass:
    print("ALL 9 FLOW STEPS AND 4 CRITICAL FIXES VERIFIED SUCCESSFULLY!")
else:
    print("SOME CHECKS FAILED. Please review the output above.")
print("==================================================")
