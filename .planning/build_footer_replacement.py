import os, re

FOOTER_CSS = '''
/* ==========================================================================
   NEURO MATES — PRODUCTION FOOTER STYLES
   ========================================================================== */

footer.nm-footer,
footer {
  position: relative;
  z-index: 10;
  background: linear-gradient(160deg, #0B3A44, #0B5260 60%, #0B6F86);
  color: rgba(232, 244, 242, 0.86);
  padding: 64px 0 0;
  overflow: hidden;
  font-family: var(--fb, 'Plus Jakarta Sans', system-ui, sans-serif);
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

/* Row 1: 4-Column Grid */
.nm-footer-grid {
  display: grid;
  grid-template-columns: 1.1fr 1.3fr 0.8fr 1.1fr;
  gap: 44px;
  align-items: start;
}

.nm-footer-col {
  display: flex;
  flex-direction: column;
}

/* Col 1: Brand */
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

/* Labels across columns */
.nm-footer-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #7FD6D0;
  display: block;
  margin-bottom: 12px;
}

/* Col 2: Vision */
.nm-footer-vision-stmt {
  font-family: var(--fd, 'Sora', sans-serif);
  font-size: 1.25rem;
  font-weight: 700;
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

/* Col 3: Explore */
.nm-footer-nav {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.nm-footer-nav a {
  display: inline-block;
  color: rgba(232, 244, 242, 0.86);
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
  background: linear-gradient(#9AF2DB, #9AF2DB) 0 100% / 0 2px no-repeat;
  transition: background-size 0.35s cubic-bezier(.22, 1, .36, 1), color 0.25s;
  padding: 3px 0;
  align-self: flex-start;
}
.nm-footer-nav a:hover {
  color: #9AF2DB;
  background-size: 100% 2px;
}

/* Col 4: Contact Us */
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
  font-weight: 700;
  font-size: 0.88rem;
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
  font-weight: 700;
  font-size: 0.88rem;
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

/* Row 2: Team Strip */
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
  font-weight: 800;
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

/* Row 2 Animation: Staggered Rise */
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
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Row 3: Bottom Bar */
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

/* Accessibility: Focus Rings */
footer a:focus-visible,
footer button:focus-visible,
.nm-footer a:focus-visible,
.nm-footer button:focus-visible {
  outline: 3px solid #9AF2DB !important;
  outline-offset: 3px !important;
}

/* Mobile Responsive (under 900px) */
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

/* Respect prefers-reduced-motion */
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

def get_footer_html(root=""):
    return f'''<footer class="nm-footer" id="global-footer">
  <div class="nm-footer-top-line"></div>
  <div class="nm-footer-wrap">
    
    <!-- Row 1: 4-Column Grid -->
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

      <!-- Col 3: Explore -->
      <div class="nm-footer-col nm-footer-explore">
        <span class="nm-footer-label">EXPLORE</span>
        <nav class="nm-footer-nav" aria-label="Footer Explore Navigation">
          <a href="{root}neuromates-products.html#overview">Products</a>
          <a href="{root}technology/index.html">Technology</a>
          <a href="{root}insights/index.html">Insights</a>
          <a href="{root}about/index.html">About Us</a>
          <a href="{root}contact.html">Contact Us</a>
          <a href="{root}register-demo.html">Register for a Demo</a>
        </nav>
      </div>

      <!-- Col 4: Contact Us -->
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

FOOTER_OBSERVER_JS = '''
function initFooterObserver() {
  const footer = document.querySelector('footer');
  if (!footer) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    footer.classList.add('footer-in-view');
  } else {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        footer.classList.add('footer-in-view');
        observer.disconnect();
      }
    }, { threshold: 0.1 });
    observer.observe(footer);
  }

  const topBtn = footer.querySelector('.nm-footer-back-to-top');
  if (topBtn) {
    topBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}
'''

# 1. Update assets/css/tokens.css
with open('assets/css/tokens.css', 'r', encoding='utf-8') as f:
    tokens = f.read()

# Replace footer styles in tokens.css
footer_start = tokens.find('/* --- Footer --- */')
if footer_start != -1:
    footer_end = tokens.find('/* --- Chat Widget', footer_start)
    if footer_end == -1:
        footer_end = tokens.find('@media (max-width: 900px)', footer_start)
        # find end of media query
        if footer_end != -1:
            next_sec = tokens.find('/* ---', footer_end)
            if next_sec != -1:
                footer_end = next_sec
            else:
                footer_end = len(tokens)
        else:
            footer_end = len(tokens)
    tokens = tokens[:footer_start] + '/* --- Footer --- */\n' + FOOTER_CSS + '\n' + tokens[footer_end:]
else:
    tokens += '\n/* --- Footer --- */\n' + FOOTER_CSS

with open('assets/css/tokens.css', 'w', encoding='utf-8') as f:
    f.write(tokens)
print("Updated assets/css/tokens.css")

# 2. Update assets/js/shared.js
with open('assets/js/shared.js', 'r', encoding='utf-8') as f:
    shared = f.read()

# Replace getFooterHTML in shared.js
m = re.search(r'getFooterHTML:\s*function\s*\(\)\s*\{[\s\S]*?\},', shared)
if m:
    new_get_footer = f'''getFooterHTML: function () {{
      return `{get_footer_html('${root}')}`;
    }},'''
    shared = shared[:m.start()] + new_get_footer + shared[m.end():]
    print("Replaced getFooterHTML in assets/js/shared.js")

# Add initFooterObserver to shared.js if not present
if 'initFooterObserver' not in shared:
    # insert before initBackToTop() or at auto-init
    shared = shared.replace('initBackToTop();', 'initBackToTop();\n    initFooterObserver();')
    # add definition
    shared = shared.replace('function initBackToTop() {', FOOTER_OBSERVER_JS + '\n  function initBackToTop() {')
    print("Added initFooterObserver to assets/js/shared.js")

with open('assets/js/shared.js', 'w', encoding='utf-8') as f:
    f.write(shared)

print("assets/js/shared.js successfully updated!")

