import os, re

with open('.planning/test_new_brain.py', 'r', encoding='utf-8') as tf:
    tcode = tf.read()
m_code = re.search(r"test_code = '''([\s\S]*?)'''", tcode)
new_brain_code = m_code.group(1).strip()

home_files = ['index.html', 'neuromates-home.html', 'Neuro Mates _ Connected neurological care.html']

for hfile in home_files:
    if not os.path.exists(hfile):
        continue
    with open(hfile, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update #gl CSS
    html = html.replace('#gl{position:fixed;inset:0;width:100%;height:100%;z-index:1;pointer-events:none;',
                        '#gl{position:fixed;inset:0;width:100%;height:100%;z-index:1;pointer-events:auto;cursor:grab;')
    html = html.replace("s.dataset.x=='0'?.35:1", "1")
    html = html.replace("s.dataset.x=='0'?.25:.5", "1")

    # 2. Replace 3D brain script
    start_marker = "/* 3D: Anatomical Interactive 3D Human Brain with Neural Synapses & Visitor Interaction */"
    idx = html.find(start_marker)
    if idx == -1:
        idx = html.find("const T = THREE, canvas = $('#gl');")
        if idx != -1:
            idx = html.rfind('/*', 0, idx)
    
    if idx != -1:
        end_idx = html.find('</script>', idx)
        html = html[:idx] + new_brain_code + '\n\n' + html[end_idx:]
        print(f"Replaced 3D brain script in {hfile}")
    else:
        print(f"Could not find 3D brain script in {hfile}")

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {hfile}")

print("All home files updated!")

