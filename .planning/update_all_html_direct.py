import os, re

def get_footer_markup(root):
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

# Process ALL 23 HTML files
updated = 0
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
            
            footer_html = get_footer_markup(root_prefix)
            new_html = re.sub(r'<footer[\s\S]*?</footer>', footer_html, html)
            
            if new_html != html:
                with open(filepath, 'w', encoding='utf-8') as fh:
                    fh.write(new_html)
                print(f"Directly updated footer in: {filepath} (root_prefix: '{root_prefix}')")
                updated += 1
            else:
                print(f"No footer change needed in: {filepath}")

print(f"Updated {updated} files directly.")
