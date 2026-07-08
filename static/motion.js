// ponytail: one file for all motion — Lenis smooth scroll + hero parallax + history timeline
(function () {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

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

    // 6.3 — Section heading per-char rotateX reveal: letters flip in from the back
    document.querySelectorAll('section h2.text-primary').forEach((h2) => {
        // split into per-char spans (preserve whitespace as regular spaces)
        const text = h2.textContent;
        h2.style.perspective = '600px';
        h2.innerHTML = '';
        const chars = [];
        for (const ch of text) {
            if (ch === ' ') { h2.appendChild(document.createTextNode(' ')); continue; }
            const s = document.createElement('span');
            s.className = 'reveal-char';
            s.style.display = 'inline-block';
            s.style.willChange = 'transform, opacity';
            s.textContent = ch;
            h2.appendChild(s);
            chars.push(s);
        }
        gsap.set(chars, { rotateX: -90, opacity: 0, transformOrigin: '50% 100%' });
        gsap.to(chars, {
            rotateX: 0, opacity: 1,
            duration: 0.7, ease: 'back.out(1.7)',
            stagger: 0.045,
            scrollTrigger: { trigger: h2, start: 'top 82%', once: true }
        });
        // subtitle rides in just behind the heading
        const sub = h2.nextElementSibling;
        if (sub && sub.tagName === 'P') {
            gsap.from(sub, {
                opacity: 0, y: 20, duration: 0.9, ease: 'power2.out', delay: 0.5,
                scrollTrigger: { trigger: sub, start: 'top 85%', once: true }
            });
        }
    });
})();
