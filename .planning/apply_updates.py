import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Font link
old_font = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&display=swap">'
new_font = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Sora:wght@300;400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap">'
if old_font in html:
    html = html.replace(old_font, new_font)
    print("Replaced font link in index.html")
else:
    print("Font link not matched exactly, looking with regex")
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?family=DM\+Sans:[^"]+">', new_font, html)

# Font variables
html = html.replace('--fd:Fraunces,Georgia,serif;', "--fd:'Sora','Plus Jakarta Sans',system-ui,sans-serif;")
html = html.replace("--fb:'DM Sans',system-ui,sans-serif;", "--fb:'Plus Jakarta Sans','DM Sans',system-ui,sans-serif;")

# Headings and large font sizes
html = html.replace('h1{font-size:clamp(2.8rem,6.4vw,5.6rem)}', 'h1{font-size:clamp(2.0rem,3.8vw,3.15rem);letter-spacing:-.02em;line-height:1.14}')
html = html.replace('h2{font-size:clamp(2rem,4.2vw,3.5rem);max-width:17em}', 'h2{font-size:clamp(1.5rem,2.6vw,2.25rem);max-width:20em;letter-spacing:-.015em;line-height:1.22}')
html = html.replace('.cd .n{font:700 clamp(4rem,10vw,8rem)/1 var(--fd);opacity:.32}', '.cd .n{font:700 clamp(2.4rem,5.5vw,4.2rem)/1 var(--fd);opacity:.35}')
html = html.replace('im b{font:700 clamp(2.2rem,5.5vw,4.4rem)/1.05 var(--fd);display:block;letter-spacing:-.02em;transition:color .5s}', 'im b{font:700 clamp(1.6rem,3.2vw,2.4rem)/1.15 var(--fd);display:block;letter-spacing:-.015em;transition:color .5s}')

# Replace footer in index.html
old_footer_match = re.search(r'<footer>[\s\S]*?</footer>', html)
if old_footer_match:
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
    html = html[:old_footer_match.start()] + new_footer + html[old_footer_match.end():]
    print("Replaced footer in index.html")

# Replace 3D brain script in index.html
brain_marker = "/* 3D: Pink Glowing Human Brain Animation covering hero background */"
brain_idx = html.find(brain_marker)
if brain_idx != -1:
    end_script = html.find('</script>', brain_idx)
    with open('.planning/test_brain_code.py', 'r', encoding='utf-8') as bf:
        bcode_text = bf.read()
    # extract brain_js
    m = re.search(r"brain_js = '''([\s\S]*?)'''", bcode_text)
    if m:
        new_brain_code = m.group(1).strip()
        html = html[:brain_idx] + new_brain_code + '\n' + html[end_script:]
        print("Replaced 3D brain script in index.html")
else:
    print("Could not find brain marker!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated!")

