with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos_js = t.find("const cvs = document.getElementById('relationship-canvas');")
print("Canvas JS context:\n", t[pos_js:pos_js+2500])

