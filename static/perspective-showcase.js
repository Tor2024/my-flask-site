// 3D Perspective Scroll Showcase — vanilla port of perspective-scroll-showcase.tsx
// Uses GSAP ScrollTrigger (already loaded) for scroll progress instead of framer-motion.
// ponytail: bg marquee text removed — irrelevant for historical timeline section.
(function () {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const stack = document.getElementById('timeline-stack');
  if (!stack) return;

  const cards = Array.from(stack.querySelectorAll('.timeline-era'));
  if (!cards.length) return;

  // Inject minimal CSS: full-bleed stage, backface hidden, preserve-3d
  const style = document.createElement('style');
  style.textContent = `
    #timeline-stack { perspective: 1200px; perspective-origin: 50% 50%; }
    #timeline-stack .timeline-era {
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      will-change: transform, opacity;
      transform-style: preserve-3d;
    }
    @media (prefers-reduced-motion: reduce) {
      #timeline-stack .timeline-era { backface-visibility: visible !important; }
    }
  `;
  document.head.appendChild(style);

  if (reduce) {
    // Static fallback: keep current sticky-stack layout, no 3D rotation.
    return;
  }

  // Sticky viewport holds the visible area; stage rotates inside it.
  const viewport = document.createElement('div');
  viewport.style.cssText = 'position: sticky; top: 0; height: 100dvh; width: 100%; overflow: hidden; display: flex; align-items: center; justify-content: center;';
  const stage = document.createElement('div');
  // 90% of viewport width/height, centered — leaves 5% breathing room on each side
  stage.style.cssText = 'position: relative; width: 90%; height: 90%; transform-style: preserve-3d;';

  // Move cards into stage as absolute full-bleed layers
  cards.forEach((card) => {
    card.classList.remove('sticky', 'top-0', 'min-h-[100dvh]', 'flex', 'items-center', 'justify-start', 'justify-center');
    card.style.position = 'absolute';
    card.style.inset = '0';
    card.style.width = '100%';
    card.style.height = '100%';
    card.style.minHeight = '0';
    card.style.display = 'flex';
    card.style.borderRadius = '1rem';
    card.style.overflow = 'hidden';
    stage.appendChild(card);
  });

  viewport.appendChild(stage);
  stack.innerHTML = '';
  stack.appendChild(viewport);

  // Stack height = N * 100vh for scroll room
  stack.style.height = (cards.length * 100) + 'vh';
  stack.style.position = 'relative';

  // Each card rotated i*180° so they stack like pages of a flip-book
  cards.forEach((card, i) => {
    card.dataset.baseRot = (i * 180).toString();
    card.style.transform = 'rotateX(' + (i * 180) + 'deg)';
    card.style.visibility = i === 0 ? 'visible' : 'hidden';
  });

  // GSAP scroll progress → rotate the stage, show only active card
  if (window.gsap && window.ScrollTrigger) {
    window.gsap.registerPlugin(window.ScrollTrigger);
    const totalRot = Math.max(0, cards.length - 1) * 180;

    const rotState = { v: 0 };
    window.gsap.to(rotState, {
      v: totalRot,
      ease: 'none',
      scrollTrigger: {
        trigger: stack,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.6,
        onUpdate: () => {
          stage.style.transform = 'rotateX(' + (-rotState.v) + 'deg)';
          const idx = Math.round(rotState.v / 180);
          cards.forEach((card, i) => {
            const dist = Math.abs(i - idx);
            card.style.visibility = dist <= 0.5 ? 'visible' : 'hidden';
          });
        }
      }
    });
  }
})();
