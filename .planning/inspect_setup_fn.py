with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("function setup")
print(t[pos-50:pos+2500])

