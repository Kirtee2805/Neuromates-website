import os, glob, re

HTML_FILES = [
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
    'insights/resources.html',
    'about/index.html',
    'about/vision-mission.html',
    'about/our-approach.html',
    'about/impact.html',
    'contact.html',
    'register-demo.html',
    '404.html'
]

FORBIDDEN_HARDWARE = [
    'mpu6050', 'mpu-6050', 'esp32', 'esp-32', 'esp8266', 
    'bioamp', 'stm32', 'arduino', 'raspberry pi', 'nrf52'
]

# Claims that assert prevention or diagnosis (excluding disclaimers with "not" or "never")
POSITIVE_FORBIDDEN_REGEX = [
    r'\b(?:will|can|to)\s+prevent\s+seizures\b',
    r'\bprevention\s+of\s+seizures\b',
    r'\bguaranteed\s+detection\b',
    r'\bcures?\s+epilepsy\b',
    r'\bdiagnose\s+epilepsy\b'
]

BASE_DIR = r'D:\Neuromates(website)'
audit_results = {
    'total_checked': 0,
    'passed': 0,
    'warnings': [],
    'errors': []
}

print("====================================================================")
print("  NEURO MATES — MASTER SYSTEM AUDIT (PHASE 6)")
print("====================================================================\n")

for rel_path in HTML_FILES:
    abs_path = os.path.join(BASE_DIR, rel_path.replace('/', os.sep))
    if not os.path.exists(abs_path):
        audit_results['errors'].append(f"Missing file: {rel_path}")
        continue

    audit_results['total_checked'] += 1
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_errors = []
    file_warnings = []

    # 1. Check for single H1 (except products pages with 5 views)
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1_matches) == 0:
        file_errors.append("No <h1> tag found.")
    elif len(h1_matches) > 1 and 'products' not in rel_path:
        file_warnings.append(f"Multiple ({len(h1_matches)}) <h1> tags found.")

    # 2. Check viewport meta
    if 'name="viewport"' not in content:
        file_errors.append("Missing viewport meta tag.")

    # 3. Check for forbidden hardware component names
    lower_content = content.lower()
    for hw in FORBIDDEN_HARDWARE:
        if hw in lower_content:
            file_errors.append(f"Forbidden hardware component model found: '{hw}'")

    # 4. Check for forbidden medical / seizure claims
    for pattern in POSITIVE_FORBIDDEN_REGEX:
        match = re.search(pattern, lower_content)
        if match:
            # Check if immediately preceded by "does not" or "not" or "cannot"
            start_idx = max(0, match.start() - 30)
            prefix = lower_content[start_idx:match.start()]
            if not any(neg in prefix for neg in ['not', 'cannot', 'never', 'does not']):
                file_errors.append(f"Forbidden medical claim found: '{match.group(0)}'")

    # 5. Check for invalid script tag for tokens.css
    if 'tokens.css"></script>' in content:
        file_errors.append("Invalid <script src=\"...tokens.css\"></script> tag found.")

    # 6. Check for alt attributes on img tags
    img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    for img in img_tags:
        if 'alt=' not in img:
            file_errors.append(f"Image missing alt attribute: {img[:50]}...")

    # Log file status
    if not file_errors and not file_warnings:
        audit_results['passed'] += 1
        print(f" [PASS] {rel_path} ({len(content)} bytes)")
    else:
        status_sym = "[FAIL]" if file_errors else "[WARN]"
        print(f" {status_sym} {rel_path}")
        for e in file_errors:
            print(f"    ! ERROR: {e}")
            audit_results['errors'].append(f"{rel_path}: {e}")
        for w in file_warnings:
            print(f"    * WARNING: {w}")
            audit_results['warnings'].append(f"{rel_path}: {w}")

print("\n====================================================================")
print(f"Audit Summary: {audit_results['passed']}/{audit_results['total_checked']} files passed cleanly.")
print(f"Total Errors: {len(audit_results['errors'])}, Total Warnings: {len(audit_results['warnings'])}")
print("====================================================================")
