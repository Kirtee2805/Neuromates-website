import os, re

with open('.planning/orig_brain_js.txt', 'r', encoding='utf-8') as f:
    orig_brain_js = f.read()

home_files = ['index.html', 'neuromates-home.html', 'Neuro Mates _ Connected neurological care.html']

for hfile in home_files:
    if not os.path.exists(hfile):
        continue
    with open(hfile, 'r', encoding='utf-8') as f:
        html = f.read()

    # Restore #gl CSS
    html = re.sub(
        r'#gl\{position:fixed;inset:0;width:100%;height:100%;z-index:1;pointer-events:[^;]+;[^}]*\}',
        '#gl{position:fixed;inset:0;width:100%;height:100%;z-index:1;pointer-events:none;opacity:0;transition:opacity 1.2s}',
        html
    )
    # Restore scroll opacity formula
    html = html.replace("$('#gl').style.setProperty('--o',1)",
                        "$('#gl').style.setProperty('--o',innerWidth>900?(s.dataset.x=='0'?.35:1):(s.dataset.x=='0'?.25:.5))")

    # Replace 3D brain script with original calm pink brain
    # find start
    m = re.search(r'/\* 3D: [^\*]+ \*/\s*\(\(\)\s*=>\s*\{', html)
    if m:
        start_idx = m.start()
        end_idx = html.find('</script>', start_idx)
        html = html[:start_idx] + orig_brain_js + '\n\n' + html[end_idx:]
        print(f"Reverted 3D brain script in {hfile}")
    else:
        print(f"Could not find 3D brain script pattern in {hfile}")

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved {hfile}")

print("Revert complete!")
