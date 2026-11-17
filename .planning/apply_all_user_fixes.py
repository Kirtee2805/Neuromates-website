import os
import re

print("Starting fixes...")

# -------------------------------------------------------------
# 1. FIX PRODUCTS OVERVIEW HERO (.orb & care text overlap) AND
#    EPILEPSY EVERYDAY SUPPORT (3 aligned cards)
# -------------------------------------------------------------
prod_files = ['neuromates-products.html', 'products.html', 'Products _ Neuro Mates.html']

support_old_html = re.compile(
    r'<section class="sec t z"><div class="w two"><div class="r"><p class="ey">EVERYDAY SUPPORT</p><h2>Support beyond the alert\.</h2><div class="rm">.*?</div></div><div class="wb r">.*?</div></div></section>',
    re.DOTALL
)

support_new_html = '''<section class="sec t z">
  <div class="w">
    <div class="r" style="margin-bottom:28px">
      <p class="ey">EVERYDAY SUPPORT</p>
      <h2>Support beyond the alert.</h2>
    </div>
    <div class="support-grid r">
      <div class="cardx support-card" style="background:#fff">
        <span class="support-card-tag">Routine Care</span>
        <h3>Medication Reminder</h3>
        <p>Supports awareness of scheduled medication.</p>
      </div>
      <div class="cardx support-card" style="background:#fff">
        <span class="support-card-tag">Clinical Follow-up</span>
        <h3>Appointment Reminder</h3>
        <p>Helps patients keep track of scheduled clinical appointments.</p>
      </div>
      <div class="cardx support-card support-card-wb" style="background:#fff">
        <span class="support-card-tag" style="color:#0E7A5A;background:#E8F8F2;">Clinical Protocol</span>
        <h3>Responsible Wording</h3>
        <p>Neuro Mates monitors for abnormal EEG signals that may indicate a seizure. It does not diagnose, predict or prevent seizures, and detection cannot be guaranteed.</p>
      </div>
    </div>
  </div>
</section>'''

prod_css_add = '''
/* Fix hero text overlap with .orb */
#v-overview .ph { position: relative; overflow: visible; padding-top: clamp(120px, 14vw, 160px); padding-bottom: clamp(60px, 8vw, 90px); }
#v-overview .ph .w { max-width: 58%; position: relative; z-index: 3; }
#v-overview .ph h1 { max-width: 14em; }
.orb { position: absolute; right: 2%; top: 18%; width: 38%; height: 64%; pointer-events: none; z-index: 1; }
.orb img { position: absolute; width: clamp(110px, 14vw, 175px); aspect-ratio: 1; object-fit: cover; border-radius: 50%; border: 6px solid #fff; box-shadow: 0 20px 50px rgba(14,59,67,.2); animation: bob 5s ease-in-out infinite; }
.orb img:nth-child(1) { left: 16%; top: 0; }
.orb img:nth-child(2) { right: 0; top: 8%; animation-delay: -1.2s; }
.orb img:nth-child(3) { left: 26%; bottom: 0; animation-delay: -2.4s; }
.orb img:nth-child(4) { right: 4%; bottom: 8%; animation-delay: -3.4s; }

/* Everyday Support 3-Card Balanced Alignment */
.support-grid { display: grid; grid-template-columns: 1fr 1fr 1.15fr; gap: 20px; align-items: stretch; margin-top: 10px; }
.support-card { display: flex; flex-direction: column; justify-content: flex-start; padding: 28px; border-radius: 24px; border: 1px solid rgba(14, 59, 67, 0.08); box-shadow: 0 10px 30px rgba(14, 59, 67, 0.05); }
.support-card-tag { display: inline-block; align-self: flex-start; font-family: var(--font-heading, sans-serif); font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #0B7A7C; background: #EAF6F5; padding: 4px 10px; border-radius: 99px; margin-bottom: 14px; }
.support-card h3 { margin: 0 0 10px !important; font-size: 1.18rem; }
.support-card p { margin: 0; color: var(--mu); line-height: 1.55; font-size: 0.94rem; }
.support-card-wb { border-color: rgba(43, 181, 138, 0.35); background: linear-gradient(160deg, #ffffff, #F0FAF7) !important; }
@media (max-width: 900px) {
  #v-overview .ph .w { max-width: 100%; }
  .orb { display: none; }
  .support-grid { grid-template-columns: 1fr; }
}
'''

for fn in prod_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace support section
    if support_old_html.search(content):
        content = support_old_html.sub(support_new_html, content)
        print(f"Updated support section in {fn}")
    else:
        print(f"support_old_html not found in {fn}")

    # Remove redundant crumb in overview
    content = content.replace('<p class="crumb">NEURO MATES / PRODUCTS</p>', '')

    # Add CSS if not present
    if '.support-grid' not in content:
        content = content.replace('</style>', prod_css_add + '\n</style>', 1)
        print(f"Added CSS in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)


# -------------------------------------------------------------
# 2. FIX TECHNOLOGY/AI-MACHINE-LEARNING.HTML (Image 3)
# -------------------------------------------------------------
ai_fn = 'technology/ai-machine-learning.html'
if os.path.exists(ai_fn):
    with open(ai_fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove breadcrumb from ai-hero
    content = re.sub(r'<nav class="breadcrumb"[^>]*>.*?</nav>\s*', '', content, flags=re.DOTALL)

    # Ensure hero styling is clean and properly padded
    ai_css_fix = '''
    .ai-hero {
      position: relative;
      overflow: hidden;
      min-height: 48vh;
      padding: clamp(120px, 14vw, 165px) 0 clamp(48px, 6vw, 72px) !important;
      display: flex;
      align-items: center;
    }
    .ai-hero .w {
      position: relative;
      z-index: 2;
      pointer-events: auto;
    }
    .ai-hero .ey {
      margin-bottom: 16px;
      display: inline-block;
    }
    .ai-hero h1 {
      margin: 0;
      position: relative;
      z-index: 2;
    }
    '''
    content = content.replace('</style>', ai_css_fix + '\n</style>', 1)
    with open(ai_fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {ai_fn}")


# -------------------------------------------------------------
# 3. FIX INSIGHTS/INDEX.HTML (Image 4)
# -------------------------------------------------------------
ins_fn = 'insights/index.html'
if os.path.exists(ins_fn):
    with open(ins_fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace breadcrumb with clean eyebrow
    ins_breadcrumb = re.compile(r'<nav class="breadcrumb"[^>]*>.*?</nav>\s*', re.DOTALL)
    content = ins_breadcrumb.sub('<span class="ey">INSIGHTS</span>\n        ', content)

    # Ensure hero has proper padding and alignment
    ins_css_fix = '''
    .insights-hero {
      position: relative;
      padding: clamp(120px, 14vw, 165px) 0 clamp(48px, 6vw, 72px) !important;
      overflow: hidden;
    }
    .insights-hero .w {
      position: relative;
      z-index: 2;
    }
    .insights-hero .ey {
      margin-bottom: 16px;
      display: inline-block;
    }
    .insights-hero h1 {
      margin: 0 0 16px;
    }
    '''
    content = content.replace('</style>', ins_css_fix + '\n</style>', 1)
    with open(ins_fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {ins_fn}")


# -------------------------------------------------------------
# 4. REMOVE BREADCRUMBS WITH "HOME / ..." ACROSS OTHER SUBPAGES
#    to eliminate "Home" appearing behind headers/logos
# -------------------------------------------------------------
other_files = [
    'insights/research.html',
    'insights/resources.html',
    'technology/index.html',
    'technology/connected-care-platform.html',
    'technology/connected-devices.html',
    'technology/monitoring-analytics.html',
    'about/index.html',
    'about/impact.html',
    'about/our-approach.html',
    'about/vision-mission.html',
    'contact.html',
    'epilepsy-care.html',
    'products/epilepsy-care.html'
]

bcrumb_regex = re.compile(r'<nav class="breadcrumb"[^>]*>.*?</nav>\s*', re.DOTALL)

for fn in other_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    if bcrumb_regex.search(content):
        content = bcrumb_regex.sub('', content)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed breadcrumb from {fn}")

print("All tasks completed successfully!")
