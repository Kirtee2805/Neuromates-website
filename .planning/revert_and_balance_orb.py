import os
import re

prod_files = ['neuromates-products.html', 'products.html', 'Products _ Neuro Mates.html']

old_ph_re = re.compile(r'<header class="ph">.*?</header>', re.DOTALL)

proper_header_html = '''<header class="ph">
  <div class="w">
    <span class="ey">PRODUCTS</span>
    <h1 class="hl" data-h="rise">Neurological care, <br>designed around the condition.</h1>
    <p class="bl" style="margin-top:20px">Neuro Mates brings together disease-specific products for Parkinson’s, Alzheimer’s, Epilepsy and Paralysis. Each product combines appropriate monitoring, connected technology and personalised care support for the needs of the condition.</p>
  </div>
  <div class="orb" aria-hidden="true">
    <img data-k="p_person" alt="Parkinson's Care Wearable">
    <img data-k="a_person" alt="Alzheimer's Care Wearable">
    <img data-k="e_person" alt="Epilepsy Monitoring Headband">
    <img data-k="pa_face" alt="Paralysis Care Rehabilitation">
  </div>
</header>'''

proper_ph_css = '''
/* ==========================================================================
   NEURO MATES — PRODUCTS OVERVIEW HERO (REVERTED & BALANCED)
   Proper headline with no overlap, and consistent, well-proportioned circular photos
   ========================================================================== */
#v-overview .ph {
  position: relative;
  overflow: visible;
  padding-top: clamp(120px, 14vw, 165px);
  padding-bottom: clamp(60px, 8vw, 95px);
}
#v-overview .ph .w {
  max-width: 52%;
  position: relative;
  z-index: 3;
}
#v-overview .ph .ey {
  display: inline-block;
  margin-bottom: 14px;
}
#v-overview .ph h1 {
  font-size: clamp(2.1rem, 3.8vw, 3.3rem) !important;
  line-height: 1.15 !important;
  letter-spacing: -0.015em;
  font-weight: 700;
  margin: 0;
  max-width: 14em;
  color: var(--ink, #0E3B43);
}
#v-overview .ph p.bl {
  max-width: 32em;
  line-height: 1.6;
}

/* Four Balanced Circular Product Photos on the Right */
.orb {
  position: absolute;
  right: 4%;
  top: 18%;
  width: 40%;
  height: clamp(340px, 34vw, 440px);
  pointer-events: none;
  z-index: 2;
}
.orb img {
  position: absolute;
  /* Equal, consistent balanced sizing across all 4 circles */
  width: clamp(120px, 11vw, 148px) !important;
  height: clamp(120px, 11vw, 148px) !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  border: 5px solid #FFFFFF !important;
  box-shadow: 0 16px 38px rgba(14, 59, 67, 0.16) !important;
  animation: bob 5s ease-in-out infinite;
  background: #E8F6F3;
}
/* Shifted away from text so 'care,' is never overlapped */
.orb img:nth-child(1) {
  left: 14% !important;
  top: 0 !important;
}
.orb img:nth-child(2) {
  right: 4% !important;
  top: 6% !important;
  animation-delay: -1.2s;
}
.orb img:nth-child(3) {
  left: 24% !important;
  bottom: 0 !important;
  animation-delay: -2.4s;
}
.orb img:nth-child(4) {
  right: 0 !important;
  bottom: 8% !important;
  animation-delay: -3.4s;
}

@media (max-width: 900px) {
  #v-overview .ph .w {
    max-width: 100%;
  }
  .orb {
    display: none !important;
  }
}
'''

for fn in prod_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean out any previous showcase CSS
    content = re.sub(r'/\* ==========================================================================\s*NEURO MATES — PRODUCT HERO SUITE SHOWCASE.*?</style>', '</style>', content, flags=re.DOTALL)
    content = re.sub(r'/\* Robust 2-Column Hero Grid: Zero overlap.*?@media \(max-width: 580px\) \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* ==========================================================================\s*NEURO MATES — PRODUCTS OVERVIEW HERO \(REVERTED & BALANCED\).*?</style>', '</style>', content, flags=re.DOTALL)

    # Replace header markup inside #v-overview
    idx = content.find('id="v-overview"')
    if idx != -1:
        h_start = content.find('<header class="ph">', idx)
        h_end = content.find('</header>', h_start) + len('</header>')
        content = content[:h_start] + proper_header_html + content[h_end:]
        print(f"Replaced header in {fn}")

    # Inject proper CSS
    content = content.replace('</style>', proper_ph_css + '\n</style>', 1)
    print(f"Injected proper_ph_css in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished reverting and balancing products hero.")
