about_path = r"D:\Neuromates(website)\about\index.html"
with open(about_path, "r", encoding="utf-8") as f:
    t = f.read()

# 1. Revert Hero Collage CSS to 8s
t = t.replace("""    .kb-slide {
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
    }""", """    .kb-slide {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0;
      animation: kenBurnsCycle 24s infinite linear;
    }
    .kb-slide:nth-child(1) {
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
    }""")

# 2. Revert Hero Collage images
t = t.replace("""        <div class="ken-burns-collage" aria-label="Caregiver and patient support photography collage">
          <img class="kb-slide" src="../assets/images/page_5_Image-7572533686.jpg" alt="Patient and caregiver sitting together in outdoor park setting">
          <img class="kb-slide" src="../assets/images/the-challenge-reality.jpg" alt="The reality of neurological care outside short clinic visits">
          <img class="kb-slide" src="../assets/images/ecosystem-architecture-live.jpg" alt="Ecosystem Architecture connecting Patient, Caretaker, Doctor, Admin">
          <div class="collage-overlay"></div>
          <div class="collage-badge">Care Beyond The Clinic</div>
        </div>""", """        <div class="ken-burns-collage" aria-label="Caregiver and patient support photography collage">
          <img class="kb-slide" src="../assets/images/page_5_Image-7572533686.jpg" alt="Patient and caregiver sitting together in outdoor park setting">
          <img class="kb-slide" src="../assets/images/page_10_Image-7888911063.jpg" alt="Wearable location safety device on patient's arm">
          <img class="kb-slide" src="../assets/images/page_15_Image-8784015711.jpg" alt="Continuous EEG sensing headband for neurological monitoring">
          <div class="collage-overlay"></div>
          <div class="collage-badge">Care Beyond The Clinic</div>
        </div>""")

# 3. Revert Section 1 (THE REALITY)
t = t.replace('<img src="../assets/images/the-challenge-reality.jpg" alt="The Reality: Neurological care challenges outside short clinic visits" loading="lazy" style="width:100%;height:auto;display:block;border-radius:24px;box-shadow:0 18px 48px rgba(14,59,67,0.12);">', '<img src="../assets/images/page_5_Image-7572533686.jpg" alt="Compassionate family care and daily support" loading="lazy">')

# 4. Revert Section 2 (ECOSYSTEM ARCHITECTURE) HTML
t = t.replace("""        <div class="diagram-panel" id="diagram-trigger" style="padding:clamp(20px, 3.5vw, 36px);">
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
        </div>""", """        <div class="diagram-panel" id="diagram-trigger">
          <div class="diagram-canvas-wrap">
            <canvas id="relationship-canvas" aria-label="Self-drawing relationship diagram connecting Patient, Caretaker, Doctor, Admin surrounding Neuro Mates"></canvas>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;flex-wrap:wrap;gap:12px;">
            <span class="demo-tag">Illustration, not real patient data</span>
            <span style="font-size:0.85rem;color:var(--mu);">Dynamic role-based telemetry &amp; bi-directional communication</span>
          </div>
        </div>""")

# 5. Revert relationship-canvas JS
pos_start = t.find("const cvs = document.getElementById('relationship-canvas');")
pos_end = t.find("    });\n  </script>", pos_start)

orig_canvas_js = """const cvs = document.getElementById('relationship-canvas');
      if (cvs) {
        const ctx = cvs.getContext('2d');
        let animProgress = 0;
        let isVisible = false;

        const satellites = [
          { label: 'Patient', col: '#2F7FE0', sub: 'Movement & Vitals' },
          { label: 'Caretaker', col: '#7C6CFF', sub: 'Safety & Alerts' },
          { label: 'Doctor', col: '#2BB58A', sub: 'Clinical Telemetry' },
          { label: 'Admin', col: '#F5A623', sub: 'Device & Config' }
        ];

        function resizeAndDraw() {
          const w = cvs.width = cvs.offsetWidth;
          const h = cvs.height = cvs.offsetHeight;
          ctx.clearRect(0, 0, w, h);

          const cx = w / 2;
          const cy = h / 2;
          const r = Math.min(w * 0.35, h * 0.38, 170);

          // Draw animated orbital ring
          if (animProgress > 0.1) {
            ctx.save();
            ctx.setLineDash([6, 6]);
            ctx.strokeStyle = 'rgba(11, 122, 124, 0.22)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.arc(cx, cy, r, 0, Math.PI * 2 * Math.min(1, (animProgress - 0.1) * 1.5));
            ctx.stroke();
            ctx.restore();
          }

          // Satellites positions
          const coords = satellites.map((s, i) => {
            const angle = (i * Math.PI / 2) - Math.PI / 2;
            return {
              x: cx + Math.cos(angle) * r,
              y: cy + Math.sin(angle) * r,
              label: s.label,
              col: s.col,
              sub: s.sub
            };
          });

          // Draw connecting spokes and traveling data pulses
          coords.forEach((pt, i) => {
            const spokeProgress = Math.min(1, Math.max(0, (animProgress - 0.25 - i * 0.1) * 2));
            if (spokeProgress > 0) {
              ctx.strokeStyle = 'rgba(11, 122, 124, 0.28)';
              ctx.lineWidth = 2;
              ctx.beginPath();
              ctx.moveTo(cx, cy);
              ctx.lineTo(cx + (pt.x - cx) * spokeProgress, cy + (pt.y - cy) * spokeProgress);
              ctx.stroke();

              // Traveling pulse dot
              if (animProgress >= 0.9) {
                const now = Date.now() / 1000;
                const t = ((now * 0.6) + (i * 0.25)) % 1;
                const px = cx + (pt.x - cx) * t;
                const py = cy + (pt.y - cy) * t;
                ctx.fillStyle = pt.col;
                ctx.beginPath();
                ctx.arc(px, py, 4, 0, Math.PI * 2);
                ctx.fill();
              }
            }
          });

          // Draw Center Hub: Neuro Mates Care Platform
          if (animProgress > 0.05) {
            const hubScale = Math.min(1, animProgress * 2);
            // Outer halo
            const haloGrad = ctx.createRadialGradient(cx, cy, 10, cx, cy, 48 * hubScale);
            haloGrad.addColorStop(0, 'rgba(11, 122, 124, 0.25)');
            haloGrad.addColorStop(1, 'rgba(11, 122, 124, 0)');
            ctx.fillStyle = haloGrad;
            ctx.beginPath();
            ctx.arc(cx, cy, 48 * hubScale, 0, Math.PI * 2);
            ctx.fill();

            // Core circle
            ctx.fillStyle = '#0B7A7C';
            ctx.beginPath();
            ctx.arc(cx, cy, 32 * hubScale, 0, Math.PI * 2);
            ctx.fill();

            ctx.strokeStyle = '#7FD6D0';
            ctx.lineWidth = 2.5;
            ctx.stroke();

            // Label
            ctx.fillStyle = '#FFFFFF';
            ctx.font = '700 11px "DM Sans", sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('NEURO MATES', cx, cy - 6);
            ctx.font = '500 9px "DM Sans", sans-serif';
            ctx.fillStyle = '#A3E3DE';
            ctx.fillText('Care Platform', cx, cy + 8);
          }

          // Draw Satellite Cards
          coords.forEach((pt, i) => {
            const nodeProgress = Math.min(1, Math.max(0, (animProgress - 0.4 - i * 0.1) * 2));
            if (nodeProgress <= 0) return;

            ctx.save();
            ctx.translate(pt.x, pt.y);
            ctx.scale(nodeProgress, nodeProgress);

            // Card background pill
            const cardW = 100;
            const cardH = 44;
            ctx.fillStyle = '#FFFFFF';
            ctx.shadowColor = 'rgba(14, 59, 67, 0.12)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 4;
            ctx.beginPath();
            ctx.roundRect(-cardW / 2, -cardH / 2, cardW, cardH, 12);
            ctx.fill();

            // Colored indicator pill
            ctx.shadowColor = 'transparent';
            ctx.fillStyle = pt.col;
            ctx.beginPath();
            ctx.arc(-cardW / 2 + 14, 0, 5, 0, Math.PI * 2);
            ctx.fill();

            // Text
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = '#0E3B43';
            ctx.font = '700 12px "DM Sans", sans-serif';
            ctx.fillText(pt.label, -cardW / 2 + 25, -6);
            ctx.fillStyle = '#6E8588';
            ctx.font = '500 9px "DM Sans", sans-serif';
            ctx.fillText(pt.sub, -cardW / 2 + 25, 8);

            ctx.restore();
          });
        }

        // Trigger self-drawing animation on scroll
        const trigger = document.getElementById('diagram-trigger');
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting && !isVisible) {
              isVisible = true;
              let startTime = null;
              function step(timestamp) {
                if (!startTime) startTime = timestamp;
                const elapsed = timestamp - startTime;
                animProgress = Math.min(1, elapsed / 1800);
                resizeAndDraw();
                if (animProgress < 1) {
                  requestAnimationFrame(step);
                } else {
                  // Continuous loop for traveling pulses
                  function loop() {
                    if (isVisible) {
                      resizeAndDraw();
                      requestAnimationFrame(loop);
                    }
                  }
                  requestAnimationFrame(loop);
                }
              }
              requestAnimationFrame(step);
              observer.unobserve(trigger);
            }
          });
        }, { threshold: 0.2 });
        observer.observe(trigger);

        window.addEventListener('resize', () => {
          if (animProgress > 0) resizeAndDraw();
        });
      }"""

if pos_start != -1 and pos_end != -1:
    t = t[:pos_start] + orig_canvas_js + t[pos_end:]

with open(about_path, "w", encoding="utf-8") as f:
    f.write(t)

print("Reverted about/index.html to original state.")

