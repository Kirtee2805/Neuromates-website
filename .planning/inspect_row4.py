with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find('id="row-rehab"')
print(t[pos:pos+900])

