/**
 * NEURO MATES — Shared Core Script
 * Handles navigation, dropdowns, Care Line progress, Lenis smooth scrolling,
 * and page transitions.
 */

(function () {
  'use strict';

  const $ = (s, p = document) => p.querySelector(s);
  const $$ = (s, p = document) => [...p.querySelectorAll(s)];
  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Determine root path prefix based on directory depth
  const path = window.location.pathname.replace(/\\/g, '/');
  const isSubdir = path.includes('/technology/') || path.includes('/insights/') || path.includes('/about/');
  const root = isSubdir ? '../' : './';

  // 1. Care Line: 3px progress indicator at left edge
  function initCareLine() {
    let care = $('#care');
    if (!care) {
      care = document.createElement('div');
      care.id = 'care';
      document.body.prepend(care);
    }

    if (isReducedMotion) {
      care.style.display = 'none';
      return;
    }

    let ticking = false;
    function updateCareLine() {
      if (!ticking) {
        requestAnimationFrame(() => {
          const h = document.documentElement;
          const st = window.scrollY || h.scrollTop;
          const sh = h.scrollHeight - h.clientHeight;
          const progress = sh > 0 ? (st / sh) * 100 : 0;
          care.style.height = `${progress}vh`;
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', updateCareLine, { passive: true });
    updateCareLine();
  }

  // 2. Navbar: Sticky elevation & Mobile menu toggle
  function initNav() {
    const nav = $('#nav');
    if (!nav) return;

    // Sticky shadow toggle with RAF throttling
    let navTicking = false;
    function onScroll() {
      if (!navTicking) {
        requestAnimationFrame(() => {
          if (window.scrollY > 20) {
            nav.classList.add('s');
          } else {
            nav.classList.remove('s');
          }
          navTicking = false;
        });
        navTicking = true;
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Mobile menu button with outside-click closing
    const mb = $('#mb');
    if (mb) {
      mb.setAttribute('aria-expanded', 'false');
      mb.onclick = (e) => {
        e.stopPropagation();
        const isOpen = nav.classList.toggle('o');
        mb.setAttribute('aria-expanded', String(isOpen));
        mb.textContent = isOpen ? 'Close' : 'Menu';
      };
      document.addEventListener('click', (e) => {
        if (nav.classList.contains('o') && !nav.contains(e.target)) {
          nav.classList.remove('o');
          mb.setAttribute('aria-expanded', 'false');
          mb.textContent = 'Menu';
        }
      });
    }

    // Keyboard support for dropdowns
    $$('.dd', nav).forEach(dd => {
      const trigger = dd.querySelector(':scope > a');
      const menu = dd.querySelector(':scope > div');
      if (!trigger || !menu) return;

      trigger.setAttribute('aria-haspopup', 'true');
      trigger.setAttribute('aria-expanded', 'false');

      dd.addEventListener('focusin', () => trigger.setAttribute('aria-expanded', 'true'));
      dd.addEventListener('focusout', (e) => {
        if (!dd.contains(e.relatedTarget)) {
          trigger.setAttribute('aria-expanded', 'false');
        }
      });

      dd.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          trigger.setAttribute('aria-expanded', 'false');
          trigger.focus();
        }
      });
    });

    // Highlight active menu item based on current URL
    const curPath = window.location.pathname;
    $$('nav ul a').forEach(a => {
      const href = a.getAttribute('href');
      if (href && href !== '#' && !href.startsWith('http') && curPath.endsWith(href.replace('../', '').replace('./', ''))) {
        a.closest('li')?.classList.add('active');
      }
    });
  }

  // 3. Back to Top & Footer Observer
  function initFooterObserver() {
    const footer = document.querySelector('footer');
    if (!footer) return;
    footer.classList.add('nm-footer');
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      footer.classList.add('footer-in-view');
    } else {
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          footer.classList.add('footer-in-view');
          observer.disconnect();
        }
      }, { threshold: 0.1 });
      observer.observe(footer);
    }
    footer.addEventListener('click', (e) => {
      const topBtn = e.target.closest('.nm-footer-back-to-top');
      if (topBtn) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  }

  function initBackToTop() {
    const topBtn = $('footer a.top, footer .nm-footer-back-to-top');
    if (topBtn) {
      topBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: isReducedMotion ? 'auto' : 'smooth' });
      });
    }
  }

  // 4. Smooth Scrolling: Use native 60fps/120fps hardware-accelerated scrolling
  function initSmoothScroll() {
    // Disable virtual-scroll hijacking to ensure 0ms input latency and zero scroll lag
    return;
  }

  // 5. Shared Navbar Generator / Normalizer (if markup needs standardizing)
  window.NeuroShared = {
    root,
    isReducedMotion,
    getNavHTML: function (activeGroup = '') {
      return `
        <a class="lg" href="${root}index.html" aria-label="Neuro Mates Home">
          <img src="${root}assets/images/logo.png" alt="Neuro Mates">
        </a>
        <button id="mb" aria-label="Toggle menu">Menu</button>
        <ul>
          <li class="dd ${activeGroup === 'products' ? 'active' : ''}">
            <a href="${root}neuromates-products.html#overview">Products</a>
            <div>
              <a href="${root}neuromates-products.html#overview">Products Overview</a>
              <a href="${root}neuromates-products.html#parkinsons-care">Parkinson’s Care</a>
              <a href="${root}neuromates-products.html#alzheimers-care">Alzheimer’s Care</a>
              <a href="${root}neuromates-products.html#epilepsy-care">Epilepsy Care</a>
              <a href="${root}neuromates-products.html#paralysis-care">Paralysis Care</a>
            </div>
          </li>
          <li class="dd ${activeGroup === 'technology' ? 'active' : ''}">
            <a href="${root}technology/index.html">Technology</a>
            <div>
              <a href="${root}technology/index.html">Technology Overview</a>
              <a href="${root}technology/connected-devices.html">Connected Devices</a>
              <a href="${root}technology/ai-machine-learning.html">AI &amp; Machine Learning</a>
              <a href="${root}technology/monitoring-analytics.html">Monitoring &amp; Analytics</a>
              <a href="${root}technology/connected-care-platform.html">Connected Care Platform</a>
            </div>
          </li>
          <li class="dd ${activeGroup === 'insights' ? 'active' : ''}">
            <a href="${root}insights/index.html">Insights</a>
            <div>
              <a href="${root}insights/index.html">Insights Overview</a>
              <a href="${root}insights/research.html">Research</a>
              <a href="${root}insights/resources.html">Resources</a>
            </div>
          </li>
          <li class="dd ${activeGroup === 'about' ? 'active' : ''}">
            <a href="${root}about/index.html">About Us</a>
            <div>
              <a href="${root}about/index.html">About Neuro Mates</a>
              <a href="${root}about/vision-mission.html">Vision &amp; Mission</a>
              <a href="${root}about/our-approach.html">Our Approach</a>
              <a href="${root}about/impact.html">Impact</a>
            </div>
          </li>
          <li class="${activeGroup === 'contact' ? 'active' : ''}">
            <a href="${root}contact.html">Contact Us</a>
          </li>
          <li>
            <a class="btn" href="${root}register-demo.html">Register for a Demo</a>
          </li>
        </ul>
      `;
    },
    getFooterHTML: function () {
      setTimeout(initFooterObserver, 0);
      return `<div class="nm-footer-top-line"></div>
  <div class="nm-footer-wrap">
    
    <!-- Row 1: 3-Column Grid (Brand, Our Vision, Contact Us) -->
    <div class="nm-footer-grid">
      <!-- Col 1: Brand -->
      <div class="nm-footer-col nm-footer-brand">
        <a class="nm-footer-logo-tile" href="${root}index.html" aria-label="Neuro Mates Home">
          <img src="${root}assets/images/logo.png" alt="Neuro Mates">
        </a>
        <p class="nm-footer-tagline">MONITOR · DETECT · ALERT · CARE</p>
        <p class="nm-footer-brand-desc">An AI and IoT-based smart care system for Parkinson's, Alzheimer's, Epilepsy and Paralysis.</p>
      </div>

      <!-- Col 2: Our Vision -->
      <div class="nm-footer-col nm-footer-vision">
        <span class="nm-footer-label">Our vision</span>
        <p class="nm-footer-vision-stmt">A future where neurological care stays connected.</p>
        <p class="nm-footer-vision-body">Our vision is to make continuous neurological care more accessible, connected and personalised by bringing patients, families, healthcare professionals and technology into one care ecosystem.</p>
      </div>

      <!-- Col 3: Contact Us -->
      <div class="nm-footer-col nm-footer-contact">
        <span class="nm-footer-label">CONTACT US</span>
        <p class="nm-footer-contact-body">Interested in Neuro Mates, our products, healthcare collaboration or a product demonstration? Get in touch with our team.</p>
        <div class="nm-footer-buttons">
          <a class="nm-btn-contact" href="${root}contact.html">Contact us →</a>
          <a class="nm-btn-demo" href="${root}register-demo.html">Register for a demo →</a>
        </div>
        <!-- SLOT: Address, phone, email, legal and social links can be placed here in future updates -->
      </div>
    </div>

    <!-- Row 2: Team Strip -->
    <div class="nm-footer-team-strip">
      <span class="nm-footer-label">Our team</span>
      <div class="nm-footer-team-pills">
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#6EC1F0;">BS</span>
          <span class="nm-team-name">Bhavik Solanki</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#9B8CFF;">AB</span>
          <span class="nm-team-name">Anandi Bhayani</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#5BE7C4;">KP</span>
          <span class="nm-team-name">Kirtee Pitroda</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#F5B14C;">MM</span>
          <span class="nm-team-name">Maulik Mehta</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#FF9AD0;">VJ</span>
          <span class="nm-team-name">Vasu Janjrukiya</span>
        </div>
        <div class="nm-team-pill">
          <span class="nm-team-avatar" style="background:#7FD6D0;">DV</span>
          <span class="nm-team-name">Darshil Vashnani</span>
        </div>
      </div>
    </div>

    <!-- Row 3: Bottom Bar -->
    <div class="nm-footer-bottom-bar">
      <div class="nm-footer-bottom-left">
        <span>&copy; Neuro Mates &middot; Connected neurological care</span>
      </div>
      <div class="nm-footer-bottom-right">
        <span class="nm-footer-disclaimer">Not a substitute for professional medical advice</span>
        <a class="nm-footer-back-to-top" href="#" aria-label="Back to top">&uarr; Back to top</a>
      </div>
    </div>

  </div>`;
    },
    getCTAHTML: function () {
      return `
        <div class="w">
          <h2 class="r">Let’s build a more <em>connected</em> approach to neurological care.</h2>
          <p class="bl r">Whether you are a patient, caregiver, healthcare professional, hospital or organisation interested in Neuro Mates, we would like to hear from you.</p>
          <div class="bt r">
            <a class="btn" href="${root}register-demo.html">Register for a demo →</a>
            <a class="b2" href="${root}contact.html">Contact us →</a>
          </div>
        </div>
      `;
    }
  };

  // Auto-init on DOMContentLoaded with instant scroll reset
  document.addEventListener('DOMContentLoaded', () => {
    if (!window.location.hash) {
      window.scrollTo(0, 0);
    }
    initCareLine();
    initNav();
    initBackToTop();
    initFooterObserver();
    initSmoothScroll();

    // Automatically load Frontend AI Chat Widget
    if (!document.getElementById('neuro-chat-launcher') && !window.NeuroChatInitialized) {
      const chatScript = document.createElement('script');
      chatScript.src = `${root}assets/js/chat-widget.js`;
      chatScript.async = true;
      document.body.appendChild(chatScript);
    }
  });
})();

