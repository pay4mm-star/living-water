/* Interlock wash, sand & seal estimator — no dependencies. $3.50 per sq ft, HST added. */
(function () {
  var root = document.getElementById('estimator');
  if (!root) return;
  var RATE = parseFloat(root.dataset.rate) || 3.5, HST = parseFloat(root.dataset.hst) || 0.13, M2 = 10.7639;
  var rowsEl = root.querySelector('#est-rows'), unit = 'ft', fired = false;
  var TYPES = ['Driveway', 'Front walkway', 'Backyard patio', 'Steps & landing', 'Pool deck', 'Side path', 'Other area'];
  var money = function (n) { return n.toLocaleString('en-CA', { style: 'currency', currency: 'CAD' }); };
  var num = function (v) { v = parseFloat(v); return isFinite(v) && v > 0 ? v : 0; };

  function rowHtml(type, l, w, mode) {
    var opts = TYPES.map(function (t) { return '<option' + (t === type ? ' selected' : '') + '>' + t + '</option>'; }).join('');
    return '<div class="est-row" data-mode="' + (mode || 'lw') + '">' +
      '<label class="r-t">Area<select class="r-type">' + opts + '</select></label>' +
      '<label class="r-lw">Length (<span class="u">' + unit + '</span>)<input class="r-l" type="number" min="0" step="any" inputmode="decimal" value="' + (l || '') + '" placeholder="0"></label>' +
      '<label class="r-lw">Width (<span class="u">' + unit + '</span>)<input class="r-w" type="number" min="0" step="any" inputmode="decimal" value="' + (w || '') + '" placeholder="0"></label>' +
      '<label class="r-sfl">Total sq <span class="u2">' + (unit === 'ft' ? 'ft' : 'm') + '</span><input class="r-s" type="number" min="0" step="any" inputmode="decimal" placeholder="0"></label>' +
      '<div class="r-out"><b class="r-sf">0</b> sq ft<button type="button" class="r-mode">' + 'Know total sq ' + (unit === 'ft' ? 'ft' : 'm') + '?</button></div>' +
      '<button type="button" class="r-del" aria-label="Remove this area">&times;</button></div>';
  }

  function addRow(type, l, w) {
    var d = document.createElement('div'); d.innerHTML = rowHtml(type || 'Driveway', l, w); rowsEl.appendChild(d.firstChild); calc();
  }

  function rowSqft(r) {
    var sf = r.dataset.mode === 'sf' ? num(r.querySelector('.r-s').value) : num(r.querySelector('.r-l').value) * num(r.querySelector('.r-w').value);
    return unit === 'm' ? sf * M2 : sf;
  }

  function calc() {
    var total = 0, lines = [];
    rowsEl.querySelectorAll('.est-row').forEach(function (r) {
      var sf = rowSqft(r); total += sf;
      r.querySelector('.r-sf').textContent = Math.round(sf).toLocaleString('en-CA');
      if (sf > 0) lines.push(r.querySelector('.r-type').value + ': ' + Math.round(sf) + ' sq ft');
    });
    total = Math.round(total);
    var sub = total * RATE, tax = sub * HST;
    root.querySelector('#est-area').textContent = total.toLocaleString('en-CA') + ' sq ft';
    root.querySelector('#est-sub').textContent = money(sub);
    root.querySelector('#est-hst').textContent = money(tax);
    root.querySelector('#est-total').textContent = money(sub + tax);
    root.classList.toggle('has-total', total > 0);
    var f = document.getElementById('est-quote-form');
    if (f) {
      f.querySelector('[name=estimate_sqft]').value = total;
      f.querySelector('[name=estimate_before_hst]').value = total ? money(sub) : '';
      f.querySelector('[name=estimate_details]').value = lines.join(' | ');
      f.querySelector('[name=subject]').value = 'Interlock quote request' + (total ? ' — ' + total + ' sq ft, about ' + money(sub) + ' + HST' : '') + ' — livingwater-pws.com';
    }
    if (total > 0 && !fired) { fired = true; if (window.gtag) gtag('event', 'estimate_calculated', { value: Math.round(sub), currency: 'CAD', sqft: total }); }
  }

  rowsEl.addEventListener('input', calc);
  rowsEl.addEventListener('change', calc);
  rowsEl.addEventListener('click', function (e) {
    var r = e.target.closest('.est-row'); if (!r) return;
    if (e.target.closest('.r-del')) { if (rowsEl.children.length > 1) r.remove(); else { r.querySelectorAll('input').forEach(function (i) { i.value = ''; }); } calc(); }
    if (e.target.closest('.r-mode')) { r.dataset.mode = r.dataset.mode === 'sf' ? 'lw' : 'sf'; var b = e.target.closest('.r-mode'); b.textContent = r.dataset.mode === 'sf' ? 'Use length × width' : 'Know total sq ' + (unit === 'ft' ? 'ft' : 'm') + '?'; calc(); }
  });
  root.querySelector('#est-add').addEventListener('click', function () { addRow('Other area'); });
  root.querySelectorAll('[data-preset]').forEach(function (b) {
    b.addEventListener('click', function () {
      var p = b.dataset.preset.split('|'), l = +p[1], w = +p[2];
      if (unit === 'm') { l = Math.round(l / 3.281 * 10) / 10; w = Math.round(w / 3.281 * 10) / 10; }
      var first = rowsEl.children[0];
      if (rowsEl.children.length === 1 && rowSqft(first) === 0) rowsEl.innerHTML = '';
      addRow(p[0], l, w);
    });
  });
  root.querySelectorAll('[data-unit]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (unit === b.dataset.unit) return;
      unit = b.dataset.unit;
      root.querySelectorAll('[data-unit]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      root.querySelectorAll('.u').forEach(function (s) { s.textContent = unit; });
      root.querySelectorAll('.u2').forEach(function (s) { s.textContent = unit === 'ft' ? 'ft' : 'm'; });
      rowsEl.querySelectorAll('.r-mode').forEach(function (m) { var r = m.closest('.est-row'); m.textContent = r.dataset.mode === 'sf' ? 'Use length × width' : 'Know total sq ' + (unit === 'ft' ? 'ft' : 'm') + '?'; });
      calc();
    });
  });
  addRow('Driveway');
})();
