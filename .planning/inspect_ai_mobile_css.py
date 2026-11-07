with open(r"D:\Neuromates(website)\technology\ai-machine-learning.html", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("@media(max-width: 900px)")
if pos == -1:
    pos = t.find("@media")
print(t[pos:pos+600])

