import re

about_path = r"D:\Neuromates(website)\about\index.html"
with open(about_path, "r", encoding="utf-8") as f:
    t = f.read()

# 1. Update Hero Collage cycle from 24s (8s each) to 6s (2s each)
old_kb_css = """    .kb-slide:nth-child(1) {
      animation-delay: 0s;
    }
    .kb-slide:nth-child(2) {
      animation-delay: 8s;
    }
    .kb-slide:nth-child(3) {
      animation-delay: 16s;
    }

    @keyframes kenBurnsCycle {
      0% {
        opacity: 0;
        transform: scale(1) translate(0, 0);
      }
      4% {
        opacity: 1;
      }
      30% {
        opacity: 1;
      }
      34% {
        opacity: 0;
        transform: scale(1.08) translate(-1%, -1%);
      }
      100% {
        opacity: 0;
        transform: scale(1.08) translate(-1%, -1%);
      }
    }"""

new_kb_css = """    .kb-slide {
      animation: kenBurnsCycle 6s infinite linear;
    }
    .kb-slide:nth-child(1) {
      animation-delay: 0s;
    }
    .kb-slide:nth-child(2) {
      animation-delay: 2s;
    }
    .kb-slide:nth-child(3) {
      animation-delay: 4s;
    }

    @keyframes kenBurnsCycle {
      0% {
        opacity: 0;
        transform: scale(1) translate(0, 0);
      }
      8% {
        opacity: 1;
      }
      30% {
        opacity: 1;
      }
      38% {
        opacity: 0;
        transform: scale(1.06) translate(-1%, -1%);
      }
      100% {
        opacity: 0;
        transform: scale(1.06) translate(-1%, -1%);
      }
    }"""

if old_kb_css in t:
    t = t.replace(old_kb_css, new_kb_css)
    print("Updated Hero Collage CSS to 2-second transitions.")
else:
    print("WARNING: old_kb_css not found!")

# 2. Update Hero Collage Images to include user's photos
old_kb_html = """        <div class="ken-burns-collage" aria-label="Caregiver and patient support photography collage">
          <img class="kb-slide" src="../assets/images/page_5_Image-7572533686.jpg" alt="Patient and caregiver sitting together in outdoor park setting">
          <img class="kb-slide" src="../assets/images/page_10_Image-7888911063.jpg" alt="Wearable location safety device on patient's arm">
          <img class="kb-slide" src="../assets/images/page_15_Image-8784015711.jpg" alt="Continuous EEG sensing headband for neurological monitoring">
          <div class="collage-overlay"></div>
          <div class="collage-badge">Care Beyond The Clinic</div>
        </div>"""

new_kb_html = """        <div class="ken-burns-collage" aria-label="Caregiver and patient support photography collage">
          <img class="kb-slide" src="../assets/images/page_5_Image-7572533686.jpg" alt="Patient and caregiver sitting together in outdoor park setting">
          <img class="kb-slide" src="../assets/images/the-challenge-reality.jpg" alt="The reality of neurological care outside short clinic visits">
          <img class="kb-slide" src="../assets/images/ecosystem-architecture-live.jpg" alt="Ecosystem Architecture connecting Patient, Caretaker, Doctor, Admin">
          <div class="collage-overlay"></div>
          <div class="collage-badge">Care Beyond The Clinic</div>
        </div>"""

if old_kb_html in t:
    t = t.replace(old_kb_html, new_kb_html)
    print("Updated Hero Collage slides with user images.")
else:
    print("WARNING: old_kb_html not found!")

# 3. Update Section 1 (THE REALITY / The challenge) to user's given image
old_reality_img = '<img src="../assets/images/page_5_Image-7572533686.jpg" alt="Compassionate family care and daily support" loading="lazy">'
new_reality_img = '<img src="../assets/images/the-challenge-reality.jpg" alt="The Reality: Neurological care challenges outside short clinic visits" loading="lazy" style="width:100%;height:auto;display:block;border-radius:24px;box-shadow:0 18px 48px rgba(14,59,67,0.12);">'

if old_reality_img in t:
    t = t.replace(old_reality_img, new_reality_img)
    print("Updated Section 1 (THE REALITY) with the-challenge-reality.jpg.")
else:
    print("WARNING: old_reality_img not found!")

# 4. Update Section 2 (ECOSYSTEM ARCHITECTURE) HTML & Live Animation
# Replace .diagram-panel HTML
old_diagram_html = """        <div class="diagram-panel" id="diagram-trigger">
          <div class="diagram-canvas-wrap">
            <canvas id="relationship-canvas" aria-label="Self-drawing relationship diagram connecting Patient, Caretaker, Doctor, Admin surrounding Neuro Mates"></canvas>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;flex-wrap:wrap;gap:12px;">
            <span class="demo-tag">Illustration, not real patient data</span>
            <span style="font-size:0.85rem;color:var(--mu);">Dynamic role-based telemetry &amp; bi-directional communication</span>
          </div>
        </div>"""

new_diagram_html = """        <div class="diagram-panel" id="diagram-trigger" style="padding:clamp(20px, 3.5vw, 36px);">
          <div class="eco-stage-container" style="position:relative;width:100%;max-width:960px;margin:0 auto;border-radius:24px;overflow:hidden;box-shadow:0 24px 64px rgba(14,59,67,0.14);background:#EBF5F9;">
            <img src="../assets/images/ecosystem-architecture-live.jpg" alt="Neuro Mates Ecosystem Architecture: Patient, Caretaker, Doctor, and Admin around central platform" style="width:100%;height:auto;display:block;">
            <canvas id="relationship-canvas" aria-label="Live animated data signals connecting Patient, Caretaker, Doctor, and Admin" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;"></canvas>
            <div class="eco-live-badge" style="position:absolute;left:18px;bottom:18px;background:rgba(14,59,67,0.88);backdrop-filter:blur(10px);color:#FFFFFF;font:600 0.82rem var(--fb);padding:8px 18px;border-radius:99px;display:flex;align-items:center;gap:10px;box-shadow:0 4px 18px rgba(0,0,0,0.22);letter-spacing:0.02em;">
              <span class="live-pulse-dot" style="width:9px;height:9px;border-radius:50%;background:#5BE7C4;box-shadow:0 0 10px #5BE7C4;display:inline-block;"></span>
              <span id="eco-telemetry-text">Telemetry Streaming: Patient Wearable active · Continuous Monitoring</span>
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;flex-wrap:wrap;gap:12px;">
            <span class="demo-tag">Live System Architecture · Interactive Telemetry Active</span>
            <span style="font-size:0.85rem;color:var(--mu);">Dynamic role-based telemetry &amp; bi-directional communication</span>
          </div>
        </div>"""

if old_diagram_html in t:
    t = t.replace(old_diagram_html, new_diagram_html)
    print("Updated Section 2 (ECOSYSTEM ARCHITECTURE) with ecosystem-architecture-live.jpg and live stage container.")
else:
    print("WARNING: old_diagram_html not found!")

# 5. Update JavaScript for relationship-canvas to draw live orbiting pulses and 2-second role ticker
old_canvas_js_pattern = re.compile(
    r"const cvs = document\.getElementById\('relationship-canvas'\);.*?requestAnimationFrame\(loop\);\s*\}\s*\}\);",
    re.DOTALL
)

new_canvas_js = """const cvs = document.getElementById('relationship-canvas');
      const telemetryText = document.getElementById('eco-telemetry-text');
      if (cvs) {
        const ctx = cvs.getContext('2d');
        let isRunning = true;
        let t = 0;

        // 4 Portal Telemetry status updates cycling every 2 seconds
        const telemetryStates = [
          "🟢 Patient Active · Continuous vitals & EEG telemetry streaming to Neuro Mates Platform",
          "🔵 Caretaker Connected · Automated WhatsApp alerts & safe-zone monitoring synchronized",
          "🟣 Doctor Portal Live · Long-term neurological trend reports & telemetry accessible",
          "🟢 Admin Verified · Device network security & fleet operational status 100%"
        ];
        let roleIdx = 0;
        setInterval(() => {
          roleIdx = (roleIdx + 1) % telemetryStates.length;
          if (telemetryText) telemetryText.textContent = telemetryStates[roleIdx];
        }, 2000);

        function resize() {
          cvs.width = cvs.offsetWidth;
          cvs.height = cvs.offsetHeight;
        }
        window.addEventListener('resize', resize, { passive: true });
        resize();

        // 8 orbiting telemetry packets along the circular connectome
        const packets = Array.from({ length: 8 }, (_, i) => ({
          phase: (i / 8),
          speed: 0.12 + (i % 2) * 0.04,
          color: i % 2 === 0 ? '#5BE7C4' : '#6EC1F0'
        }));

        function drawLiveEcosystem() {
          if (!isRunning) return;
          const w = cvs.width;
          const h = cvs.height;
          ctx.clearRect(0, 0, w, h);

          const cx = w * 0.504;
          const cy = h * 0.495;
          const orbitR = Math.min(w * 0.355, h * 0.375);

          t += 0.016;

          // 1. Central Radar Pulse emanating from Neuro Mates Platform
          const pulseR = ((t * 0.5) % 1) * orbitR * 1.15;
          const pulseAlpha = Math.max(0, 1 - pulseR / (orbitR * 1.15)) * 0.35;
          ctx.save();
          ctx.strokeStyle = `rgba(91, 231, 196, ${pulseAlpha})`;
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.arc(cx, cy, pulseR, 0, Math.PI * 2);
          ctx.stroke();
          ctx.restore();

          // 2. Glowing telemetry packets traveling along the circular orbit ring
          packets.forEach(p => {
            const angle = (t * p.speed + p.phase) * Math.PI * 2;
            const px = cx + Math.cos(angle) * orbitR;
            const py = cy + Math.sin(angle) * orbitR;

            // Packet glow
            ctx.save();
            ctx.shadowColor = p.color;
            ctx.shadowBlur = 10;
            ctx.fillStyle = '#FFFFFF';
            ctx.beginPath();
            ctx.arc(px, py, 3.5, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(px, py, 2.2, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          });

          // 3. Spoke signals pulsing between central platform and 4 portals
          // Angles: Top (-90°), Right (0°), Bottom (90°), Left (180°)
          const spokeAngles = [-Math.PI / 2, 0, Math.PI / 2, Math.PI];
          spokeAngles.forEach((ang, i) => {
            const spokeProgress = ((t * 0.8 + i * 0.25) % 1.0);
            const rSpoke = orbitR * 0.85;
            const sx = cx + Math.cos(ang) * (rSpoke * spokeProgress);
            const sy = cy + Math.sin(ang) * (rSpoke * spokeProgress);

            ctx.save();
            ctx.fillStyle = i === roleIdx ? '#5BE7C4' : 'rgba(110, 193, 240, 0.85)';
            ctx.shadowColor = ctx.fillStyle;
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(sx, sy, 3, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          });

          requestAnimationFrame(drawLiveEcosystem);
        }

        const io = new IntersectionObserver(entries => {
          entries.forEach(e => {
            isRunning = e.isIntersecting;
            if (isRunning) requestAnimationFrame(drawLiveEcosystem);
          });
        }, { threshold: 0.1 });
        io.observe(cvs);

        requestAnimationFrame(drawLiveEcosystem);
      }
    });"""

if old_canvas_js_pattern.search(t):
    t = old_canvas_js_pattern.sub(new_canvas_js, t)
    print("Replaced relationship-canvas JS with live animated ecosystem renderer.")
else:
    print("WARNING: old_canvas_js_pattern not matched!")

with open(about_path, "w", encoding="utf-8") as f:
    f.write(t)
print("Saved about/index.html successfully.")

