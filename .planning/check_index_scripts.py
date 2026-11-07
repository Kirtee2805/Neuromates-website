with open(r"D:\Neuromates(website)\index.html", "r", encoding="utf-8") as f:
    t = f.read()

print("shared.js in index.html:", "shared.js" in t)
pos = t.find("<script")
while pos != -1:
    end = t.find(">", pos)
    print(t[pos:end+1])
    pos = t.find("<script", end)

