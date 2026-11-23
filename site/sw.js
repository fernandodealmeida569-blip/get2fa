/* Get2FA offline cache. Only static files are cached; secrets are never involved. */
const V = 'q2fa-v7';
const FILES = ["/", "/pt/", "/es/", "/vi/", "/id/", "/de/", "/th/", "/fr/", "/ru/", "/tr/", "/ja/", "/ko/", "/zh/", "/hi/", "/ar/", "/bn/", "/km/", "/assets/style.css", "/assets/totp.js", "/assets/app.js", "/assets/qrread.js", "/assets/icon.svg"];
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== V).map(x => caches.delete(x)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin || u.pathname.startsWith('/cdn-cgi/')) return;
  e.respondWith(fetch(e.request).then(r => {
    /* keep only good same-origin answers: no error pages, no redirects */
    if (r.ok && r.type === 'basic') { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); }
    return r;
  }).catch(() => caches.match(e.request, { ignoreSearch: true })
    .then(r => r || (e.request.mode === 'navigate' ? caches.match('/') : Response.error()))));
});
