// ponytail: one file for all motion — Lenis smooth scroll + hero parallax + history timeline
(function () {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // 6.10 — Lenis smooth scroll, paused while #appointment is on screen
    if (typeof Lenis !== 'undefined') {
        const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => lenis.raf(time * 1000));
        gsap.ticker.lagSmoothing(0);
        window.__lenis = lenis;

        const appt = document.getElementById('appointment');
        if (appt) {
            new IntersectionObserver((entries) => {
                entries.forEach((e) => {
                    if (e.isIntersecting) lenis.stop(); else lenis.start();
                });
            }, { threshold: 0.5 }).observe(appt);
        }
    }

    // 6.1 — Hero parallax: background image moves slower than scroll
    const heroImg = document.querySelector('.hero-bg-image');
    if (heroImg) {
        gsap.to(heroImg, {
            yPercent: 18,
            ease: 'none',
            scrollTrigger: {
                trigger: '#hero',
                start: 'top top',
                end: 'bottom top',
                scrub: true
            }
        });
    }

    // 6.2 — History timeline now handled by static/perspective-showcase.js (3D rotateX)
    // ponytail: removed sticky-stack to avoid double-binding with perspective-showcase.js
})();
