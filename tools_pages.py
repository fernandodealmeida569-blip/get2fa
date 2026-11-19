# -*- coding: utf-8 -*-
"""Extra tool pages for Get2FA (EN + PT)."""

ADV = {
 "en": ("Advanced settings", "Algorithm", "Digits", "Period"),
 "pt": ("Configurações avançadas", "Algoritmo", "Dígitos", "Período"),
}

def adv(code):
    a = ADV[code]
    return f"""<details class="adv">
      <summary>{a[0]}</summary>
      <div class="adv-grid">
        <label>{a[1]}<select id="alg"><option>SHA1</option><option>SHA256</option><option>SHA512</option></select></label>
        <label>{a[2]}<select id="digits"><option>6</option><option>8</option></select></label>
        <label>{a[3]}<select id="period"><option value="30">30 s</option><option value="60">60 s</option></select></label>
      </div>
    </details>"""

TOOLS = [
# ------------------------------------------------------------------ generator
{"key": "gen", "scripts": ["totp.js", "qrcode.js", "tools.js"],
 "en": {
  "path": "/2fa-key-generator",
  "title": "2FA Secret Key & QR Code Generator (TOTP) – Free, In Your Browser",
  "desc": "Generate a random 2FA secret key, its otpauth:// link and QR code for Google Authenticator and any TOTP app. Created on your device with Web Crypto.",
  "h1": "2FA secret key & QR code generator",
  "sub": "Create a random TOTP secret, the otpauth:// link and a QR code that any authenticator app can scan. Perfect for developers testing 2FA or setting up their own app.",
  "card": "Key & QR generator", "cardDesc": "Create a random 2FA secret and its QR code for any authenticator app.",
  "i18n": {"copied": "Copied"},
  "tool": lambda: f"""
  <section class="tool" aria-label="Generator">
    <div class="grid2">
      <label class="fld">Issuer (app or site name)<input id="gIssuer" type="text" placeholder="MyApp" autocomplete="off"></label>
      <label class="fld">Account (user or email)<input id="gAccount" type="text" placeholder="alice@example.com" autocomplete="off"></label>
    </div>
    <div class="row">
      <label class="fld inline">Key length<select id="gBytes"><option value="10">80-bit (16 chars)</option><option value="20" selected>160-bit (32 chars, recommended)</option><option value="32">256-bit (52 chars)</option></select></label>
      <span class="spacer"></span>
      <button class="btn primary" id="gNew" type="button">New key</button>
    </div>
    {adv('en')}
    <div class="genout">
      <div class="qrbox" id="gQr" aria-label="QR code"></div>
      <div class="genfields">
        <div class="lbl">Secret key</div>
        <div class="row tight"><code class="k big" id="gSecret"></code><button class="btn sm" id="gSecretCopy" type="button" data-copy="">Copy</button></div>
        <div class="lbl">otpauth:// link</div>
        <textarea id="gUri" readonly spellcheck="false" rows="3"></textarea>
        <div class="row tight"><button class="btn sm" id="gUriCopy" type="button" data-copy="">Copy link</button><button class="btn sm" id="gDl" type="button">Download QR (SVG)</button><a class="btn sm" id="gOpen" href="/">Open in generator</a></div>
        <div class="lbl">Current code <small id="gLeft"></small></div>
        <div class="code" id="gCode">— — —</div>
      </div>
    </div>
    <div class="hint">The key is created with your browser's secure random generator and never leaves this page.</div>
  </section>""",
  "content": """
    <h2>How to use it</h2>
    <ol class="steps"><li><b>Name it</b>Type the issuer (your app or site) and the account. They become the label people see in their authenticator.</li><li><b>Scan or copy</b>Scan the QR code with Google Authenticator, Microsoft Authenticator, 2FAS or any TOTP app, or copy the otpauth:// link.</li><li><b>Check the code</b>The current code updates live, so you can confirm the app shows the same number.</li></ol>
    <h2>What is an otpauth:// link?</h2>
    <p>It's the standard format authenticator apps read from a QR code: <code class="k">otpauth://totp/Issuer:account?secret=KEY&amp;issuer=Issuer</code>. Optional parameters set the algorithm, digits and period. Most services use SHA-1, 6 digits and 30 seconds, which are the defaults here.</p>
    <h2>Is it safe to generate keys online?</h2>
    <p>Keys are created with <code class="k">crypto.getRandomValues</code> in your browser and nothing is uploaded. For production systems, generate secrets on your own server and store them encrypted; use this tool to test, prototype or set up personal accounts.</p>
    <h2>Which key length should I use?</h2>
    <p>160 bits (32 Base32 characters) is what RFC 4226 recommends and what most services use. 80 bits is the minimum some older apps accept; 256 bits works with modern apps.</p>"""
 },
 "pt": {
  "path": "/pt/gerador-de-chave-2fa",
  "title": "Gerador de chave 2FA e QR code (TOTP) – Grátis, no seu navegador",
  "desc": "Gere uma chave secreta 2FA aleatória, o link otpauth:// e o QR code para Google Authenticator e qualquer app TOTP. Criado no seu aparelho com Web Crypto.",
  "h1": "Gerador de chave 2FA e QR code",
  "sub": "Crie uma chave TOTP aleatória, o link otpauth:// e um QR code que qualquer app autenticador lê. Ideal para desenvolvedores testando 2FA ou configurando o próprio app.",
  "card": "Gerador de chave e QR", "cardDesc": "Crie uma chave 2FA aleatória e o QR code para qualquer app autenticador.",
  "i18n": {"copied": "Copiado"},
  "tool": lambda: f"""
  <section class="tool" aria-label="Gerador">
    <div class="grid2">
      <label class="fld">Emissor (nome do app ou site)<input id="gIssuer" type="text" placeholder="MeuApp" autocomplete="off"></label>
      <label class="fld">Conta (usuário ou e-mail)<input id="gAccount" type="text" placeholder="joao@exemplo.com" autocomplete="off"></label>
    </div>
    <div class="row">
      <label class="fld inline">Tamanho da chave<select id="gBytes"><option value="10">80 bits (16 caracteres)</option><option value="20" selected>160 bits (32 caracteres, recomendado)</option><option value="32">256 bits (52 caracteres)</option></select></label>
      <span class="spacer"></span>
      <button class="btn primary" id="gNew" type="button">Nova chave</button>
    </div>
    {adv('pt')}
    <div class="genout">
      <div class="qrbox" id="gQr" aria-label="QR code"></div>
      <div class="genfields">
        <div class="lbl">Chave secreta</div>
        <div class="row tight"><code class="k big" id="gSecret"></code><button class="btn sm" id="gSecretCopy" type="button" data-copy="">Copiar</button></div>
        <div class="lbl">Link otpauth://</div>
        <textarea id="gUri" readonly spellcheck="false" rows="3"></textarea>
        <div class="row tight"><button class="btn sm" id="gUriCopy" type="button" data-copy="">Copiar link</button><button class="btn sm" id="gDl" type="button">Baixar QR (SVG)</button><a class="btn sm" id="gOpen" href="/pt/">Abrir no gerador</a></div>
        <div class="lbl">Código atual <small id="gLeft"></small></div>
        <div class="code" id="gCode">— — —</div>
      </div>
    </div>
    <div class="hint">A chave é criada pelo gerador aleatório seguro do navegador e nunca sai desta página.</div>
  </section>""",
  "content": """
    <h2>Como usar</h2>
    <ol class="steps"><li><b>Dê um nome</b>Digite o emissor (seu app ou site) e a conta. Eles viram o nome que aparece no app autenticador.</li><li><b>Escaneie ou copie</b>Escaneie o QR code com Google Authenticator, Microsoft Authenticator, 2FAS ou qualquer app TOTP, ou copie o link otpauth://.</li><li><b>Confira o código</b>O código atual atualiza ao vivo, para você confirmar que o app mostra o mesmo número.</li></ol>
    <h2>O que é um link otpauth://?</h2>
    <p>É o formato padrão que os apps autenticadores leem do QR code: <code class="k">otpauth://totp/Emissor:conta?secret=CHAVE&amp;issuer=Emissor</code>. Parâmetros opcionais definem algoritmo, dígitos e período. A maioria dos serviços usa SHA-1, 6 dígitos e 30 segundos, que são os padrões aqui.</p>
    <h2>É seguro gerar chaves online?</h2>
    <p>As chaves são criadas com <code class="k">crypto.getRandomValues</code> no seu navegador e nada é enviado. Em sistemas de produção, gere as chaves no seu próprio servidor e guarde criptografadas; use esta ferramenta para testar, prototipar ou configurar contas pessoais.</p>
    <h2>Qual tamanho de chave usar?</h2>
    <p>160 bits (32 caracteres Base32) é o recomendado pela RFC 4226 e o que a maioria dos serviços usa. 80 bits é o mínimo aceito por alguns apps antigos; 256 bits funciona nos apps modernos.</p>"""
 }},
# ------------------------------------------------------------------ checker
{"key": "check", "scripts": ["totp.js", "tools.js"],
 "en": {
  "path": "/check-2fa-code",
  "title": "Check a 2FA Code – Why Is My Authenticator Code Wrong? | Clock Check",
  "desc": "Paste your 2FA secret and the code your app shows to see if they match, and check if your device clock is off. Find out why your authenticator code isn't working.",
  "h1": "Check a 2FA code and your clock",
  "sub": "Paste your secret key and the code your authenticator shows. We'll tell you if it matches, and if your device's clock is the reason codes are rejected.",
  "card": "2FA code checker", "cardDesc": "See if a code matches your key and whether your device clock is off.",
  "i18n": {"copied": "Copied", "clockOk": "✓ Your device clock is correct (within 2 seconds).",
           "clockAhead": "⚠ Your device clock is about {n} s ahead. Turn on automatic date and time.",
           "clockBehind": "⚠ Your device clock is about {n} s behind. Turn on automatic date and time.",
           "clockUnknown": "Couldn't check your clock right now.",
           "badKey": "That doesn't look like a valid 2FA secret key.", "badCode": "Type the {n}-digit code from your app.",
           "match": "✓ The code matches the current code. Your app and key are correct.",
           "matchPast": "⚠ The code matches one from {s} s ago. Your device clock is probably behind, or the code was old.",
           "matchFuture": "⚠ The code matches one {s} s in the future. The device that made it has its clock ahead.",
           "noMatch": "✗ No match within ±5 minutes. The key, the account or the settings (digits, period, algorithm) are different.",
           "expected": "Current code for this key:"},
  "tool": lambda: f"""
  <section class="tool" aria-label="Checker">
    <div class="note" id="cClock">Checking your clock…</div>
    <label class="fld">Secret key<textarea id="cSecret" rows="2" spellcheck="false" autocomplete="off" placeholder="JBSW Y3DP EHPK 3PXP"></textarea></label>
    <div class="row">
      <label class="fld inline">Code from your app<input id="cCode" type="text" inputmode="numeric" autocomplete="one-time-code" placeholder="123456"></label>
      <span class="spacer"></span>
      <button class="btn primary" id="cCheck" type="button">Check code</button>
    </div>
    {adv('en')}
    <div class="note" id="cResult" aria-live="polite"></div>
    <div class="hint" id="cNow"></div>
  </section>""",
  "content": """
    <h2>What the result means</h2>
    <ul>
    <li><b>Matches the current code:</b> your key and app are fine. If a site still rejects it, the site may have a different key (2FA was reset) or the code expired while typing.</li>
    <li><b>Matches an older or newer code:</b> one of the clocks is off. Turn on automatic date and time on the phone that runs the authenticator.</li>
    <li><b>No match:</b> the key belongs to another account, was copied incompletely, or the site uses 8 digits, 60 seconds or SHA-256.</li>
    </ul>
    <h2>How the clock check works</h2>
    <p>We compare your device's time with the time reported by our server in a normal page request. TOTP codes change every 30 seconds, so a difference of more than a few seconds is enough to make codes fail.</p>
    <p>Still stuck? Read <a href="/guides/2fa-code-not-working">2FA code not working: 7 reasons</a>.</p>"""
 },
 "pt": {
  "path": "/pt/verificar-codigo-2fa",
  "title": "Verificar código 2FA – Por que meu código não funciona? | Teste de relógio",
  "desc": "Cole sua chave 2FA e o código do app para ver se batem, e confira se o relógio do aparelho está errado. Descubra por que o código do autenticador não funciona.",
  "h1": "Verificar código 2FA e o relógio",
  "sub": "Cole a chave secreta e o código que o seu autenticador mostra. Dizemos se bate e se o relógio do seu aparelho é o motivo de os códigos serem recusados.",
  "card": "Verificador de código", "cardDesc": "Veja se um código bate com a chave e se o relógio do aparelho está errado.",
  "i18n": {"copied": "Copiado", "clockOk": "✓ O relógio do seu aparelho está certo (diferença de até 2 segundos).",
           "clockAhead": "⚠ O relógio do seu aparelho está cerca de {n} s adiantado. Ative data e hora automáticas.",
           "clockBehind": "⚠ O relógio do seu aparelho está cerca de {n} s atrasado. Ative data e hora automáticas.",
           "clockUnknown": "Não foi possível verificar o relógio agora.",
           "badKey": "Isso não parece uma chave secreta 2FA válida.", "badCode": "Digite o código de {n} dígitos do seu app.",
           "match": "✓ O código bate com o código atual. Seu app e sua chave estão certos.",
           "matchPast": "⚠ O código bate com um de {s} s atrás. O relógio do aparelho provavelmente está atrasado, ou o código era antigo.",
           "matchFuture": "⚠ O código bate com um de {s} s no futuro. O aparelho que gerou está com o relógio adiantado.",
           "noMatch": "✗ Nenhum código igual em ±5 minutos. A chave, a conta ou as configurações (dígitos, período, algoritmo) são diferentes.",
           "expected": "Código atual desta chave:"},
  "tool": lambda: f"""
  <section class="tool" aria-label="Verificador">
    <div class="note" id="cClock">Verificando o relógio…</div>
    <label class="fld">Chave secreta<textarea id="cSecret" rows="2" spellcheck="false" autocomplete="off" placeholder="JBSW Y3DP EHPK 3PXP"></textarea></label>
    <div class="row">
      <label class="fld inline">Código do seu app<input id="cCode" type="text" inputmode="numeric" autocomplete="one-time-code" placeholder="123456"></label>
      <span class="spacer"></span>
      <button class="btn primary" id="cCheck" type="button">Verificar código</button>
    </div>
    {adv('pt')}
    <div class="note" id="cResult" aria-live="polite"></div>
    <div class="hint" id="cNow"></div>
  </section>""",
  "content": """
    <h2>O que o resultado significa</h2>
    <ul>
    <li><b>Bate com o código atual:</b> sua chave e o app estão certos. Se o site ainda recusar, ele pode ter outra chave (o 2FA foi redefinido) ou o código expirou enquanto você digitava.</li>
    <li><b>Bate com um código anterior ou posterior:</b> algum relógio está errado. Ative data e hora automáticas no celular onde está o autenticador.</li>
    <li><b>Não bate:</b> a chave é de outra conta, foi copiada incompleta, ou o site usa 8 dígitos, 60 segundos ou SHA-256.</li>
    </ul>
    <h2>Como funciona o teste do relógio</h2>
    <p>Comparamos o horário do seu aparelho com o horário informado pelo nosso servidor numa requisição normal da página. Os códigos TOTP mudam a cada 30 segundos, então uma diferença de poucos segundos já basta para os códigos falharem.</p>
    <p>Ainda com problema? Leia <a href="/pt/guias/codigo-2fa-nao-funciona">Código 2FA não funciona: 7 motivos</a>.</p>"""
 }},
# ------------------------------------------------------------------ reader
{"key": "read", "scripts": ["totp.js", "qrread.js", "tools.js"],
 "en": {
  "path": "/read-2fa-qr-code",
  "title": "Read a 2FA QR Code – Extract the Secret Key (Google Authenticator Export Too)",
  "desc": "Upload or paste a 2FA QR code screenshot to extract the secret key and otpauth link. Also decodes Google Authenticator export (otpauth-migration) QR codes. Runs in your browser.",
  "h1": "Read a 2FA QR code and get the secret key",
  "sub": "Drop, paste or upload a screenshot of a 2FA QR code. You'll get the secret key, issuer, account and settings, even from Google Authenticator export codes.",
  "card": "2FA QR code reader", "cardDesc": "Extract the secret key from any 2FA QR code, including Google Authenticator exports.",
  "i18n": {"copied": "Copied", "copy": "Copy", "copyUri": "Copy otpauth link", "openGen": "Get codes", "issuer": "Issuer", "account": "Account",
           "secret": "Secret key", "settings": "Settings", "found": "Found {n} account(s).", "reading": "Reading the image…",
           "qrNotFound": "No 2FA QR code found in that image. Try a sharper screenshot that shows the whole code.",
           "qrUnsupported": "Couldn't load the QR reader. Check your connection and try again."},
  "tool": lambda: """
  <section class="tool" aria-label="QR reader">
    <div class="drop" id="rDrop" role="button" tabindex="0"><b>Drop a QR code image here</b><span>or click to choose a file · or press Ctrl+V to paste a screenshot</span></div>
    <input type="file" id="rFile" accept="image/*" hidden>
    <label class="fld">…or paste an otpauth:// or otpauth-migration:// link<input id="rText" type="text" spellcheck="false" autocomplete="off" placeholder="otpauth-migration://offline?data=…"></label>
    <div id="rOut" aria-live="polite"></div>
    <div class="hint">The image is decoded on your device and is never uploaded.</div>
  </section>""",
  "content": """
    <h2>When is this useful?</h2>
    <ul>
    <li>You have a screenshot of a 2FA QR code and want to save the key in a password manager.</li>
    <li>You exported accounts from Google Authenticator and want the actual keys, not just a transfer to another phone.</li>
    <li>You're a developer checking what your app's QR code really contains.</li>
    </ul>
    <h2>Google Authenticator export codes</h2>
    <p>The <em>Transfer accounts → Export accounts</em> screen makes QR codes in a special <code class="k">otpauth-migration://</code> format that holds several accounts. This reader decodes it and lists each account with its key. See <a href="/guides/transfer-google-authenticator-new-phone">how to transfer Google Authenticator</a>.</p>
    <h2>Privacy</h2>
    <p>Decoding uses your browser's built-in barcode reader or an open-source library loaded from this site. Delete the screenshot when you're done: anyone with it can generate your codes.</p>"""
 },
 "pt": {
  "path": "/pt/ler-qr-code-2fa",
  "title": "Ler QR code 2FA – Extrair a chave secreta (inclui exportação do Google Authenticator)",
  "desc": "Envie ou cole o print de um QR code 2FA para extrair a chave secreta e o link otpauth. Também lê QR de exportação do Google Authenticator (otpauth-migration). Funciona no navegador.",
  "h1": "Ler QR code 2FA e pegar a chave secreta",
  "sub": "Arraste, cole ou envie o print de um QR code de 2FA. Você recebe a chave secreta, o emissor, a conta e as configurações, até de códigos de exportação do Google Authenticator.",
  "card": "Leitor de QR code 2FA", "cardDesc": "Extraia a chave secreta de qualquer QR code 2FA, inclusive exportações do Google Authenticator.",
  "i18n": {"copied": "Copiado", "copy": "Copiar", "copyUri": "Copiar link otpauth", "openGen": "Ver códigos", "issuer": "Emissor", "account": "Conta",
           "secret": "Chave secreta", "settings": "Configurações", "found": "{n} conta(s) encontrada(s).", "reading": "Lendo a imagem…",
           "qrNotFound": "Nenhum QR code de 2FA encontrado na imagem. Tente um print mais nítido, com o código inteiro.",
           "qrUnsupported": "Não foi possível carregar o leitor de QR. Confira a conexão e tente de novo."},
  "tool": lambda: """
  <section class="tool" aria-label="Leitor de QR">
    <div class="drop" id="rDrop" role="button" tabindex="0"><b>Arraste a imagem do QR code aqui</b><span>ou clique para escolher um arquivo · ou aperte Ctrl+V para colar um print</span></div>
    <input type="file" id="rFile" accept="image/*" hidden>
    <label class="fld">…ou cole um link otpauth:// ou otpauth-migration://<input id="rText" type="text" spellcheck="false" autocomplete="off" placeholder="otpauth-migration://offline?data=…"></label>
    <div id="rOut" aria-live="polite"></div>
    <div class="hint">A imagem é lida no seu aparelho e nunca é enviada.</div>
  </section>""",
  "content": """
    <h2>Quando isso é útil?</h2>
    <ul>
    <li>Você tem o print de um QR code de 2FA e quer guardar a chave num gerenciador de senhas.</li>
    <li>Você exportou contas do Google Authenticator e quer as chaves de verdade, não só passar para outro celular.</li>
    <li>Você é desenvolvedor e quer conferir o que o QR code do seu app realmente contém.</li>
    </ul>
    <h2>Códigos de exportação do Google Authenticator</h2>
    <p>A tela <em>Transferir contas → Exportar contas</em> gera QR codes num formato especial, <code class="k">otpauth-migration://</code>, com várias contas. Este leitor decodifica e lista cada conta com a chave. Veja <a href="/pt/guias/transferir-google-authenticator-novo-celular">como transferir o Google Authenticator</a>.</p>
    <h2>Privacidade</h2>
    <p>A leitura usa o leitor de código de barras do próprio navegador ou uma biblioteca de código aberto carregada deste site. Apague o print depois: quem tem a imagem consegue gerar seus códigos.</p>"""
 }},
]
