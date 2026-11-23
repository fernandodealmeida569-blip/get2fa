// Run with: node tests/totp.test.js
// Checks the TOTP engine against the official test vectors from RFC 4226 and RFC 6238.
const assert = require('assert');
const T = require('../site/assets/totp.js');

function b32(buf) {
  const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
  let bits = 0, v = 0, o = '';
  for (const b of buf) { v = (v << 8) | b; bits += 8; while (bits >= 5) { o += A[(v >>> (bits - 5)) & 31]; bits -= 5; } v &= 255; }
  if (bits > 0) o += A[(v << (5 - bits)) & 31];
  return o;
}

(async () => {
  let passed = 0;

  // RFC 4226 Appendix D (HOTP, SHA-1, 6 digits)
  const k1 = b32(Buffer.from('12345678901234567890'));
  const hotp = ['755224', '287082', '359152', '969429', '338314', '254676', '287922', '162583', '399871', '520489'];
  for (let i = 0; i < hotp.length; i++) { assert.strictEqual(await T.hotp(k1, i), hotp[i]); passed++; }

  // RFC 6238 Appendix B (TOTP, 8 digits)
  const keys = {
    SHA1: b32(Buffer.from('12345678901234567890')),
    SHA256: b32(Buffer.from('12345678901234567890123456789012')),
    SHA512: b32(Buffer.from('1234567890123456789012345678901234567890123456789012345678901234')),
  };
  const vectors = [
    [59, '94287082', '46119246', '90693936'],
    [1111111109, '07081804', '68084774', '25091201'],
    [1111111111, '14050471', '67062674', '99943326'],
    [1234567890, '89005924', '91819424', '93441116'],
    [2000000000, '69279037', '90698825', '38618901'],
    [20000000000, '65353130', '77737706', '47863826'],
  ];
  for (const [t, s1, s256, s512] of vectors) {
    assert.strictEqual(await T.totp(keys.SHA1, { time: t * 1000, digits: 8 }), s1);
    assert.strictEqual(await T.totp(keys.SHA256, { time: t * 1000, digits: 8, algorithm: 'SHA256' }), s256);
    assert.strictEqual(await T.totp(keys.SHA512, { time: t * 1000, digits: 8, algorithm: 'SHA512' }), s512);
    passed += 3;
  }

  // Input parsing
  assert.strictEqual(T.parseLine('jbsw y3dp ehpk 3pxp').secret, 'JBSWY3DPEHPK3PXP');
  assert.strictEqual(T.parseLine('user@mail.com|Pass123|JBSWY3DPEHPK3PXPJBSWY3DPEHPK3PXP').secret, 'JBSWY3DPEHPK3PXPJBSWY3DPEHPK3PXP');
  assert.strictEqual(T.parseLine('otpauth://totp/GitHub:me?secret=JBSWY3DPEHPK3PXP&issuer=GitHub').issuer, 'GitHub');
  assert.ok(T.parseLine('not a key!').error);
  passed += 4;

  // Space-separated account lines must not be glued into one fake key
  assert.strictEqual(T.parseLine('john secret JBSWY3DPEHPK3PXP').secret, 'JBSWY3DPEHPK3PXP');
  assert.strictEqual(T.parseLine('john@x.com pass123 JBSWY3DPEHPK3PXP').secret, 'JBSWY3DPEHPK3PXP');
  assert.strictEqual(T.parseLine('jbsw y3dp ehpk 3pxp abcd efgh ijkl mnop').secret, 'JBSWY3DPEHPK3PXPABCDEFGHIJKLMNOP');
  assert.strictEqual(T.parseLine('JBSW Y3DPE HPK3PXP').secret, 'JBSWY3DPEHPK3PXP');
  // Out-of-range settings in a URI are clamped instead of producing garbage
  const odd = T.parseUri('otpauth://totp/X:a?secret=JBSWY3DPEHPK3PXP&period=-5&digits=99');
  assert.strictEqual(odd.digits, 10); assert.strictEqual(odd.period, 1);
  passed += 6;

  console.log(`All ${passed} checks passed.`);
})().catch((e) => { console.error(e); process.exit(1); });
