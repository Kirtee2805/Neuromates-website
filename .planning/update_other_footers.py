import os, re

files_to_check = [
    'neuromates-products.html',
    'products.html',
    'neuromates-home.html',
    'Neuro Mates _ Connected neurological care.html',
    'Products _ Neuro Mates.html'
]

new_footer = '''<footer>
  <div class="w fg">
    <div class="fb">
      <a class="lg" href="index.html" aria-label="Neuro Mates Home">
        <img src="assets/images/logo.png" alt="Neuro Mates" style="height:44px;width:auto;">
      </a>
      <p>MONITOR · DETECT · ALERT · CARE</p>
      <p class="desc" style="font-size:0.9rem;line-height:1.55;color:#335C64;max-width:32ch;margin:8px 0 16px;">Continuous, connected neurological intelligence empowering patients, caregivers, and clinicians with proactive care.</p>
      <a class="btn" href="register-demo.html">Register for a demo →</a>
    </div>

    <div class="fc">
      <h4>About Us</h4>
      <a href="about/index.html">Who We Are</a>
      <a href="about/our-approach.html">Our Approach</a>
      <a href="technology/index.html">Technology &amp; R&amp;D</a>
      <a href="insights/index.html">Clinical Insights</a>
      <a href="neuromates-products.html#overview">Products &amp; Ecosystem</a>
    </div>

    <div class="fc">
      <h4>Our Vision</h4>
      <p style="font-size:0.88rem;line-height:1.55;color:#335C64;margin-bottom:10px;">Pioneering proactive neurological intervention—transforming periodic clinic visits into continuous 24/7 protection and peace of mind.</p>
      <a href="about/vision-mission.html">Vision &amp; Mission →</a>
      <a href="contact.html">Get in Touch →</a>
    </div>

    <div class="fc">
      <h4>Our Team</h4>
      <div class="team-list">
        <span class="team-member"><span class="dot"></span>Bhavik Solanki</span>
        <span class="team-member"><span class="dot"></span>Anandi Bhayani</span>
        <span class="team-member"><span class="dot"></span>Kirtee Pitroda</span>
        <span class="team-member"><span class="dot"></span>Maulik Mehta</span>
        <span class="team-member"><span class="dot"></span>Vasu Janjrukiya</span>
        <span class="team-member"><span class="dot"></span>Darshil Vashnani</span>
      </div>
    </div>

    <a class="top" href="#" aria-label="Back to top">↑ Top</a>
  </div>
  <div class="w fl">
    <span>&copy; 2026 Neuro Mates. All rights reserved.</span>
    <span>Connected Neurological Care</span>
  </div>
</footer>'''

for fname in files_to_check:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace footer if present
    m = re.search(r'<footer>[\s\S]*?</footer>', content)
    if m:
        content = content[:m.start()] + new_footer + content[m.end():]
        print(f"Updated footer in {fname}")
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)

