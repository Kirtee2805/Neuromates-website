with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

# 1. Check kenBurnsCycle CSS
pos_kb = t.find("@keyframes kenBurnsCycle")
print("Keyframes context:\n", t[pos_kb-300:pos_kb+400])

