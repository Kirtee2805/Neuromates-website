with open(r"D:\Neuromates(website)\technology\ai-machine-learning.html", "r", encoding="utf-8") as f:
    t = f.read()

# 1. Update CSS: Replace .ai-canvas-box styles with .ai-live-card styles
old_canvas_box_css = """    .ai-canvas-box {
      width: 100%;
      height: 290px;
      border-radius: 24px;
      background: #08282F;
      box-shadow: 0 16px 36px rgba(14,59,67,0.1);
      position: relative;
      overflow: hidden;
    }
    .ai-canvas {
      width: 100%;
      height: 100%;
      display: block;
    }"""

new_live_card_css = """    .ai-live-card {
      width: 100%;
      border-radius: 24px;
      background: #FFFFFF;
      border: 1px solid rgba(14,59,67,0.08);
      box-shadow: 0 18px 48px rgba(14,59,67,0.08);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.4s var(--e), box-shadow 0.4s var(--e);
    }
    .ai-live-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 24px 60px rgba(14,59,67,0.12);
    }
    .ai-live-media {
      position: relative;
      width: 100%;
      overflow: hidden;
      background: #F4F6F6;
    }
    .ai-live-media img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.6s var(--e);
    }
    .ai-live-card:hover .ai-live-media img {
      transform: scale(1.02);
    }

    /* Live Telemetry Animated Badges */
    .ai-live-pill {
      position: absolute;
      top: 14px;
      left: 14px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: rgba(14, 59, 67, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: 99px;
      color: #FFFFFF;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
      z-index: 5;
    }
    .ai-live-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      display: inline-block;
      animation: aiPulse 1.8s infinite ease-in-out;
    }
    @keyframes aiPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(1.35); }
    }

    /* Animated Scan Line sweeping over live telemetry graphs */
    .ai-scan-sweep {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 3;
      overflow: hidden;
    }
    .ai-scan-sweep::after {
      content: "";
      position: absolute;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent 5%, rgba(91, 231, 196, 0.85) 50%, transparent 95%);
      box-shadow: 0 0 16px rgba(91, 231, 196, 0.7);
      animation: aiScanMove 3.8s ease-in-out infinite;
    }
    @keyframes aiScanMove {
      0% { top: 0%; opacity: 0; }
      15% { opacity: 0.85; }
      85% { opacity: 0.85; }
      100% { top: 100%; opacity: 0; }
    }

    /* Live Telemetry Caption Bar */
    .ai-card-footer {
      padding: 14px 20px;
      background: #FFFFFF;
      border-top: 1px solid rgba(14,59,67,0.06);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .ai-card-footer span {
      font-size: 0.84rem;
      font-weight: 600;
      color: #0E3B43;
    }
    .ai-card-badge {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 99px;
      background: rgba(14,59,67,0.06);
      color: #0B7A7C;
    }"""

if old_canvas_box_css in t:
    t = t.replace(old_canvas_box_css, new_live_card_css)
    print("Updated CSS in ai-machine-learning.html")
else:
    print("Warning: old_canvas_box_css not matched!")

# Also update responsive media query for .ai-canvas-box
t = t.replace(".ai-canvas-box {\n        height: 240px;\n      }", "/* responsive live cards */")
t = t.replace(".ai-canvas-box {\r\n        height: 240px;\r\n      }", "/* responsive live cards */")

# 2. Update the 4 application rows HTML
old_rows_html = """        <!-- 1. Movement -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-canvas-box">
              <canvas class="ai-canvas" id="canvas-movement" aria-label="Tremor spike detection chart"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;">
                <span class="demo-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8);">Illustration, not real patient data</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--parkinsons-1);">MOVEMENT MONITORING</span>
            <h2>Movement</h2>
            <p class="body-text">Movement information can be analysed for abnormal activity such as tremors or falls.</p>
          </div>
        </div>

        <!-- 2. Brain Activity -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-canvas-box">
              <canvas class="ai-canvas" id="canvas-brain" aria-label="EEG signal wave analysis"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;">
                <span class="demo-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8);">Illustration, not real patient data</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--epilepsy-1);">BRAIN ACTIVITY MONITORING</span>
            <h2>Brain activity</h2>
            <p class="body-text">Brain-activity information can be monitored for abnormal EEG signals that may indicate a seizure.</p>
          </div>
        </div>

        <!-- 3. Daily Activity -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-canvas-box">
              <canvas class="ai-canvas" id="canvas-activity" aria-label="Daily activity timeline and memory query generation"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;">
                <span class="demo-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8);">Illustration, not real patient data</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--alzheimers-1);">MEMORY &amp; ROUTINE</span>
            <h2>Daily activity</h2>
            <p class="body-text">Daily activity information can support personalised memory-recall questions.</p>
          </div>
        </div>

        <!-- 4. Rehabilitation -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-canvas-box">
              <canvas class="ai-canvas" id="canvas-rehab" aria-label="Facial feature tracking outline for interactive physiotherapy"></canvas>
              <div style="position:absolute;bottom:12px;left:18px;">
                <span class="demo-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8);">Illustration, not real patient data</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--paralysis-1);">INTERACTIVE REHABILITATION</span>
            <h2>Rehabilitation</h2>
            <p class="body-text">Interactive rehabilitation can use patient movement and facial interaction.</p>
          </div>
        </div>"""

new_rows_html = """        <!-- 1. Movement Monitoring (1st Photo) -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-live-card">
              <div class="ai-live-media">
                <span class="ai-live-pill"><span class="ai-live-dot" style="background:#2F7FE0;box-shadow:0 0 10px #2F7FE0;"></span>Live Motion Analysis</span>
                <div class="ai-scan-sweep"></div>
                <img src="../assets/images/ai-movement-monitoring.jpg" alt="Wearable motion sensor, abnormal movement detection and automatic WhatsApp family alert" loading="lazy">
              </div>
              <div class="ai-card-footer">
                <span>Wearable motion sensor &bull; Abnormal movement detected &bull; Alert to family</span>
                <span class="ai-card-badge" style="background:rgba(47,127,224,0.1);color:#2F7FE0;">Live Telemetry</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--parkinsons-1);">MOVEMENT MONITORING</span>
            <h2>Movement</h2>
            <p class="body-text">Movement information can be analysed for abnormal activity such as tremors or falls.</p>
          </div>
        </div>

        <!-- 2. Brain Activity Monitoring (2nd Photo) -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-live-card">
              <div class="ai-live-media">
                <span class="ai-live-pill"><span class="ai-live-dot" style="background:#2BB58A;box-shadow:0 0 10px #2BB58A;"></span>Continuous EEG Telemetry</span>
                <div class="ai-scan-sweep" style="animation-delay:1.2s;"></div>
                <img src="../assets/images/ai-brain-monitoring.jpg" alt="Continuous brain-activity monitoring headband with five brain-wave bands: Delta, Theta, Alpha, Beta, Gamma" loading="lazy">
              </div>
              <div class="ai-card-footer">
                <span>Brain-activity monitoring headband &bull; 5 brain-wave bands</span>
                <span class="ai-card-badge" style="background:rgba(43,181,138,0.1);color:#2BB58A;">Continuous EEG</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--epilepsy-1);">BRAIN ACTIVITY MONITORING</span>
            <h2>Brain activity</h2>
            <p class="body-text">Brain-activity information can be monitored for abnormal EEG signals that may indicate a seizure.</p>
          </div>
        </div>

        <!-- 3. Memory & Routine (3rd Photo) -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-live-card">
              <div class="ai-live-media">
                <span class="ai-live-pill"><span class="ai-live-dot" style="background:#7C6CFF;box-shadow:0 0 10px #7C6CFF;"></span>Routine &amp; Memory Generator</span>
                <div class="ai-scan-sweep" style="animation-delay:2.4s;"></div>
                <img src="../assets/images/ai-memory-routine.jpg" alt="Daily activity timeline and personalized memory recall questions generated from recorded activities" loading="lazy">
              </div>
              <div class="ai-card-footer">
                <span>Daily activity timeline &bull; Memory recall questions created next day</span>
                <span class="ai-card-badge" style="background:rgba(124,108,255,0.1);color:#7C6CFF;">Cognitive Support</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--alzheimers-1);">MEMORY &amp; ROUTINE</span>
            <h2>Daily activity</h2>
            <p class="body-text">Daily activity information can support personalised memory-recall questions.</p>
          </div>
        </div>

        <!-- 4. Interactive Rehabilitation (4th Photo) -->
        <div class="ai-row">
          <div class="ai-visual-col">
            <div class="ai-live-card">
              <div class="ai-live-media">
                <span class="ai-live-pill"><span class="ai-live-dot" style="background:#F5A623;box-shadow:0 0 10px #F5A623;"></span>BioAmp EMG Active</span>
                <div class="ai-scan-sweep" style="animation-delay:0.6s;"></div>
                <img src="../assets/images/ai-interactive-rehab.jpg" alt="Interactive game-based physiotherapy rehabilitation with facial, hand and leg sensor feedback" loading="lazy">
              </div>
              <div class="ai-card-footer">
                <span>Game-based rehabilitation &bull; Face, hand and leg exercise games</span>
                <span class="ai-card-badge" style="background:rgba(245,166,35,0.1);color:#D48600;">Interactive Motor</span>
              </div>
            </div>
          </div>
          <div class="ai-info-col">
            <span class="ey" style="color:var(--paralysis-1);">INTERACTIVE REHABILITATION</span>
            <h2>Rehabilitation</h2>
            <p class="body-text">Interactive rehabilitation can use patient movement and facial interaction.</p>
          </div>
        </div>"""

if old_rows_html in t:
    t = t.replace(old_rows_html, new_rows_html)
    print("Replaced 4 application rows with user's photos and live telemetry animations.")
else:
    print("Warning: old_rows_html not matched exactly!")

# 3. Update JavaScript: Remove old 4 canvas animation loops (Canvas Visual 1 through 4)
pos_cvs1 = t.find("// 2. Canvas Visual 1: Movement")
pos_scrub = t.find("// 6. Responsible Intelligence: Word-by-word scroll-scrubbed text coloring")

if pos_cvs1 != -1 and pos_scrub != -1:
    t = t[:pos_cvs1] + "// 2. Live telemetry presentation active on official images\n      " + t[pos_scrub:]
    print("Removed old synthetic canvas animation scripts from ai-machine-learning.html")
else:
    print(f"Indices: cvs1={pos_cvs1}, scrub={pos_scrub}")

with open(r"D:\Neuromates(website)\technology\ai-machine-learning.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Saved technology/ai-machine-learning.html successfully.")

