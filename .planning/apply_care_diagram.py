with open(r"D:\Neuromates(website)\technology\connected-care-platform.html", "r", encoding="utf-8") as f:
    t = f.read()

# 1. Replace the hub-canvas-wrapper HTML
old_hub_wrapper = """          <!-- 3D Hub and Spoke Canvas -->
          <div class="hub-canvas-wrapper" id="hub-container">
            <canvas id="hub-canvas" aria-label="3D hub and spoke connected ecosystem"></canvas>
            
            <!-- Projected Satellite Labels -->
            <div class="satellite-label" id="lbl-patient">Patient</div>
            <div class="satellite-label" id="lbl-caretaker">Caretaker</div>
            <div class="satellite-label" id="lbl-doctor">Doctor</div>
            <div class="satellite-label" id="lbl-admin">Admin</div>

            <div style="position:absolute;bottom:14px;left:18px;z-index:20;">
              <span class="demo-tag">Illustration, not real patient data</span>
            </div>
          </div>"""

new_hub_wrapper = """          <!-- Clean Medical Architecture Diagram Container -->
          <div class="hub-canvas-wrapper" id="hub-container" style="background:#FFFFFF;border:1px solid rgba(14,59,67,0.08);box-shadow:0 20px 50px rgba(14,59,67,0.08);padding:14px;display:flex;align-items:center;justify-content:center;position:relative;">
            <img id="connected-platform-diagram" src="../assets/images/connected-care-diagram.svg" alt="Neuro Mates Connected Care Platform: Central Cloud Platform connecting Patient, Caretaker, Doctor, and Admin" style="width:100%;height:100%;max-height:460px;object-fit:contain;display:block;">
            <div style="position:absolute;bottom:14px;left:18px;z-index:20;">
              <span class="demo-tag">Illustration, not real patient data</span>
            </div>
          </div>"""

if old_hub_wrapper in t:
    t = t.replace(old_hub_wrapper, new_hub_wrapper)
    print("Replaced hub-canvas-wrapper with clean SVG diagram container.")
else:
    print("Warning: old_hub_wrapper not matched exactly!")

# 2. Update JavaScript: Remove Three.js setup and keep smooth accordion logic
pos_js_start = t.find("// 1. Accordion interaction")
pos_js_end = t.find("</script>\n</body>", pos_js_start)
if pos_js_end == -1:
    pos_js_end = t.find("</script>\r\n</body>", pos_js_start)

new_js = """// 1. Accordion interaction
      const items = document.querySelectorAll('.portal-item');

      items.forEach((item, idx) => {
        const btn = item.querySelector('.portal-header');
        btn.addEventListener('click', () => {
          items.forEach(other => {
            if (other === item) {
              const isOpen = other.classList.toggle('open');
              btn.setAttribute('aria-expanded', String(isOpen));
            } else {
              other.classList.remove('open');
              other.querySelector('.portal-header').setAttribute('aria-expanded', 'false');
            }
          });
        });
      });
    });"""

if pos_js_start != -1 and pos_js_end != -1:
    t = t[:pos_js_start] + new_js + t[pos_js_end:]
    print("Replaced heavy Three.js script with clean accordion JS.")
else:
    print(f"Indices for JS: {pos_js_start}, {pos_js_end}")

# 3. Remove unnecessary Three.js CDN script tags from head/body of connected-care-platform.html if present
t = t.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>', '<!-- Clean diagram presentation -->')
t = t.replace('<script src="../assets/js/three-core.js"></script>', '')

with open(r"D:\Neuromates(website)\technology\connected-care-platform.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Saved technology/connected-care-platform.html successfully.")

