import glob, re

files = glob.glob("D:/Neuromates(website)/**/*.html", recursive=True) + glob.glob("D:/Neuromates(website)/**/*.js", recursive=True)

claude_links = []
for f in files:
    if "node_modules" in f or ".planning" in f: continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    matches = re.findall(r'href=["\'](https?://claude\.ai[^"\']*)["\']', c)
    if matches:
        claude_links.append((f, matches))

print(f"Files with claude.ai links ({len(claude_links)}):")
for f, ms in claude_links:
    print(f"\n{f}:")
    for m in set(ms):
        print("  -", m)

