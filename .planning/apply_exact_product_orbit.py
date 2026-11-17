import re

targets = [
    r"d:\Neuromates(website)\neuromates-products.html",
    r"d:\Neuromates(website)\products.html",
    r"d:\Neuromates(website)\Products _ Neuro Mates.html"
]

new_css = """/* ==========================================================================
   NEURO MATES — PRODUCTS OVERVIEW HERO (EXACT ORBIT STAGE DESIGN)
   ========================================================================== */
#v-overview .ph {
  position: relative;
  overflow: visible;
  padding-top: clamp(120px, 14vw, 160px);
  padding-bottom: clamp(60px, 8vw, 95px);
  background: var(--bg, #FAF8F5);
}
.ph-hero-grid {
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  align-items: center;
  gap: clamp(24px, 4vw, 48px);
  position: relative;
  z-index: 2;
}
.ph-hero-text {
  max-width: 540px;
}
.ph-hero-text .ey {
  display: inline-block;
  font-family: var(--font-heading, sans-serif);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #0B7A7C;
  margin-bottom: 14px;
}
.ph-hero-text h1 {
  font-family: var(--font-heading, sans-serif);
  font-size: clamp(2.3rem, 4vw, 3.6rem) !important;
  line-height: 1.15 !important;
  letter-spacing: -0.018em;
  font-weight: 700;
  margin: 0;
  color: var(--ink, #0E3B43);
}
.ph-hero-text p.bl {
  max-width: 440px;
  margin-top: 22px;
  line-height: 1.65;
  color: var(--mu, #4F6F73);
  font-size: 1rem;
}

/* Orbit Stage Container */
.product-orbit-stage {
  position: relative;
  width: 100%;
  max-width: 480px;
  height: 440px;
  margin-left: auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Central Soft Glow Aura (Teal / Purple) */
.orbit-glow {
  position: absolute;
  width: 360px;
  height: 360px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(160, 235, 225, 0.45) 0%, rgba(205, 195, 255, 0.38) 45%, rgba(250, 248, 245, 0) 72%);
  filter: blur(10px);
  pointer-events: none;
  z-index: 1;
}

/* Dashed Orbit Ring */
.orbit-ring {
  position: absolute;
  width: 330px;
  height: 330px;
  border-radius: 50%;
  border: 1.5px dashed rgba(43, 181, 138, 0.42);
  pointer-events: none;
  z-index: 2;
}

/* 4 Circular Product Photos on Orbit */
.orbit-photos {
  position: absolute;
  inset: 0;
  z-index: 3;
}
.orbit-photo {
  position: absolute;
  border-radius: 50% !important;
  object-fit: cover !important;
  border: 4px solid #FFFFFF !important;
  background: #E8F6F3;
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease;
  animation: orbitFloat 5s ease-in-out infinite;
}
.orbit-photo:hover {
  transform: scale(1.06);
  box-shadow: 0 20px 42px rgba(14, 59, 67, 0.22) !important;
  z-index: 10;
}

/* 1. Parkinson's (Top-Left: 10:30) */
.orbit-p1 {
  width: 146px;
  height: 146px;
  top: 18px;
  left: 18px;
  box-shadow: 0 14px 32px rgba(14, 59, 67, 0.14) !important;
}

/* 2. Alzheimer's (Top-Right: 1:30) */
.orbit-p2 {
  width: 136px;
  height: 136px;
  top: 6px;
  right: 20px;
  box-shadow: 0 14px 32px rgba(14, 59, 67, 0.14) !important;
  animation-delay: -1.2s;
}

/* 3. Epilepsy (Bottom-Left: 6:45) */
.orbit-p3 {
  width: 160px;
  height: 160px;
  bottom: 10px;
  left: 92px;
  box-shadow: 0 16px 38px rgba(14, 59, 67, 0.16) !important;
  animation-delay: -2.4s;
}

/* 4. Paralysis (Middle-Right: 4:15) */
.orbit-p4 {
  width: 138px;
  height: 138px;
  top: 195px;
  right: 6px;
  box-shadow: 0 14px 32px rgba(14, 59, 67, 0.14) !important;
  animation-delay: -3.5s;
}

@keyframes orbitFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-7px); }
}

@media (max-width: 900px) {
  .ph-hero-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .product-orbit-stage {
    margin: 0 auto;
    max-width: 400px;
    height: 380px;
  }
  .orbit-glow { width: 300px; height: 300px; }
  .orbit-ring { width: 270px; height: 270px; }
  .orbit-p1 { width: 120px; height: 120px; top: 10px; left: 10px; }
  .orbit-p2 { width: 112px; height: 112px; top: 0px; right: 10px; }
  .orbit-p3 { width: 130px; height: 130px; bottom: 8px; left: 70px; }
  .orbit-p4 { width: 114px; height: 114px; top: 160px; right: 0px; }
}

@media (max-width: 540px) {
  .product-orbit-stage {
    display: none;
  }
}"""

new_header_html = """<header class="ph">
  <div class="w ph-hero-grid">
    <div class="ph-hero-text">
      <span class="ey">PRODUCTS</span>
      <h1 class="hl" data-h="rise">Neurological care,<br>designed around the<br>condition.</h1>
      <p class="bl" style="margin-top:22px">Neuro Mates brings together disease-specific products for Parkinson’s, Alzheimer’s, Epilepsy and Paralysis. Each product combines appropriate monitoring, connected technology and personalised care support for the needs of the condition.</p>
    </div>
    <div class="product-orbit-stage" aria-hidden="true">
      <div class="orbit-glow"></div>
      <div class="orbit-ring"></div>
      <div class="orbit-photos">
        <img data-k="p_person" class="orbit-photo orbit-p1" alt="Parkinson's Care Wearable">
        <img data-k="a_person" class="orbit-photo orbit-p2" alt="Alzheimer's Care Wearable">
        <img data-k="e_person" class="orbit-photo orbit-p3" alt="Epilepsy Monitoring Headband">
        <img data-k="pa_face" class="orbit-photo orbit-p4" alt="Paralysis Care Rehabilitation">
      </div>
    </div>
  </div>
</header>"""

css_regex = re.compile(
    r'/\* ==========================================================================\s*'
    r'NEURO MATES — PRODUCTS OVERVIEW HERO.*?</style>',
    re.DOTALL
)

header_regex = re.compile(
    r'<header class="ph">\s*<div class="w">.*?<div class="orb" aria-hidden="true">.*?</div>\s*</header>',
    re.DOTALL
)

for target in targets:
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace CSS
    css_match = css_regex.search(content)
    if css_match:
        content = content[:css_match.start()] + new_css + "\n</style>" + content[css_match.end():]
        print(f"Replaced CSS in {target}")
    else:
        print(f"CSS pattern not found in {target}")

    # Replace Header HTML
    header_match = header_regex.search(content)
    if header_match:
        content = content[:header_match.start()] + new_header_html + content[header_match.end():]
        print(f"Replaced Header in {target}")
    else:
        print(f"Header pattern not found in {target}")

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)

print("Exact product orbit stage applied successfully!")
