with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("v=='alzheimers-care'")
if pos == -1:
    pos = t.find("alzheimers-care")
print("Found at:", pos)
while pos != -1:
    print("--- MATCH ---")
    print(t[pos:pos+400])
    pos = t.find("alzheimers-care", pos + 400)

