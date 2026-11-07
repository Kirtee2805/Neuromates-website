with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find('id="v-alzheimers-care"')
print("Found at:", pos)
print(t[pos:pos+1000])

