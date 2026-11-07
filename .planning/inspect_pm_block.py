with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("Personalised memories")
print(t[pos-100:pos+1500])

