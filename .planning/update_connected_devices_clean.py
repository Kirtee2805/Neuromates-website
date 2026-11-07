with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

# 1. Update CSS for .device-media-card
old_css_part = """    .device-canvas-box {
      width: 100%;
      height: 380px;
      border-radius: 28px;
      background: radial-gradient(circle at center, rgba(255,255,255,0.85) 0%, rgba(246,244,238,0.4) 75%);
      box-shadow: 0 16px 40px rgba(14,59,67,0.06);
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .device-glow {
      position: absolute;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      filter: blur(50px);
      opacity: 0.35;
      pointer-events: none;
      z-index: 1;
    }
    .device-canvas {
      width: 100%;
      height: 100%;
      position: relative;
      z-index: 2;
    }
    .device-photo-thumb {
      margin-top: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      background: #FFFFFF;
      padding: 8px 14px;
      border-radius: 16px;
      box-shadow: 0 4px 16px rgba(14,59,67,0.06);
    }
    .device-photo-thumb img {
      width: 48px;
      height: 48px;
      object-fit: cover;
      border-radius: 10px;
    }
    .device-photo-thumb span {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--ink);
    }"""

new_css_part = """    .device-media-card {
      width: 100%;
      border-radius: 28px;
      background: #FFFFFF;
      border: 1px solid rgba(14,59,67,0.08);
      box-shadow: 0 18px 48px rgba(14,59,67,0.08);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.4s var(--e), box-shadow 0.4s var(--e), border-color 0.4s var(--e);
    }
    .device-media-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 24px 60px rgba(14,59,67,0.12);
      border-color: rgba(11,122,124,0.3);
    }
    .device-media-card img {
      width: 100%;
      height: 310px;
      object-fit: cover;
      display: block;
      background: #F4F6F6;
    }
    .device-card-caption {
      padding: 16px 22px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(14,59,67,0.06);
    }
    .device-card-caption span {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--ink);
      letter-spacing: 0.01em;
    }
    .device-card-badge {
      font-size: 0.74rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 4px 12px;
      border-radius: 99px;
      background: rgba(11,122,124,0.1);
      color: #0B7A7C;
    }"""

if old_css_part in t:
    t = t.replace(old_css_part, new_css_part)
    print("Updated CSS in connected-devices.html")
else:
    print("Warning: old_css_part not found in connected-devices.html")

# 2. Replace the 4 device rows' visual columns
# Row 1: Alzheimer's
old_row1_vis = """          <div class="device-visual-col">
            <div class="device-canvas-box">
              <div class="device-glow" style="background:#7C6CFF;"></div>
              <canvas class="device-canvas" id="canvas-alzheimers" aria-label="3D location tracker device"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;z-index:3;">
                <span class="demo-tag">Illustration, not real patient data</span>
              </div>
            </div>
            <div class="device-photo-thumb">
              <img src="../assets/images/page_5_Image-7572533686.jpg" alt="Patient safety wearable">
              <span>Patient Safety Wearable &bull; Arm Band</span>
            </div>
          </div>"""

new_row1_vis = """          <div class="device-visual-col">
            <div class="device-media-card">
              <img src="../assets/images/page_10_Image-7888911063.jpg" alt="Alzheimer's Patient Safety Wearable location tracker on patient arm" loading="lazy">
              <div class="device-card-caption">
                <span>Patient Safety Wearable &bull; Arm Band</span>
                <span class="device-card-badge" style="background:rgba(124,108,255,0.12);color:#7C6CFF;">GPS &bull; Safe-Zone</span>
              </div>
            </div>
          </div>"""

if old_row1_vis in t:
    t = t.replace(old_row1_vis, new_row1_vis)
    print("Updated Row 1 (Alzheimer's) visual")
else:
    print("Warning: old_row1_vis not found")

# Row 2: Parkinson's
old_row2_vis = """          <div class="device-visual-col">
            <div class="device-canvas-box">
              <div class="device-glow" style="background:#2F7FE0;"></div>
              <canvas class="device-canvas" id="canvas-parkinsons" aria-label="3D motion sensor wearable"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;z-index:3;">
                <span class="demo-tag">Illustration, not real patient data</span>
              </div>
            </div>
            <div class="device-photo-thumb">
              <img src="../assets/images/page_4_Image-9750469207.jpg" alt="Movement monitoring wearable">
              <span>Movement Monitoring Wearable &bull; Back of Hand</span>
            </div>
          </div>"""

new_row2_vis = """          <div class="device-visual-col">
            <div class="device-media-card">
              <img src="../assets/images/page_4_Image-9750469207.jpg" alt="Parkinson's Movement Monitoring Wearable worn on back of hand" loading="lazy">
              <div class="device-card-caption">
                <span>Movement Monitoring Wearable &bull; Back of Hand</span>
                <span class="device-card-badge" style="background:rgba(47,127,224,0.12);color:#2F7FE0;">Tremor &bull; Falls</span>
              </div>
            </div>
          </div>"""

if old_row2_vis in t:
    t = t.replace(old_row2_vis, new_row2_vis)
    print("Updated Row 2 (Parkinson's) visual")
else:
    print("Warning: old_row2_vis not found")

# Row 3: Epilepsy
old_row3_vis = """          <div class="device-visual-col">
            <div class="device-canvas-box">
              <div class="device-glow" style="background:#2BB58A;"></div>
              <canvas class="device-canvas" id="canvas-epilepsy" aria-label="3D brain-signal headband"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;z-index:3;">
                <span class="demo-tag">Illustration, not real patient data</span>
              </div>
            </div>
            <div class="device-photo-thumb">
              <img src="../assets/images/page_15_Image-8784015711.jpg" alt="Epilepsy monitoring wearable">
              <span>Epilepsy Monitoring Wearable &bull; Headband</span>
            </div>
          </div>"""

new_row3_vis = """          <div class="device-visual-col">
            <div class="device-media-card">
              <img src="../assets/images/page_15_Image-8784015711.jpg" alt="Epilepsy Monitoring Wearable continuous EEG sensing headband" loading="lazy">
              <div class="device-card-caption">
                <span>Epilepsy Monitoring Wearable &bull; Headband</span>
                <span class="device-card-badge" style="background:rgba(43,181,138,0.12);color:#2BB58A;">Continuous EEG</span>
              </div>
            </div>
          </div>"""

if old_row3_vis in t:
    t = t.replace(old_row3_vis, new_row3_vis)
    print("Updated Row 3 (Epilepsy) visual")
else:
    print("Warning: old_row3_vis not found")

# Row 4: Rehabilitation
old_row4_vis = """          <div class="device-visual-col">
            <div class="device-canvas-box">
              <div class="device-glow" style="background:#F5A623;"></div>
              <canvas class="device-canvas" id="canvas-rehab" aria-label="3D muscle sensor pads"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;z-index:3;">
                <span class="demo-tag">Illustration, not real patient data</span>
              </div>
            </div>
            <div class="device-photo-thumb">
              <img src="../assets/images/page_12_Image-2708199956.jpg" alt="Rehabilitation muscle sensor">
              <span>Muscle-Signal Sensors &bull; Hand &amp; Facial</span>
            </div>
          </div>"""

new_row4_vis = """          <div class="device-visual-col">
            <div class="device-media-card">
              <img src="../assets/images/page_12_Image-2708199956.jpg" alt="Rehabilitation BioAmp muscle sensor hardware and interactive platform" loading="lazy">
              <div class="device-card-caption">
                <span>Muscle-Signal Sensors &bull; Hand &amp; Facial</span>
                <span class="device-card-badge" style="background:rgba(245,166,35,0.12);color:#D48600;">BioAmp EMG</span>
              </div>
            </div>
          </div>"""

if old_row4_vis in t:
    t = t.replace(old_row4_vis, new_row4_vis)
    print("Updated Row 4 (Rehab) visual")
else:
    print("Warning: old_row4_vis not found")

# 3. Update JavaScript: Remove Three.js rotating device loop, add auto-roaming geofence
pos_js_start = t.find("// 2. Three.js Rotating 3D Devices on Scroll")
pos_js_geofence = t.find("// 3. Geofence Interactive Drag Simulator", pos_js_start)

# Replace the Three.js block with a comment
if pos_js_start != -1 and pos_js_geofence != -1:
    t = t[:pos_js_start] + "// 2. Clean Medical Product Presentation (3D primitives replaced with high-res photography)\n      " + t[pos_js_geofence:]
    print("Removed Three.js rotating devices from connected-devices.html")

# Remove Three.js and three-core scripts if present
t = t.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>', '<!-- Clean Healthcare Tech Presentation -->')
t = t.replace('<script src="../assets/js/three-core.js"></script>', '')

with open(r"D:\Neuromates(website)\technology\connected-devices.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Saved technology/connected-devices.html successfully.")

