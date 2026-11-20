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
    var grid = bar.parentElement.querySelector('.filterable'); if (!grid) return;
    var items = grid.querySelectorAll('[data-cat]');
    function apply(f) {
      bar.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.filter === f); });
      items.forEach(function (it) { it.hidden = !(f === 'all' || (' ' + it.dataset.cat + ' ').indexOf(' ' + f + ' ') > -1); });
      // hide filter buttons with no matches
    }
    bar.querySelectorAll('button').forEach(function (b) {
      var f = b.dataset.filter;
      if (f !== 'all' && !grid.querySelector('[data-cat~="' + f + '"]')) b.style.display = 'none';
      b.addEventListener('click', function () { apply(f); history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f); });
    });
    var h = location.hash.slice(1); if (h && bar.querySelector('[data-filter="' + h + '"]')) apply(h);
  });
  // play only one video at a time
  document.addEventListener('play', function (e) { document.querySelectorAll('video').forEach(function (v) { if (v !== e.target) v.pause(); }); }, true);
})();
// gallery: show-more pagination that cooperates with filters
(function () {
  var grid = document.querySelector('.masonry.filterable[data-page]'), btn = document.querySelector('.load-more');
  if (!grid || !btn) return;
  var page = +grid.dataset.page, shown = page;
  function refresh() {
    var filtered = document.querySelector('.filters [aria-pressed=true]');
    var f = filtered ? filtered.dataset.filter : 'all';
    var n = 0;
    grid.querySelectorAll('[data-cat]').forEach(function (it) {
      var match = f === 'all' || (' ' + it.dataset.cat + ' ').indexOf(' ' + f + ' ') > -1;
      if (match) { n++; it.hidden = n > shown; } else it.hidden = true;
    });
    btn.parentElement.style.display = n > shown ? '' : 'none';
  }
  btn.addEventListener('click', function () { shown += page; refresh(); });
  document.querySelectorAll('.filters button').forEach(function (b) { b.addEventListener('click', function () { shown = page; setTimeout(refresh, 0); }); });
  grid.querySelectorAll('.more').forEach(function (x) { x.classList.remove('more'); });
  refresh();
})();
