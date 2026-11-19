/*! Get2FA QR reader: decodes QR images on this device.
    Native BarcodeDetector when available, otherwise the self-hosted jsQR (loaded only when needed). */
(function () {
  'use strict';
  var jsqrPromise = null;
  function base() { return document.documentElement.getAttribute('data-root') || '/'; }
  function loadJsQR() {
    if (window.jsQR) return Promise.resolve(window.jsQR);
    if (!jsqrPromise) {
      jsqrPromise = new Promise(function (ok, fail) {
        var s = document.createElement('script');
        s.src = base() + 'assets/jsQR.js';
        s.onload = function () { window.jsQR ? ok(window.jsQR) : fail(new Error('jsQR')); };
        s.onerror = function () { jsqrPromise = null; fail(new Error('jsQR')); };
        document.head.appendChild(s);
      });
    }
    return jsqrPromise;
  }
  async function decodeImage(file) {
    var bmp = await createImageBitmap(file);
    if ('BarcodeDetector' in window) {
      try {
        var det = new window.BarcodeDetector({ formats: ['qr_code'] });
        var codes = await det.detect(bmp);
        if (codes.length) return codes.map(function (c) { return c.rawValue; });
      } catch (e) { /* fall back to jsQR */ }
    }
    var jsQR = await loadJsQR();
    var found = [];
    var scales = [1, Math.min(1, 1000 / Math.max(bmp.width, bmp.height))];
    for (var i = 0; i < scales.length && !found.length; i++) {
      var w = Math.max(1, Math.round(bmp.width * scales[i])), h = Math.max(1, Math.round(bmp.height * scales[i]));
      var c = document.createElement('canvas'); c.width = w; c.height = h;
      var ctx = c.getContext('2d', { willReadFrequently: true });
      ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, w, h); ctx.drawImage(bmp, 0, 0, w, h);
      var img = ctx.getImageData(0, 0, w, h);
      var r = jsQR(img.data, w, h, { inversionAttempts: 'attemptBoth' });
      if (r && r.data) found.push(r.data);
    }
    return found;
  }
  window.QRRead = { decodeImage: decodeImage };
})();
