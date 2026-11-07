with open(r"D:\Neuromates(website)\index.html", "r", encoding="utf-8") as f:
    c = f.read()

pos = c.find("(()=>{if(!window.THREE)return;try{const T=THREE,c=$('#gl')")
print(c[pos:pos+3000])
