/*! Get2FA UI. Secrets live only in this page's memory: never stored, never sent. */
(function () {
  'use strict';
  var T = window.TOTP;
  var L = window.I18N || {};
  var $ = function (s) { return document.querySelector(s); };
  var input = $('#secret'), results = $('#results'), bulkWrap = $('#bulkWrap'), bulkOut = $('#bulkOut');
  var algSel = $('#alg'), digSel = $('#digits'), perSel = $('#period'), autoCopy = $('#autoCopy');
  var entries = [], timer = null, lastAutoCopied = '';
  var CIRC = 2 * Math.PI * 20;

  function pref(k, v) {
    try { if (v === undefined) return localStorage.getItem('q2fa.' + k); localStorage.setItem('q2fa.' + k, v); } catch (e) { return null; }
  }

  /* ---------- toast & clipboard ---------- */
  var toastEl = $('#toast'), toastT;
  function toast(msg) {
    toastEl.textContent = msg; toastEl.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.classList.remove('show'); }, 1800);
  }
  function copy(text, msg) {
    var done = function () { toast(msg || L.copied); };
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
    }
    fallbackCopy(text); done(); return Promise.resolve();
  }
  function fallbackCopy(text) {
    var t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', '');
    t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select();
    try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(t);
  }

  function fmt(code) {
    var h = Math.ceil(code.length / 2);
    return code.slice(0, h) + ' ' + code.slice(h);
  }

  /* ---------- parsing ---------- */
  function parseAll() {
    var out = T.parseInput(input.value);
    out.forEach(function (e) {
      if (!e.error && !/^otpauth:/i.test(e.raw)) {
        e.algorithm = algSel.value; e.digits = +digSel.value; e.period = +perSel.value;
      }
      if (!e.error && e.type && e.type !== 'totp') e.error = 'hotp';
    });
    return out;
  }

  /* ---------- rendering ---------- */
  function ringSvg() {
    return '<svg viewBox="0 0 48 48" aria-hidden="true"><circle class="track" cx="24" cy="24" r="20"/>' +
      '<circle class="bar" cx="24" cy="24" r="20" stroke-dasharray="' + CIRC.toFixed(2) + '"/></svg><b></b>';
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }

  function render() {
    entries = parseAll();
    results.innerHTML = '';
    var valid = entries.filter(function (e) { return !e.error; });
    if (!entries.length) {
      results.innerHTML = '<div class="empty">' + esc(L.empty) + '</div>';
      bulkWrap.hidden = true; return;
    }
    var single = valid.length === 1 && entries.length === 1;
    entries.forEach(function (e, i) {
      var el = document.createElement('div');
      if (e.error) {
        el.className = 'card err';
        el.innerHTML = esc(e.error === 'hotp' ? L.hotp : L.invalid) + ' <code>' + esc(e.raw.length > 80 ? e.raw.slice(0, 80) + '…' : e.raw) + '</code>';
      } else {
        el.className = 'card' + (single ? ' single' : '');
        el.innerHTML = '<div class="ring">' + ringSvg() + '</div>' +
          '<div class="meta"><div class="name">' + esc(e.label || (L.key + ' ' + (i + 1))) + ' · ' + esc(e.secret.slice(0, 4)) + '…' + esc(e.secret.slice(-4)) + '</div>' +
          '<button class="code" type="button" title="' + esc(L.clickCopy) + '" aria-live="polite">— — —</button>' +
          '<div class="next">' + esc(L.next) + ' <span class="nv">…</span></div></div>' +
          '<button class="btn primary cp" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><span>' + esc(L.copy) + '</span></button>';
        var cp = function () { if (e.code) copy(e.code); };
        el.querySelector('.code').addEventListener('click', cp);
        el.querySelector('.cp').addEventListener('click', cp);
      }
      e.el = el; e.counter = -1;
      results.appendChild(el);
    });
    bulkWrap.hidden = valid.length < 2;
    tick(true);
  }

  async function tick(force) {
    var now = Date.now(), changed = false;
    await Promise.all(entries.map(async function (e) {
      if (e.error) return;
      var p = e.period, c = T.counterAt(now, p);
      var left = p - (now / 1000) % p;
      var ring = e.el.querySelector('.ring');
      ring.querySelector('.bar').style.strokeDashoffset = (CIRC * (1 - left / p)).toFixed(2);
      ring.querySelector('b').textContent = Math.ceil(left);
      var low = left <= 5;
      ring.classList.toggle('low', low); e.el.classList.toggle('low-code', low);
      if (c !== e.counter || force === true) {
        e.counter = c;
        try {
          var o = { algorithm: e.algorithm, digits: e.digits, period: p };
          var r = await Promise.all([T.hotp(e.secret, c, o), T.hotp(e.secret, c + 1, o)]);
          e.code = r[0];
          e.el.querySelector('.code').textContent = fmt(r[0]);
          e.el.querySelector('.nv').textContent = fmt(r[1]);
          changed = true;
        } catch (err) {
          e.el.className = 'card err'; e.el.textContent = L.invalid + ' ' + e.raw; e.error = true;
        }
      }
    }));
    if (changed) afterUpdate();
  }

  function afterUpdate() {
    var valid = entries.filter(function (e) { return !e.error && e.code; });
    if (valid.length > 1) bulkOut.value = valid.map(function (e) { return e.raw + '|' + e.code; }).join('\n');
    if (autoCopy.checked && valid.length === 1 && entries.length === 1) {
      var key = valid[0].secret + valid[0].code;
      if (key !== lastAutoCopied && document.hasFocus()) { lastAutoCopied = key; copy(valid[0].code, L.autoCopied); }
    }
  }

  function start() { clearInterval(timer); timer = setInterval(tick, 250); }

  /* ---------- input wiring ---------- */
  var deb;
  input.addEventListener('input', function () { clearTimeout(deb); deb = setTimeout(render, 120); });
  [algSel, digSel, perSel].forEach(function (s) { s.addEventListener('change', render); });
  autoCopy.checked = pref('autocopy') === '1';
  autoCopy.addEventListener('change', function () { pref('autocopy', autoCopy.checked ? '1' : '0'); lastAutoCopied = ''; afterUpdate(); });

  $('#pasteBtn').addEventListener('click', function () {
    if (!navigator.clipboard || !navigator.clipboard.readText) { input.focus(); toast(L.pasteManual); return; }
    navigator.clipboard.readText().then(function (t) { input.value = t.trim(); render(); }, function () { input.focus(); toast(L.pasteManual); });
  });
  $('#clearBtn').addEventListener('click', function () {
    input.value = ''; lastAutoCopied = '';
    if (location.hash) history.replaceState(null, '', location.pathname + location.search);
    render(); input.focus();
  });
  $('#copyAllBtn').addEventListener('click', function () { copy(bulkOut.value, L.copiedAll); });
  $('#shareBtn').addEventListener('click', function () {
    var v = entries.filter(function (e) { return !e.error; });
    if (!v.length) { toast(L.noKey); return; }
    var link = location.origin + location.pathname + '#' + encodeURIComponent(v.map(function (e) { return e.secret; }).join(','));
    copy(link, L.linkCopied);
    $('#shareNote').hidden = false;
  });

  /* ---------- #SECRET links (fragment is never sent to the server) ---------- */
  function fromHash() {
    var h = decodeURIComponent(location.hash.slice(1) || '');
    if (!h) return;
    input.value = h.split(',').join('\n'); render();
  }
  window.addEventListener('hashchange', fromHash);

  /* ---------- QR codes: upload, paste or drop an image ---------- */
  var qrFile = $('#qrFile');
  $('#qrBtn').addEventListener('click', function () { qrFile.click(); });
  qrFile.addEventListener('change', function () { if (qrFile.files[0]) readQr(qrFile.files[0]); qrFile.value = ''; });
  document.addEventListener('paste', function (ev) {
    var items = (ev.clipboardData && ev.clipboardData.items) || [];
    for (var i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image/') === 0) { ev.preventDefault(); readQr(items[i].getAsFile()); return; }
    }
  });
  var tool = $('.tool');
  ['dragenter', 'dragover'].forEach(function (t) { tool.addEventListener(t, function (e) { e.preventDefault(); tool.classList.add('dropping'); }); });
  ['dragleave', 'drop'].forEach(function (t) { tool.addEventListener(t, function () { tool.classList.remove('dropping'); }); });
  tool.addEventListener('drop', function (e) {
    e.preventDefault();
    var f = e.dataTransfer.files[0];
    if (f && f.type.indexOf('image/') === 0) readQr(f);
    else { var t = e.dataTransfer.getData('text'); if (t) { input.value = t; render(); } }
  });

  /* QR decoding lives in qrread.js (shared with the QR reader page) */
  function decodeImage(file) { return window.QRRead.decodeImage(file); }

  async function readQr(file) {
    var values;
    try { values = await decodeImage(file); }
    catch (e) { toast(L.qrUnsupported); return; }
    var found = values.filter(function (v) { return /^otpauth(-migration)?:\/\//i.test(v); });
    if (!found.length) { toast(L.qrNotFound); return; }
    input.value = (input.value.trim() ? input.value.trim() + '\n' : '') + found.join('\n');
    render(); toast(L.qrAdded);
  }

  /* ---------- theme ---------- */
  var root = document.documentElement;
  var saved = pref('theme'); if (saved) root.setAttribute('data-theme', saved);
  $('#themeBtn').addEventListener('click', function () {
    var dark = root.getAttribute('data-theme') ? root.getAttribute('data-theme') === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next); pref('theme', next);
  });

  /* ---------- clock check: TOTP depends on the device clock ---------- */
  document.addEventListener('visibilitychange', function () { if (!document.hidden) tick(true); });

  /* ---------- offline support ---------- */
  if ('serviceWorker' in navigator && location.protocol === 'https:' && window.top === window.self) {
    navigator.serviceWorker.register((root.getAttribute('data-root') || '/') + 'sw.js').catch(function () {});
  }

  render(); fromHash(); start();
  if (!input.value) input.focus({ preventScroll: true });
})();

/* Keep users coming back: bookmark hint + install button (shown once, dismissible) */
(function () {
  var bar = document.getElementById('keepBar'); if (!bar) return;
  var seen; try { seen = localStorage.getItem('q2fa.keep'); } catch (e) {}
  var installBtn = document.getElementById('installBtn'), deferred = null;
  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault(); deferred = e; installBtn.hidden = false;
  });
  installBtn.addEventListener('click', function () {
    if (!deferred) return; deferred.prompt();
    deferred.userChoice.finally(function () { deferred = null; installBtn.hidden = true; });
  });
  document.getElementById('keepOk').addEventListener('click', function () {
    bar.hidden = true; try { localStorage.setItem('q2fa.keep', '1'); } catch (e) {}
  });
  // show after the first code is generated, so it never gets in the way
  if (!seen) {
    var obs = new MutationObserver(function () {
      if (document.querySelector('#results .card:not(.err)')) { bar.hidden = false; obs.disconnect(); }
    });
    obs.observe(document.getElementById('results'), { childList: true });
  }
})();
