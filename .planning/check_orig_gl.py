import subprocess
out = subprocess.run(['git', 'show', '2c3b46e:index.html'], capture_output=True, text=True, encoding='utf-8')
text = out.stdout
idx = text.find("const Rn = new T.WebGLRenderer({ canvas: c")
print(text[idx-100:idx+1500])
