about_path = r"D:\Neuromates(website)\about\index.html"
with open(about_path, "r", encoding="utf-8") as f:
    t = f.read()

pos_start = t.find("const cvs = document.getElementById('relationship-canvas');")
pos_end = t.find("    });\n  </script>", pos_start)

if pos_start == -1 or pos_end == -1:
    print(f"Indices not found: start={pos_start}, end={pos_end}")
else:
    new_canvas_js = """const cvs = document.getElementById('relationship-canvas');
      const telemetryText = document.getElementById('eco-telemetry-text');
      if (cvs) {
        const ctx = cvs.getContext('2d');
        let isRunning = true;
        let t = 0;

        // 4 Portal Telemetry status updates cycling every 2 seconds
        const telemetryStates = [
          "🟢 Telemetry Streaming: Patient Wearable active · Continuous Monitoring",
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

        // Orbiting telemetry packets along circular connectome
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

          // 1. Central Radar Wave pulse emanating from Neuro Mates Platform
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
      }"""
    t = t[:pos_start] + new_canvas_js + t[pos_end:]
    with open(about_path, "w", encoding="utf-8") as f:
        f.write(t)
    print("Replaced relationship-canvas JS successfully in about/index.html!")

