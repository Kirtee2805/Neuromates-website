import os
import re

prod_files = ['neuromates-products.html', 'products.html', 'Products _ Neuro Mates.html']

# Regex to match the overview header
old_header_re = re.compile(
    r'<header class="ph">\s*<div class="w">\s*<p class="ey">PRODUCTS</p>\s*<h1 class="hl"[^>]*>Neurological care, designed around the condition\.</h1>\s*<p class="bl"[^>]*>.*?</p>\s*</div>\s*<div class="orb"[^>]*>.*?</div>\s*</header>',
    re.DOTALL
)

new_header_html = '''<header class="ph">
  <div class="w ph-hero-grid">
    <div class="ph-hero-text">
      <p class="ey">PRODUCTS</p>
      <h1 class="hl" data-h="rise">Neurological care, <br class="ph-desktop-br">designed around the condition.</h1>
      <p class="bl" style="margin-top:20px">Neuro Mates brings together disease-specific products for Parkinson’s, Alzheimer’s, Epilepsy and Paralysis. Each product combines appropriate monitoring, connected technology and personalised care support for the needs of the condition.</p>
    </div>
    <div class="orb" aria-hidden="true">
      <img data-k="p_person" alt="">
      <img data-k="a_person" alt="">
      <img data-k="e_person" alt="">
      <img data-k="pa_face" alt="">
    </div>
  </div>
</header>'''

new_css = '''
/* Robust 2-Column Hero Grid: Zero overlap between heading and floating circles */
#v-overview .ph {
  padding-top: clamp(120px, 14vw, 160px);
  padding-bottom: clamp(60px, 8vw, 90px);
  position: relative;
  overflow: visible;
}
.ph-hero-grid {
  display: grid !important;
  grid-template-columns: 1.15fr 0.85fr !important;
  gap: clamp(28px, 4vw, 56px) !important;
  align-items: center !important;
  position: relative;
  z-index: 2;
}
.ph-hero-text {
  max-width: 580px;
}
.ph-hero-text h1 {
  font-size: clamp(2.1rem, 3.8vw, 3.2rem) !important;
  line-height: 1.14 !important;
  letter-spacing: -0.015em;
  font-weight: 700;
  margin: 0;
}
.ph-desktop-br {
  display: block;
}
.ph-hero-grid .orb {
  position: relative !important;
  right: auto !important;
  top: auto !important;
  width: 100% !important;
  height: clamp(340px, 32vw, 420px) !important;
  pointer-events: none;
}
.ph-hero-grid .orb img {
  position: absolute;
  border-radius: 50%;
  object-fit: cover;
  border: 5px solid #fff;
  box-shadow: 0 16px 40px rgba(14, 59, 67, 0.18);
  animation: bob 5s ease-in-out infinite;
}
.ph-hero-grid .orb img:nth-child(1) {
  width: clamp(100px, 11vw, 145px) !important;
  aspect-ratio: 1;
  left: 6% !important;
  top: 6% !important;
}
.ph-hero-grid .orb img:nth-child(2) {
  width: clamp(90px, 10vw, 130px) !important;
  aspect-ratio: 1;
  right: 4% !important;
  top: 0 !important;
  animation-delay: -1.2s;
}
.ph-hero-grid .orb img:nth-child(3) {
  width: clamp(105px, 12vw, 160px) !important;
  aspect-ratio: 1;
  left: 18% !important;
  bottom: 0 !important;
  animation-delay: -2.4s;
}
.ph-hero-grid .orb img:nth-child(4) {
  width: clamp(80px, 9vw, 115px) !important;
  aspect-ratio: 1;
  right: 0 !important;
  bottom: 12% !important;
  animation-delay: -3.4s;
}

@media (max-width: 900px) {
  .ph-hero-grid {
    grid-template-columns: 1fr !important;
  }
  .ph-hero-grid .orb {
    display: none !important;
  }
  .ph-desktop-br {
    display: inline;
  }
}
'''

for fn in prod_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_header_re.search(content):
        content = old_header_re.sub(new_header_html, content)
        print(f"Updated hero header HTML in {fn}")
    else:
        # Fallback manual string replacement
        target = '<header class="ph"><div class="w"><p class="ey">PRODUCTS</p><h1 class="hl" data-h="rise" style="max-width:11em">Neurological care, designed around the condition.</h1>'
        if target in content:
            idx = content.find(target)
            end_idx = content.find('</header>', idx) + len('</header>')
            content = content[:idx] + new_header_html + content[end_idx:]
            print(f"Fallback replaced hero header HTML in {fn}")
        else:
            print(f"Header pattern not found in {fn}")

    if '.ph-hero-grid' not in content:
        content = content.replace('</style>', new_css + '\n</style>', 1)
        print(f"Added grid CSS in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating products files.")

