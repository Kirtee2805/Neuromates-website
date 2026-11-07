with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("relationship-canvas")
pos2 = t.find("const cvs = document.getElementById('relationship-canvas');")
print(t[pos2:pos2+3500])

