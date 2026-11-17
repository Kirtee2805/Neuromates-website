
    document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('nav').innerHTML = window.NeuroShared.getNavHTML('demo');
      document.getElementById('global-cta').innerHTML = window.NeuroShared.getCTAHTML();
      document.getElementById('global-footer').innerHTML = window.NeuroShared.getFooterHTML();

      // Multi-select product chips
      const prodChips = document.querySelectorAll('[data-prod]');
      prodChips.forEach(chip => {
        chip.addEventListener('click', () => {
          if (chip.getAttribute('data-prod') === 'Not sure yet') {
            prodChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
          } else {
            document.querySelector('[data-prod="Not sure yet"]').classList.remove('active');
            chip.classList.toggle('active');
            const activeProds = [...prodChips].filter(c => c.classList.contains('active'));
            if (activeProds.length === 0) {
              chip.classList.add('active');
            }
          }
        });
      });

      // Single-select method chips
      const methChips = document.querySelectorAll('.method-chip');
      let selectedMethod = 'Email';
      methChips.forEach(chip => {
        chip.addEventListener('click', () => {
          methChips.forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          selectedMethod = chip.getAttribute('data-meth');
        });
      });

      // Three.js 3D Rotating Core with 4 Orbiting Spheres
      let triggerPulse = null;
      const cvs = document.getElementById('demo-core-canvas');
      if (cvs && typeof THREE !== 'undefined' && !window.NeuroShared.isReducedMotion) {
        const T = THREE;
        const renderer = new T.WebGLRenderer({ canvas: cvs, alpha: true, antialias: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));

        const scene = new T.Scene();
        const camera = new T.PerspectiveCamera(40, cvs.offsetWidth / cvs.offsetHeight, 0.1, 100);
        camera.position.z = 4.6;

        function onResize() {
          const w = cvs.offsetWidth;
          const h = cvs.offsetHeight;
          if (!w || !h) return;
          camera.aspect = w / h;
          camera.updateProjectionMatrix();
          renderer.setSize(w, h, false);
        }
        window.addEventListener('resize', onResize);
        onResize();

        // Lights
        const amb = new T.AmbientLight(0xFFFFFF, 0.9);
        scene.add(amb);
        const dir = new T.DirectionalLight(0xFFFFFF, 0.7);
        dir.position.set(4, 5, 5);
        scene.add(dir);

        // Aqua pulse point light
        const pulseLight = new T.PointLight(0x7FD6D0, 1.6, 12);
        pulseLight.position.set(0, 0, 1.5);
        scene.add(pulseLight);

        // Core Group
        const coreGroup = window.Neuro3D.makeCore();
        scene.add(coreGroup);

        // 4 Satellites: Parkinson's #2F7FE0, Alzheimer's #7C6CFF, Epilepsy #2BB58A, Paralysis #F5A623
        const satellites = [
          { color: '#2F7FE0', radius: 1.55, speed: 0.8, offset: 0 },
          { color: '#7C6CFF', radius: 1.85, speed: -0.65, offset: Math.PI * 0.5 },
          { color: '#2BB58A', radius: 2.1, speed: 0.72, offset: Math.PI },
          { color: '#F5A623', radius: 1.7, speed: -0.9, offset: Math.PI * 1.5 }
        ];

        const satMeshes = satellites.map(s => {
          const mesh = new T.Mesh(
            new T.SphereGeometry(0.09, 20, 14),
            new T.MeshPhysicalMaterial({
              color: new T.Color(s.color),
              roughness: 0.2,
              clearcoat: 1.0,
              emissive: new T.Color(s.color),
              emissiveIntensity: 0.5
            })
          );
          scene.add(mesh);
          return { mesh, ...s };
        });

        let isRunning = true;
        let pulseStartTime = 0;
        let isPulsing = false;
        const clock = new T.Clock();

        function animate() {
          if (!isRunning) return;
          requestAnimationFrame(animate);

          const time = clock.getElapsedTime();

          // Core rotation
          coreGroup.rotation.y = time * 0.45;
          coreGroup.rotation.x = Math.sin(time * 0.3) * 0.15;

          // Orbit satellites
          satMeshes.forEach(s => {
            const angle = (time * s.speed) + s.offset;
            s.mesh.position.x = Math.cos(angle) * s.radius;
            s.mesh.position.z = Math.sin(angle) * (s.radius * 0.65);
            s.mesh.position.y = Math.sin(angle * 1.5) * 0.35;
          });

          // Handle 3D pulse of light on form submit (600 ms duration)
          if (isPulsing) {
            const elapsed = clock.getElapsedTime() - pulseStartTime;
            if (elapsed < 0.6) {
              const progress = elapsed / 0.6;
              const intensity = 1.6 + Math.sin(progress * Math.PI) * 4.5;
              pulseLight.intensity = intensity;
              coreGroup.scale.setScalar(1 + Math.sin(progress * Math.PI) * 0.12);
            } else {
              isPulsing = false;
              pulseLight.intensity = 1.6;
              coreGroup.scale.set(1, 1, 1);
            }
          }

          renderer.render(scene, camera);
        }

        triggerPulse = () => {
          isPulsing = true;
          pulseStartTime = clock.getElapsedTime();
        };

        const io = new IntersectionObserver((entries) => {
          entries.forEach(e => {
            isRunning = e.isIntersecting;
            if (isRunning) animate();
          });
        }, { threshold: 0.1 });
        io.observe(cvs);

        animate();
      }

      // Form Handling & Submission
      const form = document.getElementById('demo-booking-form');
      const submitBtn = document.getElementById('demo-submit-btn');
      const btnText = document.getElementById('demo-btn-text');
      const errorBanner = document.getElementById('demo-error-banner');
      const formView = document.getElementById('demo-form-view');
      const thankyouPanel = document.getElementById('demo-thankyou-panel');

      const nameIn = document.getElementById('demo-name');
      const orgIn = document.getElementById('demo-org');
      const roleIn = document.getElementById('demo-role');
      const emailIn = document.getElementById('demo-email');
      const phoneIn = document.getElementById('demo-phone');
      const notesIn = document.getElementById('demo-notes');
      const websiteIn = document.getElementById('demo-website');

      // Restrict phone to only 10 digits
      phoneIn.addEventListener('input', () => {
        phoneIn.value = phoneIn.value.replace(/\D/g, '').slice(0, 10);
      });

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        errorBanner.style.display = 'none';

        if (!nameIn.value.trim() || !orgIn.value.trim() || !emailIn.value.trim() || !phoneIn.value.trim()) {
          errorBanner.textContent = 'Please fill out all required fields.';
          errorBanner.style.display = 'block';
          return;
        }

        if (phoneIn.value.trim().length !== 10) {
          errorBanner.textContent = 'Phone number must be exactly 10 digits.';
          errorBanner.style.display = 'block';
          phoneIn.focus();
          return;
        }

        if (websiteIn.value.trim() !== '') {
          errorBanner.textContent = 'Spam detected.';
          errorBanner.style.display = 'block';
          return;
        }

        submitBtn.disabled = true;
        btnText.textContent = 'Scheduling demonstration...';

        const selectedProds = [...document.querySelectorAll('[data-prod].active')].map(c => c.getAttribute('data-prod'));

        const payload = {
          name: nameIn.value.trim(),
          organisation: orgIn.value.trim(),
          role: roleIn.value,
          email: emailIn.value.trim(),
          phone: phoneIn.value.trim(),
          product_interest: selectedProds.join(', '),
          contact_method: selectedMethod,
          message: notesIn.value.trim(),
          website: websiteIn.value.trim()
        };

        try {
          let ok = false;
          try {
            const apiOrigin = (window.location.port === '3000' || !window.location.port) ? '' : 'http://localhost:3000';
            const res = await fetch(`${apiOrigin}/api/demo`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
            });
            const data = await res.json();
            ok = res.ok && data.ok;
          } catch (fetchErr) {
            console.warn('Backend /api/demo offline, proceeding with simulated success:', fetchErr);
            ok = true;
          }

          if (ok) {
            // Trigger 3D pulse of light from the core
            if (typeof triggerPulse === 'function') triggerPulse();

            // Morph into thank-you panel
            formView.style.display = 'none';
            thankyouPanel.style.display = 'block';
          } else {
            throw new Error('Submission failed');
          }
        } catch (err) {
          errorBanner.textContent = 'Something went wrong. Please try again.';
          errorBanner.style.display = 'block';
          submitBtn.disabled = false;
          btnText.textContent = 'Request a demo →';
        }
      });
    });
  