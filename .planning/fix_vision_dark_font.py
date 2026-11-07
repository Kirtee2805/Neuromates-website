with open(r"D:\Neuromates(website)\about\vision-mission.html", "r", encoding="utf-8") as f:
    t = f.read()

# Replace CSS in about/vision-mission.html
old_css_block = """    /* Pinned Stage Container */
    .vm-stage {
      position: relative;
      background: linear-gradient(145deg, #0B3A44 0%, #0B5260 55%, #082930 100%);
      color: #FFFFFF;
      overflow: hidden;
      min-height: 100vh;
    }
    #particle-cloud-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      pointer-events: none;
    }

    .vm-statements-wrap {
      position: relative;
      z-index: 2;
      max-width: 1100px;
      margin: 0 auto;
      padding: clamp(60px, 10vw, 120px) 24px;
      display: flex;
      flex-direction: column;
      gap: clamp(80px, 14vw, 160px);
    }

    .manifesto-card {
      position: relative;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-radius: 36px;
      padding: clamp(40px, 7vw, 84px) clamp(28px, 6vw, 72px);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.25);
      transition: transform 0.6s var(--e), border-color 0.6s var(--e);
    }
    .manifesto-card:hover {
      border-color: rgba(127, 214, 208, 0.4);
      transform: translateY(-4px);
    }

    .manifesto-eyebrow {
      font-family: var(--fb);
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--aq);
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 24px;
    }
    .manifesto-eyebrow::before {
      content: "";
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--aq);
      box-shadow: 0 0 12px var(--aq);
    }

    .manifesto-quote {
      font-family: var(--fd);
      font-size: clamp(2.2rem, 5vw, 4.2rem);
      line-height: 1.15;
      font-weight: 700;
      color: #FFFFFF;
      margin: 0;
      letter-spacing: -0.02em;
    }
    .manifesto-quote em {
      font-style: italic;
      background: linear-gradient(100deg, #7FD6D0, #2BB58A 55%, #6EC1F0);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Fallback gradient if 3D disabled */
    .no-3d-bg {
      background: radial-gradient(circle at 75% 30%, rgba(43, 181, 138, 0.15), transparent 60%),
                  radial-gradient(circle at 25% 70%, rgba(110, 193, 240, 0.18), transparent 60%);
    }"""

new_css_block = """    /* Pinned Stage Container - Warm Light Theme for Optimal Readability */
    .vm-stage {
      position: relative;
      background: var(--bg);
      color: #0E3B43;
      overflow: hidden;
      min-height: 80vh;
      border-top: 1px solid rgba(14, 59, 67, 0.06);
    }
    #particle-cloud-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      pointer-events: none;
      opacity: 0.45;
    }

    .vm-statements-wrap {
      position: relative;
      z-index: 2;
      max-width: 1100px;
      margin: 0 auto;
      padding: clamp(60px, 8vw, 100px) 24px;
      display: flex;
      flex-direction: column;
      gap: clamp(48px, 8vw, 80px);
    }

    .manifesto-card {
      position: relative;
      background: #FFFFFF;
      border: 1px solid rgba(14, 59, 67, 0.08);
      border-radius: 32px;
      padding: clamp(40px, 6vw, 72px) clamp(28px, 5vw, 64px);
      box-shadow: 0 20px 60px rgba(14, 59, 67, 0.06);
      transition: transform 0.6s var(--e), border-color 0.6s var(--e), box-shadow 0.6s var(--e);
    }
    .manifesto-card:hover {
      border-color: #0B7A7C;
      box-shadow: 0 28px 70px rgba(14, 59, 67, 0.12);
      transform: translateY(-4px);
    }

    .manifesto-eyebrow {
      font-family: var(--fb);
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #0B7A7C;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 24px;
    }
    .manifesto-eyebrow::before {
      content: "";
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #0B7A7C;
      box-shadow: 0 0 10px rgba(11, 122, 124, 0.35);
    }

    .manifesto-quote {
      font-family: var(--fd);
      font-size: clamp(2rem, 4.5vw, 3.6rem);
      line-height: 1.25;
      font-weight: 700;
      color: #0E3B43; /* Dark High-Contrast Heading Font */
      margin: 0;
      letter-spacing: -0.02em;
    }
    .manifesto-quote em {
      font-style: italic;
      color: #0B7A7C;
      background: linear-gradient(100deg, #0B7A7C, #2BB58A);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Soft ambient background */
    .no-3d-bg {
      background: radial-gradient(circle at 85% 20%, rgba(43, 181, 138, 0.08), transparent 50%),
                  radial-gradient(circle at 15% 80%, rgba(11, 122, 124, 0.08), transparent 50%),
                  var(--bg);
    }"""

if old_css_block in t:
    t = t.replace(old_css_block, new_css_block)
    print("Replaced CSS in vision-mission.html with dark high-contrast readable typography.")
else:
    print("Warning: old_css_block not found in vision-mission.html!")

# Update particle colors in Three.js script to darker/richer teal and mint so they look good on light bg
t = t.replace("const colMint = new T.Color('#5BE7C4');", "const colMint = new T.Color('#0B7A7C');")
t = t.replace("const colSky = new T.Color('#6EC1F0');", "const colSky = new T.Color('#2BB58A');")
t = t.replace("const colWhite = new T.Color('#FFFFFF');", "const colWhite = new T.Color('#7FD6D0');")

with open(r"D:\Neuromates(website)\about\vision-mission.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Saved about/vision-mission.html successfully.")

