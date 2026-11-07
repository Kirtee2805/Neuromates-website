/**
 * NEURO MATES — Shared Three.js Core Builders
 * Provides makeCore, makeDevices, and scene runner with:
 * - Pinned Three.js r128 compatibility
 * - MeshPhysicalMaterial with clearcoat (glossy look)
 * - SphereGeometry, TorusGeometry, TubeGeometry, CylinderGeometry, BoxGeometry
 * - AmbientLight + DirectionalLight + Aqua PointLight
 * - Pixel ratio capped at 1.5
 * - Auto-pausing via IntersectionObserver and Page Visibility API
 * - Still gradient fallback when 3D is unsupported or disabled
 */

(function () {
  'use strict';

  if (typeof THREE === 'undefined') {
    console.warn('Three.js r128 not loaded yet.');
    return;
  }

  const T = THREE;

  /**
   * Helper to create glossy physical material
   */
  function gl(color, opts = {}) {
    return new T.MeshPhysicalMaterial({
      color: new T.Color(color),
      roughness: opts.roughness !== undefined ? opts.roughness : 0.25,
      metalness: opts.metalness !== undefined ? opts.metalness : 0.1,
      clearcoat: opts.clearcoat !== undefined ? opts.clearcoat : 0.8,
      clearcoatRoughness: 0.15,
      transparent: opts.transparent || false,
      opacity: opts.opacity !== undefined ? opts.opacity : 1.0,
      emissive: opts.emissive ? new T.Color(opts.emissive) : new T.Color(0x000000),
      emissiveIntensity: opts.emissiveIntensity || 0,
      ...opts
    });
  }

  /**
   * Glossy teal core with white medical cross and wireframe sphere (as in Home)
   */
  function makeCore() {
    const g = new T.Group();

    // Inner glowing sphere
    const sphere = new T.Mesh(
      new T.SphereGeometry(0.62, 48, 32),
      gl('#0B8F8F', { emissive: '#0B7A7C', emissiveIntensity: 0.45, roughness: 0.2, clearcoat: 1.0 })
    );
    g.add(sphere);

    // Wireframe icosahedron shell
    const wireframe = new T.Mesh(
      new T.IcosahedronGeometry(0.82, 1),
      new T.MeshBasicMaterial({ color: 0xFFFFFF, wireframe: true, transparent: true, opacity: 0.4 })
    );
    g.add(wireframe);
    g.userData.wireframe = wireframe;

    // White medical cross on core
    const crossMat = gl('#FFFFFF', { roughness: 0.2, clearcoat: 0.9 });
    [[0.34, 0.1], [0.1, 0.34]].forEach(([w, h]) => {
      const crossPart = new T.Mesh(new T.BoxGeometry(w, h, 0.1), crossMat);
      crossPart.position.z = 0.6;
      g.add(crossPart);
    });

    return g;
  }

  /**
   * 4 condition-specific 3D devices (as in Home and Products)
   * Alzheimer's location tracker, Epilepsy headband, Parkinson's motion sensor, Rehabilitation muscle sensor pads
   */
  function makeDevices() {
    const navy = gl('#143E5C', { roughness: 0.55, clearcoat: 0.3 });
    const white = gl('#F7FBFB', { roughness: 0.2, clearcoat: 0.9 });
    const silver = gl('#C9D3DB', { metalness: 0.9, roughness: 0.2, clearcoat: 0.5 });
    const amber = gl('#F5B14C', { roughness: 0.3, clearcoat: 0.8 });
    const out = [];

    const el = (sx, sy, sz, x, y, z) => {
      const m = new T.Mesh(new T.SphereGeometry(1, 32, 20), white);
      m.scale.set(sx, sy, sz);
      m.position.set(x, y, z);
      return m;
    };
    const led = (color, x, y, z) => {
      const m = new T.Mesh(new T.SphereGeometry(0.035, 12, 8), new T.MeshBasicMaterial({ color: new T.Color(color) }));
      m.position.set(x, y, z);
      return m;
    };
    const tor = (R, r, rx, ry, mat = navy) => {
      const m = new T.Mesh(new T.TorusGeometry(R, r, 16, 48), mat);
      m.rotation.set(rx, ry, 0);
      return m;
    };

    // 0: Alzheimer's Location Tracker (arm/wrist band + casing + LED)
    let g0 = new T.Group();
    g0.name = 'device-alzheimers';
    g0.add(tor(0.3, 0.05, 0, 1.57), el(0.3, 0.24, 0.12, 0, 0, 0.32), led('#5BE7C4', 0, 0.13, 0.43));
    out.push(g0);

    // 1: Epilepsy Headband (wide band + sensor + silver reference electrode behind ear)
    let g1 = new T.Group();
    g1.name = 'device-epilepsy';
    g1.add(tor(0.46, 0.06, 1.57, 0), el(0.3, 0.12, 0.1, 0, 0, 0.46), led('#5BE7C4', 0.1, 0, 0.55));
    const sideDisc = new T.Mesh(new T.CylinderGeometry(0.07, 0.07, 0.03, 24), silver);
    sideDisc.position.set(0.46, -0.08, 0);
    sideDisc.rotation.z = 1.57;
    g1.add(sideDisc);
    out.push(g1);

    // 2: Parkinson's Wearable Motion Sensor (strap + module + LED)
    let g2 = new T.Group();
    g2.name = 'device-parkinsons';
    g2.add(tor(0.3, 0.09, 1.57, 0), el(0.22, 0.28, 0.09, 0, 0, 0.33), led('#5BE7C4', 0, 0.16, 0.41));
    out.push(g2);

    // 3: Paralysis Rehabilitation Muscle Sensors (3 white/amber discs + wires + teal board)
    let g3 = new T.Group();
    g3.name = 'device-rehabilitation';
    const pts = [];
    [[-0.22, 0.12], [0.22, 0.12], [0, -0.2]].forEach(([px, py]) => {
      const disc = new T.Mesh(new T.CylinderGeometry(0.14, 0.14, 0.03, 28), white);
      disc.rotation.x = 1.57;
      disc.position.set(px, py, 0);
      const innerAmber = new T.Mesh(new T.CylinderGeometry(0.06, 0.06, 0.04, 20), amber);
      innerAmber.rotation.x = 1.57;
      innerAmber.position.set(px, py, 0.01);
      g3.add(disc, innerAmber);
      pts.push(new T.Vector3(px, py, 0));
    });

    const board = new T.Mesh(new T.BoxGeometry(0.34, 0.14, 0.05), gl('#0B7A7C', { roughness: 0.3, clearcoat: 0.6 }));
    board.position.set(0, -0.55, 0);
    g3.add(board);

    pts.forEach(p => {
      const curve = new T.CatmullRomCurve3([
        p,
        new T.Vector3(p.x * 0.6, (p.y - 0.55) / 2, 0.08),
        new T.Vector3(p.x * 0.4, -0.5, 0)
      ]);
      g3.add(new T.Mesh(new T.TubeGeometry(curve, 12, 0.012, 6, false), amber));
    });
    out.push(g3);

    return out;
  }

  /**
   * Helper to initialize a Three.js scene with standard lighting, renderer,
   * pixel ratio cap, resize handling, and IntersectionObserver pause.
   */
  function initThreeScene({ canvas, cameraZ = 5, onRender = null, antialias = true, alpha = true }) {
    if (!canvas) return null;

    try {
      const renderer = new T.WebGLRenderer({
        canvas,
        alpha,
        antialias,
        powerPreference: 'high-performance'
      });
      // Cap pixel ratio at 1.5 as per instructions
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
      renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);

      const scene = new T.Scene();
      const camera = new T.PerspectiveCamera(40, canvas.clientWidth / canvas.clientHeight, 0.1, 100);
      camera.position.z = cameraZ;

      // Lights: AmbientLight + DirectionalLight + PointLight (aqua)
      const ambientLight = new T.AmbientLight(0xFFFFFF, 0.85);
      scene.add(ambientLight);

      const dirLight = new T.DirectionalLight(0xFFFFFF, 0.8);
      dirLight.position.set(5, 8, 6);
      scene.add(dirLight);

      const aquaPoint = new T.PointLight(0x7FD6D0, 1.4, 15);
      aquaPoint.position.set(-3, -2, 4);
      scene.add(aquaPoint);

      let isPaused = false;
      let reqId = null;
      const sceneData = {
        renderer,
        scene,
        camera,
        onRender: onRender
      };

      function resize() {
        const w = canvas.clientWidth;
        const h = canvas.clientHeight;
        if (!w || !h) return;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h, false);
      }
      window.addEventListener('resize', resize, { passive: true });

      function animate(time) {
        if (isPaused || document.hidden) {
          reqId = null;
          return;
        }
        const activeRender = sceneData.onRender || onRender;
        if (activeRender) activeRender({ time, scene, camera, renderer });
        renderer.render(scene, camera);
        reqId = requestAnimationFrame(animate);
      }

      function resume() {
        if (!reqId && !isPaused && !document.hidden) {
          reqId = requestAnimationFrame(animate);
        }
      }

      reqId = requestAnimationFrame(animate);

      // Pause rendering completely when canvas is offscreen
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          isPaused = !entry.isIntersecting;
          if (!isPaused) {
            resume();
          } else if (reqId) {
            cancelAnimationFrame(reqId);
            reqId = null;
          }
        });
      }, { threshold: 0.05 });
      observer.observe(canvas);

      // Pause rendering when tab is hidden
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          if (reqId) {
            cancelAnimationFrame(reqId);
            reqId = null;
          }
        } else if (!isPaused) {
          resume();
        }
      });

      sceneData.destroy = () => {
        if (reqId) cancelAnimationFrame(reqId);
        observer.disconnect();
        window.removeEventListener('resize', resize);
        renderer.dispose();
      };

      return sceneData;
    } catch (err) {
      console.warn('Three.js scene init failed, falling back to static gradient:', err);
      if (canvas) {
        canvas.style.display = 'none';
        const fallback = document.createElement('div');
        fallback.className = 'canvas-fallback';
        fallback.style.cssText = 'position:absolute;inset:0;background:radial-gradient(circle at center, rgba(127,214,208,0.25), transparent 70%);pointer-events:none;';
        canvas.parentNode.insertBefore(fallback, canvas);
      }
      return null;
    }
  }

  window.Neuro3D = {
    gl,
    makeCore,
    makeDevices,
    initThreeScene
  };
})();

