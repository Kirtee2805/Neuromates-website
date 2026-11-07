with open(r"D:\Neuromates(website)\assets\css\tokens.css", "r", encoding="utf-8") as f:
    t = f.read()

print("Tokens CSS length:", len(t))
pos = t.find("@media")
while pos != -1:
    print(t[pos:pos+180])
    pos = t.find("@media", pos + 1)

