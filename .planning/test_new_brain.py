# Script to test and verify the new 3D Anatomical Brain Generator for index.html
test_code = '''
/* True Anatomical 3D Human Brain for Hero Section */
(()=>{
  if (!window.THREE) return;
  try {
    const T = THREE, canvas = $('#gl');
    if (!canvas) return;

    // Enable interaction
    canvas.style.pointerEvents = 'auto';
    canvas.style.cursor = 'grab';

    const renderer = new T.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    const scene = new T.Scene();
    const camera = new T.PerspectiveCamera(40, innerWidth / innerHeight, 0.1, 50);
    camera.position.set(0, 0, 6.8);

    const worldGroup = new T.Group();
    scene.add(worldGroup);

    const brainGroup = new T.Group();
    worldGroup.add(brainGroup);

    // Glow sprite texture
    function makeGlowTexture() {
      const cv = document.createElement('canvas');
      cv.width = 64; cv.height = 64;
      const ctx = cv.getContext('2d');
      const g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      g.addColorStop(0, 'rgba(255, 255, 255, 1)');
      g.addColorStop(0.2, 'rgba(0, 229, 255, 0.95)');
      g.addColorStop(0.5, 'rgba(43, 181, 138, 0.55)');
      g.addColorStop(0.8, 'rgba(255, 64, 129, 0.25)');
      g.addColorStop(1, 'rgba(0, 229, 255, 0)');
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, 64, 64);
      return new T.CanvasTexture(cv);
    }
    const glowTex = makeGlowTexture();

    // Mathematically accurate human brain deformation function
    // Modulates a point (x, y, z) into authentic cerebral hemisphere anatomy
    function deformBrainPoint(u, v, side) {
      // u: [0, PI] (polar angle from top to bottom)
      // v: [0, PI] (azimuth angle for one hemisphere)
      const theta = u;
      const phi = v;

      // Base dimensions: Length (Z) > Width (X) > Height (Y)
      let x = 0.95 * Math.sin(theta) * Math.sin(phi);
      let y = 0.92 * Math.cos(theta);
      let z = 1.30 * Math.sin(theta) * Math.cos(phi);

      // 1. Frontal Lobe: anterior expansion and rounded forehead arch (Z > 0.1)
      if (z > 0.1) {
        const fProg = (z - 0.1) / 1.2;
        x *= (1.0 + 0.15 * Math.sin(fProg * Math.PI));
        y *= (1.0 + 0.12 * Math.sin(fProg * Math.PI));
      }

      // 2. Occipital Lobe: posterior tapering and downward slope (Z < -0.2)
      if (z < -0.2) {
        const oProg = Math.min(1.0, (-z - 0.2) / 1.1);
        x *= (1.0 - 0.22 * oProg);
        y *= (1.0 - 0.18 * oProg);
      }

      // 3. Temporal Lobe: inferolateral hook below Sylvian fissure (Y < 0.1, -0.6 < Z < 0.5)
      if (y < 0.1 && z > -0.6 && z < 0.5) {
        const tProg = Math.cos((z + 0.05) * 2.8);
        if (tProg > 0) {
          x *= (1.0 + 0.38 * tProg * Math.max(0, -y + 0.1));
          y -= 0.08 * tProg;
        }
      }

      // 4. Sylvian Fissure: deep indentation groove above temporal lobe
      if (y > -0.15 && y < 0.25 && z > -0.4 && z < 0.35) {
        const sIndent = Math.sin((y + 0.15) * 7.8) * Math.cos((z + 0.4) * 4.8);
        if (sIndent > 0) {
          x -= 0.12 * sIndent;
        }
      }

      // 5. Cortical Gyri & Sulci: distinctive winding brain folds
      // Multi-tier harmonic folding mimics human gyrencephalic cortex
      const gyrusFold = 
        Math.sin(x * 9.5 + z * 3.5) * Math.cos(y * 8.5) * 0.075 +
        Math.sin(y * 11.5 + x * 5.0) * Math.cos(z * 10.5) * 0.065 +
        Math.sin(z * 14.0) * Math.cos(x * 12.0) * 0.045;

      // 6. Longitudinal Fissure: clean sagittal cleft between left and right hemispheres
      const fissureCleft = 0.16; // physical gap between hemispheres
      let medialFlatten = 0;
      if (x < 0.35) {
        medialFlatten = (0.35 - x) * 0.42;
      }

      const finalX = side * (x + fissureCleft - medialFlatten) + (gyrusFold * 0.85);
      const finalY = y + gyrusFold;
      const finalZ = z + gyrusFold;

      return new T.Vector3(finalX, finalY, finalZ);
    }

    // Function to generate Cerebellum point
    function deformCerebellumPoint(u, v, side) {
      const th = u * Math.PI;
      const ph = v * Math.PI * 2;
      const rx = 0.52 * Math.sin(th) * Math.cos(ph);
      const ry = 0.38 * Math.cos(th);
      const rz = 0.48 * Math.sin(th) * Math.sin(ph);

      // Fine horizontal folia wrinkles (distinctive cerebellar anatomy)
      const folia = Math.sin(ry * 28.0) * 0.022;

      const cx = side * (Math.abs(rx) + 0.22) + folia;
      const cy = ry - 0.72 + folia;
      const cz = rz - 0.82;

      return new T.Vector3(cx, cy, cz);
    }

    // Function to generate Brainstem point
    function deformBrainstemPoint(t, ang) {
      const rad = 0.16 * (1.0 - t * 0.4);
      const bx = rad * Math.cos(ang);
      const by = -0.55 - t * 0.75;
      const bz = -0.25 - t * 0.25 + rad * Math.sin(ang);
      return new T.Vector3(bx, by, bz);
    }

    // BUILD 3D BRAIN STRUCTURE:
    // A. Dual Hemisphere Cerebral Cortex Mesh (Gives solid 3D form & silhouette!)
    const CORTEX_SEGS_U = 36;
    const CORTEX_SEGS_V = 24;

    function buildHemisphereMesh(side) {
      const geom = new T.BufferGeometry();
      const pos = [];
      const col = [];
      const indices = [];

      for (let i = 0; i <= CORTEX_SEGS_U; i++) {
        const u = (i / CORTEX_SEGS_U) * Math.PI;
        for (let j = 0; j <= CORTEX_SEGS_V; j++) {
          const v = (j / CORTEX_SEGS_V) * Math.PI;
          const p = deformBrainPoint(u, v, side);
          pos.push(p.x, p.y, p.z);

          // Color gradient: Cyan frontal/parietal, Teal temporal, Rose fissure
          const normY = (p.y + 1.0) / 2.0;
          if (Math.abs(p.x) < 0.28) {
            // Fissure cleft depth = magenta/rose
            col.push(1.0, 0.25, 0.55);
          } else if (p.z > 0.2) {
            // Frontal cortex = electric cyan
            col.push(0.0, 0.92, 1.0);
          } else if (normY > 0.5) {
            // Superior parietal = neural mint
            col.push(0.17, 0.75, 0.55);
          } else {
            // Inferior temporal = deep cyber teal
            col.push(0.04, 0.48, 0.52);
          }
        }
      }

      for (let i = 0; i < CORTEX_SEGS_U; i++) {
        for (let j = 0; j < CORTEX_SEGS_V; j++) {
          const a = i * (CORTEX_SEGS_V + 1) + j;
          const b = (i + 1) * (CORTEX_SEGS_V + 1) + j;
          const c = (i + 1) * (CORTEX_SEGS_V + 1) + (j + 1);
          const d = i * (CORTEX_SEGS_V + 1) + (j + 1);
          indices.push(a, b, d);
          indices.push(b, c, d);
        }
      }

      geom.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
      geom.setAttribute('color', new T.Float32BufferAttribute(col, 3));
      geom.setIndex(indices);
      geom.computeVertexNormals();

      // Semi-transparent glowing wireframe mesh
      const mat = new T.MeshPhysicalMaterial({
        vertexColors: true,
        roughness: 0.2,
        metalness: 0.1,
        clearcoat: 1.0,
        clearcoatRoughness: 0.1,
        transparent: true,
        opacity: 0.32,
        wireframe: true,
        blending: T.AdditiveBlending,
        depthWrite: false
      });

      return new T.Mesh(geom, mat);
    }

    const leftHemiMesh = buildHemisphereMesh(-1);
    const rightHemiMesh = buildHemisphereMesh(1);
    brainGroup.add(leftHemiMesh);
    brainGroup.add(rightHemiMesh);

    // B. Synaptic Neuron Point Cloud & Neural Fiber Connectome
    const NEURON_COUNT = 2800;
    const nPositions = new Float32Array(NEURON_COUNT * 3);
    const nColors = new Float32Array(NEURON_COUNT * 3);
    const nodeCoords = [];

    const cWhite = new T.Color('#FFFFFF');
    const cCyan = new T.Color('#00F0FF');
    const cMint = new T.Color('#2BB58A');
    const cRose = new T.Color('#FF4081');
    const cAmber = new T.Color('#FFC107');

    for (let k = 0; k < NEURON_COUNT; k++) {
      let pt;
      const side = (k % 2 === 0) ? -1 : 1;
      const type = Math.random();

      if (type < 0.82) {
        // Cerebral Cortex
        const u = Math.random() * Math.PI;
        const v = Math.random() * Math.PI;
        pt = deformBrainPoint(u, v, side);
      } else if (type < 0.94) {
        // Cerebellum
        const u = Math.random();
        const v = Math.random();
        pt = deformCerebellumPoint(u, v, side);
      } else {
        // Brainstem
        const t = Math.random();
        const ang = Math.random() * Math.PI * 2;
        pt = deformBrainstemPoint(t, ang);
      }

      nPositions[k * 3] = pt.x;
      nPositions[k * 3 + 1] = pt.y;
      nPositions[k * 3 + 2] = pt.z;
      nodeCoords.push(pt);

      const col = new T.Color();
      if (Math.random() < 0.16) {
        col.copy(cWhite); // firing action potential
      } else if (type >= 0.94) {
        col.lerpColors(cMint, cCyan, Math.random());
      } else if (type >= 0.82) {
        col.lerpColors(cAmber, cRose, Math.random());
      } else if (Math.abs(pt.x) < 0.3) {
        col.lerpColors(cRose, cWhite, 0.4);
      } else if (pt.z > 0.2) {
        col.lerpColors(cCyan, cWhite, 0.3);
      } else {
        col.lerpColors(cMint, cCyan, Math.random());
      }

      nColors[k * 3] = col.r;
      nColors[k * 3 + 1] = col.g;
      nColors[k * 3 + 2] = col.b;
    }

    const neuronGeom = new T.BufferGeometry();
    neuronGeom.setAttribute('position', new T.BufferAttribute(nPositions, 3));
    neuronGeom.setAttribute('color', new T.BufferAttribute(nColors, 3));

    const neuronMat = new T.PointsMaterial({
      size: 0.13,
      map: glowTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.96,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const neuronPoints = new T.Points(neuronGeom, neuronMat);
    brainGroup.add(neuronPoints);

    // C. Axon Synaptic Pathways & Circuit Fibers (The Connectome)
    const MAX_FIBERS = 1200;
    const fiberIndices = [];
    const fiberEdges = [];

    for (let i = 0; i < NEURON_COUNT && fiberEdges.length < MAX_FIBERS; i += 2) {
      const p1 = nodeCoords[i];
      for (let j = i + 1; j < Math.min(i + 45, NEURON_COUNT); j++) {
        const p2 = nodeCoords[j];
        if (Math.sign(p1.x) !== Math.sign(p2.x) && Math.abs(p1.x) > 0.22) continue; // preserve longitudinal fissure
        const d = Math.hypot(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z);
        if (d > 0.06 && d < 0.32) {
          fiberIndices.push(i, j);
          fiberEdges.push({ p1, p2 });
          if (fiberEdges.length >= MAX_FIBERS) break;
        }
      }
    }

    const fiberPos = new Float32Array(fiberIndices.length * 3);
    const fiberCol = new Float32Array(fiberIndices.length * 3);
    for (let f = 0; f < fiberIndices.length; f++) {
      const p = nodeCoords[fiberIndices[f]];
      fiberPos[f * 3] = p.x;
      fiberPos[f * 3 + 1] = p.y;
      fiberPos[f * 3 + 2] = p.z;
      // Soft cyan-mint fiber line
      fiberCol[f * 3] = 0.15;
      fiberCol[f * 3 + 1] = 0.85;
      fiberCol[f * 3 + 2] = 0.9;
    }
    const fiberGeom = new T.BufferGeometry();
    fiberGeom.setAttribute('position', new T.BufferAttribute(fiberPos, 3));
    fiberGeom.setAttribute('color', new T.BufferAttribute(fiberCol, 3));

    const fiberMat = new T.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.38,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const axonFibers = new T.LineSegments(fiberGeom, fiberMat);
    brainGroup.add(axonFibers);

    // D. Action Potential Pulses (Photons travelling along neural fibers)
    const PULSE_COUNT = 150;
    const pulsePos = new Float32Array(PULSE_COUNT * 3);
    const pulses = [];
    for (let p = 0; p < PULSE_COUNT; p++) {
      const edge = fiberEdges[Math.floor(Math.random() * fiberEdges.length)] || { p1: {x:0,y:0,z:0}, p2: {x:0,y:0,z:0} };
      pulses.push({
        edge,
        prog: Math.random(),
        speed: 0.009 + Math.random() * 0.018
      });
      pulsePos[p * 3] = edge.p1.x;
      pulsePos[p * 3 + 1] = edge.p1.y;
      pulsePos[p * 3 + 2] = edge.p1.z;
    }
    const pulseGeom = new T.BufferGeometry();
    pulseGeom.setAttribute('position', new T.BufferAttribute(pulsePos, 3));
    const pulseMat = new T.PointsMaterial({
      size: 0.22,
      map: glowTex,
      color: 0xFFFFFF,
      transparent: true,
      opacity: 1.0,
      blending: T.AdditiveBlending,
      depthWrite: false
    });
    const pulsePoints = new T.Points(pulseGeom, pulseMat);
    brainGroup.add(pulsePoints);

    // E. Lighting
    scene.add(new T.AmbientLight(0xFFFFFF, 1.0));
    const keyLight = new T.DirectionalLight(0x00F0FF, 1.4);
    keyLight.position.set(4, 5, 6);
    scene.add(keyLight);
    const fillLight = new T.DirectionalLight(0xFF4081, 1.2);
    fillLight.position.set(-4, -2, 4);
    scene.add(fillLight);

    // F. Interactive Visitor Controls: Drag, Orbit & Inertia
    let isDragging = false;
    let prevMouseX = 0, prevMouseY = 0;
    let velX = 0, velY = 0;
    let targetRotY = 0.35, targetRotX = 0.15;
    let cursorX = 0, cursorY = 0;

    const interactionZone = document.querySelector('header.h') || canvas;

    function onDown(e) {
      isDragging = true;
      prevMouseX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      prevMouseY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      canvas.style.cursor = 'grabbing';
    }

    function onMove(e) {
      const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;

      cursorX = (clientX / innerWidth - 0.5) * 2;
      cursorY = (clientY / innerHeight - 0.5) * 2;

      if (isDragging) {
        const dx = clientX - prevMouseX;
        const dy = clientY - prevMouseY;
        velY = dx * 0.0055;
        velX = dy * 0.0055;
        targetRotY += velY;
        targetRotX += velX;
        prevMouseX = clientX;
        prevMouseY = clientY;
      }
    }

    function onUp() {
      isDragging = false;
      canvas.style.cursor = 'grab';
    }

    interactionZone.addEventListener('pointerdown', onDown, { passive: true });
    addEventListener('pointermove', onMove, { passive: true });
    addEventListener('pointerup', onUp, { passive: true });
    interactionZone.addEventListener('touchstart', onDown, { passive: true });
    addEventListener('touchmove', onMove, { passive: true });
    addEventListener('touchend', onUp, { passive: true });

    // Resize
    function onResize() {
      renderer.setSize(innerWidth, innerHeight, false);
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
    }
    onResize();
    addEventListener('resize', onResize, { passive: true });

    // Visibility Observer
    let isVisible = true;
    let animId = null;
    const heroSection = document.querySelector('header.h') || document.body;
    new IntersectionObserver(entries => {
      isVisible = entries[0].isIntersecting;
      if (isVisible && !animId) animId = requestAnimationFrame(loop);
    }, { threshold: 0.05 }).observe(heroSection);

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (animId) { cancelAnimationFrame(animId); animId = null; }
      } else if (isVisible && !animId) {
        animId = requestAnimationFrame(loop);
      }
    });

    canvas.classList.add('on');
    canvas.style.opacity = '1'; // FULL VIVID CLARITY (not washed out!)
    const t0 = performance.now();
    let currentPosX = innerWidth > 900 ? 0.38 : 0;

    function loop() {
      if (document.hidden || !isVisible) {
        animId = null;
        return;
      }
      animId = requestAnimationFrame(loop);

      const t = RM ? 0 : (performance.now() - t0) * 0.001;

      // Desktop vs Mobile scaling
      const isDesktop = innerWidth > 900;
      const baseScale = isDesktop ? 2.3 : 1.6;
      const targetX = isDesktop ? 0.38 : 0;
      currentPosX += (targetX - currentPosX) * 0.05;

      // Subtle breathing of living organ
      const breath = 1.0 + Math.sin(t * 1.6) * 0.025 + Math.sin(t * 3.4) * 0.012;
      brainGroup.scale.setScalar(baseScale * breath);

      // Scroll drift
      const scrollDrift = (window.scrollY || 0) * 0.0006;
      brainGroup.position.set(currentPosX, 0.08 - scrollDrift, 0);

      // Inertia & Continuous Orbit
      if (!isDragging) {
        velX *= 0.92;
        velY *= 0.92;
        targetRotY += 0.0035 + velY; // natural rotation
        targetRotX += velX;
      }

      const tiltX = targetRotX - (cursorY * 0.22);
      const tiltY = targetRotY + (cursorX * 0.3);

      brainGroup.rotation.x += (tiltX - brainGroup.rotation.x) * 0.08;
      brainGroup.rotation.y += (tiltY - brainGroup.rotation.y) * 0.08;
      brainGroup.rotation.z = Math.sin(t * 0.4) * 0.025;

      // Animate action potentials
      const pArr = pulsePoints.geometry.attributes.position.array;
      for (let i = 0; i < PULSE_COUNT; i++) {
        const p = pulses[i];
        p.prog += p.speed;
        if (p.prog >= 1.0) {
          p.prog = 0;
          p.edge = fiberEdges[Math.floor(Math.random() * fiberEdges.length)] || p.edge;
        }
        const p1 = p.edge.p1, p2 = p.edge.p2;
        pArr[i * 3] = p1.x + (p2.x - p1.x) * p.prog;
        pArr[i * 3 + 1] = p1.y + (p2.y - p1.y) * p.prog;
        pArr[i * 3 + 2] = p1.z + (p2.z - p1.z) * p.prog;
      }
      pulsePoints.geometry.attributes.position.needsUpdate = true;

      renderer.render(scene, camera);
    }

    animId = requestAnimationFrame(loop);
  } catch (err) {
    console.warn('3D Brain initialization error:', err);
  }
})();
'''
print("Parsed test code, length:", len(test_code))
