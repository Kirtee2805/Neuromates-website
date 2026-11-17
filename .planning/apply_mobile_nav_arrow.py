import re
import os

chevron_btn = '<button class="dd-toggle" type="button" aria-label="Toggle submenu" aria-expanded="false"><svg viewBox="0 0 14 14" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5l4 4 4-4"/></svg></button>'

# 1. Update assets/js/shared.js
with open('assets/js/shared.js', 'r', encoding='utf-8') as f:
    shared_js = f.read()

# Update getNavHTML with dd-toggle
def add_toggle_to_getNav(match):
    tag_a = match.group(1)
    return tag_a + '\n            ' + chevron_btn

shared_js = re.sub(
    r'(<a href="[^"]*">[^<]+</a>)(?=\s*<div>)',
    add_toggle_to_getNav,
    shared_js
)

# In initNav() in shared.js, add dropdown accordion support
initnav_addon = """    // Dropdown toggle buttons and accordion support for mobile
    $$('.dd', nav).forEach(dd => {
      const trigger = dd.querySelector(':scope > a');
      const menu = dd.querySelector(':scope > div');
      if (!trigger || !menu) return;

      let toggle = dd.querySelector('.dd-toggle');
      if (!toggle) {
        toggle = document.createElement('button');
        toggle.className = 'dd-toggle';
        toggle.type = 'button';
        const label = trigger.textContent.trim();
        toggle.setAttribute('aria-label', `Toggle ${label} menu`);
        toggle.setAttribute('aria-expanded', 'false');
        toggle.innerHTML = '<svg viewBox="0 0 14 14" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5l4 4 4-4"/></svg>';
        trigger.after(toggle);
      }

      toggle.onclick = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = dd.classList.toggle('open');
        toggle.setAttribute('aria-expanded', String(isOpen));
      };

      trigger.addEventListener('click', (e) => {
        if (window.innerWidth <= 960) {
          const href = trigger.getAttribute('href');
          if (!href || href === '#' || href === '#overview' || href.startsWith('javascript:')) {
            e.preventDefault();
            const isOpen = dd.classList.toggle('open');
            toggle.setAttribute('aria-expanded', String(isOpen));
          }
        }
      });

      menu.querySelectorAll('a').forEach(subLink => {
        subLink.addEventListener('click', () => {
          nav.classList.remove('o');
          const mb = $('#mb');
          if (mb) {
            mb.setAttribute('aria-expanded', 'false');
            mb.textContent = 'Menu';
          }
        });
      });
"""

if 'Dropdown toggle buttons and accordion support for mobile' not in shared_js:
    shared_js = shared_js.replace(
        "$$('.dd', nav).forEach(dd => {",
        initnav_addon + "\n    $$('.dd', nav).forEach(dd => {"
    )

with open('assets/js/shared.js', 'w', encoding='utf-8') as f:
    f.write(shared_js)
print("Updated assets/js/shared.js")


# 2. Update assets/css/tokens.css
with open('assets/css/tokens.css', 'r', encoding='utf-8') as f:
    tokens_css = f.read()

tokens_dropdown_css = """/* Dropdown Cards & Toggle */
nav .dd {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.dd-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  padding: 0 0 0 4px;
  margin: 0;
  color: var(--ink);
  cursor: pointer;
  transition: transform 0.25s var(--sp), color 0.2s ease;
}

.dd:hover .dd-toggle,
.dd:focus-within .dd-toggle {
  transform: rotate(180deg);
  color: var(--te);
}

.dd > div {
  display: none;
  position: absolute;
  top: 56px;
  left: -20px;
  min-width: 270px;
  padding: 12px;
  border-radius: 20px;
  background: #FFFFFF;
  box-shadow: 0 20px 60px rgba(14, 59, 67, 0.18);
  border: 1px solid rgba(14, 59, 67, 0.06);
  z-index: 600;
}"""

if '/* Dropdown Cards & Toggle */' not in tokens_css:
    tokens_css = tokens_css.replace(
        "/* Dropdown Cards */\n.dd > div {",
        tokens_dropdown_css + "\n/* old drop replaced */\n.dd_old_replaced > div {"
    )

# Mobile replacement in tokens.css
tokens_mobile_old = """  nav li {
    width: 100%;
  }
  nav li > a:not(.btn) {
    min-height: 44px;
    display: flex;
    align-items: center;
    padding: 10px 0;
    font-size: 0.95rem;
  }
  .dd > div {
    display: block !important;
    position: static;
    box-shadow: none;
    border: none;
    padding: 0 0 10px 16px;
    background: transparent;
  }
  .dd > div a {
    min-height: 44px;
    display: flex;
    align-items: center;
    padding: 8px 10px;
    font-size: 0.88rem;
    color: var(--mu);
  }"""

tokens_mobile_new = """  nav li {
    width: 100%;
    border-bottom: 1px solid rgba(14, 59, 67, 0.06);
  }
  nav li:last-child {
    border-bottom: none;
  }
  nav li.dd {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
  }
  nav li > a:not(.btn) {
    min-height: 48px;
    display: flex;
    align-items: center;
    padding: 12px 0;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--ink);
    flex: 1;
  }
  .dd-toggle {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    background: rgba(11, 122, 124, 0.08) !important;
    border: 1px solid rgba(11, 122, 124, 0.16) !important;
    border-radius: 50% !important;
    color: var(--te) !important;
    cursor: pointer !important;
    transition: transform 0.3s ease, background 0.2s ease, color 0.2s ease !important;
    margin-left: 8px !important;
    -webkit-tap-highlight-color: transparent !important;
  }
  .dd.open .dd-toggle {
    transform: rotate(180deg) !important;
    background: var(--te) !important;
    color: #FFFFFF !important;
    border-color: var(--te) !important;
  }
  .dd > div {
    display: none !important;
    width: 100% !important;
    position: static !important;
    box-shadow: none !important;
    border: 1px solid rgba(11, 122, 124, 0.12) !important;
    background: #F3F9F8 !important;
    border-radius: 16px !important;
    padding: 6px 6px 8px !important;
    margin: 2px 0 12px !important;
  }
  .dd.open > div {
    display: block !important;
    animation: ddSlide 0.25s ease-out forwards;
  }
  @keyframes ddSlide {
    from {
      opacity: 0;
      transform: translateY(-6px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  .dd > div a {
    min-height: 42px;
    display: flex !important;
    align-items: center;
    padding: 8px 14px !important;
    border-radius: 10px;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    transition: background 0.15s ease, color 0.15s ease !important;
  }
  .dd > div a:hover,
  .dd > div a:active {
    background: #E0F2EE !important;
    color: var(--te) !important;
  }"""

if tokens_mobile_old in tokens_css:
    tokens_css = tokens_css.replace(tokens_mobile_old, tokens_mobile_new)
    print("Replaced tokens.css mobile dropdown block")

with open('assets/css/tokens.css', 'w', encoding='utf-8') as f:
    f.write(tokens_css)
print("Updated assets/css/tokens.css")


# 3. Update root standalone pages
root_pages = [
    'index.html',
    'neuromates-home.html',
    'neuromates-products.html',
    'products.html',
    'Products _ Neuro Mates.html',
    'Neuro Mates _ Connected neurological care.html'
]

root_css_desktop = """nav .dd{position:relative;display:inline-flex;align-items:center}
.dd-toggle{display:inline-flex;align-items:center;justify-content:center;background:transparent;border:none;padding:0 0 0 4px;margin:0;color:var(--ink);cursor:pointer;transition:transform .25s var(--sp),color .2s ease}
.dd:hover .dd-toggle,.dd:focus-within .dd-toggle{transform:rotate(180deg);color:var(--te)}
"""

root_css_mobile = """nav li.dd{display:flex!important;flex-wrap:wrap!important;align-items:center!important;justify-content:space-between!important;width:100%!important;border-bottom:1px solid rgba(14,59,67,.06)}
nav li>a:not(.btn){display:flex!important;align-items:center!important;min-height:48px!important;padding:12px 0!important;font-size:.95rem!important;font-weight:700!important;color:var(--ink)!important;flex:1!important}
.dd-toggle{display:inline-flex!important;align-items:center!important;justify-content:center!important;width:40px!important;height:40px!important;background:rgba(11,122,124,.08)!important;border:1px solid rgba(11,122,124,.16)!important;border-radius:50%!important;color:var(--te)!important;cursor:pointer!important;transition:transform .3s ease,background .2s ease,color .2s ease!important;margin-left:8px!important;-webkit-tap-highlight-color:transparent!important}
.dd.open .dd-toggle{transform:rotate(180deg)!important;background:var(--te)!important;color:#fff!important;border-color:var(--te)!important}
.dd>div{display:none!important;width:100%!important;position:static!important;box-shadow:none!important;border:1px solid rgba(11,122,124,.12)!important;background:#F3F9F8!important;border-radius:16px!important;padding:6px 6px 8px!important;margin:2px 0 12px!important}
.dd.open>div{display:block!important;animation:ddSlide .25s ease-out forwards}
@keyframes ddSlide{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.dd>div a{display:flex!important;align-items:center!important;min-height:42px!important;padding:8px 14px!important;border-radius:10px!important;font-size:.88rem!important;font-weight:600!important;color:var(--ink)!important;text-transform:none!important;letter-spacing:0!important;transition:background .15s ease,color .15s ease!important}
.dd>div a:hover,.dd>div a:active{background:#E0F2EE!important;color:var(--te)!important}"""

root_js_code = """
/* Mobile Nav Dropdown Accordion */
(function(){
  function initMobileMenu(){
    const n = document.querySelector('#nav');
    if (!n) return;
    n.querySelectorAll('.dd').forEach(dd => {
      const t = dd.querySelector(':scope > a');
      const m = dd.querySelector(':scope > div');
      if (!t || !m) return;
      let b = dd.querySelector('.dd-toggle');
      if (!b) {
        b = document.createElement('button');
        b.className = 'dd-toggle';
        b.type = 'button';
        b.setAttribute('aria-label', 'Toggle submenu');
        b.setAttribute('aria-expanded', 'false');
        b.innerHTML = '<svg viewBox="0 0 14 14" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5l4 4 4-4"/></svg>';
        t.after(b);
      }
      b.onclick = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = dd.classList.toggle('open');
        b.setAttribute('aria-expanded', String(isOpen));
      };
      t.onclick = (e) => {
        if (window.innerWidth <= 900) {
          const href = t.getAttribute('href');
          if (!href || href === '#' || href === '#overview' || href.startsWith('javascript:')) {
            e.preventDefault();
            const isOpen = dd.classList.toggle('open');
            b.setAttribute('aria-expanded', String(isOpen));
          }
        }
      };
      m.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          n.classList.remove('o');
          const mb = document.querySelector('#mb');
          if (mb) {
            mb.textContent = 'Menu';
            mb.setAttribute('aria-expanded', 'false');
          }
        });
      });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileMenu);
  } else {
    initMobileMenu();
  }
})();
"""

for fn in root_pages:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add desktop .dd-toggle styles if not present
    if 'nav .dd{position:relative;display:inline-flex;' not in content:
        content = content.replace('nav li{position:relative}', 'nav li{position:relative}\n' + root_css_desktop, 1)

    # 2. Replace .dd>div{display:none!important}
    if '.dd>div{display:none!important}' in content:
        content = content.replace('.dd>div{display:none!important}', root_css_mobile, 1)
    elif '.dd>div{display:none !important}' in content:
        content = content.replace('.dd>div{display:none !important}', root_css_mobile, 1)

    # 3. Add JS logic
    if '/* Mobile Nav Dropdown Accordion */' not in content:
        content = content.replace('</script>', root_js_code + '\n</script>', 1)

    # 4. Insert toggle button in HTML if not present
    def insert_btn(m):
        link_str = m.group(1)
        return link_str + chevron_btn

    # Replace <li class="dd"><a href="...">...</a><div> with toggle
    content = re.sub(
        r'(<li class="dd">\s*<a[^>]*>[^<]+</a>)(?!\s*<button class="dd-toggle")(<div>)',
        r'\1' + chevron_btn + r'\2',
        content
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fn}")

print("All navigation updates applied!")
