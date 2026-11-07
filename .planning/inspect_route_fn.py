with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("function route")
if pos == -1:
    pos = t.find("route(")
print(t[pos-50:pos+800])

