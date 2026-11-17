import os, re

with open('.planning/test_new_brain.py', 'r', encoding='utf-8') as tf:
    tcode = tf.read()
m_code = re.search(r"test_code = '''([\s\S]*?)'''", tcode)
new_brain_code = m_code.group(1).strip()

home_files = ['neuromates-home.html', 'Neuro Mates _ Connected neurological care.html']

for hfile in home_files:
    if not os.path.exists(hfile):
        continue
    with open(hfile, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the #gl block
    idx = html.find("const Rn = new T.WebGLRenderer({ canvas: c")
    if idx != -1:
        start_func = html.rfind('(()=>{', 0, idx)
        if start_func == -1:
            start_func = html.rfind('(function()', 0, idx)
        end_func = html.find('})();', idx) + 5
        html = html[:start_func] + new_brain_code + html[end_func:]
        print(f"Updated 3D brain in {hfile}")
        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)

