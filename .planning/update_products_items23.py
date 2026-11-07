import re

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

# Replacement for Personalised memories
old_ppl_markup = '<div class="ppl" aria-hidden="true"><i></i><i></i><i></i></div>'
new_ppl_markup = """<div class="memory-quiz-preview" style="margin-top:16px;padding:14px;border-radius:16px;background:linear-gradient(135deg,#F3EFFF 0%,#FFF6F9 100%);border:1px solid rgba(124,108,255,0.18);">
    <div style="display:flex;align-items:center;gap:12px;">
      <div style="position:relative;width:52px;height:52px;border-radius:50%;overflow:hidden;border:2.5px solid #7C6CFF;box-shadow:0 4px 12px rgba(124,108,255,0.25);flex-shrink:0;">
        <img src="assets/images/page_5_Image-7572533686.jpg" alt="Family member photograph" style="width:100%;height:100%;object-fit:cover;">
      </div>
      <div>
        <span style="font-size:0.75rem;font-weight:700;color:#7C6CFF;text-transform:uppercase;letter-spacing:0.04em;">Personalized Memory Quiz</span>
        <div style="font-size:0.92rem;font-weight:600;color:#0E3B43;line-height:1.3;margin-top:2px;">"Who visited you this morning?"</div>
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap;">
      <span style="padding:4px 12px;background:#E8F8F3;color:#0B7A7C;border:1px solid #7FD6D0;border-radius:99px;font-size:0.8rem;font-weight:600;">✓ Daughter (Maya)</span>
      <span style="padding:4px 12px;background:#FFFFFF;color:#6E8588;border:1px solid rgba(14,59,67,0.12);border-radius:99px;font-size:0.8rem;">Sister (Sunita)</span>
    </div>
  </div>"""

# Replacement for Geofence roaming JS
old_gf_pattern = re.compile(
    r"const gf=\$\('#gf'\),zr=\$\('#zr'\),pd=\$\('#pd'\),ro=\$\('#ro'\);.*?"
    r"addEventListener\('resize',lay\);lay\(\)\}",
    re.DOTALL
)

new_gf_code = """const gf=$('#gf'),zr=$('#zr'),pd=$('#pd'),ro=$('#ro');
let R=0,px=0,py=0,dr=0,autoActive=1,roamT=0,lastUserTime=0;
const lay=()=>{
  const w=gf.clientWidth,h=gf.clientHeight;
  R=Math.min(w,h)*.34;
  zr.style.width=zr.style.height=R*2+'px';
  if(!px&&!py){px=w/2+R*.45;py=h/2+R*.2}
  upd();
};

function upd(){
  const w=gf.clientWidth,h=gf.clientHeight;
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

// Automatic Live Patrol / Roaming loop
function autoRoamStep(){
  const now=Date.now();
  if(!dr && (now - lastUserTime > 2500)){
    roamT += 0.016;
    const w=gf.clientWidth,h=gf.clientHeight;
    if(w && h && R){
      const cx = w/2;
      const cy = h/2;
      // Roams inside safe zone (R * 0.4 to 0.8), then crosses boundary to R * 1.3, then returns
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
addEventListener('resize',lay);lay()}"""

for target in targets:
    with open(target, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace ppl
    if old_ppl_markup in content:
        content = content.replace(old_ppl_markup, new_ppl_markup)
        print(f"Replaced Personalised memories in {target}")
    else:
        print(f"Note: old_ppl_markup not found in {target}")

    # 2. Replace Geofence JS
    if old_gf_pattern.search(content):
        content = old_gf_pattern.sub(new_gf_code, content)
        print(f"Updated Geofence JS with automatic live roam in {target}")
    else:
        print(f"Warning: old_gf_pattern not matched in {target}")

    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

print("Finished updating product pages.")

