import os
import re

workspace = r"D:\Neuromates(website)"
for root, dirs, files in os.walk(workspace):
    if ".git" in root or "node_modules" in root or ".planning" in root:
        continue
    for f in files:
        if f.endswith(".html") or f.endswith(".js"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
            scroll_matches = re.findall(r"addEventListener\(['\"]scroll['\"]", txt)
            if scroll_matches:
                print(f"{os.path.relpath(p, workspace)}: {len(scroll_matches)} scroll listener(s)")

