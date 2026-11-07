with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos1 = t.find("THE REALITY")
print("=== SECTION 1 ===")
print(t[pos1-100:pos1+600])

pos2 = t.find("ECOSYSTEM ARCHITECTURE")
print("\n=== SECTION 2 ===")
print(t[pos2-100:pos2+1000])

