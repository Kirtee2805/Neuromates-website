with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

pos_start = t.find('<main id="main-content">')
pos_end = t.find('</main>')
print(t[pos_start:pos_start+3000])

