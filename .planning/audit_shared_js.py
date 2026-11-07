import glob

html_files = glob.glob("D:/Neuromates(website)/**/*.html", recursive=True)
has_shared = []
missing_shared = []

for h in html_files:
    if "node_modules" in h or ".planning" in h: continue
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    rel = h.replace("D:\\Neuromates(website)\\", "")
    if "shared.js" in c:
        has_shared.append(rel)
    else:
        missing_shared.append(rel)

print(f"Has shared.js ({len(has_shared)} files):")
for f in has_shared: print(" +", f)
print(f"\nMissing shared.js ({len(missing_shared)} files):")
for f in missing_shared: print(" -", f)

