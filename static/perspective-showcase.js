// Stacking-cards scroll showcase — slides advance over each other on scroll.
// Yllw "Carousel Slide (Overlay Card)": contained rounded panel per era,
// next card scrolls up and covers the previous, which recedes (scale + dim).
// ponytail: keeps existing #timeline-stack HTML intact, only injects CSS + GSAP.
(function () {
  var stack = document.getElementById('timeline-stack');
  if (!stack) return;
  var cards = Array.from(stack.querySelectorAll('.timeline-era'));
  if (!cards.length) return;

  var style = document.createElement('style');
  style.textContent = [
    '#timeline-stack { position: relative; padding: 20px 0 40px; }',
    '#timeline-stack .timeline-era {',
    '  position: sticky !important; top: 80px !important;',
    '  height: calc(100dvh - 100px) !important; min-height: 0 !important;',
    '  max-width: 1400px !important; margin: 0 auto 20px !important;',
    '  border-radius: 1.5rem !important; overflow: hidden !important;',
    '  box-shadow: 0 16px 50px -16px rgba(0,0,0,0.5);',
    '  will-change: transform, opacity; transform-origin: center top;',
    '}',
    '@media (max-width: 768px) {',
    '  #timeline-stack .timeline-era { border-radius: 1rem !important; }',
    '}',
    '@media (prefers-reduced-motion: reduce) {',
    '  #timeline-stack .timeline-era { transform: none !important; opacity: 1 !important; }',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return; // sticky stack still works statically
  if (!window.gsap || !window.ScrollTrigger) return;

  window.gsap.registerPlugin(window.ScrollTrigger);

  // Each card recedes as the NEXT card scrolls up over it.
  cards.forEach(function (card, i) {
    if (i === cards.length - 1) return; // last card stays put
    window.gsap.to(card, {
      scale: 0.9,
      opacity: 0.7,
      ease: 'none',
      scrollTrigger: {
        trigger: cards[i + 1],
        start: 'top bottom',
        end: 'top top',
        scrub: true
      }
    });
  });
})();
