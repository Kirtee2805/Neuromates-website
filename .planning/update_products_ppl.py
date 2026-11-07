import os

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

old_html = '<div class="ppl" aria-hidden="true"><i></i><i></i><i></i></div>'
new_html = """<div class="ppl-reel" id="ppl-reel" aria-label="Personalised memories of family members">
              <div class="ppl-slot" title="Loved one: Grandfather"><img src="assets/images/person-1.jpg" alt="Loved one 1" class="active"><img src="assets/images/person-4.jpg" alt="Loved one 4"></div>
              <div class="ppl-slot" title="Loved one: Daughter"><img src="assets/images/person-2.jpg" alt="Loved one 2" class="active"><img src="assets/images/person-5.jpg" alt="Loved one 5"></div>
              <div class="ppl-slot" title="Loved one: Relative"><img src="assets/images/person-3.jpg" alt="Loved one 3" class="active"><img src="assets/images/person-6.jpg" alt="Loved one 6"></div>
            </div>"""

ppl_css = """.ppl-reel{display:flex;gap:16px;margin:22px 0;align-items:center}
.ppl-slot{width:76px;height:76px;border-radius:50%;position:relative;overflow:hidden;box-shadow:0 8px 24px rgba(14,59,67,.18);border:3px solid #fff;background:linear-gradient(135deg,#E9E1FF,#FFD1E3);transition:transform .3s ease}
.ppl-slot:hover{transform:scale(1.08)}
.ppl-slot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s cubic-bezier(.22,1,.36,1),transform .6s cubic-bezier(.22,1,.36,1);transform:scale(.92);border-radius:50%}
.ppl-slot img.active{opacity:1;transform:scale(1)}"""

ppl_js = """let currentPhotoSet=0;
setInterval(()=>{
  const slots=document.querySelectorAll('.ppl-slot');
  if(!slots.length)return;
  currentPhotoSet=1-currentPhotoSet;
  slots.forEach(slot=>{
    const imgs=slot.querySelectorAll('img');
    if(imgs.length>=2){
      imgs[0].classList.toggle('active',currentPhotoSet===0);
      imgs[1].classList.toggle('active',currentPhotoSet===1);
    }
  });
},2000);"""

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Replace HTML
    if old_html in c:
        c = c.replace(old_html, new_html)
        print(f"Replaced .ppl HTML in {p}")
    else:
        print(f"old_html not found in {p}")

    # 2. Add CSS
    if ".ppl-reel" not in c:
        c = c.replace(".ppl{", ppl_css + "\n.ppl{")
        print(f"Added .ppl-reel CSS in {p}")

    # 3. Add JS
    if "currentPhotoSet" not in c:
        # insert into setup(v) when v=='alzheimers-care'
        target_pos = "if(v=='alzheimers-care'){"
        if target_pos in c:
            c = c.replace(target_pos, target_pos + "\n" + ppl_js)
            print(f"Added 2-second photo rotation JS in {p}")

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Saved {p} successfully.")

