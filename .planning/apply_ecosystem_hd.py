with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

# 1. Ensure Section 1 (THE REALITY) uses the-challenge-reality.jpg
old_sec1_img = '<img src="../assets/images/page_5_Image-7572533686.jpg" alt="Compassionate family care and daily support" loading="lazy">'
new_sec1_img = '<img src="../assets/images/the-challenge-reality.jpg" alt="The Reality: Neurological care challenges outside short clinic visits" loading="lazy" style="width:100%;height:auto;display:block;border-radius:24px;box-shadow:0 18px 48px rgba(14,59,67,0.12);">'

if old_sec1_img in t:
    t = t.replace(old_sec1_img, new_sec1_img)
    print("Updated Section 1 with the-challenge-reality.jpg")
else:
    print("Note: Section 1 img check passed or already updated.")

# 2. Update ECOSYSTEM ARCHITECTURE section markup
old_diagram_html = """        <div class="diagram-panel" id="diagram-trigger">
          <div class="diagram-canvas-wrap">
            <canvas id="relationship-canvas" aria-label="Self-drawing relationship diagram connecting Patient, Caretaker, Doctor, Admin surrounding Neuro Mates"></canvas>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;flex-wrap:wrap;gap:12px;">
            <span class="demo-tag">Illustration, not real patient data</span>
            <span style="font-size:0.85rem;color:var(--mu);">Dynamic role-based telemetry &amp; bi-directional communication</span>
          </div>
        </div>"""

new_diagram_html = """        <div class="diagram-panel" id="diagram-trigger" style="padding:clamp(20px, 3.5vw, 36px);background:#FFFFFF;border-radius:32px;box-shadow:0 24px 64px rgba(14,59,67,0.08);border:1px solid rgba(14,59,67,0.06);">
          <div class="eco-stage-container" style="position:relative;width:100%;max-width:980px;margin:0 auto;border-radius:24px;overflow:hidden;box-shadow:0 20px 50px rgba(14,59,67,0.12);background:#EBF5F9;">
            <img src="../assets/images/ecosystem-architecture-live.jpg" alt="Neuro Mates Ecosystem Architecture: Patient, Caretaker, Doctor, and Admin around central Neuro Mates Platform" style="width:100%;height:auto;display:block;">
            <canvas id="relationship-canvas" aria-label="Live animated data signals connecting Patient, Caretaker, Doctor, and Admin" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;"></canvas>
            <div class="eco-live-badge" style="position:absolute;left:20px;bottom:20px;background:rgba(14,59,67,0.92);backdrop-filter:blur(10px);color:#FFFFFF;font:600 0.82rem var(--fb);padding:8px 18px;border-radius:99px;display:flex;align-items:center;gap:10px;box-shadow:0 4px 18px rgba(0,0,0,0.22);letter-spacing:0.02em;">
              <span class="live-pulse-dot" style="width:9px;height:9px;border-radius:50%;background:#5BE7C4;box-shadow:0 0 10px #5BE7C4;display:inline-block;"></span>
              <span id="eco-telemetry-text">Telemetry Streaming: Patient Wearable active · Continuous Monitoring</span>
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;flex-wrap:wrap;gap:12px;">
            <span class="demo-tag">Illustration, not real patient data</span>
            <span style="font-size:0.85rem;color:var(--mu);">Dynamic role-based telemetry &amp; bi-directional communication</span>
          </div>
        </div>"""

if old_diagram_html in t:
    t = t.replace(old_diagram_html, new_diagram_html)
    print("Updated ECOSYSTEM ARCHITECTURE HTML with high-resolution image and live overlay container.")
else:
    print("Warning: old_diagram_html not matched exactly, checking if already updated...")

# 3. Update the relationship-canvas JS
pos_js_start = t.find("// Self-drawing 2D Canvas Relationship Diagram")
pos_js_end = t.find("</script>\n</body>", pos_js_start)
if pos_js_end == -1:
    pos_js_end = t.find("</script>\r\n</body>", pos_js_start)
if pos_js_end == -1:
    pos_js_end = t.find("});\n  </script>", pos_js_start)
if pos_js_end == -1:
    pos_js_end = t.find("});\r\n  </script>", pos_js_start)

new_live_js = """// Live Animated 2D Telemetry Overlay on Ecosystem Architecture
      const cvs = document.getElementById('relationship-canvas');
      const telemetryText = document.getElementById('eco-telemetry-text');
      if (cvs) {
        const ctx = cvs.getContext('2d');
        let isRunning = true;
        let t = 0;

        // 4 Portal Telemetry status updates cycling every 2 seconds
        const telemetryStates = [
          "Patient Wearable Active · Continuous vitals & EEG telemetry streaming",
          "Caretaker Synchronized · Automated safe-zone & medication alerts active",
          "Doctor Clinical Telemetry · Long-term neurological trend reports accessible",
          "Admin Portal Operational · Device network security & status 100%"
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

        // 8 orbiting telemetry packets along circular connectome
        const packets = Array.from({ length: 8 }, (_, i) => ({
          phase: (i / 8),
          speed: 0.11 + (i % 2) * 0.04,
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
          const pulseAlpha = Math.max(0, 1 - pulseR / (orbitR * 1.15)) * 0.4;
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
            const rSpoke = orbitR * 0.86;
            const sx = cx + Math.cos(ang) * (rSpoke * spokeProgress);
            const sy = cy + Math.sin(ang) * (rSpoke * spokeProgress);

            ctx.save();
            ctx.fillStyle = i === roleIdx ? '#5BE7C4' : 'rgba(110, 193, 240, 0.85)';
            ctx.shadowColor = ctx.fillStyle;
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(sx, sy, 3.2, 0, Math.PI * 2);
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

if pos_js_start != -1 and pos_js_end != -1:
    t = t[:pos_js_start] + new_live_js + t[pos_js_end:]
    print("Replaced relationship canvas JS with live animation overlay.")
else:
    print(f"Indices: start={pos_js_start}, end={pos_js_end}")

with open(r"D:\Neuromates(website)\about\index.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Saved about/index.html successfully.")

