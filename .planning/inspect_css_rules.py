with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re
style = re.search(r'<style>(.*?)</style>', content, re.DOTALL).group(1)

# print selectors and rules
for s in ['#nav', '.btn', 'footer', '#care', '.cta', '.lg', 'em']:
    matches = re.findall(rf'({re.escape(s)}[^{{]*\{{[^}}]*\}})', style)
    print(f"=== Matches for {s} ===")
    for m in matches[:5]:
        print(m)

