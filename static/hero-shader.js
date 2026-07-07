// ponytail: OGLES streak shader adapted from Neuform community template.
// Horizontal light streaks on a hyperbolic surface. Palette adapted to brand blue #0055a5.
// Off-screen gate via IntersectionObserver; prefers-reduced-motion disables render.
import { Renderer, Program, Mesh, Triangle } from 'https://esm.sh/ogl@1.0.11';

const container = document.getElementById('hero-shader');
if (container && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const MAX_COLORS = 8;
    const hexToRGB = hex => {
        const c = hex.replace('#', '').padEnd(6, '0');
        return [parseInt(c.slice(0,2),16)/255, parseInt(c.slice(2,4),16)/255, parseInt(c.slice(4,6),16)/255];
    };
    const prepColors = input => {
        const base = input.slice(0, MAX_COLORS);
        const count = base.length;
        const arr = [];
        for (let i=0;i<MAX_COLORS;i++) arr.push(hexToRGB(base[Math.min(i, base.length-1)]));
        const avg = [0,0,0];
        for (let i=0;i<count;i++){ avg[0]+=arr[i][0]; avg[1]+=arr[i][1]; avg[2]+=arr[i][2]; }
        avg[0]/=count; avg[1]/=count; avg[2]/=count;
        return { arr, count, avg };
    };

    const vertex = `
    attribute vec2 position;
    attribute vec2 uv;
    varying vec2 vUv;
    void main(){ vUv = uv; gl_Position = vec4(position, 0.0, 1.0); }`;

    const fragment = `
    precision highp float;
    uniform vec3  iResolution;
    uniform vec2  iMouse;
    uniform float iTime;
    uniform vec3  uColor0; uniform vec3  uColor1; uniform vec3  uColor2; uniform vec3  uColor3;
    uniform vec3  uColor4; uniform vec3  uColor5; uniform vec3  uColor6; uniform vec3  uColor7;
    uniform int   uColorCount;
    uniform vec3  uBgColor; uniform vec3  uMouseColor;
    uniform float uSpeed; uniform int   uStreakCount; uniform float uStreakWidth;
    uniform float uStreakLength; uniform float uGlow; uniform float uDensity;
    uniform float uTwinkle; uniform float uZoom; uniform float uBgGlow;
    uniform float uOpacity; uniform float uMouseEnabled; uniform float uMouseStrength;
    uniform float uMouseRadius;
    varying vec2 vUv;
    vec3 palette(float h){
        int count = uColorCount; if (count < 1) count = 1;
        int idx = int(floor(clamp(h, 0.0, 0.999999) * float(count)));
        if (idx <= 0) return uColor0; if (idx == 1) return uColor1; if (idx == 2) return uColor2;
        if (idx == 3) return uColor3; if (idx == 4) return uColor4; if (idx == 5) return uColor5;
        if (idx == 6) return uColor6; return uColor7;
    }
    vec3 tanhv(vec3 x){ vec3 e = exp(-2.0*x); return (1.0-e)/(1.0+e); }
    vec2 sceneC(vec2 frag, vec2 r){
        vec2 P = (frag + frag - r) / r.x;
        float z = 0.0; float d = 1e3; vec4 O = vec4(0.0);
        for (int k=0;k<39;k++){
            if (d <= 1e-4) break;
            O = z * normalize(vec4(P, uZoom, 0.0)) - vec4(0.0, 4.0, 1.0, 0.0)/4.5;
            d = 1.0 - sqrt(length(O*O));
            z += d;
        }
        return vec2(O.x, atan(O.z, O.y));
    }
    void mainImage(out vec4 o, vec2 fragCoord){
        vec2 C = vec2(fragCoord.y, fragCoord.x);
        vec2 r = vec2(iResolution.y, iResolution.x);
        vec2 uv0 = (C + C - r) / r.x;
        float T = 0.1 * iTime * uSpeed + 9.0;
        float angRings = max(1.0, floor(6.28318530718 * max(uDensity, 0.05) + 0.5));
        vec2 Y = vec2(5e-3, 6.28318530718 / angRings);
        vec2 c0 = sceneC(C, r);
        vec2 cdx = sceneC(C + vec2(1.0,0.0), r);
        vec2 cdy = sceneC(C + vec2(0.0,1.0), r);
        vec2 dCx = cdx - c0; vec2 dCy = cdy - c0;
        dCx.y -= 6.28318530718 * floor(dCx.y / 6.28318530718 + 0.5);
        dCy.y -= 6.28318530718 * floor(dCy.y / 6.28318530718 + 0.5);
        vec2 fw = abs(dCx) + abs(dCy);
        C = c0;
        vec2 P = vec2(2.0, 1.0) * uv0 - (r / r.x) * vec2(0.0, 1.0);
        vec4 O = vec4(uBgColor * 90.0 * uBgGlow / (1e3 * dot(P,P) + 6.0), 0.0);
        float mGlow = 0.0;
        if (uMouseEnabled > 0.5){
            vec2 iM = vec2(iMouse.y, iMouse.x);
            vec2 mN = (iM + iM - r) / r.x;
            float md = length(uv0 - mN);
            mGlow = exp(-md*md / max(uMouseRadius*uMouseRadius, 1e-4)) * uMouseStrength;
            O.rgb += uMouseColor * mGlow * 0.25;
        }
        float zr = 5e-4 * uStreakWidth;
        vec2 rr = vec2(max(length(fw), 1e-5));
        float tail = 19.0 / max(uStreakLength, 0.05);
        for (int m=0;m<16;m++){
            if (m >= uStreakCount) break;
            float jf = float(m) + 1.0;
            float ic = fract(sin(dot(vec2(jf, floor(C.x/Y.x + 0.5)), vec2(7.0, 11.0)) * 73.0));
            vec2 Pp = C - (T + T*ic) * vec2(0.0, 1.0);
            Pp -= floor(Pp/Y + 0.5) * Y;
            float h = fract(8663.0 * ic);
            vec3 col = palette(h);
            float weight = mix(1.5, 1.0 + sin(T + 7.0*h + 4.0), uTwinkle);
            weight *= (1.0 + mGlow * 2.0);
            vec2 inner = vec2(length(max(Pp, vec2(-1.0, 0.0))), length(Pp) - zr) - zr;
            vec2 sm = vec2(1.0) - smoothstep(-rr, rr, inner);
            O.rgb += dot(sm, vec2(exp(tail * Pp.y), 3.0)) * col * weight;
            C.x += Y.x / 8.0;
        }
        vec3 colr = sqrt(tanhv(max(O.rgb * uGlow - vec3(0.04, 0.08, 0.02), 0.0)));
        o = vec4(colr, uOpacity);
    }
    void main(){
        vec4 color; mainImage(color, vUv * iResolution.xy);
        gl_FragColor = color;
    }`;

    const renderer = new Renderer({ dpr: window.devicePixelRatio || 1, alpha: true, antialias: true });
    const gl = renderer.gl;
    const canvas = gl.canvas;
    canvas.style.width = '100%'; canvas.style.height = '100%'; canvas.style.display = 'block';
    container.appendChild(canvas);

    // Steel + blue + amber — workshop character
    const config = {
        colors: ['#0055a5', '#b8c4d4', '#ff8a00'],
        backgroundColor: '#0a0a0f',
        speed: 0.6, streakCount: 3, streakWidth: 1.0, streakLength: 1.5, glow: 0.8, density: 0.3,
        twinkle: 0.8, zoom: 2.2, backgroundGlow: 0.4, opacity: 0.7, mouseInteraction: true,
        mouseStrength: 1.0, mouseRadius: 0.8, mouseDampening: 0.15
    };

    const { arr, count, avg } = prepColors(config.colors);
    const uniforms = {
        iResolution: { value: [gl.drawingBufferWidth, gl.drawingBufferHeight, 1] },
        iMouse: { value: [0, 0] }, iTime: { value: 0 },
        uColor0: { value: arr[0] }, uColor1: { value: arr[1] }, uColor2: { value: arr[2] },
        uColor3: { value: arr[3] }, uColor4: { value: arr[4] }, uColor5: { value: arr[5] },
        uColor6: { value: arr[6] }, uColor7: { value: arr[7] }, uColorCount: { value: count },
        uBgColor: { value: hexToRGB(config.backgroundColor) }, uMouseColor: { value: avg },
        uSpeed: { value: config.speed }, uStreakCount: { value: config.streakCount },
        uStreakWidth: { value: config.streakWidth }, uStreakLength: { value: config.streakLength },
        uGlow: { value: config.glow }, uDensity: { value: config.density },
        uTwinkle: { value: config.twinkle }, uZoom: { value: config.zoom },
        uBgGlow: { value: config.backgroundGlow }, uOpacity: { value: config.opacity },
        uMouseEnabled: { value: config.mouseInteraction ? 1 : 0 },
        uMouseStrength: { value: config.mouseStrength }, uMouseRadius: { value: config.mouseRadius }
    };

    const program = new Program(gl, { vertex, fragment, uniforms });
    const geometry = new Triangle(gl);
    const mesh = new Mesh(gl, { geometry, program });

    const resize = () => {
        renderer.setSize(container.clientWidth, container.clientHeight);
        uniforms.iResolution.value = [gl.drawingBufferWidth, gl.drawingBufferHeight, 1];
    };
    window.addEventListener('resize', resize);
    resize();

    let mouseTarget = [0, 0];
    const onPointerMove = e => {
        const rect = container.getBoundingClientRect();
        const scale = renderer.dpr || 1;
        mouseTarget = [(e.clientX - rect.left) * scale, (rect.height - (e.clientY - rect.top)) * scale];
        if (config.mouseDampening <= 0) uniforms.iMouse.value = mouseTarget;
    };
    if (config.mouseInteraction) window.addEventListener('pointermove', onPointerMove);

    // ponytail: off-screen gate — don't burn GPU when hero scrolled out of view
    let visible = true;
    if ('IntersectionObserver' in window) {
        new IntersectionObserver(e => { visible = e[0].isIntersecting; }, { rootMargin: '100px' }).observe(container);
    }

    let lastTime = 0;
    const loop = t => {
        requestAnimationFrame(loop);
        if (!visible) { lastTime = t; return; }
        uniforms.iTime.value = t * 0.001;
        if (config.mouseDampening > 0) {
            if (!lastTime) lastTime = t;
            const dt = (t - lastTime) / 1000; lastTime = t;
            let factor = 1 - Math.exp(-dt / Math.max(1e-4, config.mouseDampening));
            if (factor > 1) factor = 1;
            const cur = uniforms.iMouse.value;
            cur[0] += (mouseTarget[0] - cur[0]) * factor;
            cur[1] += (mouseTarget[1] - cur[1]) * factor;
        } else { lastTime = t; }
        renderer.render({ scene: mesh });
    };
    requestAnimationFrame(loop);
}
