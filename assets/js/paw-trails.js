/* Tropy łapek wzdłuż podstron (blog, wpisy, changelog, Poznajcie pupili, FAQ, 404).
   Ta sama mechanika co `.side-trails` w `index.html`: zwierzę schodzi w dół marginesem obok
   treści, ślady w trzech rozmiarach, odcinki po 8 kroków ruszają, gdy wjadą w kadr.
   Zmieniasz rytm, rozmiary albo krycie tutaj? Zmień też skrypt na dole `index.html`. */
(function () {
  var mainEl = document.querySelector('main');
  if (!mainEl) return;
  var trails = document.createElement('div');
  trails.className = 'paw-trail side-trails'; trails.setAttribute('aria-hidden', 'true');
  document.body.appendChild(trails);
  var trailObs = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { e.target.classList.toggle('go', e.isIntersecting); });
  }, { threshold: 0 }) : null;
  var SIZES = [42, 32, 24], WALK = { step: 60, t: .55 }, seed = 7;
  var CONTENT = 1080, PAD = 22; /* .wrap i .related: najszersza kolumna treści na podstronach */
  function pickSize() { seed = (seed * 9301 + 49297) % 233280; return SIZES[Math.floor(seed / 233280 * 3)]; }
  function pawTrail(box, x0, y0, x1, y1, paw, amp, ph0, off) {
    var dx = x1 - x0, dy = y1 - y0, len = Math.sqrt(dx * dx + dy * dy);
    var n = Math.max(3, Math.floor(len / paw.step)), ux = dx / len, uy = dy / len;
    var dir = Math.atan2(dy, dx) * 57.3 + 90, spread = 10, pts = [];
    for (var k = 0; k < n; k++) {
      var ph = k * 0.45 + ph0, foot = k % 2 ? 1 : -1, d = k * paw.step;
      var side = Math.sin(ph) * amp + foot * spread;
      var turn = Math.cos(ph) * amp * 0.45 / paw.step * 57.3;
      pts.push({ x: x0 + ux * d - uy * side, y: y0 + uy * d + ux * side, r: dir - turn + foot * 7, sz: pickSize() });
    }
    for (var c = 0; c < n; c += 8) {
      var part = pts.slice(c, c + 8), m = SIZES[0];
      var bx = Math.min.apply(null, part.map(function (q) { return q.x; })) - m;
      var by = Math.min.apply(null, part.map(function (q) { return q.y; })) - m;
      var seg = document.createElement('span'), html = '';
      part.forEach(function (q, k) {
        html += '<i style="--i:' + k + ';--sz:' + q.sz + 'px;--x:' + (q.x - bx).toFixed(1) + 'px;--y:' + (q.y - by).toFixed(1) +
          'px;--r:' + q.r.toFixed(0) + 'deg"></i>';
      });
      seg.className = 'seg'; seg.innerHTML = html;
      seg.style.left = bx.toFixed(1) + 'px'; seg.style.top = by.toFixed(1) + 'px';
      seg.style.width = (Math.max.apply(null, part.map(function (q) { return q.x; })) - bx + m).toFixed(1) + 'px';
      seg.style.height = (Math.max.apply(null, part.map(function (q) { return q.y; })) - by + m).toFixed(1) + 'px';
      seg.style.setProperty('--t', paw.t + 's');
      seg.style.setProperty('--dur', (part.length * paw.t + 4).toFixed(1) + 's');
      seg.style.setProperty('--off', off.toFixed(1) + 's');
      box.appendChild(seg);
      if (trailObs) trailObs.observe(seg); else seg.classList.add('go');
    }
  }
  function lanes(x, w) {
    var c = Math.max(1, Math.min(2, Math.floor(w / 170))), lw = w / c, out = [];
    for (var l = 0; l < c; l++) out.push({ cx: x + lw * (l + .5), w: lw });
    return out;
  }
  var lastKey = '';
  function drawTrails() {
    var W = document.documentElement.clientWidth, rail = 70; /* pasek ikon po prawej */
    var gut = (W - CONTENT) / 2 + PAD;
    var on = gut >= 110;
    /* Wpis zaczyna się od pełnej szerokości kolorowej okładki: trop rusza pod nią. */
    var top0 = mainEl.getBoundingClientRect().top + window.scrollY;
    var cover = mainEl.querySelector('.post-hero');
    var start = cover ? cover.getBoundingClientRect().bottom + window.scrollY : top0 + 90;
    var end = top0 + mainEl.offsetHeight - 10;
    var key = W + ':' + Math.round(start) + ':' + Math.round(end);
    if (key === lastKey) return;
    lastKey = key;
    if (trailObs) trailObs.disconnect();
    seed = 7;
    trails.innerHTML = '';
    document.body.classList.toggle('has-trails', on);
    trails.style.display = on ? '' : 'none';
    if (!on || end - start < 200) return;
    trails.style.top = start + 'px'; trails.style.height = (end - start) + 'px';
    var cols = lanes(0, gut);
    if (gut - rail >= 110) cols = cols.concat(lanes(W - gut, gut - rail));
    var h = end - start;
    cols.forEach(function (c, ci) {
      pawTrail(trails, c.cx, 30 + ci * 23, c.cx, h, WALK, Math.min(c.w * 0.16, 22), ci * 2.4, ci * 1.3);
    });
  }
  var timer;
  function later() { clearTimeout(timer); timer = setTimeout(drawTrails, 200); }
  drawTrails();
  window.addEventListener('load', drawTrails);
  window.addEventListener('resize', later);
  /* Wysokość treści zmienia się po doczytaniu obrazków i po przełączeniu języka w FAQ. */
  if ('ResizeObserver' in window) new ResizeObserver(later).observe(mainEl);
})();
