with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

old_row4 = """          <div class="device-visual-col">
            <div class="device-canvas-box">
              <div class="device-glow" style="background:#F5A623;"></div>
              <canvas class="device-canvas" id="canvas-rehab" aria-label="3D muscle sensor pads"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;z-index:3;">
                <span class="demo-tag">Illustration, not real patient data</span>
              </div>
            </div>
            <div class="device-photo-thumb">
              <img src="../assets/images/page_6_Image-8450180107.jpg" alt="Interactive physiotherapy setup">
              <span>Physiotherapy Platform &bull; Muscle-Signal Electrodes</span>
            </div>
          </div>"""

new_row4 = """          <div class="device-visual-col">
            <div class="device-media-card">
              <img src="../assets/images/page_6_Image-8450180107.jpg" alt="Paralysis rehabilitation physiotherapy setup with BioAmp muscle sensors" loading="lazy">
              <div class="device-card-caption">
                <span>Physiotherapy Platform &bull; Muscle-Signal Electrodes</span>
                <span class="device-card-badge" style="background:rgba(245,166,35,0.12);color:#D48600;">BioAmp EMG</span>
              </div>
            </div>
          </div>"""

if old_row4 in t:
    t = t.replace(old_row4, new_row4)
    print("Updated Row 4 (Rehab) visual successfully")
else:
    print("Error: old_row4 not found")

with open(r"D:\Neuromates(website)\technology\connected-devices.html", "w", encoding="utf-8") as f:
    f.write(t)

