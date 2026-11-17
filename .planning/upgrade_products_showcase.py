import os
import re

print("Starting complete overhaul of Products Hero showcase and Chat Widget logo...")

# -------------------------------------------------------------
# 1. UPDATE CHAT WIDGET SCRIPT WITH CACHE BUSTER & PERFECT FIT
# -------------------------------------------------------------
chat_path = 'assets/js/chat-widget.js'
with open(chat_path, 'r', encoding='utf-8') as f:
    chat_code = f.read()

# Update logoIconUrl with version hash so browser doesn't cache old image
chat_code = re.sub(
    r'const logoIconUrl = `\$\{root\}assets/images/logo-icon\.png[^`]*`;',
    r'const logoIconUrl = `${root}assets/images/logo-icon.png?v=3`;',
    chat_code
)

# Ensure launcher logo styling is centered and sharp
old_launcher_css = re.compile(
    r'#neuro-chat-launcher \.icon-launcher-logo\s*\{[^}]*\}',
    re.DOTALL
)

new_launcher_css = """#neuro-chat-launcher .icon-launcher-logo {
      width: 44px;
      height: 44px;
      object-fit: contain;
      border-radius: 0 !important;
      transition: transform 0.3s ease, opacity 0.2s ease;
      pointer-events: none;
      display: block;
      margin: 0 auto;
      filter: drop-shadow(0 2px 4px rgba(11, 122, 124, 0.18));
    }"""

chat_code = old_launcher_css.sub(new_launcher_css, chat_code)

with open(chat_path, 'w', encoding='utf-8') as f:
    f.write(chat_code)
print("Updated assets/js/chat-widget.js successfully.")


# -------------------------------------------------------------
# 2. OVERHAUL PRODUCTS OVERVIEW HERO IN ALL 3 PRODUCT FILES
# -------------------------------------------------------------
prod_files = ['neuromates-products.html', 'products.html', 'Products _ Neuro Mates.html']

old_header_re = re.compile(
    r'<header class="ph">\s*<div class="w[^"]*">\s*(?:<div class="ph-hero-text">)?\s*<p class="ey">PRODUCTS</p>.*?</div>\s*</header>',
    re.DOTALL
)

new_header_markup = '''<header class="ph">
  <div class="w ph-hero-layout">
    <div class="ph-hero-intro">
      <span class="ey">PRODUCTS</span>
      <h1 class="hl" data-h="rise">Neurological care, <br class="ph-desk-break">designed around the condition.</h1>
      <p class="bl" style="margin-top:20px">Neuro Mates brings together disease-specific products for Parkinson’s, Alzheimer’s, Epilepsy and Paralysis. Each product combines continuous monitoring, connected technology and personalised care support for the needs of the condition.</p>
      <div class="ph-hero-badges">
        <span class="ph-badge-chip">4 Specialised Systems</span>
        <span class="ph-badge-chip">Unified Care Platform</span>
      </div>
    </div>

    <!-- Cohesive 4-Product Care Suite Showcase (Replaces scattered circles) -->
    <div class="product-showcase-hub" aria-label="Neuro Mates Product Suite">
      <div class="showcase-hub-header">
        <span class="showcase-hub-tag"><span class="pulse-indicator"></span> CONNECTED CARE SUITE</span>
        <span class="showcase-hub-sub">Select a care system ↓</span>
      </div>

      <div class="showcase-grid-4">
        <!-- 1. Parkinson's Care -->
        <a href="#parkinsons-care" class="showcase-card" style="--card-accent:#4F9CF9">
          <div class="showcase-thumb-wrap">
            <img data-k="p_person" alt="Parkinson's Care" class="showcase-thumb">
            <span class="showcase-status-dot" style="background:#4F9CF9"></span>
          </div>
          <div class="showcase-info">
            <span class="showcase-eyebrow" style="color:#4F9CF9">PARKINSON’S</span>
            <h4>Parkinson’s Care</h4>
            <p>Tremor &amp; fall monitoring</p>
          </div>
          <span class="showcase-arrow" aria-hidden="true">→</span>
        </a>

        <!-- 2. Alzheimer's Care -->
        <a href="#alzheimers-care" class="showcase-card" style="--card-accent:#9B8CFF">
          <div class="showcase-thumb-wrap">
            <img data-k="a_person" alt="Alzheimer's Care" class="showcase-thumb">
            <span class="showcase-status-dot" style="background:#9B8CFF"></span>
          </div>
          <div class="showcase-info">
            <span class="showcase-eyebrow" style="color:#9B8CFF">ALZHEIMER’S</span>
            <h4>Alzheimer’s Care</h4>
            <p>Memory &amp; safe zone alerts</p>
          </div>
          <span class="showcase-arrow" aria-hidden="true">→</span>
        </a>

        <!-- 3. Epilepsy Care -->
        <a href="#epilepsy-care" class="showcase-card" style="--card-accent:#2BB58A">
          <div class="showcase-thumb-wrap">
            <img data-k="e_person" alt="Epilepsy Care" class="showcase-thumb">
            <span class="showcase-status-dot" style="background:#2BB58A"></span>
          </div>
          <div class="showcase-info">
            <span class="showcase-eyebrow" style="color:#0E7A5A">EPILEPSY</span>
            <h4>Epilepsy Care</h4>
            <p>Continuous EEG headband</p>
          </div>
          <span class="showcase-arrow" aria-hidden="true">→</span>
        </a>

        <!-- 4. Paralysis Care -->
        <a href="#paralysis-care" class="showcase-card" style="--card-accent:#F5B14C">
          <div class="showcase-thumb-wrap">
            <img data-k="pa_face" alt="Paralysis Care" class="showcase-thumb">
            <span class="showcase-status-dot" style="background:#F5B14C"></span>
          </div>
          <div class="showcase-info">
            <span class="showcase-eyebrow" style="color:#D9822B">PARALYSIS</span>
            <h4>Paralysis Care</h4>
            <p>Interactive motor gaming</p>
          </div>
          <span class="showcase-arrow" aria-hidden="true">→</span>
        </a>
      </div>
    </div>
  </div>
</header>'''

showcase_css = '''
/* ==========================================================================
   NEURO MATES — PRODUCT HERO SUITE SHOWCASE
   Replaces scattered floating circles with a balanced, medical-grade 4-card hub
   ========================================================================== */
#v-overview .ph {
  padding-top: clamp(120px, 14vw, 165px);
  padding-bottom: clamp(60px, 8vw, 95px);
  position: relative;
  overflow: visible;
  background: linear-gradient(180deg, rgba(232, 246, 243, 0.45) 0%, rgba(255, 255, 255, 0.95) 100%);
}
.ph-hero-layout {
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  gap: clamp(32px, 5vw, 64px);
  align-items: center;
  position: relative;
  z-index: 2;
}
.ph-hero-intro {
  max-width: 560px;
}
.ph-hero-intro .ey {
  display: inline-block;
  margin-bottom: 14px;
}
.ph-hero-intro h1 {
  font-size: clamp(2.1rem, 3.8vw, 3.2rem) !important;
  line-height: 1.14 !important;
  letter-spacing: -0.015em;
  font-weight: 700;
  margin: 0;
  color: var(--ink, #0E3B43);
}
.ph-desk-break {
  display: block;
}
.ph-hero-badges {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 24px;
}
.ph-badge-chip {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 99px;
  background: #E8F6F3;
  color: #0B7A7C;
  border: 1px solid rgba(11, 122, 124, 0.15);
}

/* 4-Product Hub Card */
.product-showcase-hub {
  background: #FFFFFF;
  border: 1px solid rgba(14, 59, 67, 0.09);
  border-radius: 28px;
  padding: clamp(20px, 3vw, 28px);
  box-shadow: 0 20px 50px rgba(14, 59, 67, 0.08), 0 4px 16px rgba(11, 122, 124, 0.04);
  position: relative;
}
.showcase-hub-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(14, 59, 67, 0.06);
}
.showcase-hub-tag {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: var(--font-heading, sans-serif);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #0B7A7C;
}
.pulse-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #2BB58A;
  box-shadow: 0 0 0 3px rgba(43, 181, 138, 0.25);
  animation: pulseDot 2s infinite;
}
@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.7; }
}
.showcase-hub-sub {
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--mu, #4F6F73);
}

/* 2x2 Showcase Grid */
.showcase-grid-4 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.showcase-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 20px;
  background: #FAFDFB;
  border: 1.5px solid rgba(14, 59, 67, 0.07);
  transition: transform 0.3s var(--sp), box-shadow 0.3s ease, border-color 0.25s ease, background 0.25s ease;
  text-decoration: none;
  color: inherit;
  position: relative;
  overflow: hidden;
}
.showcase-card:hover {
  transform: translateY(-4px);
  background: #FFFFFF;
  border-color: var(--card-accent, #0B7A7C);
  box-shadow: 0 12px 28px rgba(14, 59, 67, 0.1);
}
.showcase-thumb-wrap {
  position: relative;
  width: 58px;
  height: 58px;
  flex-shrink: 0;
}
.showcase-thumb {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  object-fit: cover;
  border: 2.5px solid #FFFFFF;
  box-shadow: 0 6px 14px rgba(14, 59, 67, 0.14);
  background: #E8F6F3;
  display: block;
}
.showcase-status-dot {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid #FFFFFF;
}
.showcase-info {
  flex: 1;
  min-width: 0;
}
.showcase-eyebrow {
  display: block;
  font-family: var(--font-heading, sans-serif);
  font-size: 0.64rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 2px;
}
.showcase-info h4 {
  font-family: var(--font-heading, sans-serif);
  font-weight: 700;
  font-size: 0.92rem;
  line-height: 1.25;
  color: var(--ink, #0E3B43);
  margin: 0 0 2px 0 !important;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.showcase-info p {
  font-size: 0.74rem;
  color: var(--mu, #4F6F73);
  line-height: 1.35;
  margin: 0 !important;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.showcase-arrow {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--card-accent, #0B7A7C);
  opacity: 0;
  transform: translateX(-4px);
  transition: opacity 0.25s ease, transform 0.25s ease;
  flex-shrink: 0;
}
.showcase-card:hover .showcase-arrow {
  opacity: 1;
  transform: translateX(0);
}

@media (max-width: 900px) {
  .ph-hero-layout {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .ph-desk-break {
    display: inline;
  }
  .showcase-grid-4 {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 580px) {
  .showcase-grid-4 {
    grid-template-columns: 1fr;
  }
}
'''

for fn in prod_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old header markup
    if old_header_re.search(content):
        content = old_header_re.sub(new_header_markup, content)
        print(f"Replaced hero header in {fn}")
    else:
        # Fallback locate <div class="pv on" id="v-overview">
        idx = content.find('id="v-overview"')
        if idx != -1:
            h_start = content.find('<header class="ph">', idx)
            h_end = content.find('</header>', h_start) + len('</header>')
            content = content[:h_start] + new_header_markup + content[h_end:]
            print(f"Fallback replaced hero header in {fn}")
        else:
            print(f"v-overview not found in {fn}")

    # Inject new CSS
    if '.product-showcase-hub' not in content:
        content = content.replace('</style>', showcase_css + '\n</style>', 1)
        print(f"Added showcase CSS in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating products files.")
