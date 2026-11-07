import os

targets = [
    r"D:\Neuromates(website)\index.html",
    r"D:\Neuromates(website)\neuromates-home.html",
    r"D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html"
]

for p in targets:
    if not os.path.exists(p):
        continue
    print(f"Optimizing {p}...")
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Disable smooth scroll on html tag so page switches and scrolls are immediate
    c = c.replace("html{scroll-behavior:smooth}", "html{scroll-behavior:auto}")
    c = c.replace("html { scroll-behavior: smooth; }", "html { scroll-behavior: auto; }")

    # 2. Throttle onS() with requestAnimationFrame
    old_listener = "addEventListener('scroll',onS,{passive:true});onS();"
    new_listener = """let homeScrTicking=false;
function requestHomeScroll(){
  if(!homeScrTicking){
    requestAnimationFrame(()=>{
      onS();
      homeScrTicking=false;
    });
    homeScrTicking=true;
  }
}
addEventListener('scroll',requestHomeScroll,{passive:true});onS();"""
    
    if old_listener in c:
        c = c.replace(old_listener, new_listener)
        print("  Throttled onS() with requestAnimationFrame.")
    else:
        print("  WARNING: old_listener not found!")

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"  Saved {p}.")

print("Done optimizing home pages.")

