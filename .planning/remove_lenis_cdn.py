import os
import re

workspace = r"D:\Neuromates(website)"
lenis_tag_pat = re.compile(r'\s*<script\s+src=["\']https://cdn\.jsdelivr\.net/npm/lenis@[^"\']+["\']></script>', re.IGNORECASE)

modified_files = []

for root, dirs, files in os.walk(workspace):
    if ".git" in root or "node_modules" in root or ".planning" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as fp:
                txt = fp.read()
            if lenis_tag_pat.search(txt):
                new_txt = lenis_tag_pat.sub("", txt)
                with open(p, "w", encoding="utf-8") as fp:
                    fp.write(new_txt)
                modified_files.append(os.path.relpath(p, workspace))

print(f"Removed Lenis CDN from {len(modified_files)} files:")
for m in modified_files:
    print(" -", m)

