with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos_start = t.find('<div class="pv" id="v-alzheimers-care">')
pos_end = t.find('<div class="pv" id="v-epilepsy-care">')
alz_html = t[pos_start:pos_end]

lines = alz_html.split('\n')
for i, l in enumerate(lines):
    print(f"{i}: {l[:120]}")

