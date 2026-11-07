with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

print("Length of connected-devices.html:", len(t))
pos = t.find("<canvas")
while pos != -1:
    print(t[pos-50:pos+200])
    pos = t.find("<canvas", pos + 1)

