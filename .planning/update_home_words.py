import os

home_files = ['index.html', 'neuromates-home.html', 'Neuro Mates _ Connected neurological care.html']

old_words_css = """.words{display:flex;flex-wrap:wrap;gap:14px 14px;margin-top:48px}
.words span{font:700 clamp(1.2rem,2.6vw,2rem)/1 var(--fd);padding:16px 30px;border-radius:99px;opacity:0;transform:scale(.3) rotate(-10deg);transition:opacity .4s,transform .8s var(--sp)}
.words span.in{opacity:1;transform:none;animation:bob 4s ease-in-out infinite}.words span:nth-child(2n).in{animation-delay:-1.3s}.words span:nth-child(3n).in{animation-delay:-2.4s}"""

new_words_css = """.words{display:flex;flex-wrap:wrap;gap:14px 14px;margin-top:48px}
.words span{font:700 clamp(1.2rem,2.6vw,2rem)/1 var(--fd);padding:16px 30px;border-radius:99px;opacity:1;transform:none;animation:bob 4s ease-in-out infinite;transition:transform .4s var(--sp),box-shadow .3s;cursor:default}
.words span:hover{transform:translateY(-4px) scale(1.03);box-shadow:0 12px 28px rgba(14,59,67,.12)}
.words span:nth-child(2n){animation-delay:-1.3s}.words span:nth-child(3n){animation-delay:-2.4s}"""

old_words_js = "$$('.words span').forEach((w,i)=>new IntersectionObserver(es=>es[0].isIntersecting&&setTimeout(()=>w.classList.add('in'),i*160),{threshold:1}).observe(w));"
new_words_js = "$$('.words span').forEach((w,i)=>{w.classList.add('in');new IntersectionObserver(es=>{if(es[0].isIntersecting){setTimeout(()=>w.classList.add('in'),i*100)}}, {threshold:0.1}).observe(w);});"

for fn in home_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_words_css in content:
        content = content.replace(old_words_css, new_words_css)
        print('Updated words CSS in', fn)
    else:
        # Try regex or relaxed replace
        content = content.replace("opacity:0;transform:scale(.3) rotate(-10deg);transition:opacity .4s,transform .8s var(--sp)}", "opacity:1;transform:none;animation:bob 4s ease-in-out infinite;transition:transform .4s var(--sp),box-shadow .3s;cursor:default}")
        print('Applied fallback words CSS in', fn)

    if old_words_js in content:
        content = content.replace(old_words_js, new_words_js)
        print('Updated words JS in', fn)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done updating home files.')

