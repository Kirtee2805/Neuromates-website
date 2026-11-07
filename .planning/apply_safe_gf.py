import re

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

pattern = re.compile(
    r"const gf=\$\('#gf'\),zr=\$\('#zr'\),pd=\$\('#pd'\),ro=\$\('#ro'\);.*?addEventListener\('resize',lay\);lay\(\)\}",
    re.DOTALL
)

clean_gf = """const gf=$('#gf'),zr=$('#zr'),pd=$('#pd'),ro=$('#ro');
if(gf && zr && pd && ro){
  let R=0,px=0,py=0,dr=0,roamT=0,lastUserTime=0;
  const lay=()=>{
    const w=gf.clientWidth,h=gf.clientHeight;
    if(!w || !h) return;
    R=Math.min(w,h)*.34;
    zr.style.width=zr.style.height=R*2+'px';
    if(!px&&!py){px=w/2+R*.45;py=h/2+R*.2}
    upd();
  };

  function upd(){
    const w=gf.clientWidth,h=gf.clientHeight;
    if(!w || !h || !R) return;
    px=clamp(px,16,w-16);
    py=clamp(py,16,h-16);
    pd.style.left=px+'px';
    pd.style.top=py+'px';
    const d=Math.hypot(px-w/2,py-h/2);
    const km=Math.abs(R-d)/R;
    const out=d>R;
    gf.classList.toggle('out',out);
    ro.classList.toggle('out',out);
    ro.textContent=out?
      'Outside safe zone · '+km.toFixed(1)+' km beyond boundary. WhatsApp alert and call sent to administrator.':
      'Within safe zone · '+km.toFixed(1)+' km from boundary. Patient safely within monitored perimeter.';
  }

  function autoRoamStep(){
    const isVis = document.body.dataset.v === 'alzheimers-care' || location.hash === '#alzheimers-care';
    const now=Date.now();
    if(isVis && !dr && (now - lastUserTime > 2500)){
      roamT += 0.016;
      const w=gf.clientWidth,h=gf.clientHeight;
      if(w && h && R){
        const cx = w/2;
        const cy = h/2;
        const rDist = R * (0.68 + 0.62 * Math.sin(roamT * 0.45));
        const angle = roamT * 0.32 + 0.4 * Math.sin(roamT * 0.7);
        px = cx + Math.cos(angle) * rDist;
        py = cy + Math.sin(angle) * rDist;
        upd();
      }
    }
    requestAnimationFrame(autoRoamStep);
  }
  requestAnimationFrame(autoRoamStep);

  pd.onpointerdown=e=>{dr=1;lastUserTime=Date.now();pd.setPointerCapture(e.pointerId)};
  pd.onpointerup=()=>{dr=0;lastUserTime=Date.now()};
  pd.onpointermove=e=>{if(!dr)return;lastUserTime=Date.now();const r=gf.getBoundingClientRect();px=e.clientX-r.left;py=e.clientY-r.top;upd()};
  pd.onkeydown=e=>{const k={ArrowLeft:[-14,0],ArrowRight:[14,0],ArrowUp:[0,-14],ArrowDown:[0,14]}[e.key];if(k){e.preventDefault();lastUserTime=Date.now();px+=k[0];py+=k[1];upd()}};
  addEventListener('resize',lay);
  setTimeout(lay, 60);
  lay();
}
}"""

for target in targets:
    with open(target, "r", encoding="utf-8") as f:
        content = f.read()

    m = pattern.search(content)
    if m:
        content = content[:m.start()] + clean_gf + content[m.end():]
        print(f"Updated Geofence JS with safe null checks in {target}")
    else:
        print(f"Pattern not found in {target}")

    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

print("Finished updating geofence code.")

