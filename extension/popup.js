/*! Get2FA extension popup. Codes are computed with Web Crypto on this device.
    Saved keys stay in this browser profile (chrome.storage.local) and are never sent anywhere. */
(async function () {
  'use strict';
  var T = window.TOTP;
  var $ = function (s) { return document.querySelector(s); };
  var hasChrome = typeof chrome !== 'undefined' && chrome.storage && chrome.i18n;

  /* ---------- i18n (falls back to a messages.json fetch when previewed outside Chrome) ---------- */
  var FALLBACK = {};
  if (!hasChrome) {
    var lang = new URLSearchParams(location.search).get('lang') || 'en';
    try { FALLBACK = await (await fetch('_locales/' + lang + '/messages.json')).json(); } catch (e) {}
  }
  function msg(k, sub) {
    var s = hasChrome ? chrome.i18n.getMessage(k, sub) : (FALLBACK[k] && FALLBACK[k].message) || k;
    if (!hasChrome && sub != null) s = s.replace(/\$[A-Z]+\$/, sub);
    return s;
  }
  document.querySelectorAll('[data-i18n]').forEach(function (el) { el.textContent = msg(el.getAttribute('data-i18n')); });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) { el.placeholder = msg(el.getAttribute('data-i18n-placeholder')); });
  document.querySelectorAll('[data-i18n-title]').forEach(function (el) { el.title = msg(el.getAttribute('data-i18n-title')); });
  document.documentElement.lang = hasChrome ? chrome.i18n.getUILanguage() : 'en';

  /* ---------- storage ---------- */
  var store = {
    get: async function () {
      if (hasChrome) return (await chrome.storage.local.get('accounts')).accounts || [];
      try { return JSON.parse(localStorage.getItem('g2fa.accounts') || '[]'); } catch (e) { return []; }
    },
    set: async function (list) {
      if (hasChrome) return chrome.storage.local.set({ accounts: list });
      localStorage.setItem('g2fa.accounts', JSON.stringify(list));
    }
  };

  var saved = await store.get();
  var temp = [];

  /* ---------- helpers ---------- */
  var toastEl = document.createElement('div'); toastEl.className = 'toast'; document.body.appendChild(toastEl);
  var toastT;
  function toast(s) { toastEl.textContent = s; toastEl.classList.add('show'); clearTimeout(toastT); toastT = setTimeout(function () { toastEl.classList.remove('show'); }, 1500); }
  function note(s, cls) { var m = $('#msg'); m.textContent = s || ''; m.className = 'msg' + (cls ? ' ' + cls : ''); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
  function fmt(c) { var h = Math.ceil(c.length / 2); return c.slice(0, h) + ' ' + c.slice(h); }
  function label(e) { return [e.issuer, e.account].filter(Boolean).join(' · ') || e.label || (e.secret.slice(0, 4) + '…' + e.secret.slice(-4)); }
  function id(e) { return [e.secret, e.algorithm, e.digits, e.period].join('|'); }
  function norm(e) {
    return { secret: e.secret, issuer: e.issuer || '', account: e.account || e.label || '',
      algorithm: (e.algorithm || 'SHA1').toUpperCase().replace('-', ''), digits: +e.digits || 6, period: +e.period || 30 };
  }
  async function copy(text) {
    try { await navigator.clipboard.writeText(text); }
    catch (e) { var t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); document.execCommand('copy'); t.remove(); }
    toast(msg('copied'));
  }

  /* ---------- rendering ---------- */
  function card(e, isTemp, i) {
    var R = 12, C = 2 * Math.PI * R;
    return '<div class="card' + (isTemp ? ' temp' : '') + '" data-i="' + i + '" data-t="' + (isTemp ? 1 : 0) + '">' +
      '<div class="info"><div class="label" title="' + esc(label(e)) + '">' + esc(label(e)) + '</div>' +
      '<button class="code" type="button" title="' + esc(msg('copy')) + '">— — —</button>' +
      '<div class="next"></div></div>' +
      '<svg class="ring" viewBox="0 0 30 30"><circle class="bg" cx="15" cy="15" r="' + R + '"/><circle class="fg" cx="15" cy="15" r="' + R + '" stroke-dasharray="' + C.toFixed(2) + '"/><text x="15" y="15"></text></svg>' +
      (isTemp ? '<button class="save" type="button">' + esc(msg('save')) + '</button>' : '') +
      '<button class="x" type="button" title="' + esc(msg('remove')) + '" aria-label="' + esc(msg('remove')) + '">×</button></div>';
  }
  function render() {
    $('#temp').innerHTML = temp.map(function (e, i) { return card(e, true, i); }).join('');
    $('#list').innerHTML = saved.map(function (e, i) { return card(e, false, i); }).join('');
    $('#savedH').style.display = saved.length ? '' : 'none';
    $('#empty').style.display = saved.length || temp.length ? 'none' : '';
    tick(true);
  }
  var last = -1;
  async function tick(force) {
    var now = Date.now();
    var cards = document.querySelectorAll('.card');
    for (var k = 0; k < cards.length; k++) {
      var el = cards[k], e = (el.dataset.t === '1' ? temp : saved)[+el.dataset.i];
      if (!e) continue;
      var p = e.period, left = p - Math.floor(now / 1000) % p;
      var ring = el.querySelector('.ring'), fg = el.querySelector('.fg'), C = 2 * Math.PI * 12;
      fg.style.strokeDashoffset = (C * (1 - left / p)).toFixed(2);
      ring.classList.toggle('low', left <= 5);
      ring.querySelector('text').textContent = left;
      var ctr = T.counterAt(now, p);
      if (force || el.dataset.ctr !== String(ctr)) {
        el.dataset.ctr = ctr;
        try {
          var o = { algorithm: e.algorithm, digits: e.digits, period: p, time: now };
          var code = await T.totp(e.secret, o);
          var next = await T.totp(e.secret, Object.assign({}, o, { time: now + p * 1000 }));
          var b = el.querySelector('.code'); b.textContent = fmt(code); b.dataset.code = code;
          el.querySelector('.next').textContent = msg('next') + ' ' + fmt(next);
        } catch (err) { el.querySelector('.code').textContent = '⚠'; }
      }
    }
  }
  setInterval(tick, 1000);

  /* ---------- actions ---------- */
  function addEntries(list) {
    var added = 0; addEntries.dup = 0;
    list.forEach(function (e) {
      if (e.error || !e.secret) return;
      var n = norm(e), key = id(n);
      if (saved.some(function (s) { return id(s) === key; }) || temp.some(function (s) { return id(s) === key; })) { addEntries.dup++; return; }
      temp.unshift(n); added++;
    });
    return added;
  }
  async function addFromText() {
    var raw = $('#input').value.trim();
    if (!raw) { $('#input').focus(); return; }
    var parsed = T.parseInput(raw);
    var bad = parsed.filter(function (e) { return e.error; }).length;
    var n = addEntries(parsed);
    if (n) { $('#input').value = ''; note(msg('addedN', String(n)), 'ok'); }
    else note(addEntries.dup ? msg('already') : msg('invalid'), 'bad');
    render();
    if (n === 1 && temp[0]) { var c = await T.totp(temp[0].secret, temp[0]); copy(c); }
  }
  $('#addBtn').addEventListener('click', addFromText);
  $('#input').addEventListener('keydown', function (e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); addFromText(); } });
  $('#input').addEventListener('paste', function () { setTimeout(addFromText, 0); });

  document.addEventListener('click', async function (ev) {
    var el = ev.target.closest('.card'); if (!el) return;
    var isTemp = el.dataset.t === '1', i = +el.dataset.i, list = isTemp ? temp : saved;
    if (ev.target.closest('.code')) { var c = ev.target.closest('.code').dataset.code; if (c) copy(c); return; }
    if (ev.target.closest('.save')) { saved.push(temp.splice(i, 1)[0]); await store.set(saved); note(msg('saved'), 'ok'); render(); return; }
    if (ev.target.closest('.x')) { list.splice(i, 1); if (!isTemp) await store.set(saved); render(); }
  });

  /* ---------- QR scanning (screenshot of the visible tab, decoded here) ---------- */
  async function decodeDataUrl(url) {
    var img = new Image(); img.src = url; await img.decode();
    var c = document.createElement('canvas'), ctx = c.getContext('2d', { willReadFrequently: true });
    var results = [];
    var tries = [1, 0.5];
    for (var t = 0; t < tries.length && !results.length; t++) {
      var s = tries[t];
      c.width = Math.round(img.naturalWidth * s); c.height = Math.round(img.naturalHeight * s);
      ctx.drawImage(img, 0, 0, c.width, c.height);
      var data = ctx.getImageData(0, 0, c.width, c.height);
      if ('BarcodeDetector' in window) {
        try {
          var det = new BarcodeDetector({ formats: ['qr_code'] });
          (await det.detect(c)).forEach(function (r) { results.push(r.rawValue); });
        } catch (e) {}
      }
      if (!results.length && window.jsQR) {
        var r = jsQR(data.data, c.width, c.height, { inversionAttempts: 'attemptBoth' });
        if (r && r.data) results.push(r.data);
      }
    }
    return results;
  }
  async function scanShot(shot) {
    note(msg('scanning'));
    try {
      var texts = await decodeDataUrl(shot);
      var entries = [];
      texts.forEach(function (t) { T.parseInput(t).forEach(function (e) { entries.push(e); }); });
      var n = addEntries(entries);
      if (n) note(msg('addedN', String(n)), 'ok'); else note(addEntries.dup ? msg('already') : texts.length ? msg('invalid') : msg('noQr'), 'bad');
      render();
    } catch (e) { note(msg('scanFailed'), 'bad'); }
  }
  $('#scanBtn').addEventListener('click', async function () {
    if (!hasChrome) return;
    try {
      var shot = await chrome.tabs.captureVisibleTab(null, { format: 'png' });
      await scanShot(shot);
    } catch (e) { note(msg('scanFailed'), 'bad'); }
  });

  /* opened from the context menu: popup.html?scan=1 in a tab */
  if (new URLSearchParams(location.search).get('scan') === '1') {
    document.body.classList.add('page');
    if (hasChrome) {
      var s = await chrome.storage.session.get(['shot', 'shotError']);
      await chrome.storage.session.remove(['shot', 'shotError']);
      if (s.shot) await scanShot(s.shot); else note(msg('scanFailed'), 'bad');
    }
  }

  render();
  $('#input').focus();
})();
