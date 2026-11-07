import os

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    
    old_target = "hero(v);setup(v)}"
    new_target = "hero(v);setup(v);if(typeof onScroll==='function')onScroll();}"
    if old_target in c:
        c = c.replace(old_target, new_target)
        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print("Updated route in", p)
    else:
        print("Target not found in", p)

