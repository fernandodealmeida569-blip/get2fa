/*! Get2FA QR encoder — byte mode, error correction level M, versions 1–20.
    Based on the algorithm in ISO/IEC 18004 (approach after Project Nayuki's MIT-licensed QR generator). */
(function (root) {
  'use strict';
  var ECC_M = [-1, 10, 16, 26, 18, 24, 16, 18, 22, 22, 26, 30, 22, 22, 24, 24, 28, 28, 26, 26, 26];
  var BLOCKS_M = [-1, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 8, 9, 9, 10, 10, 11, 13, 14, 16];
  var FORMAT_M = 0;

  function rawModules(v) {
    var r = (16 * v + 128) * v + 64;
    if (v >= 2) { var n = Math.floor(v / 7) + 2; r -= (25 * n - 10) * n - 55; if (v >= 7) r -= 36; }
    return r;
  }
  function dataCodewords(v) { return Math.floor(rawModules(v) / 8) - ECC_M[v] * BLOCKS_M[v]; }

  function gfMul(x, y) {
    var z = 0;
    for (var i = 7; i >= 0; i--) { z = (z << 1) ^ ((z >>> 7) * 0x11D); z ^= ((y >>> i) & 1) * x; }
    return z & 0xFF;
  }
  function rsDivisor(deg) {
    var d = []; for (var i = 0; i < deg - 1; i++) d.push(0); d.push(1);
    var root = 1;
    for (i = 0; i < deg; i++) {
      for (var j = 0; j < d.length; j++) { d[j] = gfMul(d[j], root); if (j + 1 < d.length) d[j] ^= d[j + 1]; }
      root = gfMul(root, 0x02);
    }
    return d;
  }
  function rsRemainder(data, div) {
    var res = div.map(function () { return 0; });
    data.forEach(function (b) {
      var f = b ^ res.shift(); res.push(0);
      div.forEach(function (c, i) { res[i] ^= gfMul(c, f); });
    });
    return res;
  }

  function alignPositions(v) {
    if (v === 1) return [];
    var n = Math.floor(v / 7) + 2, size = v * 4 + 17;
    var step = Math.ceil((v * 4 + 4) / (n * 2 - 2)) * 2;
    var res = [6];
    for (var pos = size - 7; res.length < n; pos -= step) res.splice(1, 0, pos);
    return res;
  }

  function encode(text) {
    var bytes = Array.from(new TextEncoder().encode(text));
    var v;
    for (v = 1; v <= 20; v++) {
      var ccBits = v <= 9 ? 8 : 16;
      if (4 + ccBits + bytes.length * 8 <= dataCodewords(v) * 8) break;
    }
    if (v > 20) throw new Error('Text too long for QR code');
    var cap = dataCodewords(v) * 8, bits = [];
    function put(val, len) { for (var i = len - 1; i >= 0; i--) bits.push((val >>> i) & 1); }
    put(4, 4); put(bytes.length, v <= 9 ? 8 : 16);
    bytes.forEach(function (b) { put(b, 8); });
    put(0, Math.min(4, cap - bits.length));
    put(0, (8 - bits.length % 8) % 8);
    for (var pad = 0xEC; bits.length < cap; pad ^= 0xEC ^ 0x11) put(pad, 8);
    var data = [];
    for (var i = 0; i < bits.length; i += 8) {
      var x = 0; for (var k = 0; k < 8; k++) x = (x << 1) | bits[i + k]; data.push(x);
    }

    // split into blocks, add EC, interleave
    var nb = BLOCKS_M[v], ecl = ECC_M[v], raw = Math.floor(rawModules(v) / 8);
    var nShort = nb - raw % nb, shortLen = Math.floor(raw / nb);
    var div = rsDivisor(ecl), blocks = [], p = 0;
    for (i = 0; i < nb; i++) {
      var len = shortLen - ecl + (i < nShort ? 0 : 1);
      var dat = data.slice(p, p + len); p += len;
      blocks.push({ d: dat, e: rsRemainder(dat, div) });
    }
    var all = [];
    for (i = 0; i < shortLen - ecl + 1; i++) blocks.forEach(function (b) { if (i < b.d.length) all.push(b.d[i]); });
    for (i = 0; i < ecl; i++) blocks.forEach(function (b) { all.push(b.e[i]); });

    // matrix
    var size = v * 4 + 17;
    var m = [], fn = [];
    for (i = 0; i < size; i++) { m.push(new Array(size).fill(false)); fn.push(new Array(size).fill(false)); }
    function setF(x, y, dark) { m[y][x] = dark; fn[y][x] = true; }

    for (i = 0; i < size; i++) { setF(6, i, i % 2 === 0); setF(i, 6, i % 2 === 0); }
    [[3, 3], [size - 4, 3], [3, size - 4]].forEach(function (c) {
      for (var dy = -4; dy <= 4; dy++) for (var dx = -4; dx <= 4; dx++) {
        var d = Math.max(Math.abs(dx), Math.abs(dy)), xx = c[0] + dx, yy = c[1] + dy;
        if (xx >= 0 && xx < size && yy >= 0 && yy < size) setF(xx, yy, d !== 2 && d !== 4);
      }
    });
    var ap = alignPositions(v), na = ap.length;
    for (i = 0; i < na; i++) for (var j = 0; j < na; j++) {
      if ((i === 0 && j === 0) || (i === 0 && j === na - 1) || (i === na - 1 && j === 0)) continue;
      for (var ay = -2; ay <= 2; ay++) for (var ax = -2; ax <= 2; ax++)
        setF(ap[i] + ax, ap[j] + ay, Math.max(Math.abs(ax), Math.abs(ay)) !== 1);
    }
    function drawFormat(mask) {
      var d = (FORMAT_M << 3) | mask, r = d;
      for (var q = 0; q < 10; q++) r = (r << 1) ^ ((r >>> 9) * 0x537);
      var b = ((d << 10) | r) ^ 0x5412;
      function bit(n) { return ((b >>> n) & 1) !== 0; }
      for (q = 0; q <= 5; q++) setF(8, q, bit(q));
      setF(8, 7, bit(6)); setF(8, 8, bit(7)); setF(7, 8, bit(8));
      for (q = 9; q < 15; q++) setF(14 - q, 8, bit(q));
      for (q = 0; q < 8; q++) setF(size - 1 - q, 8, bit(q));
      for (q = 8; q < 15; q++) setF(8, size - 15 + q, bit(q));
      setF(8, size - 8, true);
    }
    drawFormat(0);
    if (v >= 7) {
      var r = v;
      for (i = 0; i < 12; i++) r = (r << 1) ^ ((r >>> 11) * 0x1F25);
      var vb = (v << 12) | r;
      for (i = 0; i < 18; i++) {
        var bt = ((vb >>> i) & 1) !== 0, a = size - 11 + i % 3, bb = Math.floor(i / 3);
        setF(a, bb, bt); setF(bb, a, bt);
      }
    }
    // data
    var bi = 0;
    for (var right = size - 1; right >= 1; right -= 2) {
      if (right === 6) right = 5;
      for (var vert = 0; vert < size; vert++) for (j = 0; j < 2; j++) {
        var xx = right - j, up = ((right + 1) & 2) === 0, yy = up ? size - 1 - vert : vert;
        if (!fn[yy][xx] && bi < all.length * 8) { m[yy][xx] = ((all[bi >>> 3] >>> (7 - (bi & 7))) & 1) !== 0; bi++; }
      }
    }
    var MASKS = [
      function (x, y) { return (x + y) % 2 === 0; }, function (x, y) { return y % 2 === 0; },
      function (x) { return x % 3 === 0; }, function (x, y) { return (x + y) % 3 === 0; },
      function (x, y) { return (Math.floor(x / 3) + Math.floor(y / 2)) % 2 === 0; },
      function (x, y) { return x * y % 2 + x * y % 3 === 0; },
      function (x, y) { return (x * y % 2 + x * y % 3) % 2 === 0; },
      function (x, y) { return ((x + y) % 2 + x * y % 3) % 2 === 0; }
    ];
    function applyMask(k) {
      for (var y = 0; y < size; y++) for (var x = 0; x < size; x++) if (!fn[y][x] && MASKS[k](x, y)) m[y][x] = !m[y][x];
    }
    function penalty() {
      var s = 0, x, y, run, dark = 0;
      for (y = 0; y < size; y++) { run = 1; for (x = 1; x < size; x++) { if (m[y][x] === m[y][x - 1]) { run++; if (run === 5) s += 3; else if (run > 5) s++; } else run = 1; } }
      for (x = 0; x < size; x++) { run = 1; for (y = 1; y < size; y++) { if (m[y][x] === m[y - 1][x]) { run++; if (run === 5) s += 3; else if (run > 5) s++; } else run = 1; } }
      for (y = 0; y < size - 1; y++) for (x = 0; x < size - 1; x++) { var c = m[y][x]; if (c === m[y][x + 1] && c === m[y + 1][x] && c === m[y + 1][x + 1]) s += 3; }
      for (y = 0; y < size; y++) for (x = 0; x < size; x++) if (m[y][x]) dark++;
      s += Math.floor(Math.abs(dark * 20 - size * size * 10) / (size * size)) * 10;
      return s;
    }
    var best = 0, bestScore = Infinity;
    for (var k = 0; k < 8; k++) {
      applyMask(k); drawFormat(k);
      var sc = penalty(); if (sc < bestScore) { bestScore = sc; best = k; }
      applyMask(k);
    }
    applyMask(best); drawFormat(best);
    return { size: size, version: v, modules: m };
  }

  function toSvg(qr, opts) {
    opts = opts || {};
    var border = opts.border == null ? 4 : opts.border, n = qr.size + border * 2, d = '';
    for (var y = 0; y < qr.size; y++) for (var x = 0; x < qr.size; x++)
      if (qr.modules[y][x]) d += 'M' + (x + border) + ',' + (y + border) + 'h1v1h-1z';
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + n + ' ' + n + '" shape-rendering="crispEdges">' +
      '<rect width="100%" height="100%" fill="#fff"/><path d="' + d + '" fill="#000"/></svg>';
  }

  var api = { encode: encode, toSvg: toSvg };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.QR = api;
})(typeof self !== 'undefined' ? self : this);
