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
