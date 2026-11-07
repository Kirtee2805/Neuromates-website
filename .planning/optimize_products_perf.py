import os
import re

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

for p in targets:
    if not os.path.exists(p):
        continue
    print(f"Optimizing {p}...")
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    
    # 1. Disable smooth scroll on html tag so route switching is instantaneous
    c = c.replace("html{scroll-behavior:smooth}", "html{scroll-behavior:auto}")
    
    # 2. Remove transition:filter .3s which fights scroll-driven rasterization
    c = c.replace(";transition:filter .3s}", ";will-change:transform}")
    c = c.replace("transition:filter .3s", "will-change:transform")
    
    # 3. Optimize scroll and cards handler:
    # Target old scroll handler
    old_scroll_pat = re.compile(
        r"const cards=\(\)=>.*?let mx=0,my=0;addEventListener\('pointermove',e=>\{mx=e\.clientX/innerWidth-\.5;my=e\.clientY/innerHeight-\.5\}\);",
        re.DOTALL
    )
    
    new_scroll_code = """let scrTicking=false,epStep=0;
function onScroll(){
  const y=scrollY,H=innerHeight,m=document.documentElement.scrollHeight-H;
  const careEl=$('#care');if(careEl&&m>0)careEl.style.height=(y/m*100)+'%';
  const navEl=$('#nav');if(navEl)navEl.classList.toggle('s',y>80);
  if(cur=='epilepsy-care'){
    const storyEl=$('#e-story');
    if(storyEl){
      const r=storyEl.getBoundingClientRect();
      const p=clamp(-r.top/(r.height-H),0,.999);
      epStep=Math.floor(p*5);
    }
  }
  scrTicking=false;
}
addEventListener('scroll',()=>{
  if(!scrTicking){
    requestAnimationFrame(onScroll);
    scrTicking=true;
  }
},{passive:true});
let mx=0,my=0,tiltTicking=false;
function updateTilt(){
  if(cur=='parkinsons-care'){const tl=$('.tilt');if(tl&&tl.firstElementChild)tl.firstElementChild.style.transform='rotateY('+(mx*10)+'deg) rotateX('+(-my*8)+'deg)'}
  else if(cur=='epilepsy-care'){const f=$('#v-epilepsy-care .tilt');if(f&&f.firstElementChild)f.firstElementChild.style.transform='rotateY('+(mx*8)+'deg) rotateX('+(-my*6)+'deg)'}
  else if(cur=='alzheimers-care'){const f=$('#v-alzheimers-care .tilt');if(f&&f.firstElementChild)f.firstElementChild.style.transform='rotateY('+(mx*8)+'deg) rotateX('+(-my*6)+'deg)'}
  tiltTicking=false;
}
addEventListener('pointermove',e=>{
  mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5;
  if(!tiltTicking){requestAnimationFrame(updateTilt);tiltTicking=true;}
},{passive:true});"""
    
    if old_scroll_pat.search(c):
        c = old_scroll_pat.sub(new_scroll_code, c)
        print("  Replaced scroll & pointermove handlers with RAF throttled versions.")
    else:
        print("  WARNING: old_scroll_pat not matched!")

    # 4. Optimize size(c) so it does not trigger layout reflow every frame
    old_size = "function size(c){const w=c.clientWidth;if(c._w!=w){c._w=w;c.width=w}return c.getContext('2d')}"
    new_size = "function size(c){if(!c._w||c._w!==c.clientWidth){c._w=c.clientWidth||300;c.width=c._w}return c.getContext('2d')}"
    c = c.replace(old_size, new_size)
    
    # 5. Optimize tick(t) for epilepsy-care so it does NOT call getBoundingClientRect inside the RAF loop!
    old_ep_tick = "else if(cur=='epilepsy-care'){const r=$('#e-story').getBoundingClientRect(),p=clamp(-r.top/(r.height-innerHeight),0,.999),s=Math.floor(p*5);"
    new_ep_tick = "else if(cur=='epilepsy-care'){const s=epStep;"
    c = c.replace(old_ep_tick, new_ep_tick)
    
    # Also remove duplicate tilt transforms inside tick if present
    c = c.replace(
        "const tl=$('.tilt');if(tl){const f=tl.firstElementChild;f.style.transform='rotateY('+mx*10+'deg) rotateX('+-my*8+'deg)'}",
        "/* tilt handled in pointermove */"
    )
    c = c.replace(
        "const f=$('#v-epilepsy-care .tilt');if(f)f.firstElementChild.style.transform='rotateY('+mx*8+'deg) rotateX('+-my*6+'deg)'",
        "/* tilt handled in pointermove */"
    )
    c = c.replace(
        "const f=$('#v-alzheimers-care .tilt');f.firstElementChild.style.transform='rotateY('+mx*8+'deg) rotateX('+-my*6+'deg)'",
        "/* tilt handled in pointermove */"
    )

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"  Successfully saved {p}.")

print("Done optimizing products pages.")

