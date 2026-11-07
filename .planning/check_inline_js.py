import os
import re
import subprocess
import tempfile

workspace = r"D:\Neuromates(website)"
errors = []

for root, dirs, files in os.walk(workspace):
    if ".git" in root or "node_modules" in root or ".planning" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
            scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', txt, re.DOTALL)
            for idx, s in enumerate(scripts):
                code = s.strip()
                if not code:
                    continue
                # Test syntax using node
                with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tf:
                    tf.write(code)
                    tf_path = tf.name
                try:
                    res = subprocess.run(["node", "--check", tf_path], capture_output=True, text=True)
                    if res.returncode != 0:
                        print(f"[INLINE JS ERROR] {os.path.relpath(p, workspace)} script {idx}: {res.stderr}")
                        errors.append((p, idx, res.stderr))
                finally:
                    if os.path.exists(tf_path):
                        os.remove(tf_path)

if not errors:
    print("\nALL INLINE JS SCRIPTS IN ALL HTML FILES PASS NODE SYNTAX CHECK!")
else:
    print(f"\n{len(errors)} inline JS errors found!")

