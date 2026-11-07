import glob, re

css_files = glob.glob("D:/Neuromates(website)/**/*.css", recursive=True)
html_files = glob.glob("D:/Neuromates(website)/**/*.html", recursive=True)

print("Auditing mobile responsiveness rules in CSS & HTML...")

# Check viewport meta in all HTML files
missing_viewport = []
for h in html_files:
    if "node_modules" in h or ".planning" in h: continue
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    if 'name="viewport"' not in c and "name='viewport'" not in c:
        missing_viewport.append(h)

print(f"Missing viewport meta in HTML files: {len(missing_viewport)}")
if missing_viewport:
    for m in missing_viewport: print(" -", m)

# Check tokens.css mobile rules
with open("D:/Neuromates(website)/assets/css/tokens.css", "r", encoding="utf-8") as f:
    tokens = f.read()

has_overflow_guard = "overflow-x: hidden" in tokens and "body" in tokens
print("Has body overflow-x: hidden guard in tokens.css:", has_overflow_guard)

