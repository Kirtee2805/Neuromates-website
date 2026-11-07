import os

targets = [
    r"D:\Neuromates(website)\index.html",
    r"D:\Neuromates(website)\neuromates-home.html",
    r"D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html"
]

target_str = "const hpW=new T.Group(),hpB=makeCore();"
replacement_str = """function makeCore(){const g=new T.Group();function gl(c,o){return new T.MeshPhysicalMaterial(Object.assign({color:c,roughness:.25,metalness:.05,clearcoat:1,clearcoatRoughness:.1},o||{}))}g.add(new T.Mesh(new T.SphereGeometry(.62,32,24),gl('#0B8F8F',{emissive:'#0B7A7C',emissiveIntensity:.4})));const w=new T.Mesh(new T.IcosahedronGeometry(.82,1),new T.MeshBasicMaterial({color:0xffffff,wireframe:true,transparent:true,opacity:.4}));g.add(w);g.userData.w=w;const wm=gl('#fff',{roughness:.2});[[.34,.1],[.1,.34]].forEach(s=>{const m=new T.Mesh(new T.BoxGeometry(s[0],s[1],.1),wm);m.position.z=.6;g.add(m)});return g}
const hpW=new T.Group(),hpB=makeCore();"""

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    
    if "function makeCore" not in c and target_str in c:
        c = c.replace(target_str, replacement_str)
        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Added makeCore() in {p}")
    else:
        print(f"makeCore() already present or target not found in {p}")

print("Done fixing makeCore for stage canvas g2.")

