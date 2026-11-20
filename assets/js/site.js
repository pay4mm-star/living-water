// Living Water — small progressive enhancements (no dependencies)
(function () {
  var toggle = document.querySelector('.menu-toggle'), nav = document.getElementById('nav');
  if (toggle && nav) toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open'); toggle.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('.has-sub > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement, open = li.classList.toggle('open'); b.setAttribute('aria-expanded', open);
    });
  });
  // before/after sliders
  document.querySelectorAll('.ba').forEach(function (ba) {
    var r = ba.querySelector('input'), a = ba.querySelector('.after'), bar = ba.querySelector('.bar');
    function set() { a.style.clipPath = 'inset(0 0 0 ' + r.value + '%)'; bar.style.left = r.value + '%'; }
    r.addEventListener('input', set); set();
  });
  // lightbox
  var lb = document.querySelector('.lightbox');
  if (lb) {
    var img = lb.querySelector('img'), cap = lb.querySelector('p');
    document.querySelectorAll('.masonry img').forEach(function (el) {
      el.addEventListener('click', function () {
        img.src = el.dataset.full || el.currentSrc; img.alt = el.alt; cap.textContent = el.alt; lb.classList.add('open');
      });
    });
    lb.addEventListener('click', function (e) { if (e.target !== img) lb.classList.remove('open'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('open'); });
  }
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
// preselect service on contact form from ?service=
(function () {
  var p = new URLSearchParams(location.search).get('service'), sel = document.getElementById('sv');
  if (p && sel) { [].forEach.call(sel.options, function (o) { if (o.text.toLowerCase().indexOf(p.toLowerCase()) === 0) sel.value = o.value || o.text; }); }
})();
// gallery / projects filters
(function () {
  document.querySelectorAll('.filters').forEach(function (bar) {
    var grid = (bar.closest('section') || document).querySelector('.filterable'); if (!grid) return;
    var items = grid.querySelectorAll('[data-cat]');
    function apply(f) {
      bar.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.filter === f); });
      items.forEach(function (it) { it.hidden = !(f === 'all' || (' ' + it.dataset.cat + ' ').indexOf(' ' + f + ' ') > -1); });
      // hide filter buttons with no matches
    }
    bar.querySelectorAll('button').forEach(function (b) {
      var f = b.dataset.filter;
      var tp = document.getElementById('more-tiles');
      if (f !== 'all' && !grid.querySelector('[data-cat~="' + f + '"]') && !(tp && tp.content.querySelector('[data-cat~="' + f + '"]'))) b.style.display = 'none';
      b.addEventListener('click', function () { apply(f); history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f); });
    });
    var h = location.hash.slice(1); if (h && bar.querySelector('[data-filter="' + h + '"]')) apply(h);
  });
  // play only one video at a time
  document.addEventListener('play', function (e) { document.querySelectorAll('video').forEach(function (v) { if (v !== e.target) v.pause(); }); }, true);
})();
// gallery v2: filters + paging + counts + media viewer
(function () {
  var grid = document.querySelector('.tiles.filterable');
  if (!grid) return;
  var page = +grid.dataset.page || 24, shown = page, btn = document.querySelector('.load-more'), count = document.querySelector('.gcount');
  var tpl = document.getElementById('more-tiles'), loaded = !tpl;
  function loadAll() { if (loaded) return; grid.appendChild(tpl.content.cloneNode(true)); loaded = true; tiles = [].slice.call(grid.querySelectorAll('.tile')); bindSliders(grid); }
  function bindSliders(root) {
    root.querySelectorAll('.ba').forEach(function (ba) {
      if (ba.dataset.bound) return; ba.dataset.bound = 1;
      var r = ba.querySelector('input'), a = ba.querySelector('.after'), bar = ba.querySelector('.bar');
      function set() { a.style.clipPath = 'inset(0 0 0 ' + r.value + '%)'; bar.style.left = r.value + '%'; }
      r.addEventListener('input', set); set();
    });
  }
  var tiles = [].slice.call(grid.querySelectorAll('.tile'));
  bindSliders(grid);
  function current() { var b = document.querySelector('.filters [aria-pressed=true]'); return b ? b.dataset.filter : 'all'; }
  function refresh() {
    var f = current(), n = 0;
    if (f !== 'all' || shown > page) loadAll();
    tiles.forEach(function (t) {
      var m = f === 'all' || (' ' + t.dataset.cat + ' ').indexOf(' ' + f + ' ') > -1;
      if (m) n++;
      t.hidden = !m || n > shown;
    });
    var total = loaded ? n : (tpl ? n + tpl.content.querySelectorAll('.tile').length : n);
    if (btn) btn.parentElement.style.display = (loaded ? n > shown : true) ? '' : 'none';
    if (count) count.textContent = 'Showing ' + Math.min(n, shown) + ' of ' + total;
  }
  document.querySelectorAll('.filters button').forEach(function (b) { b.addEventListener('click', function () { shown = page; setTimeout(refresh, 0); }); });
  if (btn) btn.addEventListener('click', function () { shown += page; refresh(); });
  setTimeout(refresh, 0);
  // viewer
  var v = document.querySelector('.viewer'); if (!v) return;
  var stage = v.querySelector('.v-stage'), cap = v.querySelector('.v-cap'), list = [], idx = 0, last;
  function items() { if (!loaded) { loadAll(); refresh(); } return tiles.filter(function (t) { return !t.hidden && t.querySelector('.zoom,.play'); }); }
  function show(i) {
    list = items(); if (!list.length) return; idx = (i + list.length) % list.length;
    var t = list[idx], z = t.querySelector('.zoom'), p = t.querySelector('.play');
    stage.innerHTML = '';
    if (p) { var vid = document.createElement('video'); vid.controls = true; vid.autoplay = true; vid.playsInline = true; vid.poster = p.dataset.poster; vid.src = p.dataset.video; stage.appendChild(vid); }
    else { var im = document.createElement('img'); im.src = z.dataset.full; im.alt = z.querySelector('img').alt; stage.appendChild(im); }
    cap.textContent = t.querySelector('.t').textContent;
  }
  function open(t) { last = document.activeElement; list = items(); show(list.indexOf(t)); v.hidden = false; document.body.style.overflow = 'hidden'; v.querySelector('.v-close').focus(); }
  function close() { v.hidden = true; stage.innerHTML = ''; document.body.style.overflow = ''; if (last) last.focus(); }
  grid.addEventListener('click', function (e) { var b = e.target.closest('.zoom,.play'); if (b) { e.preventDefault(); open(b.closest('.tile')); } });
  v.querySelector('.v-close').addEventListener('click', close);
  v.querySelector('.v-prev').addEventListener('click', function () { show(idx - 1); });
  v.querySelector('.v-next').addEventListener('click', function () { show(idx + 1); });
  v.addEventListener('click', function (e) { if (e.target === v) close(); });
  document.addEventListener('keydown', function (e) { if (v.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1); });
})();
