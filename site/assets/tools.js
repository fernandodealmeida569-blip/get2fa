/*! Get2FA extra tools: key + QR generator, code checker, QR reader, line splitter. Everything runs on this device. */
(function () {
  'use strict';
  var T = window.TOTP, L = window.I18N || {};
  var $ = function (s) { return document.querySelector(s); };
  var tool = document.body.getAttribute('data-tool');

  /* ---------- helpers ---------- */
  var toastEl = $('#toast'), toastT;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg; toastEl.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.classList.remove('show'); }, 1800);
  }
  function copy(text, msg) {
    var done = function () { toast(msg || L.copied); };
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text).then(done, fallback);
    fallback();
    function fallback() {
      var t = document.createElement('textarea'); t.value = text; t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(t); done();
    }
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
  function fmt(code) { var h = Math.ceil(code.length / 2); return code.slice(0, h) + ' ' + code.slice(h); }
  function group(s) { return s.replace(/(.{4})/g, '$1 ').trim(); }
  function opts() {
    return { algorithm: ($('#alg') || {}).value || 'SHA1', digits: +(($('#digits') || {}).value || 6), period: +(($('#period') || {}).value || 30) };
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]');
    if (b) copy(b.getAttribute('data-copy'));
  });
  var root = document.documentElement, saved;
  try { saved = localStorage.getItem('q2fa.theme'); } catch (e) {}
  if (saved) root.setAttribute('data-theme', saved);
  var themeBtn = $('#themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var dark = root.getAttribute('data-theme') ? root.getAttribute('data-theme') === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    var n = dark ? 'light' : 'dark'; root.setAttribute('data-theme', n); try { localStorage.setItem('q2fa.theme', n); } catch (e) {}
  });

  /* ---------- 1. key + QR generator ---------- */
  if (tool === 'gen') {
    var cur = null, timer;
    function newKey() {
      var n = +$('#gBytes').value, b = new Uint8Array(n);
      crypto.getRandomValues(b);
      cur = T.encode(b);
      update();
    }
    function uri() {
      var o = opts(), issuer = $('#gIssuer').value.trim(), acct = $('#gAccount').value.trim() || 'user';
      var label = encodeURIComponent(issuer ? issuer + ':' + acct : acct);
      var q = 'secret=' + cur + (issuer ? '&issuer=' + encodeURIComponent(issuer) : '');
      if (o.algorithm !== 'SHA1') q += '&algorithm=' + o.algorithm;
      if (o.digits !== 6) q += '&digits=' + o.digits;
      if (o.period !== 30) q += '&period=' + o.period;
      return 'otpauth://totp/' + label + '?' + q;
    }
    function update() {
      if (!cur) return;
      var u = uri();
      $('#gSecret').textContent = group(cur);
      $('#gSecretCopy').setAttribute('data-copy', cur);
      $('#gUri').value = u;
      $('#gUriCopy').setAttribute('data-copy', u);
      $('#gQr').innerHTML = window.QR.toSvg(window.QR.encode(u));
      $('#gOpen').href = (root.getAttribute('data-home') || '/') + '#' + encodeURIComponent(u);
      tick(true);
    }
    var last = -1;
    async function tick(force) {
      if (!cur) return;
      var o = opts(), now = Date.now(), c = T.counterAt(now, o.period), left = o.period - (now / 1000) % o.period;
      $('#gLeft').textContent = Math.ceil(left) + ' s';
      if (c !== last || force === true) { last = c; $('#gCode').textContent = fmt(await T.hotp(cur, c, o)); }
    }
    $('#gNew').addEventListener('click', newKey);
    ['#gIssuer', '#gAccount'].forEach(function (s) { $(s).addEventListener('input', update); });
    ['#alg', '#digits', '#period'].forEach(function (s) { $(s).addEventListener('change', update); });
    $('#gBytes').addEventListener('change', newKey);
    $('#gDl').addEventListener('click', function () {
      var blob = new Blob([$('#gQr').innerHTML], { type: 'image/svg+xml' });
      var a = document.createElement('a'); a.href = URL.createObjectURL(blob);
      a.download = 'qr-2fa' + ($('#gIssuer').value ? '-' + $('#gIssuer').value.replace(/[^\w-]+/g, '') : '') + '.svg';
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    });
    newKey();
    timer = setInterval(tick, 500);
  }

  /* ---------- 2. code checker ---------- */
  if (tool === 'check') {
    var offset = null;
    function clockCheck() {
      var box = $('#cClock'), t0 = Date.now();
      fetch(location.pathname, { method: 'HEAD', cache: 'no-store' }).then(function (r) {
        var d = r.headers.get('date'); if (!d) throw new Error('no date');
        var t1 = Date.now(), server = new Date(d).getTime() + 500;
        offset = Math.round(((t0 + t1) / 2 - server) / 1000);
        var abs = Math.abs(offset);
        if (abs <= 2) { box.className = 'note ok'; box.textContent = L.clockOk; }
        else {
          box.className = 'note ' + (abs >= 15 ? 'bad' : 'warn');
          box.textContent = (offset > 0 ? L.clockAhead : L.clockBehind).replace('{n}', abs);
        }
      }).catch(function () { box.className = 'note'; box.textContent = L.clockUnknown; });
    }
    async function check() {
      var out = $('#cResult'), e = T.parseLine($('#cSecret').value.split(/\r?\n/)[0] || '');
      var code = ($('#cCode').value || '').replace(/\D/g, '');
      if (!e || e.error) { out.className = 'note bad'; out.textContent = L.badKey; return; }
      var o = opts();
      if (/^otpauth:/i.test(e.raw)) o = { algorithm: e.algorithm, digits: e.digits, period: e.period };
      if (code.length !== o.digits) { out.className = 'note warn'; out.textContent = L.badCode.replace('{n}', o.digits); return; }
      var c = T.counterAt(Date.now(), o.period), hit = null;
      for (var d = 0; d <= 10 && hit === null; d++) {
        if (await T.hotp(e.secret, c - d, o) === code) hit = -d;
        else if (d && await T.hotp(e.secret, c + d, o) === code) hit = d;
      }
      if (hit === 0) { out.className = 'note ok'; out.textContent = L.match; }
      else if (hit !== null) {
        out.className = 'note warn';
        out.textContent = (hit < 0 ? L.matchPast : L.matchFuture).replace('{s}', Math.abs(hit) * o.period);
      } else { out.className = 'note bad'; out.textContent = L.noMatch; }
      var cur = await T.hotp(e.secret, c, o);
      $('#cNow').textContent = L.expected + ' ' + fmt(cur);
    }
    $('#cCheck').addEventListener('click', check);
    $('#cCode').addEventListener('keydown', function (ev) { if (ev.key === 'Enter') check(); });
    clockCheck();
  }

  /* ---------- 3. QR reader ---------- */
  if (tool === 'read') {
    var outEl = $('#rOut');
    function show(values) {
      var list = [];
      values.forEach(function (v) { T.parseInput(v).forEach(function (e) { list.push(e); }); });
      list = list.filter(function (e) { return !e.error; });
      if (!list.length) { outEl.innerHTML = '<div class="note bad">' + esc(L.qrNotFound) + '</div>'; return; }
      var home = root.getAttribute('data-home') || '/';
      outEl.innerHTML = '<div class="note ok">' + esc(L.found.replace('{n}', list.length)) + '</div>' + list.map(function (e) {
        var p = /^otpauth:/i.test(e.raw) ? T.parseUri(e.raw) : e;
        return '<div class="card kv">' +
          '<div><span>' + esc(L.issuer) + '</span><b>' + esc(p.issuer || '—') + '</b></div>' +
          '<div><span>' + esc(L.account) + '</span><b>' + esc(p.account || p.label || '—') + '</b></div>' +
          '<div><span>' + esc(L.secret) + '</span><code class="k">' + esc(group(e.secret)) + '</code> <button class="btn sm" type="button" data-copy="' + esc(e.secret) + '">' + esc(L.copy) + '</button></div>' +
          '<div><span>' + esc(L.settings) + '</span><b>' + esc((p.algorithm || 'SHA1') + ' · ' + (p.digits || 6) + ' · ' + (p.period || 30) + ' s') + '</b></div>' +
          '<div class="row"><a class="btn primary sm" href="' + esc(home + '#' + (/^otpauth:/i.test(e.raw) ? encodeURIComponent(e.raw) : e.secret)) + '">' + esc(L.openGen) + '</a>' +
          '<button class="btn sm" type="button" data-copy="' + esc(e.raw) + '">' + esc(L.copyUri) + '</button></div></div>';
      }).join('');
    }
    async function readFile(f) {
      outEl.innerHTML = '<div class="note">' + esc(L.reading) + '</div>';
      try { show(await window.QRRead.decodeImage(f)); }
      catch (e) { outEl.innerHTML = '<div class="note bad">' + esc(L.qrUnsupported) + '</div>'; }
    }
    var drop = $('#rDrop'), file = $('#rFile');
    drop.addEventListener('click', function () { file.click(); });
    drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); file.click(); } });
    file.addEventListener('change', function () { if (file.files[0]) readFile(file.files[0]); file.value = ''; });
    ['dragenter', 'dragover'].forEach(function (t) { drop.addEventListener(t, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (t) { drop.addEventListener(t, function () { drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { e.preventDefault(); var f = e.dataTransfer.files[0]; if (f) readFile(f); });
    document.addEventListener('paste', function (ev) {
      var items = (ev.clipboardData && ev.clipboardData.items) || [];
      for (var i = 0; i < items.length; i++) if (items[i].type.indexOf('image/') === 0) { ev.preventDefault(); readFile(items[i].getAsFile()); return; }
    });
    $('#rText').addEventListener('input', function () {
      var v = this.value.trim(); if (/^otpauth/i.test(v)) show(v.split(/\s+/));
    });
  }

  /* ---------- 4. account line splitter ---------- */
  if (tool === 'split') {
    var inp = $('#sIn'), out = $('#sOut'), delIn = $('#sDelim'), delOut = $('#sOutDelim'), cols = $('#sCols'),
        trim = $('#sTrim'), dedup = $('#sDedup'), addCode = $('#sCode'), prev = $('#sPrev'), stat = $('#sStat');
    var DELIMS = { pipe: '|', colon: ':', semi: ';', comma: ',', tab: '\t', space: ' ' };
    function detect(lines) {
      var best = 'pipe', score = -1;
      ['pipe', 'tab', 'semi', 'colon', 'comma', 'space'].forEach(function (k) {
        var d = DELIMS[k], n = 0;
        lines.slice(0, 50).forEach(function (l) { n += l.split(d).length - 1; });
        if (k === 'colon') n = n * 0.6;
        if (k === 'space') n = n * 0.4;
        if (n > score) { score = n; best = k; }
      });
      return score > 0 ? best : 'pipe';
    }
    function parseCols(str, max) {
      var r = [];
      String(str || '').split(/[\s,;]+/).forEach(function (p) {
        if (!p) return;
        var m = p.match(/^(\d+)-(\d+)$/);
        if (m) { for (var a = +m[1]; a <= +m[2]; a++) r.push(a); }
        else if (/^\d+$/.test(p)) r.push(+p);
      });
      r = r.filter(function (n) { return n >= 1 && n <= max; });
      return r.length ? r : null;
    }
    var timer;
    async function run() {
      var raw = inp.value.split(/\r?\n/);
      var lines = raw.map(function (l) { return trim.checked ? l.trim() : l; }).filter(function (l) { return l.trim() !== ''; });
      if (dedup.checked) { var seen = new Set(); lines = lines.filter(function (l) { if (seen.has(l)) return false; seen.add(l); return true; }); }
      var dk = delIn.value === 'auto' ? detect(lines) : delIn.value;
      var d = DELIMS[dk] || '|', od = DELIMS[delOut.value] || (delOut.value === 'same' ? d : '|');
      var auto = delIn.value === 'auto';
      var rows = lines.map(function (l) { var p = l.split(auto ? (DELIMS[detect([l])] || d) : d); return trim.checked ? p.map(function (x) { return x.trim(); }) : p; });
      var max = rows.reduce(function (m, r) { return Math.max(m, r.length); }, 0);
      var pick = parseCols(cols.value, max);
      /* preview of the first line */
      if (rows.length) {
        prev.innerHTML = rows[0].map(function (c, i) {
          var on = !pick || pick.indexOf(i + 1) >= 0;
          var isKey = T.isBase32(T.clean(c), 16);
          return '<button type="button" class="chip' + (on ? ' on' : '') + '" data-col="' + (i + 1) + '" title="' + esc(c) + '"><b>' + (i + 1) + '</b> ' + esc(c.length > 18 ? c.slice(0, 16) + '…' : c) + (isKey ? ' 🔑' : '') + '</button>';
        }).join('');
      } else prev.innerHTML = '';
      var now = Date.now(), o = opts();
      var res = await Promise.all(rows.map(async function (r) {
        var sel = pick ? pick.map(function (n) { return r[n - 1] == null ? '' : r[n - 1]; }) : r.slice();
        if (addCode.checked) {
          var key = null;
          for (var i = r.length - 1; i >= 0; i--) { var c = T.clean(r[i]); if (T.isBase32(c, 16)) { key = c; break; } }
          var code = '';
          if (key) { try { code = await T.totp(key, { algorithm: o.algorithm, digits: o.digits, period: o.period, time: now }); } catch (e) {} }
          sel.push(code);
        }
        return sel.join(od);
      }));
      out.value = res.join('\n');
      stat.textContent = (L.stat || '{n} · {c}').replace('{n}', rows.length).replace('{c}', max) + (delIn.value === 'auto' && rows.length ? ' · ' + (L.detected || '') + ' ' + (dk === 'tab' ? 'Tab' : dk === 'space' ? '␣' : DELIMS[dk]) : '');
    }
    function later() { clearTimeout(timer); timer = setTimeout(run, 120); }
    [inp, cols].forEach(function (el) { el.addEventListener('input', later); });
    [delIn, delOut, trim, dedup, addCode, $('#alg'), $('#digits'), $('#period')].forEach(function (el) { if (el) el.addEventListener('change', run); });
    prev.addEventListener('click', function (e) {
      var b = e.target.closest('[data-col]'); if (!b) return;
      var n = +b.getAttribute('data-col');
      var all = Array.prototype.map.call(prev.querySelectorAll('[data-col]'), function (x) { return +x.getAttribute('data-col'); });
      var cur = parseCols(cols.value, 999) || all.slice();
      cur = cur.indexOf(n) >= 0 ? cur.filter(function (x) { return x !== n; }) : cur.concat([n]);
      var sorted = cur.slice().sort(function (a, b) { return a - b; }).join(',') === all.join(',');
      cols.value = sorted ? '' : cur.join(',');
      run();
    });
    $('#sCopy').addEventListener('click', function () { if (out.value) copy(out.value, L.copied); });
    $('#sDl').addEventListener('click', function () {
      if (!out.value) return;
      var a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([out.value + '\n'], { type: 'text/plain' }));
      a.download = 'accounts.txt'; document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    });
    $('#sClear').addEventListener('click', function () { inp.value = ''; cols.value = ''; run(); inp.focus(); });
    setInterval(function () { if (addCode.checked && inp.value) run(); }, 5000);
    run();
  }
})();
