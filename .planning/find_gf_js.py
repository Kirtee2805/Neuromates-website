with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find('id="gf"')
print("id=gf found at:", pos)
pos_js = t.find('gf = document.getElementById("gf")')
if pos_js == -1:
    pos_js = t.find("document.getElementById('gf')")
if pos_js == -1:
    pos_js = t.find("'gf'")
print("JS found at:", pos_js)
if pos_js != -1:
    print(t[pos_js-100:pos_js+1200])

