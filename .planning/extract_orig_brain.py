import subprocess, re

out = subprocess.run(['git', 'show', '2c3b46e:index.html'], capture_output=True, text=True, encoding='utf-8')
orig_html = out.stdout

start_str = "/* 3D: Pink Glowing Human Brain Animation covering hero background */"
start_idx = orig_html.find(start_str)
end_idx = orig_html.find('</script>', start_idx)

orig_brain_js = orig_html[start_idx:end_idx].strip()
print("Original brain JS extracted, length:", len(orig_brain_js))
print("Start:", orig_brain_js[:200])
print("End:", orig_brain_js[-200:])

with open('.planning/orig_brain_js.txt', 'w', encoding='utf-8') as f:
    f.write(orig_brain_js)

