/**
 * NEURO MATES — Reveal & Scroll Animations (GSAP 3.12.5 + ScrollTrigger)
 * Provides standardized helpers for scroll-driven animations and reveals,
 * respecting prefers-reduced-motion.
 */

(function () {
  'use strict';

  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initReveals() {
    if (isReducedMotion || typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
      // Graceful fallback: make all reveal targets immediately visible
      document.querySelectorAll('.r, .reveal, .reveal-up').forEach(el => {
        el.classList.add('in');
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    // 1. Standard upward reveal for headings, cards, and paragraphs
    gsap.utils.toArray('.r, .reveal-up').forEach((el) => {
      gsap.fromTo(
        el,
        { opacity: 0, y: 32 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            toggleActions: 'play none none none',
            once: true
          }
        }
      );
    });

    // 2. Staggered reveal for grid or list items
    gsap.utils.toArray('.stagger-group').forEach((group) => {
      const items = group.querySelectorAll('.stagger-item');
      if (!items.length) return;

      gsap.fromTo(
        items,
        { opacity: 0, y: 24 },
        {
          opacity: 1,
          y: 0,
          duration: 0.65,
          stagger: 0.12,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: group,
            start: 'top 85%',
            once: true
          }
        }
      );
    });

    // 3. Word-by-word scrub helper (e.g. for "Responsible Intelligence")
    document.querySelectorAll('[data-scrub-words]').forEach((block) => {
      const text = block.textContent.trim();
      const words = text.split(/\s+/);
      block.innerHTML = words.map(w => `<span class="scrub-word" style="color:var(--mu);transition:color 0.2s;">${w} </span>`).join('');
      const wordSpans = block.querySelectorAll('.scrub-word');

      gsap.to(wordSpans, {
        color: '#0E3B43',
        stagger: 0.05,
        scrollTrigger: {
          trigger: block,
          start: 'top 75%',
          end: 'bottom 45%',
          scrub: 0.6
        }
      });
    });
  }

  window.NeuroReveal = {
    initReveals
  };

  document.addEventListener('DOMContentLoaded', () => {
    // Delay slightly to ensure GSAP and ScrollTrigger are loaded
    setTimeout(initReveals, 50);
  });
})();

