with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("const VS")
if pos == -1:
    pos = t.find("VS=")
print("Found VS at:", pos)
print(t[pos:pos+300])

