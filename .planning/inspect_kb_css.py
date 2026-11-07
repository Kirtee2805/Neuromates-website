with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("ken-burns-collage")
print(t[pos-50:pos+800])

