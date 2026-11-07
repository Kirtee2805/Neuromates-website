with open(r"D:\Neuromates(website)\assets\js\shared.js", "r", encoding="utf-8") as f:
    t = f.read()

pos = t.find("alzheimers-care")
while pos != -1:
    print(t[pos-80:pos+150])
    pos = t.find("alzheimers-care", pos + 1)

