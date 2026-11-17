import os, re

# 1. Update register-demo.html
with open('register-demo.html', 'r', encoding='utf-8') as f:
    demo_html = f.read()

# Fix .demo-stage padding-top
demo_html = re.sub(
    r'\.demo-stage\s*\{[\s\S]*?padding-top:[^;]+;',
    '''.demo-stage {
      min-height: 100vh;
      background: radial-gradient(circle at 18% 30%, rgba(11,93,99,0.85) 0%, transparent 60%),
                  radial-gradient(circle at 82% 70%, rgba(14,122,116,0.7) 0%, transparent 60%),
                  linear-gradient(145deg, #0B3A44 0%, #0B5260 50%, #082930 100%);
      color: #FFFFFF;
      padding-top: clamp(128px, 16vw, 165px);''',
    demo_html
)

# Fix breadcrumb margin and clearance
demo_html = re.sub(
    r'<nav class="breadcrumb" aria-label="Breadcrumb"[^>]*>',
    '<nav class="breadcrumb" aria-label="Breadcrumb" style="color:rgba(255,255,255,0.7);margin-top:10px;margin-bottom:28px;">',
    demo_html
)

# Update caption pill text
demo_html = demo_html.replace(
    'Ecosystem Telemetry Demonstration',
    'Live 3D Neurological Telemetry · 4 Condition Streams'
)

# Replace 3D animation script in register-demo.html
with open('.planning/test_demo_brain.py', 'r', encoding='utf-8') as tf:
    tcode = tf.read()
m_code = re.search(r"demo_brain_js = '''([\s\S]*?)'''", tcode)
new_anim_code = m_code.group(1).strip()

# find old 3D canvas script in register-demo.html
old_anim_pattern = re.compile(
    r'// 3D Canvas \(Three\.js\)[\s\S]*?let isRunning = true;[\s\S]*?requestAnimationFrame\(animate\);[\s\S]*?\}[\s\S]*?animate\(\);[\s\S]*?\}'
)

if old_anim_pattern.search(demo_html):
    demo_html = old_anim_pattern.sub(new_anim_code, demo_html)
    print("Replaced 3D animation script via regex")
else:
    # Look for canvas init
    cvs_start = demo_html.find("const cvs = document.getElementById('demo-core-canvas');")
    if cvs_start != -1:
        # find matching end before // Form submission handler
        form_sub = demo_html.find("// Form submission handler", cvs_start)
        if form_sub != -1:
            demo_html = demo_html[:cvs_start] + new_anim_code + '\n\n      ' + demo_html[form_sub:]
            print("Replaced 3D animation script via substring slice")

with open('register-demo.html', 'w', encoding='utf-8') as f:
    f.write(demo_html)
print("register-demo.html updated successfully!")

# 2. Update assets/css/tokens.css for perfect navbar logo vertical centering
with open('assets/css/tokens.css', 'r', encoding='utf-8') as f:
    tokens = f.read()

# Replace nav .lg styling in tokens.css
tokens = re.sub(
    r'nav \.lg\s*\{[\s\S]*?\}',
    '''nav .lg {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 0;
  margin: 0;
}''',
    tokens
)

tokens = re.sub(
    r'nav \.lg img[^{]*\{[\s\S]*?\}',
    '''nav .lg img,
nav .lo img,
.lo img,
.lg img {
  height: 38px;
  width: auto;
  display: block;
  background: transparent;
  object-fit: contain;
}''',
    tokens
)

with open('assets/css/tokens.css', 'w', encoding='utf-8') as f:
    f.write(tokens)
print("tokens.css updated with centered navbar logo styles!")

# 3. Update standalone HTML files to use assets/images/logo.png instead of base64 in navbar
standalone_files = [
    'index.html',
    'neuromates-home.html',
    'neuromates-products.html',
    'products.html',
    'Neuro Mates _ Connected neurological care.html',
    'Products _ Neuro Mates.html'
]

for fname in standalone_files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace base64 logo inside <a class="lg" ...>
    content = re.sub(
        r'<a class="lg" href="index\.html"[^>]*><img src="data:image/[^"]+" alt="Neuro Mates"></a>',
        '<a class="lg" href="index.html" aria-label="Neuro Mates Home"><img src="assets/images/logo.png" alt="Neuro Mates"></a>',
        content
    )
    
    # ensure nav .lg has vertical centering in embedded styles
    if 'nav .lg {' in content:
        content = re.sub(
            r'nav \.lg\s*\{[^}]*\}',
            'nav .lg{display:inline-flex;align-items:center;justify-content:center;height:100%;padding:0;margin:0}',
            content
        )
    else:
        # inject into <style>
        content = content.replace(
            'nav{',
            'nav .lg{display:inline-flex;align-items:center;justify-content:center;height:100%;padding:0;margin:0}nav{'
        )
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated navbar logo in standalone page: {fname}")

print("All tasks completed successfully!")
