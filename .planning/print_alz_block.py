with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("v=='alzheimers-care'")
print(t[pos:pos+1600])

