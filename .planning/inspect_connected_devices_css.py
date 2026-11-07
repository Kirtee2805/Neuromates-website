with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

pos_style = t.find('<style>')
pos_style_end = t.find('</style>')
print(t[pos_style:pos_style+2500])

