with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("relationship-canvas")
while pos != -1:
    print("Found canvas at:", pos)
    print(t[pos-50:pos+200])
    pos = t.find("relationship-canvas", pos+1)

