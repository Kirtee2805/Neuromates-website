import os

# We will write a python script that updates index.html, neuromates-home.html, and Neuro Mates _ Connected neurological care.html
# Replacing the old makeCore / makeDevices 3D scene with the pink glowing 3D brain!

brain_js_code = """/* 3D: Pink Glowing Human Brain Animation covering hero background */
(()=>{
  if(!window.THREE) return;
  try {
    const T = THREE, c = $('#gl');
    if(!c) return;

    const Rn = new T.WebGLRenderer({ canvas: c, alpha: true, antialias: true, powerPreference: 'high-performance' });
    Rn.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));

    const sc = new T.Scene();
    const cam = new T.PerspectiveCamera(40, innerWidth / innerHeight, 0.1, 50);
    cam.position.z = 7.0;

    const root = new T.Group();
    sc.add(root);

    // Glowing pink radial sprite texture for neurons
    function makeGlowSprite() {
      const cv = document.createElement('canvas');
      cv.width = 64; cv.height = 64;
      const ctx = cv.getContext('2d');
      const g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      g.addColorStop(0, 'rgba(255, 255, 255, 1)');
      g.addColorStop(0.2, 'rgba(255, 215, 225, 0.95)');
      g.addColorStop(0.5, 'rgba(244, 114, 182, 0.55)');
      g.addColorStop(0.8, 'rgba(251, 113, 133, 0.2)');
      g.addColorStop(1, 'rgba(244, 114, 182, 0)');
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, 64, 64);
      return new T.CanvasTexture(cv);
    }
    const glowTex = makeGlowSprite();

    // 1. Generate Anatomical Brain Geometry (Left & Right Hemispheres)
    const brainGroup = new T.Group();
    root.add(brainGroup);

    const NODE_COUNT = 2100;
    const positions = new Float32Array(NODE_COUNT * 3);
    const colors = new Float32Array(NODE_COUNT * 3);
    const baseCoords = [];

    // Pink Color Palette
    const cWhite = new T.Color('#FFFFFF');
    const cLightPink = new T.Color('#FFB6C1'); // light pink
    const cBlush = new T.Color('#FDA4AF');     // soft blush pink
    const cRose = new T.Color('#F472B6');      // vibrant rose pink
    const cDeepPink = new T.Color('#FB7185');  // deep pink
    const cVioletPink = new T.Color('#E879F9');// soft violet-pink sulci

    for(let i = 0; i < NODE_COUNT; i++) {
      const side = (i % 2 === 0) ? -1.0 : 1.0;
      const u = Math.floor(i / 2) / (NODE_COUNT / 2);
      const theta = Math.acos(Math.max(-1.0, Math.min(1.0, 1.0 - 2.0 * u)));
      const phi = Math.sqrt((NODE_COUNT / 2) * Math.PI) * theta;

      const sinTheta = Math.sin(theta);
      const cosPhi = Math.abs(Math.cos(phi));

      // Anatomical proportions: X = width, Y = height, Z = length
      let rx = 0.12 + 0.88 * sinTheta * cosPhi;
      let ry = Math.cos(theta) * 0.95;
      let rz = sinTheta * Math.sin(phi) * 1.35;

      let x = side * rx;
      let y = ry;
      let z = rz;

      // Anatomic lobes tuning
      if (y < -0.1 && z < -0.2) {
        // Cerebellum & brainstem
        x *= 0.72; y -= 0.14; z *= 0.86;
      } else if (y < 0.05 && Math.abs(z) < 0.45) {
        // Temporal lobes
        x *= 1.18; y *= 0.95;
      } else if (z > 0.35) {
        // Frontal lobe
        y *= 1.06; x *= 0.97;
      }

      // Cortical gyri and sulci folds
      const fold = (
        Math.sin(x * 8.5) * Math.cos(y * 7.5) * 0.055 +
        Math.sin(y * 11.0) * Math.cos(z * 9.5) * 0.045 +
        Math.sin(z * 13.0 + x * 6.0) * 0.035
      );

      // Deepen interhemispheric fissure
      let pull = 0;
      if (Math.abs(x) < 0.22) {
        pull = (0.22 - Math.abs(x)) * 0.28;
      }

      const mag = Math.hypot(x, y, z) || 1;
      x += (x / mag) * (fold - pull);
      y += (y / mag) * (fold - pull);
      z += (z / mag) * (fold - pull);

      positions[i * 3] = x;
      positions[i * 3 + 1] = y;
      positions[i * 3 + 2] = z;
      baseCoords.push({ x, y, z, side });

      // Color mapping: light pink hues with bright synaptic highlights
      const normY = (y + 1.1) / 2.2;
      const col = new T.Color();
      if (Math.random() < 0.12) {
        col.copy(cWhite); // firing synapse highlight
      } else if (normY > 0.7) {
        col.lerpColors(cLightPink, cBlush, Math.random());
      } else if (normY > 0.35) {
        col.lerpColors(cBlush, cRose, Math.random());
      } else {
        col.lerpColors(cRose, cDeepPink, Math.random());
      }
      if (Math.abs(x) < 0.25) {
        col.lerp(cVioletPink, 0.4); // fissure depth
      }

      colors[i * 3] = col.r;
      colors[i * 3 + 1] = col.g;
      colors[i * 3 + 2] = col.b;
    }

    const nodeGeometry = new T.BufferGeometry();
    nodeGeometry.setAttribute('position', new T.BufferAttribute(positions, 3));
    nodeGeometry.setAttribute('color', new T.BufferAttribute(colors, 3));

    const nodeMaterial = new T.PointsMaterial({
      size: 0.14,
      map: glowTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.92,
      blending: T.AdditiveBlending,
      depthWrite: false
    });

    const nodePoints = new T.Points(nodeGeometry, nodeMaterial);
    brainGroup.add(nodePoints);

    // 2. Generate Synaptic Connectome Axon Lines
    const lineCoords = [];
    const edges = [];
    const maxDist2 = 0.24 * 0.24;
    const minDist2 = 0.04 * 0.04;

    for (let i = 0; i < NODE_COUNT; i++) {
      let connections = 0;
      const p1 = baseCoords[i];
      for (let j = i + 1; j < Math.min(i + 38, NODE_COUNT); j++) {
        const p2 = baseCoords[j];
        if (p1.side !== p2.side && Math.abs(p1.x) > 0.18) continue; // separate hemispheres
        const dx = p1.x - p2.x, dy = p1.y - p2.y, dz = p1.z - p2.z;
        const d2 = dx * dx + dy * dy + dz * dz;
        if (d2 >= minDist2 && d2 <= maxDist2) {
          lineCoords.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
          edges.push({ p1, p2 });
          connections++;
          if (connections >= 3) break;
        }
      }
    }

    const lineGeometry = new T.BufferGeometry();
    lineGeometry.setAttribute('position', new T.BufferAttribute(new Float32Array(lineCoords), 3));
    const lineMaterial = new T.LineBasicMaterial({
      color: 0xF472B6, // pink axon lines
      transparent: true,
      opacity: 0.26,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const axonLines = new T.LineSegments(lineGeometry, lineMaterial);
    brainGroup.add(axonLines);

    // 3. Firing Synaptic Action Potentials (Glowing moving impulses)
    const PULSE_COUNT = 65;
    const pulsePositions = new Float32Array(PULSE_COUNT * 3);
    const pulses = [];
    for (let i = 0; i < PULSE_COUNT; i++) {
      const edge = edges[Math.floor(Math.random() * edges.length)] || { p1: {x:0,y:0,z:0}, p2: {x:0,y:0,z:0} };
      pulses.push({
        edge,
        progress: Math.random(),
        speed: 0.006 + Math.random() * 0.012
      });
    }

    const pulseGeometry = new T.BufferGeometry();
    pulseGeometry.setAttribute('position', new T.BufferAttribute(pulsePositions, 3));
    const pulseMaterial = new T.PointsMaterial({
      size: 0.24,
      map: glowTex,
      color: 0xFFF1F2, // brilliant white-pink spark
      transparent: true,
      opacity: 0.98,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const pulsePoints = new T.Points(pulseGeometry, pulseMaterial);
    brainGroup.add(pulsePoints);

    // 4. Volumetric Hemisphere Inner Aura (Left & Right translucent glow)
    const innerGeo = new T.SphereGeometry(0.72, 28, 20);
    const innerMat = new T.MeshBasicMaterial({
      color: 0xFB7185,
      transparent: true,
      opacity: 0.065,
      wireframe: true,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const leftHemi = new T.Mesh(innerGeo, innerMat);
    leftHemi.position.set(-0.52, 0.04, 0);
    leftHemi.scale.set(0.72, 0.88, 1.18);
    const rightHemi = new T.Mesh(innerGeo, innerMat);
    rightHemi.position.set(0.52, 0.04, 0);
    rightHemi.scale.set(0.72, 0.88, 1.18);
    brainGroup.add(leftHemi, rightHemi);

    // 5. Ambient Floating Neural Particle Field
    const AMBIENT_COUNT = 75;
    const ambPositions = new Float32Array(AMBIENT_COUNT * 3);
    const ambData = [];
    for (let i = 0; i < AMBIENT_COUNT; i++) {
      const r = 1.6 + Math.random() * 2.2;
      const th = Math.random() * Math.PI * 2;
      const ph = (Math.random() - 0.5) * Math.PI;
      const px = r * Math.cos(th) * Math.cos(ph);
      const py = r * Math.sin(ph);
      const pz = r * Math.sin(th) * Math.cos(ph);
      ambPositions[i * 3] = px;
      ambPositions[i * 3 + 1] = py;
      ambPositions[i * 3 + 2] = pz;
      ambData.push({ px, py, pz, speed: 0.2 + Math.random() * 0.4, phase: Math.random() * Math.PI * 2 });
    }
    const ambGeometry = new T.BufferGeometry();
    ambGeometry.setAttribute('position', new T.BufferAttribute(ambPositions, 3));
    const ambMaterial = new T.PointsMaterial({
      size: 0.16,
      map: glowTex,
      color: 0xFBCFE8, // soft light pink dust
      transparent: true,
      opacity: 0.65,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const ambPoints = new T.Points(ambGeometry, ambMaterial);
    brainGroup.add(ambPoints);

    // 6. Lights for depth and illumination
    sc.add(new T.AmbientLight(0xFFE4E6, 0.85));
    const pinkKey = new T.DirectionalLight(0xF472B6, 1.5);
    pinkKey.position.set(3, 4, 5);
    sc.add(pinkKey);
    const rosePoint = new T.PointLight(0xFDA4AF, 1.4, 25);
    rosePoint.position.set(-4, -2, 4);
    sc.add(rosePoint);
    const blushRim = new T.PointLight(0xFFB6C1, 1.2, 20);
    blushRim.position.set(0, 5, -4);
    sc.add(blushRim);

    // Resize handling
    const rs = () => {
      Rn.setSize(innerWidth, innerHeight, false);
      cam.aspect = innerWidth / innerHeight;
      cam.updateProjectionMatrix();
    };
    rs();
    addEventListener('resize', rs, { passive: true });

    // Interactive cursor parallax
    let mx = 0, my = 0;
    addEventListener('pointermove', e => {
      mx = e.clientX / innerWidth - 0.5;
      my = e.clientY / innerHeight - 0.5;
    }, { passive: true });

    // Visibility observer to avoid burning CPU when offscreen
    let isVisible = true;
    const heroHeader = document.querySelector('header.h') || document.body;
    new IntersectionObserver(entries => {
      isVisible = entries[0].isIntersecting;
      if (isVisible && !reqId) reqId = requestAnimationFrame(animateLoop);
    }, { threshold: 0.05 }).observe(heroHeader);

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (reqId) { cancelAnimationFrame(reqId); reqId = null; }
      } else if (isVisible && !reqId) {
        reqId = requestAnimationFrame(animateLoop);
      }
    });

    c.classList.add('on');
    const t0 = performance.now();
    let curX = innerWidth > 900 ? 0.35 : 0;
    let reqId = null;

    function animateLoop() {
      if (document.hidden || !isVisible) {
        reqId = null;
        return;
      }
      reqId = requestAnimationFrame(animateLoop);

      const t = RM ? 0 : (performance.now() - t0) * 0.001;

      // Base scale: covers the background behind the hero heading
      const isDesktop = innerWidth > 900;
      const targetBaseScale = isDesktop ? 2.4 : 1.7;
      const targetX = isDesktop ? (tx !== 0 ? tx * 0.25 + 0.35 : 0.35) : 0;
      curX += (targetX - curX) * 0.05;

      // Breathing rhythm: gentle expansion and contraction of living brain
      const breath = 1.0 + Math.sin(t * 1.6) * 0.022 + Math.sin(t * 3.4) * 0.01;
      brainGroup.scale.setScalar(targetBaseScale * breath);

      // Position: centered behind "Advancing connected care..."
      const scrollDrift = (window.scrollY || 0) * 0.0008;
      brainGroup.position.set(curX, 0.12 - scrollDrift, 0);

      // Organic rotation & cursor tilt
      brainGroup.rotation.y = t * 0.16 + (mx * 0.45);
      brainGroup.rotation.x = 0.22 + Math.sin(t * 0.3) * 0.06 - (my * 0.35);
      brainGroup.rotation.z = Math.sin(t * 0.2) * 0.035;

      // Update firing action potential pulses
      const pulsePos = pulsePoints.geometry.attributes.position.array;
      for (let i = 0; i < PULSE_COUNT; i++) {
        const p = pulses[i];
        p.progress += p.speed;
        if (p.progress >= 1.0) {
          p.progress = 0;
          p.edge = edges[Math.floor(Math.random() * edges.length)] || p.edge;
        }
        const p1 = p.edge.p1, p2 = p.edge.p2;
        const prog = p.progress;
        pulsePos[i * 3] = p1.x + (p2.x - p1.x) * prog;
        pulsePos[i * 3 + 1] = p1.y + (p2.y - p1.y) * prog;
        pulsePos[i * 3 + 2] = p1.z + (p2.z - p1.z) * prog;
      }
      pulsePoints.geometry.attributes.position.needsUpdate = true;

      // Subtle ambient particle movement
      const ambPos = ambPoints.geometry.attributes.position.array;
      for (let i = 0; i < AMBIENT_COUNT; i++) {
        const a = ambData[i];
        ambPos[i * 3 + 1] = a.py + Math.sin(t * a.speed + a.phase) * 0.12;
      }
      ambPoints.geometry.attributes.position.needsUpdate = true;

      Rn.render(sc, cam);
    }

    reqId = requestAnimationFrame(animateLoop);
  } catch(e) {
    console.warn('3D Brain initialization error:', e);
  }
})();
"""

targets = [
    r"D:\Neuromates(website)\index.html",
    r"D:\Neuromates(website)\neuromates-home.html",
    r"D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html"
]

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # Find start marker
    start_marker = "/* 3D: devices orbiting the care platform */"
    pos_start = c.find(start_marker)
    if pos_start == -1:
        print(f"Could not find start marker in {p}")
        continue
    pos_end = c.find("</script>", pos_start)
    if pos_end == -1:
        print(f"Could not find </script> after start marker in {p}")
        continue

    # Update header data-x attribute from 2.2 to 0.45 so brain covers hero background behind text
    c = c.replace('<header class="h" data-s="0" data-x="2.2">', '<header class="h" data-s="0" data-x="0.45">')

    # Replace old 3D script with the new pink 3D brain script
    c = c[:pos_start] + brain_js_code + c[pos_end:]

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Successfully updated {p} with Pink 3D Brain Animation!")

