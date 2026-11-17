# Test 3D Brain Telemetry Animation for register-demo.html
demo_brain_js = '''
      // --- INNOVATIVE 3D INTERACTIVE NEUROLOGICAL TELEMETRY MODEL ---
      const cvs = document.getElementById('demo-core-canvas');
      if (cvs && typeof THREE !== 'undefined' && !window.NeuroShared.isReducedMotion) {
        const T = THREE;
        const renderer = new T.WebGLRenderer({ canvas: cvs, alpha: true, antialias: true, powerPreference: 'high-performance' });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

        const scene = new T.Scene();
        const camera = new T.PerspectiveCamera(42, cvs.offsetWidth / cvs.offsetHeight, 0.1, 100);
        camera.position.set(0, 0, 5.2);

        function onResize() {
          const w = cvs.offsetWidth;
          const h = cvs.offsetHeight;
          if (!w || !h) return;
          camera.aspect = w / h;
          camera.updateProjectionMatrix();
          renderer.setSize(w, h, false);
        }
        window.addEventListener('resize', onResize, { passive: true });
        onResize();

        const rootGroup = new T.Group();
        scene.add(rootGroup);

        const brainGroup = new T.Group();
        rootGroup.add(brainGroup);

        // Circular glow particle texture
        function createGlowSprite() {
          const c = document.createElement('canvas');
          c.width = 64; c.height = 64;
          const ctx = c.getContext('2d');
          const g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
          g.addColorStop(0, 'rgba(255, 255, 255, 1)');
          g.addColorStop(0.25, 'rgba(127, 214, 208, 0.9)');
          g.addColorStop(0.55, 'rgba(43, 181, 138, 0.45)');
          g.addColorStop(0.85, 'rgba(11, 122, 124, 0.15)');
          g.addColorStop(1, 'rgba(11, 122, 124, 0)');
          ctx.fillStyle = g;
          ctx.fillRect(0, 0, 64, 64);
          return new T.CanvasTexture(c);
        }
        const glowTex = createGlowSprite();

        // 1. Generate 3D Anatomical Human Brain Nodes (Left & Right Hemispheres)
        const NODE_COUNT = 1600;
        const positions = new Float32Array(NODE_COUNT * 3);
        const colors = new Float32Array(NODE_COUNT * 3);
        const baseNodes = [];

        // Condition Telemetry Colors
        const conditionColors = [
          new T.Color('#2F7FE0'), // Parkinson's (Blue)
          new T.Color('#7C6CFF'), // Alzheimer's (Violet)
          new T.Color('#2BB58A'), // Epilepsy (Mint)
          new T.Color('#F5A623')  // Paralysis (Gold)
        ];
        const colTeal = new T.Color('#7FD6D0');
        const colWhite = new T.Color('#FFFFFF');

        for (let i = 0; i < NODE_COUNT; i++) {
          const side = (i % 2 === 0) ? -1 : 1;
          const u = Math.random();
          const v = Math.random();
          const theta = u * Math.PI;
          const phi = v * Math.PI;

          // Anatomical brain dimensions
          let bx = 0.88 * Math.sin(theta) * Math.sin(phi);
          let by = 0.92 * Math.cos(theta);
          let bz = 1.25 * Math.sin(theta) * Math.cos(phi);

          // Frontal lobe expansion
          if (bz > 0.15) {
            bx *= 1.08;
            by *= 1.05;
          }
          // Temporal lobe bulge
          if (by < 0.05 && Math.abs(bz) < 0.5) {
            bx *= 1.22;
          }
          // Cerebellum
          if (by < -0.25 && bz < -0.2) {
            bx *= 0.78;
            by -= 0.12;
            bz *= 0.88;
          }

          // Gyri & sulci cortical convolutions
          const gyri = 
            Math.sin(bx * 8.0) * Math.cos(by * 7.0) * 0.06 +
            Math.sin(by * 9.5) * Math.cos(bz * 8.5) * 0.045;

          // Longitudinal fissure cleft
          let fissure = 0;
          if (Math.abs(bx) < 0.3) {
            fissure = (0.3 - Math.abs(bx)) * 0.28;
          }

          const x = side * (Math.abs(bx) + 0.12) + (bx / (Math.abs(bx) || 1)) * (gyri - fissure);
          const y = by + gyri;
          const z = bz + gyri;

          positions[i * 3] = x;
          positions[i * 3 + 1] = y;
          positions[i * 3 + 2] = z;
          baseNodes.push({ x, y, z, side });

          // Color distribution representing neural activity
          const c = new T.Color();
          if (Math.random() < 0.12) {
            c.copy(colWhite);
          } else {
            // Assign to condition quadrants
            const condIdx = Math.floor(Math.random() * 4);
            c.lerpColors(conditionColors[condIdx], colTeal, 0.45);
          }

          colors[i * 3] = c.r;
          colors[i * 3 + 1] = c.g;
          colors[i * 3 + 2] = c.b;
        }

        const brainGeom = new T.BufferGeometry();
        brainGeom.setAttribute('position', new T.BufferAttribute(positions, 3));
        brainGeom.setAttribute('color', new T.BufferAttribute(colors, 3));

        const brainMat = new T.PointsMaterial({
          size: 0.13,
          map: glowTex,
          vertexColors: true,
          transparent: true,
          opacity: 0.92,
          blending: T.AdditiveBlending,
          depthWrite: false
        });
        const brainPoints = new T.Points(brainGeom, brainMat);
        brainGroup.add(brainPoints);

        // 2. Synaptic Neural Connectome Lines
        const lineIndices = [];
        const lineList = [];
        for (let i = 0; i < NODE_COUNT; i += 2) {
          const p1 = baseNodes[i];
          for (let j = i + 1; j < Math.min(i + 30, NODE_COUNT); j++) {
            const p2 = baseNodes[j];
            if (p1.side !== p2.side) continue;
            const d = Math.hypot(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z);
            if (d > 0.06 && d < 0.28) {
              lineIndices.push(i, j);
              lineList.push({ p1, p2 });
              if (lineList.length >= 800) break;
            }
          }
          if (lineList.length >= 800) break;
        }

        const linePos = new Float32Array(lineIndices.length * 3);
        const lineCol = new Float32Array(lineIndices.length * 3);
        for (let k = 0; k < lineIndices.length; k++) {
          const pt = baseNodes[lineIndices[k]];
          linePos[k * 3] = pt.x;
          linePos[k * 3 + 1] = pt.y;
          linePos[k * 3 + 2] = pt.z;
          lineCol[k * 3] = 0.3;
          lineCol[k * 3 + 1] = 0.75;
          lineCol[k * 3 + 2] = 0.8;
        }
        const lineGeom = new T.BufferGeometry();
        lineGeom.setAttribute('position', new T.BufferAttribute(linePos, 3));
        lineGeom.setAttribute('color', new T.BufferAttribute(lineCol, 3));

        const lineMat = new T.LineBasicMaterial({
          vertexColors: true,
          transparent: true,
          opacity: 0.22,
          blending: T.AdditiveBlending,
          depthWrite: false
        });
        const brainLines = new T.LineSegments(lineGeom, lineMat);
        brainGroup.add(brainLines);

        // 3. 4 Clinical Condition Telemetry Sensor Beacons
        const conditionBeacons = [
          { name: "Parkinson's", color: 0x2F7FE0, pos: new T.Vector3(-0.9, 0.45, 0.35) },
          { name: "Alzheimer's", color: 0x7C6CFF, pos: new T.Vector3(0.9, 0.45, -0.35) },
          { name: "Epilepsy", color: 0x2BB58A, pos: new T.Vector3(0.85, -0.3, 0.4) },
          { name: "Paralysis", color: 0xF5A623, pos: new T.Vector3(-0.85, -0.3, -0.4) }
        ];

        const beaconGroup = new T.Group();
        brainGroup.add(beaconGroup);

        const beaconMeshes = conditionBeacons.map(b => {
          const m = new T.Mesh(
            new T.SphereGeometry(0.09, 20, 16),
            new T.MeshPhysicalMaterial({
              color: b.color,
              emissive: b.color,
              emissiveIntensity: 0.85,
              roughness: 0.1,
              clearcoat: 1.0
            })
          );
          m.position.copy(b.pos);
          beaconGroup.add(m);

          // Glowing pulse ring
          const ringGeom = new T.RingGeometry(0.12, 0.15, 32);
          const ringMat = new T.MeshBasicMaterial({
            color: b.color,
            side: T.DoubleSide,
            transparent: true,
            opacity: 0.65
          });
          const ring = new T.Mesh(ringGeom, ringMat);
          ring.position.copy(b.pos);
          beaconGroup.add(ring);

          return { mesh: m, ring, basePos: b.pos.clone(), color: b.color };
        });

        // 4. Action Potential Impulses (Traveling sparks)
        const PULSE_COUNT = 90;
        const pulsePos = new Float32Array(PULSE_COUNT * 3);
        const pulses = [];
        for (let i = 0; i < PULSE_COUNT; i++) {
          const edge = lineList[Math.floor(Math.random() * lineList.length)] || { p1: {x:0,y:0,z:0}, p2: {x:0,y:0,z:0} };
          pulses.push({
            edge,
            prog: Math.random(),
            speed: 0.01 + Math.random() * 0.02
          });
          pulsePos[i * 3] = edge.p1.x;
          pulsePos[i * 3 + 1] = edge.p1.y;
          pulsePos[i * 3 + 2] = edge.p1.z;
        }
        const pulseGeom = new T.BufferGeometry();
        pulseGeom.setAttribute('position', new T.BufferAttribute(pulsePos, 3));
        const pulseMat = new T.PointsMaterial({
          size: 0.22,
          map: glowTex,
          color: 0xFFFFFF,
          transparent: true,
          opacity: 0.95,
          blending: T.AdditiveBlending,
          depthWrite: false
        });
        const pulsePoints = new T.Points(pulseGeom, pulseMat);
        brainGroup.add(pulsePoints);

        // 5. Lighting
        scene.add(new T.AmbientLight(0xFFFFFF, 0.85));
        const dirLight = new T.DirectionalLight(0x7FD6D0, 1.2);
        dirLight.position.set(3, 4, 5);
        scene.add(dirLight);

        // 6. Interactive Drag & Orbit Controls
        let isDragging = false;
        let prevMouseX = 0, prevMouseY = 0;
        let velX = 0, velY = 0;
        let rotY = 0.4, rotX = 0.15;
        let hoverX = 0, hoverY = 0;

        cvs.style.cursor = 'grab';

        function onPointerDown(e) {
          isDragging = true;
          cvs.style.cursor = 'grabbing';
          prevMouseX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
          prevMouseY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
        }

        function onPointerMove(e) {
          const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
          const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
          const rect = cvs.getBoundingClientRect();
          hoverX = ((clientX - rect.left) / rect.width - 0.5) * 2;
          hoverY = ((clientY - rect.top) / rect.height - 0.5) * 2;

          if (isDragging) {
            const dx = clientX - prevMouseX;
            const dy = clientY - prevMouseY;
            velY = dx * 0.006;
            velX = dy * 0.006;
            rotY += velY;
            rotX += velX;
            prevMouseX = clientX;
            prevMouseY = clientY;
          }
        }

        function onPointerUp() {
          isDragging = false;
          cvs.style.cursor = 'grab';
        }

        cvs.addEventListener('pointerdown', onPointerDown, { passive: true });
        window.addEventListener('pointermove', onPointerMove, { passive: true });
        window.addEventListener('pointerup', onPointerUp, { passive: true });
        cvs.addEventListener('touchstart', onPointerDown, { passive: true });
        window.addEventListener('touchmove', onPointerMove, { passive: true });
        window.addEventListener('touchend', onPointerUp, { passive: true });

        // Click on product interest chips triggers beacon focus
        const prodChips = document.querySelectorAll('[data-prod]');
        prodChips.forEach((chip, idx) => {
          chip.addEventListener('click', () => {
            if (beaconMeshes[idx]) {
              beaconMeshes[idx].mesh.scale.set(2, 2, 2);
              setTimeout(() => beaconMeshes[idx].mesh.scale.set(1, 1, 1), 600);
            }
          });
        });

        // Animation Loop
        let animId = null;
        const clock = new T.Clock();

        function render() {
          animId = requestAnimationFrame(render);
          const delta = clock.getDelta();
          const t = clock.getElapsedTime();

          // Continuous gentle rotation with inertia
          if (!isDragging) {
            velX *= 0.92;
            velY *= 0.92;
            rotY += 0.004 + velY;
            rotX += velX;
          }

          // Gentle breathing pulsation
          const breath = 1.0 + Math.sin(t * 1.8) * 0.025;
          brainGroup.scale.setScalar(1.4 * breath);

          // Tilt towards cursor
          const targetRotX = rotX - (hoverY * 0.2);
          const targetRotY = rotY + (hoverX * 0.3);
          brainGroup.rotation.x += (targetRotX - brainGroup.rotation.x) * 0.08;
          brainGroup.rotation.y += (targetRotY - brainGroup.rotation.y) * 0.08;
          brainGroup.rotation.z = Math.sin(t * 0.5) * 0.02;

          // Pulse condition beacon rings
          beaconMeshes.forEach((b, i) => {
            const scale = 1.0 + Math.sin(t * 3.0 + i) * 0.25;
            b.ring.scale.set(scale, scale, scale);
            b.ring.lookAt(camera.position);
          });

          // Action potential spark animation
          const pPositions = pulsePoints.geometry.attributes.position.array;
          for (let i = 0; i < PULSE_COUNT; i++) {
            const p = pulses[i];
            p.prog += p.speed;
            if (p.prog >= 1.0) {
              p.prog = 0;
              p.edge = lineList[Math.floor(Math.random() * lineList.length)] || p.edge;
            }
            const p1 = p.edge.p1;
            const p2 = p.edge.p2;
            pPositions[i * 3] = p1.x + (p2.x - p1.x) * p.prog;
            pPositions[i * 3 + 1] = p1.y + (p2.y - p1.y) * p.prog;
            pPositions[i * 3 + 2] = p1.z + (p2.z - p1.z) * p.prog;
          }
          pulsePoints.geometry.attributes.position.needsUpdate = true;

          renderer.render(scene, camera);
        }
        render();
      }
'''
print("Animation script parsed, character length:", len(demo_brain_js))
