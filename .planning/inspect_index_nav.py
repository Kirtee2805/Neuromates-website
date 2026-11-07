with open(r"D:\Neuromates(website)\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find('<nav')
print(t[pos:pos+400])

