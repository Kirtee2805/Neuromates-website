with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

pos_js = t.find('<script>')
print(t[pos_js:pos_js+3000])

