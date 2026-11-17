import subprocess, re
out = subprocess.run(['git', 'show', '2c3b46e:index.html'], capture_output=True, text=True, encoding='utf-8')
orig_html = out.stdout

for m in re.finditer(r'#gl[^{]*\{[^}]*\}', orig_html):
    print(m.group(0))
