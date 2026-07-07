// Magic Dust particle system вЂ” vanilla WebGL1, no deps.
// Cycles: scattered cloud -> text/car -> hold -> scatter -> next.
// Cars loaded from Kenney Car Kit GLB (CC0), sampled on triangle surface.

(function () {
  'use strict';

  var canvas = document.getElementById('magic-dust');
  if (!canvas) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- Sequence: 3 German texts + 3 real car models (Kenney CC0) ----
  var SEQUENCE = [
    { type: 'logo', name: 'Mercedes-Benz' },
    { type: 'logo', name: 'BMW' },
    { type: 'logo', name: 'Audi' },
    { type: 'logo', name: 'Renault' },
    { type: 'logo', name: 'Citroën' },
    { type: 'logo', name: 'Mitsubishi' },
    { type: 'logo', name: 'Ford' },
    { type: 'logo', name: 'Nissan' },
    { type: 'logo', name: 'Honda' },
    { type: 'logo', name: 'Hyundai' },
    { type: 'logo', name: 'Kia' },
    { type: 'logo', name: 'Subaru' }
  ];

  var COUNT = 18000;
  var SCATTER_R = 12;
  var HOLD_SEC = 4.5;
  var SPEED = 0.667;
  var CAR_SCALE = 2.0; // bounds ~1.5 в†’ final ~3 units, fits viewport at z=9 fov 45

  // ---- Position generators ----
  function scatteredPositions(count, radius) {
    var p = new Float32Array(count * 3);
    for (var i = 0; i < count; i++) {
      var u = Math.random(), v = Math.random();
      var theta = u * 2 * Math.PI;
      var phi = Math.acos(2 * v - 1);
      var r = Math.cbrt(Math.random()) * radius;
      p[i*3]   = r * Math.sin(phi) * Math.cos(theta);
      p[i*3+1] = r * Math.sin(phi) * Math.sin(theta);
      p[i*3+2] = r * Math.cos(phi);
    }
    return p;
  }

  function textPositions(text, count, size) {
    var c = document.createElement('canvas');
    c.width = 1024; c.height = 1024;
    var ctx = c.getContext('2d', { willReadFrequently: true });
    if (!ctx) return new Float32Array(count * 3);
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, 1024, 1024);
    ctx.fillStyle = '#fff';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    var fs = 220;
    ctx.font = '900 ' + fs + "px 'Arial Black', 'Inter', sans-serif";
    var w = ctx.measureText(text).width;
    if (w > 900) { fs = Math.floor(fs * (900 / w)); ctx.font = '900 ' + fs + "px 'Arial Black', 'Inter', sans-serif"; }
    ctx.fillText(text, 512, 512);
    var data = ctx.getImageData(0, 0, 1024, 1024).data;
    var pts = [];
    for (var i = 0; i < 1024 * 1024; i++) {
      if (data[i*4] > 128) {
        var x = i % 1024;
        var y = (i / 1024) | 0;
        pts.push((x/1024 - 0.5) * size, -(y/1024 - 0.5) * size);
      }
    }
    var out = new Float32Array(count * 3);
    if (pts.length === 0) return out;
    for (var k = 0; k < count; k++) {
      var idx = (Math.random() * (pts.length/2) | 0) * 2;
      out[k*3]   = pts[idx]   + (Math.random()-0.5)*0.15;
      out[k*3+1] = pts[idx+1] + (Math.random()-0.5)*0.15;
      out[k*3+2] = (Math.random()-0.5)*0.2;
    }
    return out;
  }

  // ---- Logo positions: Mercedes-Benz 3-pointed star (ring + 3 spokes) ----
  // Canvas-based: draw star on 1024x1024, sample white pixels (reuses textPositions technique).
  function mercedesPositions(count, size) {
    var c = document.createElement('canvas');
    c.width = 1024; c.height = 1024;
    var ctx = c.getContext('2d', { willReadFrequently: true });
    if (!ctx) return new Float32Array(count * 3);
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, 1024, 1024);
    ctx.fillStyle = '#fff';
    var cx = 512, cy = 512;
    var rOuter = 420, rInner = 320, rHub = 70;
    // outer ring (thick stroke)
    ctx.beginPath();
    ctx.arc(cx, cy, rOuter, 0, Math.PI * 2);
    ctx.arc(cx, cy, rInner, 0, Math.PI * 2, true);
    ctx.fill();
    // 3 spokes from center to ring at 0В°, 120В°, 240В° (pointing up, lower-left, lower-right)
    var spokeWidth = 60;
    for (var a = 0; a < 3; a++) {
      var angle = -Math.PI/2 + a * (Math.PI * 2 / 3); // -90В° = up
      var dx = Math.cos(angle), dy = Math.sin(angle);
      var tipX = cx + dx * rInner;
      var tipY = cy + dy * rInner;
      // perpendicular for spoke width
      var px = -dy, py = dx;
      ctx.beginPath();
      ctx.moveTo(cx + px * spokeWidth, cy + py * spokeWidth);
      ctx.lineTo(cx - px * spokeWidth, cy - py * spokeWidth);
      ctx.lineTo(tipX - px * spokeWidth * 0.4, tipY - py * spokeWidth * 0.4);
      ctx.lineTo(tipX + px * spokeWidth * 0.4, tipY + py * spokeWidth * 0.4);
      ctx.closePath();
      ctx.fill();
    }
    // central hub
    ctx.beginPath();
    ctx.arc(cx, cy, rHub, 0, Math.PI * 2);
    ctx.fill();
    var data = ctx.getImageData(0, 0, 1024, 1024).data;
    var pts = [];
    for (var i = 0; i < 1024 * 1024; i++) {
      if (data[i*4] > 128) {
        var x = i % 1024;
        var y = (i / 1024) | 0;
        pts.push((x/1024 - 0.5) * size, -(y/1024 - 0.5) * size);
      }
    }
    var out = new Float32Array(count * 3);
    if (pts.length === 0) return out;
    for (var k = 0; k < count; k++) {
      var idx = (Math.random() * (pts.length/2) | 0) * 2;
      out[k*3]   = pts[idx]   + (Math.random()-0.5)*0.15;
      out[k*3+1] = pts[idx+1] + (Math.random()-0.5)*0.15;
      out[k*3+2] = (Math.random()-0.5)*0.2;
    }
    return out;
  }

    // ---- VW logo: thick ring + V stacked over W (real proportions) ----
  // ---- Audi logo: 4 linked rings ----
  function audiPositions(count, size) {
    var c = document.createElement('canvas');
    c.width = 1024; c.height = 1024;
    var ctx = c.getContext('2d', { willReadFrequently: true });
    if (!ctx) return new Float32Array(count * 3);
    ctx.fillStyle = '#000'; ctx.fillRect(0, 0, 1024, 1024);
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 40;
    var ringR = 150;
    var spacing = 230;
    var startX = 512 - spacing * 1.5;
    var y = 512;
    for (var i = 0; i < 4; i++) {
      ctx.beginPath(); ctx.arc(startX + i * spacing, y, ringR, 0, Math.PI*2); ctx.stroke();
    }
    return sampleCanvas(ctx, c, count, size);
  }
  // ---- BMW logo: roundel with 4 quadrants + BMW letters on top arc ----
  function bmwPositions(count, size) {
    var c = document.createElement('canvas');
    c.width = 1024; c.height = 1024;
    var ctx = c.getContext('2d', { willReadFrequently: true });
    if (!ctx) return new Float32Array(count * 3);
    ctx.fillStyle = '#000'; ctx.fillRect(0, 0, 1024, 1024);
    ctx.fillStyle = '#fff';
    var cx = 512, cy = 512;
    // outer white ring (annulus: white disc with black hole inside = ring)
    ctx.fillStyle = '#fff';
    ctx.beginPath(); ctx.arc(cx, cy, 450, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#000';
    ctx.beginPath(); ctx.arc(cx, cy, 360, 0, Math.PI*2); ctx.fill();
    // inner disc split into 4 quadrants at 45° — white quadrants at NE and SW (real BMW blue/white pattern)
    // NE quadrant (top-right): from -π/2 to 0
    ctx.fillStyle = '#fff';
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, 355, -Math.PI/2, 0); ctx.closePath(); ctx.fill();
    // SW quadrant (bottom-left): from π/2 to π
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, 355, Math.PI/2, Math.PI); ctx.closePath(); ctx.fill();
    // white cross dividers (thick lines separating quadrants at 45° angles)
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 5;
    ctx.beginPath();
    // diagonal 1: top-right to bottom-left
    ctx.moveTo(cx + 355*Math.cos(-Math.PI/4), cy + 355*Math.sin(-Math.PI/4));
    ctx.lineTo(cx + 355*Math.cos(Math.PI*0.75), cy + 355*Math.sin(Math.PI*0.75));
    ctx.stroke();
    ctx.beginPath();
    // diagonal 2: top-left to bottom-right
    ctx.moveTo(cx + 355*Math.cos(Math.PI*0.75 + Math.PI/2), cy + 355*Math.sin(Math.PI*0.75 + Math.PI/2));
    ctx.lineTo(cx + 355*Math.cos(-Math.PI/4 + Math.PI/2), cy + 355*Math.sin(-Math.PI/4 + Math.PI/2));
    ctx.stroke();
    // BMW letters on outer ring, distributed across top arc
    ctx.fillStyle = '#000';
    ctx.font = 'bold 110px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.save();
    ctx.translate(cx, cy);
    var letters = ['B','M','W'];
    var angles = [-0.42, 0, 0.42];
    for (var i = 0; i < 3; i++) {
      ctx.save();
      ctx.rotate(angles[i] - Math.PI/2);
      ctx.translate(0, -405);
      ctx.fillText(letters[i], 0, 0);
      ctx.restore();
    }
    ctx.restore();
    return sampleCanvas(ctx, c, count, size);
  }



  function renaultPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.strokeStyle = '#fff';
    // Renault: diamond (vertical lozenge)
    ctx.lineWidth = 50; ctx.lineJoin = 'round';
    ctx.beginPath();
    ctx.moveTo(512, 120); ctx.lineTo(820, 512); ctx.lineTo(512, 904); ctx.lineTo(204, 512); ctx.closePath();
    ctx.stroke();
    ctx.lineWidth = 25;
    ctx.beginPath();
    ctx.moveTo(512, 240); ctx.lineTo(710, 512); ctx.lineTo(512, 784); ctx.lineTo(314, 512); ctx.closePath();
    ctx.stroke();
    return sampleCanvas(ctx, c, count, size);
  }

  function citroenPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.strokeStyle = '#fff';
    // Citroën: double chevron (two stacked V shapes)
    ctx.lineWidth = 50; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    ctx.beginPath(); ctx.moveTo(240, 600); ctx.lineTo(512, 320); ctx.lineTo(784, 600); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(240, 760); ctx.lineTo(512, 480); ctx.lineTo(784, 760); ctx.stroke();
    return sampleCanvas(ctx, c, count, size);
  }

  function mitsubishiPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // 3 diamonds (rhombi) meeting at center, 120deg apart
    var cx = 512, cy = 512, r = 280;
    for (var i = 0; i < 3; i++) {
      var a = -Math.PI/2 + i * 2*Math.PI/3;
      var tipX = cx + Math.cos(a) * r;
      var tipY = cy + Math.sin(a) * r;
      var aL = a - 0.5, aR = a + 0.5;
      var midLX = cx + Math.cos(aL) * r * 0.45;
      var midLY = cy + Math.sin(aL) * r * 0.45;
      var midRX = cx + Math.cos(aR) * r * 0.45;
      var midRY = cy + Math.sin(aR) * r * 0.45;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(midLX, midLY);
      ctx.lineTo(tipX, tipY);
      ctx.lineTo(midRX, midRY);
      ctx.closePath();
      ctx.fill();
    }
    return sampleCanvas(ctx, c, count, size);
  }

  function fordPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Blue oval with 'Ford' script — draw oval ring + wordmark
    ctx.lineWidth = 40; ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.ellipse(512, 512, 440, 240, 0, 0, Math.PI*2);
    ctx.stroke();
    // 'Ford' script italic inside oval
    ctx.save();
    ctx.translate(512, 512);
    ctx.rotate(-0.08);
    ctx.fillStyle = '#fff';
    ctx.font = 'italic bold 180px Georgia, serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('Ford', 0, 10);
    ctx.restore();
    return sampleCanvas(ctx, c, count, size);
  }

  function nissanPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Nissan = circle + horizontal bar with 'NISSAN' text
    ctx.lineWidth = 28; ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.arc(512, 512, 400, 0, Math.PI*2);
    ctx.stroke();
    // Horizontal bar across middle
    ctx.fillRect(112, 470, 800, 84);
    // Clear inside bar for text — use smaller fillText on top
    ctx.save();
    ctx.fillStyle = '#000';
    ctx.font = 'bold 90px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('NISSAN', 512, 514);
    ctx.restore();
    return sampleCanvas(ctx, c, count, size);
  }



  function hondaPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Honda = stylized H inside rounded rectangle (wing-like)
    ctx.lineWidth = 22; ctx.strokeStyle = '#fff';
    // Outer shape — trapezoid/wing
    ctx.lineJoin = 'round';
    ctx.beginPath();
    ctx.moveTo(160, 280);  // top-left
    ctx.lineTo(864, 280);  // top-right
    ctx.lineTo(780, 740);  // bottom-right
    ctx.lineTo(244, 740);  // bottom-left
    ctx.closePath();
    ctx.stroke();
    // H inside
    ctx.lineWidth = 60; ctx.lineCap = 'round';
    // Left vertical
    ctx.beginPath();
    ctx.moveTo(380, 360);
    ctx.lineTo(380, 680);
    ctx.stroke();
    // Right vertical
    ctx.beginPath();
    ctx.moveTo(644, 360);
    ctx.lineTo(644, 680);
    ctx.stroke();
    // Horizontal crossbar
    ctx.beginPath();
    ctx.moveTo(380, 520);
    ctx.lineTo(644, 520);
    ctx.stroke();
    return sampleCanvas(ctx, c, count, size);
  }


  function hyundaiPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Hyundai = italic H in oval (the H has a stylized handshake silhouette)
    ctx.lineWidth = 20; ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.ellipse(512, 512, 400, 280, 0, 0, Math.PI*2);
    ctx.stroke();
    // Stylized H — two verticals + diagonal connecting bar
    ctx.lineWidth = 60; ctx.lineCap = 'round';
    // Left vertical (slightly slanted)
    ctx.beginPath();
    ctx.moveTo(380, 320);
    ctx.lineTo(380, 720);
    ctx.stroke();
    // Right vertical (slightly slanted)
    ctx.beginPath();
    ctx.moveTo(644, 320);
    ctx.lineTo(644, 720);
    ctx.stroke();
    // Diagonal connecting bar (the handshake look)
    ctx.lineWidth = 55;
    ctx.beginPath();
    ctx.moveTo(380, 540);
    ctx.lineTo(644, 480);
    ctx.stroke();
    return sampleCanvas(ctx, c, count, size);
  }

  function kiaPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Kia = bold wordmark 'KIA' on plain background
    ctx.save();
    ctx.translate(512, 512);
    ctx.font = 'bold 280px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('KIA', 0, 0);
    ctx.restore();
    return sampleCanvas(ctx, c, count, size);
  }

  function subaruPositions(count, size) {
    var c = document.createElement('canvas'); c.width = c.height = 1024;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff';
    // Subaru = 6 stars in oval (Pleiades cluster — 1 large + 5 small)
    ctx.lineWidth = 22; ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.ellipse(512, 512, 400, 270, 0, 0, Math.PI*2);
    ctx.stroke();
    // Star drawing helper
    function drawStar(cx, cy, r) {
      ctx.beginPath();
      for (var i = 0; i < 10; i++) {
        var ang = -Math.PI/2 + i * Math.PI/5;
        var rad = (i % 2 === 0) ? r : r * 0.4;
        var x = cx + Math.cos(ang) * rad;
        var y = cy + Math.sin(ang) * rad;
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.closePath();
      ctx.fill();
    }
    // Large star (top-right)
    drawStar(640, 380, 80);
    // 5 smaller stars clustered (lower-left, Pleiades pattern)
    drawStar(380, 440, 50);
    drawStar(420, 580, 50);
    drawStar(540, 620, 50);
    drawStar(320, 600, 45);
    drawStar(480, 520, 45);
    return sampleCanvas(ctx, c, count, size);
  }





  // ---- shared: sample canvas white pixels → Float32Array(count*3) ----
  function sampleCanvas(ctx, c, count, size) {
    var data = ctx.getImageData(0, 0, 1024, 1024).data;
    var pts = [];
    for (var i = 0; i < 1024 * 1024; i++) {
      if (data[i*4] > 128) {
        var x = i % 1024;
        var y = (i / 1024) | 0;
        pts.push((x/1024 - 0.5) * size, -(y/1024 - 0.5) * size);
      }
    }
    var out = new Float32Array(count * 3);
    if (pts.length === 0) return out;
    for (var k = 0; k < count; k++) {
      var idx = (Math.random() * (pts.length/2) | 0) * 2;
      out[k*3]   = pts[idx]   + (Math.random()-0.5)*0.15;
      out[k*3+1] = pts[idx+1] + (Math.random()-0.5)*0.15;
      out[k*3+2] = (Math.random()-0.5)*0.2;
    }
    return out;
  }

// ---- GLB loader (minimal: parses all meshes, returns flat triangle soup) ----
  // Supports: glTF 2.0 binary, indexed + non-indexed triangles, FLOAT positions.
  // Returns { tris (flat soup of BODY only, centered at origin), wheels (array of {x,y,z} corner positions from node translations) }
  function parseGlb(buf) {
    var dv = new DataView(buf);
    var magic = String.fromCharCode(dv.getUint8(0), dv.getUint8(1), dv.getUint8(2), dv.getUint8(3));
    if (magic !== 'glTF') throw new Error('not a GLB');
    var jsonLen = dv.getUint32(12, true);
    var json = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, 20, jsonLen)));
    var binOff = 12 + 8 + jsonLen + 8;

    var accessors = json.accessors;
    var bufferViews = json.bufferViews;
    function readAcc(i) {
      var a = accessors[i]; var bv = bufferViews[a.bufferView];
      var off = binOff + (bv.byteOffset || 0) + (a.byteOffset || 0);
      var per = a.type === 'VEC3' ? 3 : 1;
      var arr;
      if (a.componentType === 5126) arr = new Float32Array(buf, off, a.count * per);
      else if (a.componentType === 5123) arr = new Uint16Array(buf, off, a.count * per);
      else arr = new Uint32Array(buf, off, a.count * per);
      return { data: arr, count: a.count, per: per };
    }

    // Walk nodes[]: each node has mesh index + translation [x,y,z].
    // Kenney GLB wheels are pre-centered at origin and meant to be placed by node translation.
    // Applying translation places every wheel at its authored arch position.
    var nodes = json.nodes || [];
    var meshes = json.meshes || [];
    var tris = [];
    for (var ni = 0; ni < nodes.length; ni++) {
      var node = nodes[ni];
      if (node.mesh === undefined) continue;
      var mesh = meshes[node.mesh];
      if (!mesh || !mesh.primitives) continue;
      var tx = (node.translation && node.translation[0]) || 0;
      var ty = (node.translation && node.translation[1]) || 0;
      var tz = (node.translation && node.translation[2]) || 0;
      var primList = mesh.primitives;
      for (var pi = 0; pi < primList.length; pi++) {
        var prim = primList[pi];
        if (prim.attributes.POSITION === undefined) continue;
        var pos = readAcc(prim.attributes.POSITION);
        if (prim.indices !== undefined) {
          var idx = readAcc(prim.indices);
          for (var t = 0; t < idx.count; t += 3) {
            var a = idx.data[t] * 3, b = idx.data[t+1] * 3, c = idx.data[t+2] * 3;
            tris.push(pos.data[a]   + tx, pos.data[a+1] + ty, pos.data[a+2] + tz);
            tris.push(pos.data[b]   + tx, pos.data[b+1] + ty, pos.data[b+2] + tz);
            tris.push(pos.data[c]   + tx, pos.data[c+1] + ty, pos.data[c+2] + tz);
          }
        } else {
          for (var v = 0; v < pos.count; v += 3) {
            var o = v * 3;
            tris.push(pos.data[o]   + tx, pos.data[o+1] + ty, pos.data[o+2] + tz);
            tris.push(pos.data[o+3] + tx, pos.data[o+4] + ty, pos.data[o+5] + tz);
            tris.push(pos.data[o+6] + tx, pos.data[o+7] + ty, pos.data[o+8] + tz);
          }
        }
      }
    }
    return new Float32Array(tris);
  }

  // ---- Surface sampler: uniformly distribute points on triangle surface ----
  // Method: compute area of each triangle, build cumulative area array,
  // pick triangle weighted by area, then uniform sample inside triangle.
  function sampleSurface(triSoup, count, scale) {
    var triCount = triSoup.length / 9;
    if (triCount === 0) return scatteredPositions(count, 1);

    // Cumulative areas
    var cumArea = new Float32Array(triCount);
    var totalArea = 0;
    for (var i = 0; i < triCount; i++) {
      var o = i * 9;
      var ax = triSoup[o]   - triSoup[o+6];
      var ay = triSoup[o+1] - triSoup[o+7];
      var az = triSoup[o+2] - triSoup[o+8];
      var bx = triSoup[o+3] - triSoup[o+6];
      var by = triSoup[o+4] - triSoup[o+7];
      var bz = triSoup[o+5] - triSoup[o+8];
      // cross product magnitude / 2
      var cx = ay*bz - az*by;
      var cy = az*bx - ax*bz;
      var cz = ax*by - ay*bx;
      var area = 0.5 * Math.sqrt(cx*cx + cy*cy + cz*cz);
      totalArea += area;
      cumArea[i] = totalArea;
    }

    var out = new Float32Array(count * 3);
    for (var k = 0; k < count; k++) {
      // pick triangle by weighted area (binary search)
      var r = Math.random() * totalArea;
      var lo = 0, hi = triCount - 1, picked = 0;
      while (lo <= hi) {
        var mid = (lo + hi) >> 1;
        if (cumArea[mid] < r) lo = mid + 1;
        else { picked = mid; hi = mid - 1; }
      }
      // uniform sample inside triangle (r1, r2 with sqrt)
      var to = picked * 9;
      var r1 = Math.sqrt(Math.random());
      var r2 = Math.random();
      var u = 1 - r1;
      var v = r1 * (1 - r2);
      var w = r1 * r2;
      out[k*3]   = (u*triSoup[to]   + v*triSoup[to+3] + w*triSoup[to+6]) * scale;
      out[k*3+1] = (u*triSoup[to+1] + v*triSoup[to+4] + w*triSoup[to+7]) * scale;
      out[k*3+2] = (u*triSoup[to+2] + v*triSoup[to+5] + w*triSoup[to+8]) * scale;
    }
    return out;
  }

  function orderedDelays(targets, count) {
    var d = new Float32Array(count);
    var minX=Infinity, maxX=-Infinity;
    for (var i=0;i<count;i++){
      var x = targets[i*3];
      if (x<minX) minX=x;
      if (x>maxX) maxX=x;
    }
    var range = (maxX-minX) || 1;
    for (var j=0;j<count;j++){
      var nx = (targets[j*3]-minX)/range;
      d[j] = nx*0.7 + Math.random()*0.3;
    }
    return d;
  }

  // ---- Async: load car GLBs, then build targets, then start render ----
  // Uses ground-truth wheel positions from GLB nodes[].translation (Unity-authored).
  // Wheels are generated procedurally as small discs at each corner position so the
  // particle cloud shows real wheel arches without importing the actual wheel mesh.
  // Reposition wheels of a Kenney Car Kit GLB triangle soup.
  // Heuristic: detect wheel primitives by small vertex count + small bounding box,
  // measure body bounding box, move wheel vertices to the four corners.
  // ponytail: repositionWheels removed вЂ” parseGlb reads node.translation directly

  var carCache = {};
  function loadCar(src) {
    if (carCache[src]) return Promise.resolve(carCache[src]);
    return fetch(src).then(function (r) { return r.arrayBuffer(); }).then(function (buf) {
      var triSoup = parseGlb(buf);
      var fixed = triSoup;
      // Center X/Z at origin so the car spins in place.
      var minX=Infinity, maxX=-Infinity, minZ=Infinity, maxZ=-Infinity;
      for (var i = 0; i < fixed.length; i += 3) {
        var x = fixed[i], z = fixed[i+2];
        if (x<minX) minX=x; if (x>maxX) maxX=x;
        if (z<minZ) minZ=z; if (z>maxZ) maxZ=z;
      }
      var cx = (minX+maxX)/2, cz = (minZ+maxZ)/2;
      var centered = new Float32Array(fixed.length);
      for (var j = 0; j < fixed.length; j += 3) {
        centered[j]   = fixed[j]   - cx;
        centered[j+1] = fixed[j+1];
        centered[j+2] = fixed[j+2] - cz;
      }
      carCache[src] = centered;
      return centered;
    });
  }

function buildTargets() {
    var arr = [];
    for (var i=0; i<SEQUENCE.length; i++) {
      var item = SEQUENCE[i];
      var dest, isText=false;
      if (item.type === 'text') {
        dest = textPositions(item.text, COUNT, 24);
        isText = true;
      } else if (item.type === 'logo') {
        isText = true; // all logos use text-style ease-to-2π animation
        if (item.name === 'Mercedes-Benz') dest = mercedesPositions(COUNT, 12);
        else if (item.name === 'BMW') dest = bmwPositions(COUNT, 10);
        else if (item.name === 'Audi') dest = audiPositions(COUNT, 11);
        else if (item.name === 'Renault') dest = renaultPositions(COUNT, 10);
        else if (item.name === 'Citroën') dest = citroenPositions(COUNT, 10);
        else if (item.name === 'Mitsubishi') dest = mitsubishiPositions(COUNT, 10);
        else if (item.name === 'Ford') dest = fordPositions(COUNT, 11);
        else if (item.name === 'Nissan') dest = nissanPositions(COUNT, 10);
        else if (item.name === 'Honda') dest = hondaPositions(COUNT, 10);
        else if (item.name === 'Hyundai') dest = hyundaiPositions(COUNT, 11);
        else if (item.name === 'Kia') dest = kiaPositions(COUNT, 12);
        else if (item.name === 'Subaru') dest = subaruPositions(COUNT, 10);
      } else {
        dest = sampleSurface(carCache[item.src], COUNT, CAR_SCALE);
      }
      arr.push({ dest: dest, delays: orderedDelays(dest, COUNT), isText: isText });
    }
    return arr;
  }

  function start() {
    // ---- Init WebGL ----
    var gl = canvas.getContext('webgl', { alpha: true, antialias: false, premultipliedAlpha: false });
    if (!gl) { console.warn('Magic Dust: WebGL not available'); return; }

    var vsSrc = [
      'attribute vec3 aPosition;',
      'attribute vec3 aTarget;',
      'attribute float aDelay;',
      'attribute float aSize;',
      'uniform float uProgress;',
      'uniform float uPointSize;',
      'uniform mat4 modelViewMatrix;',
      'uniform mat4 projectionMatrix;',
      'varying float vAlpha;',
      'void main(){',
      '  float p = clamp((uProgress - aDelay) * 3.0, 0.0, 1.0);',
      '  float ease = p < 0.5 ? 4.0*p*p*p : 1.0 - pow(-2.0*p+2.0, 3.0)/2.0;',
      '  vec3 fp = mix(aPosition, aTarget, ease);',
      '  vec4 mv = modelViewMatrix * vec4(fp, 1.0);',
      '  gl_PointSize = uPointSize * aSize * (1.0 / -mv.z);',
      '  gl_Position = projectionMatrix * mv;',
      '  vAlpha = smoothstep(0.0, 0.2, p);',
      '}'
    ].join('\n');

    var fsSrc = [
      'precision mediump float;',
      'uniform vec3 uColor;',
      'varying float vAlpha;',
      'void main(){',
      '  vec2 cxy = 2.0 * gl_PointCoord - 1.0;',
      '  float r = dot(cxy, cxy);',
      '  if (r > 1.0) discard;',
      '  float a = 1.0 - smoothstep(0.7, 1.0, r);',
      '  gl_FragColor = vec4(uColor, a * vAlpha);',
      '}'
    ].join('\n');

    function compile(type, src) {
      var s = gl.createShader(type);
      gl.shaderSource(s, src);
      gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
        console.error('Magic Dust shader:', gl.getShaderInfoLog(s));
        return null;
      }
      return s;
    }
    var vs = compile(gl.VERTEX_SHADER, vsSrc);
    var fs = compile(gl.FRAGMENT_SHADER, fsSrc);
    if (!vs || !fs) return;
    var prog = gl.createProgram();
    gl.attachShader(prog, vs);
    gl.attachShader(prog, fs);
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
      console.error('Magic Dust link:', gl.getProgramInfoLog(prog));
      return;
    }
    gl.useProgram(prog);

    var loc = {
      aPosition: gl.getAttribLocation(prog, 'aPosition'),
      aTarget:   gl.getAttribLocation(prog, 'aTarget'),
      aDelay:    gl.getAttribLocation(prog, 'aDelay'),
      aSize:     gl.getAttribLocation(prog, 'aSize'),
      uProgress: gl.getUniformLocation(prog, 'uProgress'),
      uPointSize:gl.getUniformLocation(prog, 'uPointSize'),
      uColor:    gl.getUniformLocation(prog, 'uColor'),
      uProj:     gl.getUniformLocation(prog, 'projectionMatrix'),
      uView:     gl.getUniformLocation(prog, 'modelViewMatrix')
    };

    var origin = scatteredPositions(COUNT, SCATTER_R);
    var sizes = new Float32Array(COUNT);
    for (var s=0; s<COUNT; s++) sizes[s] = Math.random()*0.8 + 0.4;
    var targets = buildTargets();
    var curIdx = 0;

    function makeAttr(data, size, locId) {
      var b = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, data, gl.DYNAMIC_DRAW);
      return { buffer: b, size: size, loc: locId };
    }
    var attrs = {
      pos:  makeAttr(origin, 3, loc.aPosition),
      tgt:  makeAttr(targets[0].dest, 3, loc.aTarget),
      del:  makeAttr(targets[0].delays, 1, loc.aDelay),
      sz:   makeAttr(sizes, 1, loc.aSize)
    };

    function setTarget(idx) {
      var t = targets[idx];
      gl.bindBuffer(gl.ARRAY_BUFFER, attrs.tgt.buffer);
      gl.bufferSubData(gl.ARRAY_BUFFER, 0, t.dest);
      gl.bindBuffer(gl.ARRAY_BUFFER, attrs.del.buffer);
      gl.bufferSubData(gl.ARRAY_BUFFER, 0, t.delays);
    }

    // ---- State machine ----
    var phase = 'CONSTRUCTING';
    var timer = 0;
    var curProgress = 0;
    var tgtProgress = 0;
    var rotation = 0;    // Y axis (existing auto-spin)
    var rotX = 0;        // X axis (pitch) вЂ” keyboard controlled
    var rotZ = 0;        // Z axis (roll)  вЂ” keyboard controlled
    var targetRotX = 0, targetRotZ = 0;
    var keys = {};

    // Keyboard controls (when hero is in view). Canvas is pointer-events:none
    // because it overlays hero CTAs вЂ” so drag would break buttons. Keys are safe.
    // ArrowLeft/Right  = roll (Z axis)
    // ArrowUp/Down     = pitch (X axis)
    // Space            = reset to 0,0
    window.addEventListener('keydown', function (e) {
      if (!visible) return;
      var k = e.key;
      if (k === 'ArrowLeft' || k === 'ArrowRight' || k === 'ArrowUp' || k === 'ArrowDown' || k === ' ') {
        // Only prevent default if hero is likely the focus (not in input/form)
        var tag = (document.activeElement && document.activeElement.tagName) || '';
        if (tag !== 'INPUT' && tag !== 'TEXTAREA' && tag !== 'SELECT') {
          e.preventDefault();
          if (k === ' ') { targetRotX = 0; targetRotZ = 0; }
          if (k === 'ArrowLeft')  targetRotZ -= 0.15;
          if (k === 'ArrowRight') targetRotZ += 0.15;
          if (k === 'ArrowUp')    targetRotX -= 0.15;
          if (k === 'ArrowDown')  targetRotX += 0.15;
        }
      }
    });

    // ---- Matrix helpers ----
    function perspective(fovy, aspect, near, far) {
      var f = 1.0 / Math.tan(fovy/2);
      var nf = 1 / (near - far);
      return new Float32Array([
        f/aspect, 0, 0, 0,
        0, f, 0, 0,
        0, 0, (far+near)*nf, -1,
        0, 0, 2*far*near*nf, 0
      ]);
    }

    // ---- Resize ----
    function resize() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = canvas.clientWidth * dpr;
      var h = canvas.clientHeight * dpr;
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w; canvas.height = h;
      }
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    window.addEventListener('resize', resize);

    // ---- Visibility gating ----
    var visible = true;
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
      }, { rootMargin: '50px' });
      io.observe(canvas);
    }

    // ---- Render loop ----
    gl.enable(gl.BLEND);
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE);
    gl.disable(gl.DEPTH_TEST);

    var lastT = performance.now();
    function frame(now) {
      var dt = Math.min((now - lastT) / 1000, 0.05);
      lastT = now;

      if (reduce || !visible) {
        requestAnimationFrame(frame);
        return;
      }

      if (phase === 'CONSTRUCTING') {
        tgtProgress = Math.min(1.5, tgtProgress + dt * 0.4 * SPEED);
        if (tgtProgress >= 1.5) { phase = 'HOLDING'; timer = 0; }
      } else if (phase === 'HOLDING') {
        timer += dt;
        if (timer > HOLD_SEC) phase = 'DECONSTRUCTING';
      } else {
        tgtProgress = Math.max(0.0, tgtProgress - dt * 0.6 * SPEED);
        if (tgtProgress <= 0.0) {
          curIdx = (curIdx + 1) % targets.length;
          setTarget(curIdx);
          phase = 'CONSTRUCTING';
        }
      }
      curProgress += (tgtProgress - curProgress) * 0.1;

      var t = targets[curIdx];
      // All logos spin 359° around Y during HOLD phase.
      // CONSTRUCTING: rotation stays 0 (particles assemble head-on).
      // HOLDING:      rotation eases from 0 → 359° (~6.2657 rad) across HOLD_SEC.
      // DECONSTRUCT:  rotation snaps to nearest 2π so next logo starts at 0°.
      if (phase === 'CONSTRUCTING') {
        rotation += (0 - rotation) * 0.12;
      } else if (phase === 'HOLDING') {
        // 359° in radians
        var SPIN_TARGET = 6.2657;
        var spinEase = Math.min(timer / HOLD_SEC, 1);
        // easeInOutSine for a smooth, cinematic turn (slow start, fast mid, slow end)
        var eased = -(Math.cos(Math.PI * spinEase) - 1) / 2;
        var desired = SPIN_TARGET * eased;
        rotation += (desired - rotation) * 0.18;
      } else {
        // DECONSTRUCTING: snap rotation to nearest 2π multiple
        var snapped = Math.round(rotation / (Math.PI*2)) * (Math.PI*2);
        rotation += (snapped - rotation) * 0.12;
      }
      // Ease user-controlled pitch/roll toward target
      rotX += (targetRotX - rotX) * 0.1;
      rotZ += (targetRotZ - rotZ) * 0.1;

      resize();
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT);

      gl.useProgram(prog);
      var aspect = canvas.width / canvas.height;
      var proj = perspective(45 * Math.PI/180, aspect, 0.1, 100);
      // View = Translate(0,0,-9) Г— R_x Г— R_y Г— R_z (column-major composition)
      var cx = Math.cos(rotX), sx = Math.sin(rotX);
      var cy = Math.cos(rotation), sy = Math.sin(rotation); // rotation = Y axis (auto-spin)
      var cz = Math.cos(rotZ), sz = Math.sin(rotZ);

      // R_y = [ cy 0 -sy 0; 0 1 0 0; sy 0 cy 0; 0 0 0 1 ] (column-major)
      // R_x = [ 1 0 0 0; 0 cx -sx 0; 0 sx cx 0; 0 0 0 1 ]
      // R_z = [ cz -sz 0 0; sz cz 0 0; 0 0 1 0; 0 0 0 1 ]
      // Compose Ry then Rx then Rz then translate. Final translation Z = -9.
      // Standard formula: view = Ry В· Rx В· Rz, then set view[14] = -9.
      // Compute step-by-step (each result stored in 16-element column-major array).
      function mul(a, b) {
        var r = new Float32Array(16);
        for (var col = 0; col < 4; col++) {
          for (var row = 0; row < 4; row++) {
            r[col*4 + row] = a[0*4+row]*b[col*4+0] + a[1*4+row]*b[col*4+1] + a[2*4+row]*b[col*4+2] + a[3*4+row]*b[col*4+3];
          }
        }
        return r;
      }
      var Ry = new Float32Array([ cy,0,sy,0,  0,1,0,0,  -sy,0,cy,0,  0,0,0,1 ]);
      var Rx = new Float32Array([ 1,0,0,0,  0,cx,sx,0,  0,-sx,cx,0,  0,0,0,1 ]);
      var Rz = new Float32Array([ cz,sz,0,0,  -sz,cz,0,0,  0,0,1,0,  0,0,0,1 ]);
      var R = mul(mul(Ry, Rx), Rz);
      // Translate(0,0,-9): column-major, translation in indices 12,13,14
      var view = R;
      view[12] = 0; view[13] = 0; view[14] = -9;

      gl.uniformMatrix4fv(loc.uProj, false, proj);
      gl.uniformMatrix4fv(loc.uView, false, view);
      gl.uniform1f(loc.uProgress, curProgress);
      gl.uniform1f(loc.uPointSize, Math.min(window.innerWidth, window.innerHeight) * 0.02);
      gl.uniform3f(loc.uColor, 1.0, 0.85, 0.55);

      for (var key in attrs) {
        var a = attrs[key];
        gl.bindBuffer(gl.ARRAY_BUFFER, a.buffer);
        gl.enableVertexAttribArray(a.loc);
        gl.vertexAttribPointer(a.loc, a.size, gl.FLOAT, false, 0, 0);
      }

      gl.drawArrays(gl.POINTS, 0, COUNT);

      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  // ---- Load all cars, then start ----
  var carSrcs = SEQUENCE.filter(function (x) { return x.type === 'car'; }).map(function (x) { return x.src; });
  Promise.all(carSrcs.map(loadCar)).then(start).catch(function (err) {
    console.error('Magic Dust: car load failed', err);
  });
})();
