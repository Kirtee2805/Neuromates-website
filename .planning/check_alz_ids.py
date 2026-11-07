with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

print("id='qo':", 'id="qo"' in t or "id='qo'" in t)
print("id='qm':", 'id="qm"' in t or "id='qm'" in t)
print("id='gf':", 'id="gf"' in t or "id='gf'" in t)
print("id='zr':", 'id="zr"' in t or "id='zr'" in t)
print("id='pd':", 'id="pd"' in t or "id='pd'" in t)
print("id='ro':", 'id="ro"' in t or "id='ro'" in t)

