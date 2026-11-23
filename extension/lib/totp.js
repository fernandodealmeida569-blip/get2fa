/*! Get2FA TOTP engine — RFC 4226 / RFC 6238, Web Crypto only. Nothing leaves the device. */
(function (root) {
  'use strict';
  var B32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
  var ALGS = { 'SHA1': 'SHA-1', 'SHA-1': 'SHA-1', 'SHA256': 'SHA-256', 'SHA-256': 'SHA-256', 'SHA512': 'SHA-512', 'SHA-512': 'SHA-512' };

  function clean(s) {
    return String(s || '').toUpperCase().replace(/[\s\-_.]/g, '').replace(/=+$/, '');
  }
  function isBase32(s, min) {
    return new RegExp('^[A-Z2-7]{' + (min || 8) + ',}$').test(s);
  }
  function decode(s) {
    s = clean(s);
    var bits = 0, val = 0, out = [];
    for (var i = 0; i < s.length; i++) {
      var idx = B32.indexOf(s[i]);
      if (idx < 0) throw new Error('Invalid Base32 character: ' + s[i]);
      val = ((val << 5) | idx) & 0xffff;
      bits += 5;
      if (bits >= 8) { out.push((val >>> (bits - 8)) & 0xff); bits -= 8; }
    }
    return new Uint8Array(out);
  }

  var cache = new Map();
  function key(secret, alg) {
    var id = alg + '|' + secret;
    if (!cache.has(id)) {
      if (cache.size > 500) cache.clear();
      cache.set(id, crypto.subtle.importKey('raw', decode(secret), { name: 'HMAC', hash: { name: alg } }, false, ['sign']));
    }
    return cache.get(id);
  }

  async function hotp(secret, counter, opts) {
    opts = opts || {};
    var alg = ALGS[String(opts.algorithm || 'SHA1').toUpperCase()] || 'SHA-1';
    var digits = opts.digits || 6;
    var k = await key(clean(secret), alg);
    var buf = new ArrayBuffer(8), dv = new DataView(buf);
    dv.setUint32(0, Math.floor(counter / 4294967296));
    dv.setUint32(4, counter >>> 0);
    var h = new Uint8Array(await crypto.subtle.sign('HMAC', k, buf));
    var o = h[h.length - 1] & 15;
    var bin = ((h[o] & 127) << 24) | (h[o + 1] << 16) | (h[o + 2] << 8) | h[o + 3];
    return String(bin % Math.pow(10, digits)).padStart(digits, '0');
  }

  function counterAt(timeMs, period) {
    return Math.floor(timeMs / 1000 / (period || 30));
  }

  async function totp(secret, opts) {
    opts = opts || {};
    var period = opts.period || 30;
    var t = opts.time != null ? opts.time : Date.now();
    return hotp(secret, counterAt(t, period), opts);
  }

  function clamp(n, lo, hi) { return Math.min(hi, Math.max(lo, n)); }

  /* Parse an otpauth:// URI */
  function parseUri(uri) {
    var u = new URL(uri.trim());
    if (u.protocol !== 'otpauth:') return null;
    var p = u.searchParams;
    var label = decodeURIComponent(u.pathname.replace(/^\/+/, ''));
    var issuer = p.get('issuer') || (label.indexOf(':') > -1 ? label.split(':')[0] : '');
    var account = label.indexOf(':') > -1 ? label.split(':').slice(1).join(':').trim() : label;
    return {
      type: u.host.toLowerCase() || u.pathname.split('/')[0],
      secret: clean(p.get('secret')),
      issuer: issuer,
      account: account,
      algorithm: (p.get('algorithm') || 'SHA1').toUpperCase(),
      digits: clamp(parseInt(p.get('digits'), 10) || 6, 4, 10),
      period: clamp(parseInt(p.get('period'), 10) || 30, 1, 86400)
    };
  }

  /*
   * Parse one input line. Accepts:
   *  - a plain secret ("JBSW Y3DP EHPK 3PXP")
   *  - an otpauth:// URI
   *  - account lines like "login|password|SECRET" or "mail:pass:SECRET"
   */
  function parseLine(line) {
    var raw = String(line || '').trim();
    if (!raw) return null;
    if (/^otpauth:\/\//i.test(raw)) {
      try {
        var e = parseUri(raw);
        if (e && isBase32(e.secret)) { e.raw = raw; e.label = [e.issuer, e.account].filter(Boolean).join(' · '); return e; }
      } catch (err) { /* fall through */ }
      return { raw: raw, error: true };
    }
    var whole = clean(raw), i, c;
    if (isBase32(whole) && !/[|;,:\t]/.test(raw)) {
      /* A key typed in groups ("JBSW Y3DP EHPK 3PXP") has chunks of equal length.
         Anything else with a key-like word in it ("john secret JBSWY3DPEHPK3PXP") is an account line. */
      var toks = raw.split(/\s+/);
      var len0 = toks[0].length;
      var grouped = toks.every(function (x, n) { return n === toks.length - 1 ? x.length <= len0 : x.length === len0; });
      if (toks.length > 1 && !grouped) {
        for (i = toks.length - 1; i >= 0; i--) {
          c = clean(toks[i]);
          if (isBase32(c, 16)) return { raw: raw, secret: c, label: i > 0 ? toks[0] : '', algorithm: 'SHA1', digits: 6, period: 30 };
        }
      }
      return { raw: raw, secret: whole, label: '', algorithm: 'SHA1', digits: 6, period: 30 };
    }

    var parts = raw.split(/[|;,\t]|:(?!\/\/)|\s{2,}/).map(function (s) { return s.trim(); }).filter(Boolean);
    for (i = parts.length - 1; i >= 0; i--) {
      c = clean(parts[i]);
      if (isBase32(c, 16)) {
        var rest = parts.slice(0, i).concat(parts.slice(i + 1));
        return { raw: raw, secret: c, label: rest[0] || '', algorithm: 'SHA1', digits: 6, period: 30 };
      }
    }
    /* last resort: single spaces as separators ("mail@x.com pass KEY") */
    var words = raw.split(/[|;,\s]+|:(?!\/\/)/).filter(Boolean);
    for (i = words.length - 1; i >= 0; i--) {
      c = clean(words[i]);
      if (isBase32(c, 16)) return { raw: raw, secret: c, label: i > 0 ? words[0] : '', algorithm: 'SHA1', digits: 6, period: 30 };
    }
    return { raw: raw, error: true };
  }

  function encode(bytes) {
    var out = '', bits = 0, val = 0;
    for (var i = 0; i < bytes.length; i++) {
      val = ((val << 8) | bytes[i]) & 0xffff; bits += 8;
      while (bits >= 5) { out += B32[(val >>> (bits - 5)) & 31]; bits -= 5; }
    }
    if (bits > 0) out += B32[(val << (5 - bits)) & 31];
    return out;
  }

  /* Google Authenticator export: otpauth-migration://offline?data=BASE64(protobuf) */
  function parseMigration(uri) {
    var m = /[?&]data=([^&]+)/.exec(uri);
    if (!m) return [];
    var b64 = decodeURIComponent(m[1]).replace(/-/g, '+').replace(/_/g, '/').replace(/\s/g, '');
    var bin = atob(b64), buf = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) buf[i] = bin.charCodeAt(i);
    var utf8 = new TextDecoder();

    function fields(b) {
      var p = 0, out = [];
      function varint() {
        var r = 0, s = 1, x;
        do { x = b[p++]; r += (x & 127) * s; s *= 128; } while (x & 128 && p < b.length);
        return r;
      }
      while (p < b.length) {
        var tag = varint(), f = Math.floor(tag / 8), w = tag & 7, v;
        if (w === 0) v = varint();
        else if (w === 2) { var len = varint(); v = b.subarray(p, p + len); p += len; }
        else if (w === 1) { p += 8; continue; }
        else if (w === 5) { p += 4; continue; }
        else break;
        out.push([f, v]);
      }
      return out;
    }
    var ALG = { 1: 'SHA1', 2: 'SHA256', 3: 'SHA512' }, res = [];
    fields(buf).forEach(function (fv) {
      if (fv[0] !== 1) return;
      var e = { algorithm: 'SHA1', digits: 6, period: 30, type: 'totp', issuer: '', account: '' };
      fields(fv[1]).forEach(function (x) {
        if (x[0] === 1) e.secret = encode(x[1]);
        else if (x[0] === 2) e.account = utf8.decode(x[1]);
        else if (x[0] === 3) e.issuer = utf8.decode(x[1]);
        else if (x[0] === 4) e.algorithm = ALG[x[1]] || 'SHA1';
        else if (x[0] === 5) e.digits = x[1] === 2 ? 8 : 6;
        else if (x[0] === 6) e.type = x[1] === 1 ? 'hotp' : 'totp';
      });
      if (!e.secret) return;
      var name = e.account.indexOf(':') > -1 && !e.issuer ? e.account : [e.issuer, e.account].filter(Boolean).join(':');
      e.label = [e.issuer, e.account].filter(Boolean).join(' · ');
      e.raw = 'otpauth://' + e.type + '/' + encodeURIComponent(name) + '?secret=' + e.secret +
        (e.issuer ? '&issuer=' + encodeURIComponent(e.issuer) : '') +
        (e.algorithm !== 'SHA1' ? '&algorithm=' + e.algorithm : '') + (e.digits !== 6 ? '&digits=' + e.digits : '');
      res.push(e);
    });
    return res;
  }

  /* Parse a whole textarea: returns a flat list of entries */
  function parseInput(text) {
    var out = [];
    String(text || '').split(/\r?\n/).forEach(function (l) {
      if (/^\s*otpauth-migration:\/\//i.test(l)) {
        try {
          var list = parseMigration(l.trim());
          if (list.length) { list.forEach(function (e) { out.push(e); }); return; }
        } catch (err) { /* fall through */ }
        out.push({ raw: l.trim(), error: true });
        return;
      }
      var e = parseLine(l);
      if (e) out.push(e);
    });
    return out;
  }

  var api = { clean: clean, isBase32: isBase32, decode: decode, encode: encode, hotp: hotp, totp: totp, counterAt: counterAt, parseUri: parseUri, parseLine: parseLine, parseMigration: parseMigration, parseInput: parseInput };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.TOTP = api;
})(typeof self !== 'undefined' ? self : this);
