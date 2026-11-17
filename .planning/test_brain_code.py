# Test building the 3D Anatomical Brain code
brain_js = '''/* 3D: Anatomical Interactive 3D Human Brain with Neural Synapses & Visitor Interaction */
(()=>{
  if (!window.THREE) return;
  try {
    const T = THREE, canvas = $('#gl');
    if (!canvas) return;

    const renderer = new T.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    const scene = new T.Scene();
    const camera = new T.PerspectiveCamera(42, innerWidth / innerHeight, 0.1, 50);
    camera.position.set(0, 0, 7.2);

    const worldGroup = new T.Group();
    scene.add(worldGroup);

    const brainGroup = new T.Group();
    worldGroup.add(brainGroup);

    // Glowing round sprite texture for synaptic nodes
    function createGlowTexture() {
      const cv = document.createElement('canvas');
      cv.width = 64; cv.height = 64;
      const ctx = cv.getContext('2d');
      const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.2, 'rgba(255, 130, 180, 0.95)');
      grad.addColorStop(0.5, 'rgba(240, 98, 146, 0.55)');
      grad.addColorStop(0.75, 'rgba(0, 229, 255, 0.25)');
      grad.addColorStop(1, 'rgba(0, 229, 255, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
      return new T.CanvasTexture(cv);
    }
    const glowTex = createGlowTexture();

    // 1. Generate Realistic Anatomical Human Brain Coordinates
    const NODE_COUNT = 2400;
    const positions = new Float32Array(NODE_COUNT * 3);
    const colors = new Float32Array(NODE_COUNT * 3);
    const baseCoords = [];

    const colWhite = new T.Color('#FFFFFF');
    const colCyan = new T.Color('#00E5FF');
    const colTeal = new T.Color('#2BB58A');
    const colPink = new T.Color('#FF4081');
    const colRose = new T.Color('#FF80AB');
    const colSoftPink = new T.Color('#FFD1DC');

    let idx = 0;
    // Distribute nodes across: Left Hemisphere, Right Hemisphere, Cerebellum, Brainstem
    for (let i = 0; i < NODE_COUNT; i++) {
      let x, y, z;
      const side = (i % 2 === 0) ? -1 : 1;
      const section = Math.random();

      if (section < 0.78) {
        // CEREBRAL HEMISPHERES (Frontal, Parietal, Occipital, Temporal Lobes)
        const u = Math.random();
        const v = Math.random();
        const theta = u * Math.PI; // 0 to PI
        const phi = v * Math.PI;   // 0 to PI (one side)

        // Base ellipsoid: brain is longer front-to-back (z), slightly taller (y), wider (x)
        let bx = 0.92 * Math.sin(theta) * Math.sin(phi);
        let by = 0.96 * Math.cos(theta);
        let bz = 1.35 * Math.sin(theta) * Math.cos(phi);

        // Anatomical shaping:
        // Frontal lobe expansion (anterior: z > 0)
        if (bz > 0.2) {
          bx *= (1.0 + 0.12 * Math.sin((bz - 0.2) * 1.5));
          by *= (1.0 + 0.08 * (bz - 0.2));
        }
        // Occipital lobe taper (posterior: z < -0.3)
        if (bz < -0.3) {
          bx *= (1.0 + 0.22 * (bz + 0.3));
          by *= (1.0 + 0.15 * (bz + 0.3));
        }
        // Temporal lobe bulge (inferior lateral: y < 0, |z| < 0.4)
        if (by < 0.1 && Math.abs(bz) < 0.6) {
          bx *= 1.25;
          by *= 0.92;
        }

        // Cortical Convolutions (Gyri & Sulci folds)
        const gyri = 
          Math.sin(bx * 9.0 + bz * 4.0) * Math.cos(by * 8.0) * 0.075 +
          Math.sin(by * 11.0 + bx * 6.0) * Math.cos(bz * 10.0) * 0.055 +
          Math.sin(bz * 13.0) * Math.cos(bx * 12.0) * 0.035;

        // Medial Longitudinal Fissure (clean separation between left and right hemispheres)
        const hemisphereOffset = 0.14;
        let fissureDepth = 0;
        if (Math.abs(bx) < 0.35) {
          fissureDepth = (0.35 - Math.abs(bx)) * 0.32;
        }

        x = side * (Math.abs(bx) + hemisphereOffset) + (bx / (Math.abs(bx) || 1)) * (gyri - fissureDepth);
        y = by + gyri - fissureDepth * 0.4;
        z = bz + gyri;

      } else if (section < 0.93) {
        // CEREBELLUM (Two posterior-inferior lobules with dense horizontal folia)
        const u = Math.random();
        const v = Math.random();
        const th = u * Math.PI * 2;
        const ph = (v - 0.5) * Math.PI;

        const crx = 0.48 * Math.cos(th) * Math.cos(ph);
        const cry = 0.35 * Math.sin(ph);
        const crz = 0.45 * Math.sin(th) * Math.cos(ph);

        // Horizontal cerebellar folia grooves
        const folia = Math.sin(cry * 24.0) * 0.025;

        x = side * (Math.abs(crx) + 0.18) + folia;
        y = cry - 0.65 + folia;
        z = crz - 0.72;

      } else {
        // BRAINSTEM (Pons & Medulla extending downwards)
        const t = Math.random();
        const rad = 0.16 * (1.0 - t * 0.35);
        const ang = Math.random() * Math.PI * 2;

        x = rad * Math.cos(ang);
        y = -0.5 - t * 0.75;
        z = -0.15 - t * 0.2 + rad * Math.sin(ang);
      }

      positions[i * 3] = x;
      positions[i * 3 + 1] = y;
      positions[i * 3 + 2] = z;
      baseCoords.push({ x, y, z, origX: x, origY: y, origZ: z, side });

      // Biotech Palette Color gradient:
      // Frontal & parietal = vibrant rose-pink & neon cyan
      // Depth = deep electric magenta
      // Fissure & stem = bioluminescent teal
      const c = new T.Color();
      const normH = (y + 1.2) / 2.4;
      if (Math.random() < 0.15) {
        c.copy(colWhite); // active synapsing neurons
      } else if (section >= 0.93) {
        c.lerpColors(colTeal, colCyan, Math.random());
      } else if (section >= 0.78) {
        c.lerpColors(colPink, colTeal, Math.random() * 0.7);
      } else if (normH > 0.65) {
        c.lerpColors(colRose, colSoftPink, Math.random());
      } else if (normH > 0.35) {
        c.lerpColors(colPink, colRose, Math.random());
      } else {
        c.lerpColors(colCyan, colPink, Math.random() * 0.8);
      }

      colors[i * 3] = c.r;
      colors[i * 3 + 1] = c.g;
      colors[i * 3 + 2] = c.b;
    }

    const nodeGeometry = new T.BufferGeometry();
    nodeGeometry.setAttribute('position', new T.BufferAttribute(positions, 3));
    nodeGeometry.setAttribute('color', new T.BufferAttribute(colors, 3));

    const nodeMaterial = new T.PointsMaterial({
      size: 0.14,
      map: glowTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.95,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const nodePoints = new T.Points(nodeGeometry, nodeMaterial);
    brainGroup.add(nodePoints);

    // 2. Axon Synaptic Connectome Fibers (Lines connecting neighboring neurons)
    const MAX_EDGES = 1400;
    const edgeIndices = [];
    const edgeList = [];
    for (let i = 0; i < NODE_COUNT && edgeList.length < MAX_EDGES; i += 2) {
      const p1 = baseCoords[i];
      let nearestDist = 0.38;
      let nearestIdx = -1;
      // Search local neighborhood
      for (let j = i + 1; j < Math.min(i + 50, NODE_COUNT); j++) {
        const p2 = baseCoords[j];
        if (p1.side !== p2.side && Math.abs(p1.x) > 0.22) continue; // preserve longitudinal fissure separation
        const d = Math.hypot(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z);
        if (d > 0.08 && d < nearestDist) {
          nearestDist = d;
          nearestIdx = j;
        }
      }
      if (nearestIdx !== -1) {
        edgeIndices.push(i, nearestIdx);
        edgeList.push({ p1: baseCoords[i], p2: baseCoords[nearestIdx] });
      }
    }

    const edgePositions = new Float32Array(edgeIndices.length * 3);
    const edgeColors = new Float32Array(edgeIndices.length * 3);
    for (let k = 0; k < edgeIndices.length; k++) {
      const pt = baseCoords[edgeIndices[k]];
      edgePositions[k * 3] = pt.x;
      edgePositions[k * 3 + 1] = pt.y;
      edgePositions[k * 3 + 2] = pt.z;
      // Soft rose & cyan line color
      edgeColors[k * 3] = 0.95;
      edgeColors[k * 3 + 1] = 0.45;
      edgeColors[k * 3 + 2] = 0.72;
    }
    const lineGeometry = new T.BufferGeometry();
    lineGeometry.setAttribute('position', new T.BufferAttribute(edgePositions, 3));
    lineGeometry.setAttribute('color', new T.BufferAttribute(edgeColors, 3));

    const lineMaterial = new T.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.28,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const axonLines = new T.LineSegments(lineGeometry, lineMaterial);
    brainGroup.add(axonLines);

    // 3. Action Potential Synaptic Impulses (Traveling photon particles)
    const PULSE_COUNT = 140;
    const pulsePositions = new Float32Array(PULSE_COUNT * 3);
    const pulseColors = new Float32Array(PULSE_COUNT * 3);
    const pulseData = [];

    for (let i = 0; i < PULSE_COUNT; i++) {
      const edge = edgeList[Math.floor(Math.random() * edgeList.length)] || { p1: {x:0,y:0,z:0}, p2: {x:0,y:0,z:0} };
      pulseData.push({
        edge,
        progress: Math.random(),
        speed: 0.008 + Math.random() * 0.016
      });
      pulsePositions[i * 3] = edge.p1.x;
      pulsePositions[i * 3 + 1] = edge.p1.y;
      pulsePositions[i * 3 + 2] = edge.p1.z;

      pulseColors[i * 3] = 1.0;
      pulseColors[i * 3 + 1] = 0.92;
      pulseColors[i * 3 + 2] = 0.98;
    }
    const pulseGeometry = new T.BufferGeometry();
    pulseGeometry.setAttribute('position', new T.BufferAttribute(pulsePositions, 3));
    pulseGeometry.setAttribute('color', new T.BufferAttribute(pulseColors, 3));

    const pulseMaterial = new T.PointsMaterial({
      size: 0.22,
      map: glowTex,
      vertexColors: true,
      transparent: true,
      opacity: 1.0,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const pulsePoints = new T.Points(pulseGeometry, pulseMaterial);
    brainGroup.add(pulsePoints);

    // 4. Volumetric Inner Glow Core
    const coreMat = new T.MeshBasicMaterial({
      color: 0xFF2A85,
      transparent: true,
      opacity: 0.08,
      wireframe: true
    });
    const coreMesh = new T.Mesh(new T.IcosahedronGeometry(0.85, 2), coreMat);
    brainGroup.add(coreMesh);

    // 5. Lighting
    scene.add(new T.AmbientLight(0xFFE6EE, 0.9));
    const dirLight = new T.DirectionalLight(0x00E5FF, 1.2);
    dirLight.position.set(4, 5, 6);
    scene.add(dirLight);

    // 6. Interactive Visitor Controls: Drag, Orbit & Inertia
    let isDragging = false;
    let prevMouseX = 0, prevMouseY = 0;
    let velX = 0, velY = 0;
    let targetRotY = 0.3, targetRotX = 0.15;
    let cursorX = 0, cursorY = 0;
    let neuralExcite = 0;

    // Hit area covering the hero
    const interactionTarget = document.querySelector('header.h') || canvas;

    function onPointerDown(e) {
      isDragging = true;
      prevMouseX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      prevMouseY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      neuralExcite = 1.0; // trigger neural burst
    }

    function onPointerMove(e) {
      const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;

      cursorX = (clientX / innerWidth - 0.5) * 2;
      cursorY = (clientY / innerHeight - 0.5) * 2;

      if (isDragging) {
        const dx = clientX - prevMouseX;
        const dy = clientY - prevMouseY;
        velY = dx * 0.005;
        velX = dy * 0.005;
        targetRotY += velY;
        targetRotX += velX;
        prevMouseX = clientX;
        prevMouseY = clientY;
      }
    }

    function onPointerUp() {
      isDragging = false;
    }

    interactionTarget.addEventListener('pointerdown', onPointerDown, { passive: true });
    addEventListener('pointermove', onPointerMove, { passive: true });
    addEventListener('pointerup', onPointerUp, { passive: true });
    addEventListener('pointercancel', onPointerUp, { passive: true });

    // Touch events fallback for mobile
    interactionTarget.addEventListener('touchstart', onPointerDown, { passive: true });
    addEventListener('touchmove', onPointerMove, { passive: true });
    addEventListener('touchend', onPointerUp, { passive: true });

    // Responsive Resize
    function handleResize() {
      renderer.setSize(innerWidth, innerHeight, false);
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
    }
    handleResize();
    addEventListener('resize', handleResize, { passive: true });

    // Visibility Observer (pauses loop when scrolled offscreen)
    let isVisible = true;
    let animId = null;
    const heroElem = document.querySelector('header.h') || document.body;
    new IntersectionObserver(entries => {
      isVisible = entries[0].isIntersecting;
      if (isVisible && !animId) animId = requestAnimationFrame(renderLoop);
    }, { threshold: 0.05 }).observe(heroElem);

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (animId) { cancelAnimationFrame(animId); animId = null; }
      } else if (isVisible && !animId) {
        animId = requestAnimationFrame(renderLoop);
      }
    });

    canvas.classList.add('on');
    const startTime = performance.now();
    let currentX = innerWidth > 900 ? 0.38 : 0;

    function renderLoop() {
      if (document.hidden || !isVisible) {
        animId = null;
        return;
      }
      animId = requestAnimationFrame(renderLoop);

      const t = RM ? 0 : (performance.now() - startTime) * 0.001;

      // Scaling & Positioning: nicely framing the hero heading
      const isDesktop = innerWidth > 900;
      const baseScale = isDesktop ? 2.35 : 1.65;
      const targetPosX = isDesktop ? 0.38 : 0;
      currentX += (targetPosX - currentX) * 0.05;

      // Breathing rhythm
      const breath = 1.0 + Math.sin(t * 1.5) * 0.025 + Math.sin(t * 3.2) * 0.012;
      brainGroup.scale.setScalar(baseScale * breath);

      // Parallax scroll drift
      const scrollDrift = (window.scrollY || 0) * 0.0007;
      brainGroup.position.set(currentX, 0.1 - scrollDrift, 0);

      // Inertia & Continuous Orbit
      if (!isDragging) {
        velX *= 0.92;
        velY *= 0.92;
        targetRotY += 0.0035 + velY; // gentle natural spin
        targetRotX += velX;
      }

      // Tilt slightly toward cursor when not violently dragged
      const tiltX = targetRotX - (cursorY * 0.25);
      const tiltY = targetRotY + (cursorX * 0.35);

      brainGroup.rotation.x += (tiltX - brainGroup.rotation.x) * 0.08;
      brainGroup.rotation.y += (tiltY - brainGroup.rotation.y) * 0.08;
      brainGroup.rotation.z = Math.sin(t * 0.4) * 0.03;

      // Neural excitation fade
      neuralExcite *= 0.96;

      // Animate Action Potential Synapses
      const pPos = pulsePoints.geometry.attributes.position.array;
      for (let i = 0; i < PULSE_COUNT; i++) {
        const p = pulseData[i];
        p.progress += p.speed * (1.0 + neuralExcite * 2.5);
        if (p.progress >= 1.0) {
          p.progress = 0;
          p.edge = edgeList[Math.floor(Math.random() * edgeList.length)] || p.edge;
        }
        const p1 = p.edge.p1;
        const p2 = p.edge.p2;
        const pr = p.progress;
        pPos[i * 3] = p1.x + (p2.x - p1.x) * pr;
        pPos[i * 3 + 1] = p1.y + (p2.y - p1.y) * pr;
        pPos[i * 3 + 2] = p1.z + (p2.z - p1.z) * pr;
      }
      pulsePoints.geometry.attributes.position.needsUpdate = true;

      renderer.render(scene, camera);
    }

    animId = requestAnimationFrame(renderLoop);
  } catch (err) {
    console.warn('3D Brain initialization error:', err);
  }
})();
'''
print("Code parsed successfully, character count:", len(brain_js))

