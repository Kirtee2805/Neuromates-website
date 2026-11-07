import os
import re
import subprocess

workspace = r"D:\Neuromates(website)"
errors = []

for root, dirs, files in os.walk(workspace):
    if ".git" in root or "node_modules" in root or ".planning" in root:
        continue
    for f in files:
        if f.endswith(".js"):
            p = os.path.join(root, f)
            res = subprocess.run(["node", "--check", p], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"[JS ERROR] {p}: {res.stderr}")
                errors.append(p)
            else:
                print(f"[JS OK] {os.path.relpath(p, workspace)}")

if not errors:
    print("\nALL JS FILES PASS NODE SYNTAX CHECK!")
else:
    print(f"\n{len(errors)} JS syntax errors found!")

