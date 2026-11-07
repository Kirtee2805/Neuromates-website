with open(r"D:\Neuromates(website)\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.rfind("</body>")
print(t[pos-300:pos+100])

