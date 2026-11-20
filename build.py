#!/usr/bin/env python3
"""Generates the Get2FA static site (EN, PT, ES, VI, ID, DE) into ./site"""
import json, os, html

SITE = "https://get2fa.online"
BRAND = "Get2FA"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
CONTACT = "contact@get2fa.online"
UPDATED = "2026-11-19"

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#2f5cff"/>'
        '<path d="M16 7l7 3v5.2c0 4.6-3 8.3-7 9.8-4-1.5-7-5.2-7-9.8V10z" fill="#fff"/>'
        '<path d="M12.6 16.2l2.4 2.4 4.6-4.8" fill="none" stroke="#2f5cff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

ICON_PASTE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="3" width="8" height="4" rx="1"/><path d="M16 5h2a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h2"/></svg>'
ICON_QR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/></svg>'
ICON_LINK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>'
ICON_MOON = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'

from i18n_base import L
import importlib
LANGS = ["en", "pt", "es", "vi", "id", "de", "th"]
NEW = ["es", "vi", "id", "de", "th"]
for _c in NEW:
    L[_c] = importlib.import_module("lang_" + _c).T
L["en"]["langName"], L["en"]["ogLocale"] = "English", "en_US"
L["pt"]["langName"], L["pt"]["ogLocale"] = "Português", "pt_BR"
for _c in LANGS:
    L[_c]["code"] = _c


THEME_JS = """<script>
(function(){var r=document.documentElement;document.getElementById('themeBtn').addEventListener('click',function(){var d=r.getAttribute('data-theme')?r.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme: dark)').matches;var n=d?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('q2fa.theme',n)}catch(e){}});})();
</script>"""

def hreflang(alts):
    out = [f'<link rel="alternate" hreflang="{L[c]["lang"]}" href="{SITE}{p}">' for c, p in alts.items() if p]
    if alts.get("en"):
        out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}">')
    return "\n".join(out)

def head(t, title, desc, canonical, alts, extra=""):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}" data-root="/" data-home="{t['path']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{hreflang(alts)}
<meta name="referrer" content="no-referrer">
<meta name="theme-color" content="#2f5cff">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:locale" content="{t['ogLocale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/icon-192.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="stylesheet" href="/assets/style.css">
<script>try{{var t=localStorage.getItem('q2fa.theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<!-- AdSense: paste your <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXX"> here and add class="ads-on" to <body> -->
{extra}
</head>
"""

def lang_menu(t, alts):
    items = []
    for c in LANGS:
        u = L[c]
        href = (alts or {}).get(c) or u["path"]
        cur = ' aria-current="true"' if c == t["code"] else ""
        items.append(f'<a href="{href}" hreflang="{u["lang"]}" lang="{u["lang"]}"{cur}>{u["langName"]}</a>')
    return (f'<details class="langmenu"><summary class="pill" aria-label="Language">🌐 <span class="t">{t["langName"]}</span></summary>'
            f'<div class="langlist">{"".join(items)}</div></details>'
            '<script>document.addEventListener("click",function(e){var d=document.querySelector(".langmenu");if(d&&d.open&&!d.contains(e.target))d.open=false});</script>')

def header(t, alts=None):
    home = t["path"]
    return f"""<header class="wrap top">
  <a class="brand" href="{home}">{LOGO}<span>{BRAND}</span></a>
  <nav class="nav">
    <a class="pill" href="{t['path']}#tools">🧰 <span class="t">{t['tools']}</span></a>
    <a class="pill" href="{t['guidesPath']}">📘 <span class="t">{t['guides']}</span></a>
    {lang_menu(t, alts)}
    <button class="pill" id="themeBtn" type="button" aria-label="Theme">{ICON_MOON}</button>
  </nav>
</header>"""

from split_tool import SUGGEST
LANG_HINT = "<script>(function(){try{if(localStorage.getItem('q2fa.lh'))return}catch(e){}var S=%s;var cur=(document.documentElement.lang||'en').slice(0,2).toLowerCase();var alts={};Array.prototype.forEach.call(document.querySelectorAll('link[rel=alternate][hreflang]'),function(l){var h=l.getAttribute('hreflang').slice(0,2).toLowerCase();if(h!=='x-')alts[h]=l.getAttribute('href')});var pref=(navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'']);for(var i=0;i<pref.length;i++){var c=String(pref[i]).slice(0,2).toLowerCase();if(c===cur)return;if(alts[c]&&S[c]){var d=document.createElement('div');d.className='langhint';d.setAttribute('lang',c);var a=document.createElement('a');a.href=alts[c].replace(/^https:\\/\\/get2fa\\.online/,'');a.textContent=S[c]+' →';var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Close');b.textContent='×';b.onclick=function(){d.remove();try{localStorage.setItem('q2fa.lh','1')}catch(e){}};d.appendChild(a);d.appendChild(b);document.body.appendChild(d);return}}})();</script>" % json.dumps(SUGGEST, ensure_ascii=False)

def footer(t, alts=None):
    langs = "".join(f'<a href="{(alts or {}).get(c) or L[c]["path"]}" hreflang="{L[c]["lang"]}" lang="{L[c]["lang"]}">{L[c]["langName"]}</a>' for c in LANGS if c != t["code"])
    return f"""<footer>
  <div class="wrap">
    <div>© 2026 {BRAND}. {t['foot']}</div>
    <nav>{tool_links(t)}<a href="{t['guidesPath']}">{t['guides']}</a><a href="https://github.com/fernandodealmeida569-blip/get2fa" rel="noopener">{t['openSource']}</a><a href="{t['privacy']}">{t['privacyLink']}</a><a href="mailto:{CONTACT}">{t['contactLink']}</a></nav>
    <nav class="langs">{langs}</nav>
  </div>
</footer>
""" + LANG_HINT

def ad(t, slot):
    return f'<div class="ad-slot" data-label="{t["ad"]}" data-slot="{slot}"><!-- AdSense unit: {slot} --></div>'

from articles import ARTICLES
import new_articles as _na
ARTICLES = [_na.WHAT_IS] + ARTICLES[:6] + [_na.FB_CODE, _na.FORTNITE, _na.TOTP, _na.MS_AUTH, _na.GOVBR] + ARTICLES[6:]

def gpath(code, a):
    return L[code]["guidesPath"] + a[code]["slug"] if a.get(code) else None


def guide_cards(code):
    t = L[code]
    return "".join(f'<a class="feature" href="{gpath(code, a)}" style="text-decoration:none;color:inherit"><b>{a[code]["h1"]}</b><span>{a[code]["desc"]}</span><span style="display:block;margin-top:8px;color:var(--accent);font-weight:600">{t["read"]}</span></a>' for a in ARTICLES if a.get(code))

def page_guides(code):
    t = L[code]
    canonical = SITE + t["guidesPath"]
    alts = {c: L[c]["guidesPath"] for c in LANGS}
    title = f"{t['guidesH']} | {BRAND}"
    return head(t, title, t["guidesLead"], canonical, alts) + f"""<body>
{header(t, alts)}
<main class="wrap content">
  <section class="hero"><h1>{t['guidesH']}</h1><p>{t['guidesLead']}</p></section>
  <div class="features">{guide_cards(code)}</div>
  {ad(t, 'guides-index')}
</main>
{footer(t, alts)}
{THEME_JS}
</body>
</html>
"""

def page_article(code, a):
    t = L[code]; x = a[code]
    canonical = SITE + gpath(code, a)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": x["h1"], "description": x["desc"],
          "inLanguage": t["lang"], "datePublished": UPDATED, "dateModified": UPDATED,
          "author": {"@type": "Organization", "name": BRAND, "url": SITE},
          "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + "/assets/icon-512.png"}},
          "mainEntityOfPage": canonical, "image": SITE + "/assets/og.png"}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": BRAND, "item": SITE + t["path"]},
        {"@type": "ListItem", "position": 2, "name": t["guides"], "item": SITE + t["guidesPath"]},
        {"@type": "ListItem", "position": 3, "name": x["h1"], "item": canonical}]}
    extra = ('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>\n'
             '<script type="application/ld+json">' + json.dumps(crumbs, ensure_ascii=False) + '</script>')
    more = "".join(f'<li><a href="{gpath(code, b)}">{b[code]["h1"]}</a></li>' for b in ARTICLES if b is not a and b.get(code))
    alts = {c: gpath(c, a) for c in LANGS if a.get(c)}
    menu = {c: alts.get(c) or L[c]["guidesPath"] for c in LANGS}
    return head(t, f"{x['title']} | {BRAND}", x["desc"], canonical, alts, extra) + f"""<body>
{header(t, menu)}
<main class="wrap content article">
  <p><a href="{t['guidesPath']}">{t['back']}</a></p>
  <h1 style="font-size:clamp(26px,4vw,36px);line-height:1.2;letter-spacing:-.02em;margin:6px 0 10px">{x['h1']}</h1>
  <p class="lead">{x['lead']}</p>
  <p class="hint">{t['updatedLbl']} {UPDATED}</p>
  <div class="cta"><b>{t['cta']}</b><a class="btn primary" href="{t['path']}">{t['ctaBtn']}</a></div>
  {x['body']}
  {ad(t, 'article')}
  <div class="cta"><b>{t['cta']}</b><a class="btn primary" href="{t['path']}">{t['ctaBtn']}</a></div>
  <h2>{t['guides']}</h2>
  <ul>{more}</ul>
</main>
{footer(t, menu)}
{THEME_JS}
</body>
</html>
"""

from tools_pages import TOOLS

def adv_html(t):
    return f"""<details class="adv">
      <summary>{t['adv']}</summary>
      <div class="adv-grid">
        <label>{t['alg']}<select id="alg"><option>SHA1</option><option>SHA256</option><option>SHA512</option></select></label>
        <label>{t['digits']}<select id="digits"><option>6</option><option>8</option></select></label>
        <label>{t['period']}<select id="period"><option value="30">30 s</option><option value="60">60 s</option></select></label>
      </div>
    </details>"""

def tpl_gen(t, u):
    return f"""
  <section class="tool" aria-label="{u['aria']}">
    <div class="grid2">
      <label class="fld">{u['issuer']}<input id="gIssuer" type="text" placeholder="{u['issuerPh']}" autocomplete="off"></label>
      <label class="fld">{u['account']}<input id="gAccount" type="text" placeholder="{u['accountPh']}" autocomplete="off"></label>
    </div>
    <div class="row">
      <label class="fld inline">{u['keyLen']}<select id="gBytes"><option value="10">{u['opt80']}</option><option value="20" selected>{u['opt160']}</option><option value="32">{u['opt256']}</option></select></label>
      <span class="spacer"></span>
      <button class="btn primary" id="gNew" type="button">{u['newKey']}</button>
    </div>
    {adv_html(t)}
    <div class="genout">
      <div class="qrbox" id="gQr" aria-label="QR code"></div>
      <div class="genfields">
        <div class="lbl">{u['secret']}</div>
        <div class="row tight"><code class="k big" id="gSecret"></code><button class="btn sm" id="gSecretCopy" type="button" data-copy="">{u['copy']}</button></div>
        <div class="lbl">{u['uri']}</div>
        <textarea id="gUri" readonly spellcheck="false" rows="3"></textarea>
        <div class="row tight"><button class="btn sm" id="gUriCopy" type="button" data-copy="">{u['copyLink']}</button><button class="btn sm" id="gDl" type="button">{u['dl']}</button><a class="btn sm" id="gOpen" href="{t['path']}">{u['openGen']}</a></div>
        <div class="lbl">{u['current']} <small id="gLeft"></small></div>
        <div class="code" id="gCode">— — —</div>
      </div>
    </div>
    <div class="hint">{u['hint']}</div>
  </section>"""

def tpl_check(t, u):
    return f"""
  <section class="tool" aria-label="{u['aria']}">
    <div class="note" id="cClock">{u['checking']}</div>
    <label class="fld">{u['secret']}<textarea id="cSecret" rows="2" spellcheck="false" autocomplete="off" placeholder="JBSW Y3DP EHPK 3PXP"></textarea></label>
    <div class="row">
      <label class="fld inline">{u['code']}<input id="cCode" type="text" inputmode="numeric" autocomplete="one-time-code" placeholder="123456"></label>
      <span class="spacer"></span>
      <button class="btn primary" id="cCheck" type="button">{u['check']}</button>
    </div>
    {adv_html(t)}
    <div class="note" id="cResult" aria-live="polite"></div>
    <div class="hint" id="cNow"></div>
  </section>"""

def tpl_read(t, u):
    return f"""
  <section class="tool" aria-label="{u['aria']}">
    <div class="drop" id="rDrop" role="button" tabindex="0"><b>{u['dropB']}</b><span>{u['dropS']}</span></div>
    <input type="file" id="rFile" accept="image/*" hidden>
    <label class="fld">{u['link']}<input id="rText" type="text" spellcheck="false" autocomplete="off" placeholder="otpauth-migration://offline?data=…"></label>
    <div id="rOut" aria-live="polite"></div>
    <div class="hint">{u['hint']}</div>
  </section>"""

TPL = {"gen": tpl_gen, "check": tpl_check, "read": tpl_read}
from split_tool import SPLIT, SUGGEST, tpl_split
_split = {"key": "split", "scripts": ["totp.js", "tools.js"]}
for _c in LANGS:
    _d = dict(SPLIT[_c])
    _d["tool"] = (lambda t, u: (lambda: tpl_split(t, u, adv_html)))(L[_c], _d["ui"])
    _split[_c] = _d
TOOLS.append(_split)
for _c in NEW:
    _m = importlib.import_module("content_" + _c)
    for x in TOOLS:
        if x["key"] not in _m.TOOLS: continue
        d = dict(_m.TOOLS[x["key"]])
        d["tool"] = (lambda f, t, u: (lambda: f(t, u)))(TPL[x["key"]], L[_c], d["ui"])
        x[_c] = d
    for a in ARTICLES:
        a[_c] = a.get(_c) or _m.GUIDES.get(a["key"])

def tool_links(t):
    c = t["code"]
    return "".join(f'<a href="{x[c]["path"]}">{x[c]["card"]}</a>' for x in TOOLS)

def tool_cards(code, skip=None):
    t = L[code]
    return "".join(f'<a class="feature" href="{x[code]["path"]}" style="text-decoration:none;color:inherit"><b>{x[code]["card"]}</b><span>{x[code]["cardDesc"]}</span><span style="display:block;margin-top:8px;color:var(--accent);font-weight:600">{t["open"]}</span></a>' for x in TOOLS if x["key"] != skip)

def page_tool(code, x):
    t = L[code]; d = x[code]; alts = {c: x[c]["path"] for c in LANGS}
    canonical = SITE + d["path"]
    ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": d["h1"], "url": canonical,
          "applicationCategory": "SecurityApplication", "operatingSystem": "Any", "inLanguage": t["lang"],
          "description": d["desc"], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'
    i18n = json.dumps(d["i18n"], ensure_ascii=False)
    scripts = "".join(f'<script src="/assets/{f}" defer></script>' for f in x["scripts"])
    return head(t, d["title"] + " | " + BRAND, d["desc"], canonical, alts, extra) + f"""<body data-tool="{x['key']}">
{header(t, alts)}
<main class="wrap">
  <section class="hero">
    <h1>{d['h1']}</h1>
    <p>{d['sub']}</p>
  </section>
  {d['tool']()}
  {ad(t, 'below-tool')}
  <article class="content">
    {d['content']}
    <h2>{t['toolsH']}</h2>
    <div class="features"><a class="feature" href="{t['path']}" style="text-decoration:none;color:inherit"><b>{t['ctaBtn']}</b><span>{t['desc']}</span><span style="display:block;margin-top:8px;color:var(--accent);font-weight:600">{t['open']}</span></a>{tool_cards(code, x['key'])}</div>
  </article>
</main>
{footer(t, alts)}
<div class="toast" id="toast" role="status"></div>
<script>window.I18N={i18n};</script>
{scripts}
</body>
</html>
"""

def page_home(code):
    t = L[code]
    canonical = SITE + t["path"]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    app_ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": BRAND, "url": canonical,
              "applicationCategory": "SecurityApplication", "operatingSystem": "Any", "inLanguage": t["lang"],
              "description": t["desc"], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    ld = ('<script type="application/ld+json">' + json.dumps(app_ld, ensure_ascii=False) + '</script>\n'
          '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>')
    trust = "".join(f"<span><i></i>{x}</span>" for x in t["trust"])
    how = "".join(f"<li><b>{a}</b>{b}</li>" for a, b in t["how"])
    feat = "".join(f'<div class="feature"><b>{a}</b><span>{b}</span></div>' for a, b in t["feat"])
    cmp_rows = "".join(f'<tr><td>{a}</td><td class="yes">✓</td><td class="no">{c}</td></tr>' for a, b, c in t["cmp"])
    cols = "".join(f"<th>{c}</th>" for c in t["cmpCols"])
    safe = "".join(f"<p>{p}</p>" for p in t["safe"])
    where = "".join(f"<h3>{a}</h3><p>{b}</p>" for a, b in t["where"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    i18n = json.dumps(t["i18n"], ensure_ascii=False)
    return head(t, t["title"], t["desc"], canonical, {c: L[c]["path"] for c in LANGS}, ld) + f"""<body>
{header(t)}
<main class="wrap">
  <section class="hero">
    <h1>{t['h1']}</h1>
    <p>{t['sub']}</p>
    <div class="trust">{trust}</div>
  </section>

  <section class="tool" aria-label="2FA">
    <label class="lbl" for="secret">{t['label']} <small>{t['labelSmall']}</small></label>
    <textarea id="secret" spellcheck="false" autocomplete="off" autocapitalize="off" autocorrect="off" placeholder="{html.escape(t['placeholder'])}"></textarea>
    <div class="row">
      <button class="btn" id="pasteBtn" type="button">{ICON_PASTE}<span>{t['paste']}</span></button>
      <button class="btn" id="qrBtn" type="button">{ICON_QR}<span>{t['qr']}</span></button>
      <input type="file" id="qrFile" accept="image/*" hidden>
      <button class="btn" id="shareBtn" type="button">{ICON_LINK}<span>{t['share']}</span></button>
      <span class="spacer"></span>
      <button class="btn ghost" id="clearBtn" type="button">{t['clear']}</button>
    </div>
    <div class="hint">{t['hint']}</div>
    <div class="hint" id="shareNote" hidden>{t['shareNote']}</div>
    <details class="adv">
      <summary>{t['adv']}</summary>
      <div class="adv-grid">
        <label>{t['alg']}<select id="alg"><option>SHA1</option><option>SHA256</option><option>SHA512</option></select></label>
        <label>{t['digits']}<select id="digits"><option>6</option><option>8</option></select></label>
        <label>{t['period']}<select id="period"><option value="30">30 s</option><option value="60">60 s</option></select></label>
      </div>
      <label class="hint" style="display:flex;gap:8px;align-items:center;margin-top:10px"><input type="checkbox" id="autoCopy"> {t['autocopy']}</label>
    </details>
    <div class="results" id="results" aria-live="polite"></div>
    <div class="bulk" id="bulkWrap" hidden>
      <div class="row"><label class="lbl" for="bulkOut" style="margin:0">{t['bulk']}</label><span class="spacer"></span>
      <button class="btn primary" id="copyAllBtn" type="button">{t['copyAll']}</button></div>
      <textarea id="bulkOut" readonly spellcheck="false" style="margin-top:8px"></textarea>
    </div>
  </section>

  <div class="keep" id="keepBar" hidden><span>{t['keep']}</span><span class="spacer"></span><button class="btn sm primary" id="installBtn" type="button" hidden>{t['keepInstall']}</button><button class="btn sm ghost" id="keepOk" type="button">{t['keepOk']}</button></div>

  <section class="content" id="tools">
    <h2>{t['toolsH']}</h2>
    <div class="features four">{tool_cards(code)}</div>
  </section>

  {ad(t, 'below-tool')}

  <article class="content">
    <h2>{t['howH']}</h2>
    <ol class="steps">{how}</ol>

    <h2>{t['featH']}</h2>
    <div class="features">{feat}</div>

    <h2>{t['cmpH']}</h2>
    <div class="table-wrap"><table><thead><tr>{cols}</tr></thead><tbody>{cmp_rows}</tbody></table></div>

    {ad(t, 'in-content')}

    <h2>{t['safeH']}</h2>
    {safe}

    <h2>{t['whereH']}</h2>
    {where}

    <h2>{t['guidesH']}</h2>
    <div class="features">{guide_cards(code)}</div>

    <h2>{t['faqH']}</h2>
    <div class="faq">{faq}</div>
  </article>
</main>
{footer(t)}
<div class="toast" id="toast" role="status"></div>
<script>window.I18N={i18n};</script>
<script src="/assets/totp.js" defer></script>
<script src="/assets/qrread.js" defer></script>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""

def page_privacy(code):
    t = L[code]; pv = t["pv"]
    canonical = SITE + t["privacy"]
    body = "".join(f"<h2>{a}</h2><p>{b}</p>" for a, b in pv["body"])
    return head(t, pv["title"], pv["body"][0][1], canonical, {c: L[c]["privacy"] for c in LANGS}, ) + f"""<body>
{header(t, {c: L[c]["privacy"] for c in LANGS})}
<main class="wrap legal content">
  <h1>{pv['h1']}</h1>
  <p class="lead">{pv['updated']} {UPDATED}</p>
  {body}
</main>
{footer(t, {c: L[c]["privacy"] for c in LANGS})}
<script>
(function(){{var r=document.documentElement;document.getElementById('themeBtn').addEventListener('click',function(){{var d=r.getAttribute('data-theme')?r.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme: dark)').matches;var n=d?'light':'dark';r.setAttribute('data-theme',n);try{{localStorage.setItem('q2fa.theme',n)}}catch(e){{}}}});}})();
</script>
</body>
</html>
"""

import hashlib
def _ver(rel):
    try: return hashlib.md5(open(os.path.join(OUT, rel), "rb").read()).hexdigest()[:8]
    except OSError: return "1"
ASSET_V = {a: _ver("assets/" + a) for a in ("style.css", "app.js", "totp.js", "qrread.js", "qrcode.js", "tools.js")}

def w(rel, content):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    if rel.endswith(".html"):
        for a, v in ASSET_V.items():
            content = content.replace('/assets/' + a + '"', '/assets/' + a + '?v=' + v + '"')
    open(p, "w", encoding="utf-8").write(content)

def fname(path):
    p = path.lstrip("/")
    return p + "index.html" if (p == "" or p.endswith("/")) else p + ".html"

for c in LANGS:
    t = L[c]
    w(fname(t["path"]), page_home(c))
    w(fname(t["guidesPath"]), page_guides(c))
    w(fname(t["privacy"]), page_privacy(c))
    for a in ARTICLES:
        if a.get(c):
            w(fname(gpath(c, a)), page_article(c, a))
    for x in TOOLS:
        w(fname(x[c]["path"]), page_tool(c, x))
def page_404():
    t = L["en"]
    homes = "".join(f'<a class="pill" href="{L[c]["path"]}" lang="{L[c]["lang"]}">{L[c]["langName"]}</a> ' for c in LANGS)
    tools = "".join(f'<li><a href="{x["en"]["path"]}">{x["en"]["card"]}</a></li>' for x in TOOLS)
    return f"""<!DOCTYPE html>
<html lang="en" data-root="/" data-home="/">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | {BRAND}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
<script>try{{var t=localStorage.getItem('q2fa.theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
</head>
<body>
<header class="wrap top"><a class="brand" href="/">{LOGO}<span>{BRAND}</span></a></header>
<main class="wrap content">
  <section class="hero"><h1>404 – Page not found</h1><p>This page doesn't exist. Get your 2FA code on the home page, or pick your language:</p></section>
  <p style="display:flex;flex-wrap:wrap;gap:8px">{homes}</p>
  <div class="cta"><b>{t['cta']}</b><a class="btn primary" href="/">{t['ctaBtn']}</a></div>
  <h2>{t['toolsH']}</h2><ul>{tools}</ul>
  <p><a href="/guides/">{t['guidesH']}</a></p>
</main>
</body>
</html>
"""

w("404.html", page_404())
try:
    from PIL import Image
    Image.open(os.path.join(OUT, "assets/icon-192.png")).convert("RGBA").save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
except Exception as e:
    print("favicon skipped:", e)
w("assets/icon.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
w("ads.txt", "# Replace with your AdSense line, e.g.:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")

groups = [({c: L[c]["path"] for c in LANGS}, "1.0")] + [({c: x[c]["path"] for c in LANGS}, "0.9") for x in TOOLS] \
    + [({c: L[c]["guidesPath"] for c in LANGS}, "0.8")] + [({c: gpath(c, a) for c in LANGS if a.get(c)}, "0.7") for a in ARTICLES] \
    + [({c: L[c]["privacy"] for c in LANGS}, "0.3")]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for alts, pr in groups:
    links = ""
    if len(alts) > 1:
        links = "".join(f'<xhtml:link rel="alternate" hreflang="{L[c]["lang"]}" href="{SITE}{p}"/>' for c, p in alts.items())
        if "en" in alts:
            links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}"/>'
    for c, loc in alts.items():
        sm.append(f'  <url><loc>{SITE}{loc}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority>{links}</url>')
sm.append('</urlset>')
w("sitemap.xml", "\n".join(sm) + "\n")

w("manifest.webmanifest", json.dumps({
  "name": "Get2FA – 2FA Code Generator", "short_name": BRAND, "start_url": "/", "scope": "/",
  "display": "standalone", "background_color": "#f6f7fb", "theme_color": "#2f5cff",
  "icons": [{"src": "/assets/icon.svg", "sizes": "any", "type": "image/svg+xml"},
            {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))

w("sw.js", """/* Get2FA offline cache. Only static files are cached; secrets are never involved. */
const V = 'q2fa-v5';
const FILES = ['/', '/pt/', '/assets/style.css', '/assets/totp.js', '/assets/app.js', '/assets/qrread.js', '/assets/icon.svg'];
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== V).map(x => caches.delete(x)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(V).then(x => x.put(e.request, c)); return r; })
    .catch(() => caches.match(e.request, { ignoreSearch: true }).then(r => r || caches.match('/'))));
});
""")

# Netlify / Cloudflare Pages headers (security + clean URLs)
w("_headers", """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  X-Frame-Options: DENY
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

/assets/*
  Cache-Control: public, max-age=604800
""")
print("ok")
