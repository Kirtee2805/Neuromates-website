import os
import re

# 1. Revert neuromates-products.html and products.html
targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

ppl_reel_pat = re.compile(r'<div class="ppl-reel".*?</div>\s*</div>', re.DOTALL)
orig_ppl_html = '<div class="ppl" aria-hidden="true"><i></i><i></i><i></i></div></div>'

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # Revert HTML
    if ppl_reel_pat.search(c):
        c = ppl_reel_pat.sub(orig_ppl_html, c)
        print(f"Reverted .ppl HTML in {p}")
    
    # Remove added JS interval
    c = re.sub(r'let currentPhotoSet=0;\s*setInterval\(.*?2000\);', '', c, flags=re.DOTALL)

    # Remove added .ppl-reel CSS
    c = c.replace(""".ppl-reel{display:flex;gap:16px;margin:22px 0;align-items:center}
.ppl-slot{width:76px;height:76px;border-radius:50%;position:relative;overflow:hidden;box-shadow:0 8px 24px rgba(14,59,67,.18);border:3px solid #fff;background:linear-gradient(135deg,#E9E1FF,#FFD1E3);transition:transform .3s ease}
.ppl-slot:hover{transform:scale(1.08)}
.ppl-slot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s cubic-bezier(.22,1,.36,1),transform .6s cubic-bezier(.22,1,.36,1);transform:scale(.92);border-radius:50%}
.ppl-slot img.active{opacity:1;transform:scale(1)}\n""", "")

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Saved {p}")

print("Done reverting products.")

