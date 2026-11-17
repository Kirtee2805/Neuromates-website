import os, re

# Define the exact Google Fonts link tag and @import
GOOGLE_FONTS_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600;1,700&family=Sora:wght@600;700&display=swap" rel="stylesheet">'
GOOGLE_FONTS_IMPORT = "@import url('https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600;1,700&family=Sora:wght@600;700&display=swap');"

# 3-Column Footer HTML (without Explore column)
def get_3col_footer(root=""):
    return f'''<footer class="nm-footer" id="global-footer">
  <div class="nm-footer-top-line"></div>
  <div class="nm-footer-wrap">
    
    <!-- Row 1: 3-Column Grid (Brand, Our Vision, Contact Us) -->
    <div class="nm-footer-grid">
      <!-- Col 1: Brand -->
      <div class="nm-footer-col nm-footer-brand">
        <a class="nm-footer-logo-tile" href="{root}index.html" aria-label="Neuro Mates Home">
          <img src="{root}assets/images/logo.png" alt="Neuro Mates">
        </a>
        <p class="nm-footer-tagline">MONITOR · DETECT · ALERT · CARE</p>
        <p class="nm-footer-brand-desc">An AI and IoT-based smart care system for Parkinson's, Alzheimer's, Epilepsy and Paralysis.</p>
      </div>

      <!-- Col 2: Our Vision -->
      <div class="nm-footer-col nm-footer-vision">
        <span class="nm-footer-label">Our vision</span>
        <p class="nm-footer-vision-stmt">A future where neurological care stays connected.</p>
        <p class="nm-footer-vision-body">Our vision is to make continuous neurological care more accessible, connected and personalised by bringing patients, families, healthcare professionals and technology into one care ecosystem.</p>
      </div>

      <!-- Col 3: Contact Us -->
      <div class="nm-footer-col nm-footer-contact">
        <span class="nm-footer-label">CONTACT US</span>
        <p class="nm-footer-contact-body">Interested in Neuro Mates, our products, healthcare collaboration or a product demonstration? Get in touch with our team.</p>
        <div class="nm-footer-buttons">
          <a class="nm-btn-contact" href="{root}contact.html">Contact us →</a>
          <a class="nm-btn-demo" href="{root}register-demo.html">Register for a demo →</a>
        </div>
        <!-- SLOT: Address, phone, email, legal and social links can be placed here in future updates -->
      </div>
    </div>

    <!-- Row 2: Team Strip -->
    <div class="nm-footer-team-strip">
      <span class="nm-footer-label">Our team</span>
      <div class="nm-footer-team-pills">
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#6EC1F0;">BS</span>
          <span class="nm-team-name">Bhavik Solanki</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#9B8CFF;">AB</span>
          <span class="nm-team-name">Anandi Bhayani</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#5BE7C4;">KP</span>
          <span class="nm-team-name">Kirtee Pitroda</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#F5B14C;">MM</span>
          <span class="nm-team-name">Maulik Mehta</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#FF9AD0;">VJ</span>
          <span class="nm-team-name">Vasu Janjrukiya</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#7FD6D0;">DV</span>
          <span class="nm-team-name">Darshil Vashnani</span>
        </div>
      </div>
    </div>

    <!-- Row 3: Bottom Bar -->
    <div class="nm-footer-bottom-bar">
      <div class="nm-footer-bottom-left">
        <span>&copy; Neuro Mates &middot; Connected neurological care</span>
      </div>
      <div class="nm-footer-bottom-right">
        <span class="nm-footer-disclaimer">Not a substitute for professional medical advice</span>
        <a class="nm-footer-back-to-top" href="#" aria-label="Back to top">&uarr; Back to top</a>
      </div>
    </div>

  </div>
</footer>'''

# 3-Column Footer Inner (for shared.js)
def get_3col_footer_inner(root="${root}"):
    full = get_3col_footer(root)
    # strip outer <footer...> and </footer>
    inner = full[full.find('>')+1 : full.rfind('</footer>')].strip()
    return inner

# Unified Core Typography & Layout CSS
CORE_TYPOGRAPHY_CSS = '''
/* ==========================================================================
   NEURO MATES — TYPOGRAPHY & DESIGN TOKENS
   Fonts: Sora (Headings: 600, 700) & Figtree (Body & UI: 400, 500, 600, 700)
   ========================================================================== */

:root {
  --font-heading: 'Sora', "Segoe UI", system-ui, sans-serif;
  --font-body: 'Figtree', "Segoe UI", system-ui, sans-serif;
  --fd: var(--font-heading);
  --fb: var(--font-body);
}

body {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.65;
  font-weight: 400;
  color: var(--ink, #0E3B43);
}

p {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.65;
  max-width: 68ch;
  font-weight: 400;
}

/* Headings: Sora (600 and 700 only) */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  margin: 0;
  letter-spacing: -0.015em;
  color: var(--ink, #0E3B43);
  overflow-wrap: anywhere;
}

header.h h1,
.hero h1,
.hero-h1 {
  font-size: clamp(2.1rem, 4.2vw, 3.6rem);
  line-height: 1.12;
  letter-spacing: -0.015em;
  font-weight: 700;
  max-width: 16em;
}

h1 {
  font-size: clamp(1.9rem, 3.6vw, 3.1rem);
  line-height: 1.15;
  font-weight: 700;
}

h2 {
  font-size: clamp(1.55rem, 2.7vw, 2.3rem);
  line-height: 1.2;
  font-weight: 600;
}

h3 {
  font-size: clamp(1.15rem, 1.7vw, 1.4rem);
  line-height: 1.3;
  font-weight: 600;
}

h4 {
  font-size: 1.05rem;
  line-height: 1.35;
  font-weight: 600;
}

/* Headline accent phrase: gradient color only, NO italic */
h1 em,
h2 em,
h3 em,
.hero em,
em {
  font-family: inherit;
  font-style: normal !important;
  font-weight: 600;
  background: linear-gradient(100deg, #0B7A7C, #2BB58A 55%, #3B6CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Large statements (impact words, mission and vision) */
.large-statement,
.im b,
.vision-stmt,
.nm-footer-vision-stmt {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 3.4vw, 2.9rem);
  line-height: 1.2;
  font-weight: 600;
  overflow-wrap: anywhere;
}

/* Lead paragraph (hero body) */
.bl,
p.lead,
.hero-lead {
  font-family: var(--font-body);
  font-size: 1.075rem;
  line-height: 1.6;
  max-width: 34em;
}

/* Small text and captions */
small, .caption, .subtext {
  font-family: var(--font-body);
  font-size: 0.875rem;
  line-height: 1.5;
}

/* Eyebrows and labels */
.ey,
.nm-footer-label,
.eyebrow,
label {
  font-family: var(--font-body);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

/* Navbar items */
nav ul,
nav li > a,
.navbar-item {
  font-family: var(--font-body);
  font-size: 0.74rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

/* Buttons */
.btn,
.b2,
button,
.nm-btn-contact,
.nm-btn-demo {
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 600;
}

/* Numbers in steps, charts, timelines: Tabular Numbers */
.cd .n,
.nd,
#steps,
.tabular-nums,
.metric-num,
.stat-number,
.timeline {
  font-variant-numeric: tabular-nums;
  font-family: var(--font-body);
}

/* Site Navigation (Pinned at top, does not scroll down over content) */
nav#nav,
nav {
  position: absolute !important;
  top: calc(16px + env(safe-area-inset-top, 0px)) !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: min(1240px, calc(100% - 24px));
  z-index: 500;
}

/* Footer: 3-column layout without Explore */
footer.nm-footer,
footer {
  position: relative;
  z-index: 10;
  background: linear-gradient(160deg, #0B3A44, #0B5260 60%, #0B6F86);
  color: rgba(232, 244, 242, 0.86);
  padding: 64px 0 0;
  overflow: hidden;
  font-family: var(--font-body);
}

.nm-footer-top-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, #0B7A7C, #2BB58A, #6EC1F0, #A99BFF, #FFC857);
}

.nm-footer-wrap {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 clamp(20px, 4vw, 36px);
  box-sizing: border-box;
}

.nm-footer-grid {
  display: grid;
  grid-template-columns: 1.15fr 1.45fr 1.1fr;
  gap: 48px;
  align-items: start;
}

.nm-footer-col {
  display: flex;
  flex-direction: column;
}

.nm-footer-logo-tile {
  display: inline-block;
  background: #FFFFFF;
  border-radius: 16px;
  padding: 8px 14px;
  align-self: flex-start;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.12);
  transition: transform 0.2s ease;
}
.nm-footer-logo-tile:hover {
  transform: translateY(-2px);
}
.nm-footer-logo-tile img {
  height: 42px;
  width: auto;
  display: block;
}

.nm-footer-tagline {
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  color: #7FD6D0;
  margin: 18px 0 10px;
  text-transform: uppercase;
}

.nm-footer-brand-desc {
  font-size: 0.92rem;
  line-height: 1.55;
  color: rgba(232, 244, 242, 0.86);
  margin: 0;
}

.nm-footer-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #7FD6D0;
  display: block;
  margin-bottom: 12px;
}

.nm-footer-vision-stmt {
  font-family: var(--font-heading);
  font-size: clamp(1.25rem, 2vw, 1.45rem);
  font-weight: 600;
  color: #FFFFFF;
  line-height: 1.35;
  margin: 0 0 12px;
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.7s cubic-bezier(.22, 1, .36, 1), transform 0.7s cubic-bezier(.22, 1, .36, 1);
}
.footer-in-view .nm-footer-vision-stmt {
  opacity: 1;
  transform: translateY(0);
}

.nm-footer-vision-body {
  font-size: 0.92rem;
  line-height: 1.6;
  color: rgba(232, 244, 242, 0.86);
  margin: 0;
}

.nm-footer-contact-body {
  font-size: 0.92rem;
  line-height: 1.55;
  color: rgba(232, 244, 242, 0.86);
  margin: 0 0 20px;
}

.nm-footer-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.nm-btn-contact {
  background: #FFFFFF;
  color: #0B6F6F !important;
  border-radius: 99px;
  padding: 10px 22px;
  font-weight: 600;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.14);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  align-self: flex-start;
}
.nm-btn-contact:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.22);
}

.nm-btn-demo {
  background: transparent;
  border: 2px solid #7FD6D0;
  color: #7FD6D0 !important;
  border-radius: 99px;
  padding: 9px 20px;
  font-weight: 600;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: background 0.2s ease, color 0.2s ease, transform 0.2s ease;
  align-self: flex-start;
}
.nm-btn-demo:hover {
  background: rgba(127, 214, 208, 0.12);
  color: #FFFFFF !important;
  transform: translateY(-2px);
}

.nm-footer-team-strip {
  margin-top: 44px;
  border-top: 1px solid rgba(255, 255, 255, 0.16);
  padding-top: 28px;
}

.nm-footer-team-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.nm-team-pill {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 99px;
  padding: 5px 18px 5px 6px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  opacity: 0;
  transform: translateY(14px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  transition: background 0.2s ease, transform 0.2s ease;
}
.nm-team-pill:hover {
  background: rgba(255, 255, 255, 0.14);
  transform: translateY(-2px) !important;
}

.nm-team-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-weight: 700;
  font-size: 0.82rem;
  color: #04161C;
  letter-spacing: -0.02em;
}

.nm-team-name {
  font-weight: 600;
  font-size: 0.88rem;
  color: #E8F4F2;
  white-space: nowrap;
}

.footer-in-view .nm-team-pill {
  animation: nmPillRise 0.5s cubic-bezier(.22, 1, .36, 1) forwards;
}
.footer-in-view .nm-team-pill:nth-child(1) { animation-delay: 0ms; }
.footer-in-view .nm-team-pill:nth-child(2) { animation-delay: 60ms; }
.footer-in-view .nm-team-pill:nth-child(3) { animation-delay: 120ms; }
.footer-in-view .nm-team-pill:nth-child(4) { animation-delay: 180ms; }
.footer-in-view .nm-team-pill:nth-child(5) { animation-delay: 240ms; }
.footer-in-view .nm-team-pill:nth-child(6) { animation-delay: 300ms; }

@keyframes nmPillRise {
  from { opacity: 0; transform: translateY(14px); }
  to { opacity: 1; transform: translateY(0); }
}

.nm-footer-bottom-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.16);
  margin-top: 36px;
  padding: 24px 0 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 0.84rem;
  color: rgba(232, 244, 242, 0.72);
}

.nm-footer-bottom-left {
  display: flex;
  align-items: center;
}

.nm-footer-bottom-right {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.nm-footer-disclaimer {
  font-style: italic;
  opacity: 0.85;
}

.nm-footer-back-to-top {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #7FD6D0 !important;
  font-weight: 700;
  text-decoration: none;
  background: rgba(127, 214, 208, 0.1);
  padding: 6px 14px;
  border-radius: 99px;
  transition: background 0.2s ease, transform 0.2s ease;
}
.nm-footer-back-to-top:hover {
  background: rgba(127, 214, 208, 0.22);
  color: #FFFFFF !important;
  transform: translateY(-2px);
}

footer a:focus-visible,
footer button:focus-visible,
.nm-footer a:focus-visible,
.nm-footer button:focus-visible {
  outline: 3px solid #9AF2DB !important;
  outline-offset: 3px !important;
}

/* Mobile Adjustments (under 640px and 900px) */
@media (max-width: 900px) {
  footer.nm-footer,
  footer {
    padding-top: 48px;
  }
  .nm-footer-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .nm-btn-contact,
  .nm-btn-demo {
    width: 100%;
    align-self: stretch;
    text-align: center;
  }
  .nm-footer-bottom-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 14px;
  }
  .nm-footer-bottom-right {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    width: 100%;
  }
  .nm-footer-back-to-top {
    align-self: flex-start;
  }
}

@media (max-width: 640px) {
  header.h h1,
  .hero h1,
  .hero-h1,
  h1 {
    font-size: 2.1rem !important;
    line-height: 1.15;
  }
  h2 {
    font-size: 1.55rem !important;
    line-height: 1.22;
  }
  .large-statement,
  .im b,
  .vision-stmt,
  .nm-footer-vision-stmt {
    font-size: 1.7rem !important;
    line-height: 1.25;
  }
  * {
    overflow-wrap: anywhere;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-team-pill,
  .nm-footer-vision-stmt {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
    transition: none !important;
  }
}
'''

# 1. Update assets/css/tokens.css
with open('assets/css/tokens.css', 'r', encoding='utf-8') as f:
    tokens = f.read()

# Replace font import
tokens = re.sub(r'@import url\(\'https://fonts\.googleapis\.com[^\']+\'\);', GOOGLE_FONTS_IMPORT, tokens)

# Replace :root font variables
tokens = re.sub(r'--font-heading:[^;]+;', "--font-heading: 'Sora', \"Segoe UI\", system-ui, sans-serif;", tokens)
tokens = re.sub(r'--font-body:[^;]+;', "--font-body: 'Figtree', \"Segoe UI\", system-ui, sans-serif;", tokens)
tokens = re.sub(r'--fd:[^;]+;', "--fd: var(--font-heading);", tokens)
tokens = re.sub(r'--fb:[^;]+;', "--fb: var(--font-body);", tokens)

# Replace entire footer and typography section in tokens.css
footer_idx = tokens.find('/* --- Footer --- */')
if footer_idx != -1:
    tokens = tokens[:footer_idx] + '/* --- Footer --- */\n' + CORE_TYPOGRAPHY_CSS
else:
    tokens += '\n' + CORE_TYPOGRAPHY_CSS

# Clean up any leftover old fonts in tokens.css
tokens = tokens.replace('Fraunces', 'Sora').replace('DM Sans', 'Figtree').replace('Plus Jakarta Sans', 'Figtree').replace('IBM Plex Mono', 'Figtree')

with open('assets/css/tokens.css', 'w', encoding='utf-8') as f:
    f.write(tokens)
print("Updated tokens.css with Sora + Figtree and 3-column footer!")

# 2. Update assets/js/shared.js
with open('assets/js/shared.js', 'r', encoding='utf-8') as f:
    shared = f.read()

# Replace getFooterHTML
shared = re.sub(
    r'getFooterHTML:\s*function\s*\(\)\s*\{[\s\S]*?\},',
    f'''getFooterHTML: function () {{
      setTimeout(initFooterObserver, 0);
      return `{get_3col_footer_inner()}`;
    }},''',
    shared
)
with open('assets/js/shared.js', 'w', encoding='utf-8') as f:
    f.write(shared)
print("Updated shared.js with 3-column footer!")

# 3. Process all 23 HTML files
html_count = 0
for root_dir, dirs, files in os.walk('.'):
    if '.git' in root_dir or '.planning' in root_dir:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root_dir, f)
            rel_dir = os.path.relpath(root_dir, '.')
            root_prefix = '' if rel_dir == '.' else '../'
            if rel_dir.count(os.sep) > 0:
                root_prefix = '../' * (rel_dir.count(os.sep) + 1)
            
            with open(filepath, 'r', encoding='utf-8') as fh:
                html = fh.read()
            
            # Replace Google Font link tag
            html = re.sub(
                r'<link[^>]*fonts\.googleapis\.com[^>]*>(?:\s*<link[^>]*fonts\.gstatic\.com[^>]*>)?(?:\s*<link[^>]*family=[^>]*>)?',
                GOOGLE_FONTS_LINK,
                html,
                flags=re.IGNORECASE
            )
            # Remove any extra font links
            html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]+">', '', html)
            
            # Remove old font names
            html = html.replace('Fraunces', 'Sora').replace('DM Sans', 'Figtree').replace('Plus Jakarta Sans', 'Figtree').replace('IBM Plex Mono', 'Figtree')
            
            # Ensure --font-heading and --font-body in style tags
            html = re.sub(r'--fd:[^;]+;', '--fd:var(--font-heading);', html)
            html = re.sub(r'--fb:[^;]+;', '--fb:var(--font-body);', html)
            
            # Update footer with 3-column layout (no Explore)
            footer_markup = get_3col_footer(root_prefix)
            html = re.sub(r'<footer[\s\S]*?</footer>', footer_markup, html)
            
            # For standalone pages, inject CORE_TYPOGRAPHY_CSS into <style> if not loading tokens.css
            if 'tokens.css' not in html:
                # remove old nm-footer styles if present to prevent duplicates
                html = re.sub(r'/\* ==========================================================================\s*NEURO MATES — PRODUCTION FOOTER STYLES[\s\S]*?(?=</style>)', '', html)
                html = re.sub(r'/\* ==========================================================================\s*NEURO MATES — TYPOGRAPHY & DESIGN TOKENS[\s\S]*?(?=</style>)', '', html)
                
                style_end = html.find('</style>')
                if style_end != -1:
                    html = html[:style_end] + '\n' + CORE_TYPOGRAPHY_CSS + '\n</style>' + html[style_end+8:]
            
            with open(filepath, 'w', encoding='utf-8') as fh:
                fh.write(html)
            html_count += 1
            print(f"Updated {filepath}")

print(f"All {html_count} HTML files processed!")

