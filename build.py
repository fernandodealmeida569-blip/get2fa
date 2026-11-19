#!/usr/bin/env python3
"""Generates the Get2FA static site (EN + PT) into ./site"""
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

L = {
 "en": {
  "lang": "en", "path": "/", "root": "/", "privacy": "/privacy",
  "title": "2FA Code Generator – Get Your Authenticator Code Online | Get2FA",
  "desc": "Paste your 2FA secret key and get the 6-digit authenticator code instantly. Works with Google, Facebook, Instagram, Microsoft and more. 100% in your browser: your key is never sent.",
  "h1": "Get your 2FA code from a secret key",
  "sub": "Paste a 2FA secret, an <code class=\"k\">otpauth://</code> link or a QR code and get the same 6-digit code your authenticator app shows. Fast, free and computed only on your device.",
  "trust": ["Your key never leaves this device", "Many keys at once", "Works offline"],
  "label": "2FA secret key", "labelSmall": "one per line",
  "placeholder": "Paste your secret key, e.g. JBSW Y3DP EHPK 3PXP\nor many lines like login|password|SECRET",
  "paste": "Paste", "qr": "Scan QR image", "share": "Copy link", "clear": "Clear",
  "autocopy": "Auto-copy code",
  "hint": "Tip: paste or drop a QR code screenshot anywhere on the page. Google Authenticator export QR codes work too.",
  "shareNote": "Link copied. The key is after the <b>#</b>, which browsers never send to any server, but anyone you share the link with can generate your codes.",
  "adv": "Advanced settings", "alg": "Algorithm", "digits": "Digits", "period": "Period",
  "bulk": "Results (line|code) — ready to paste into a spreadsheet", "copyAll": "Copy all",
  "ad": "Advertisement",
  "i18n": {
    "copy": "Copy", "copied": "Code copied", "autoCopied": "New code copied automatically", "copiedAll": "All codes copied",
    "next": "Next:", "key": "Key", "clickCopy": "Click to copy",
    "empty": "Your codes will appear here as soon as you paste a key.",
    "invalid": "Not a valid 2FA secret:", "hotp": "Counter-based (HOTP) keys are not supported:",
    "noKey": "Paste a key first", "linkCopied": "Link copied",
    "pasteManual": "Press Ctrl+V (or ⌘V) to paste",
    "qrUnsupported": "Couldn't load the QR reader. Check your connection or paste the text key.",
    "qrNotFound": "No 2FA QR code found in that image", "qrAdded": "Key added from QR code"
  },
  "langSwitch": ("Português", "/pt/"),
  "howH": "How to get your 2FA code",
  "how": [("Find your secret key", "When you turn on 2FA, the site shows a QR code and a text key (often under “Can't scan it?”). Save that key."),
          ("Paste it above", "Paste the key, the otpauth:// link, or an image of the QR code. Spaces and lowercase letters are fine."),
          ("Copy the code", "Click the code to copy it and enter it before the ring runs out. A new code appears every 30 seconds.")],
  "featH": "Why Get2FA",
  "feat": [("Private by design", "Codes are calculated with your browser's built-in Web Crypto. No key, code or account name is ever uploaded, logged or stored."),
           ("Bulk mode", "Paste hundreds of keys or account lines such as <code class=\"k\">login|password|SECRET</code>. We find the key in each line and give you a ready-to-copy list."),
           ("Current and next code", "See how many seconds are left and the code that comes next, so you never type one that is about to expire."),
           ("QR codes and otpauth links", "Drop or paste a QR screenshot, or paste an otpauth:// link. Issuer, account, digits and period are read automatically."),
           ("Fast links that stay private", "Bookmark get2fa.online/#YOURKEY. The part after # stays in your browser; it is never sent to our server."),
           ("Works everywhere", "Phone or desktop, light or dark mode, and it keeps working offline once loaded. SHA-1, SHA-256, SHA-512, 6 or 8 digits.")],
  "cmpH": "How we compare",
  "cmpCols": ["", "Get2FA", "Typical 2FA sites"],
  "cmp": [("Key processed only on your device", True, "Often unclear"),
          ("Key kept out of the URL sent to the server", True, "Often in the path (/tok/KEY)"),
          ("Many keys at once", True, "Sometimes"),
          ("Shows next code and time left", True, "Rarely"),
          ("QR image and otpauth:// support", True, "Rarely"),
          ("SHA-256/512, 8 digits, 60 s", True, "Rarely"),
          ("Reads Google Authenticator export QR", True, "No"),
          ("Works offline", True, "No")],
  "safeH": "Is it safe to paste a 2FA key into a website?",
  "safe": ["A 2FA secret key is as sensitive as a password: anyone who has it can generate your codes. That's why Get2FA does all the math inside your browser with the standard algorithm (RFC 6238) and never sends the key anywhere. You can check it yourself: open your browser's developer tools, go to the Network tab and paste a key. No request contains it.",
           "Still, a website is not a replacement for an authenticator app. For accounts you use every day, keep the key in an app such as Google Authenticator, Microsoft Authenticator, 2FAS, Aegis or a password manager, and use Get2FA when you're on another device, setting up a new phone, or managing many accounts."],
  "whereH": "Where to find your 2FA secret key",
  "where": [("Google", "Google Account → Security → 2-Step Verification → Authenticator → Set up → “Can't scan it?”."),
            ("Facebook", "Accounts Center → Password and security → Two-factor authentication → Authentication app. The key is shown below the QR code."),
            ("Instagram", "Settings → Accounts Center → Password and security → Two-factor authentication → Authentication app → “Copy key”."),
            ("Microsoft", "Security → Advanced security options → Add a sign-in method → Authenticator app → “I want to use a different app” → “Can't scan the image?”."),
            ("Discord, X/Twitter, Amazon, GitHub", "When you set up an authenticator app, look for “enter key manually” or “can't scan the code”. That text is your secret key.")],
  "faqH": "Frequently asked questions",
  "faq": [("Is Get2FA free?", "Yes. It's free and needs no sign-up. The site is supported by ads, which never appear inside the generator."),
          ("Will the code be the same as in Google Authenticator?", "Yes. Every app that follows the TOTP standard gives the same code for the same key at the same time, including Google Authenticator, Microsoft Authenticator, Authy and 2FAS."),
          ("Why is my code not accepted?", "The most common reason is a wrong device clock. TOTP codes depend on the exact time, so turn on automatic date and time on your device. Also check that you copied the full key and that the site doesn't use 8 digits or a 60-second period (see Advanced settings)."),
          ("Do you save my keys?", "No. Keys exist only in this tab's memory and disappear when you close it. We don't use cookies or storage for keys; only your theme and auto-copy choice are remembered on your device."),
          ("Can I get codes for many accounts at once?", "Yes. Paste one key per line, or full lines like login|password|SECRET. You'll get a code for each one plus a list in the format line|code that you can copy at once."),
          ("What is a 2FA secret key?", "It's a random code, usually 16 to 32 letters A–Z and numbers 2–7 (Base32), that a website shares with your authenticator when you turn on two-factor authentication. The QR code is just this key in picture form."),
          ("I lost my phone. Can Get2FA recover my codes?", "Only if you saved the secret key. Get2FA can't read keys from another device. If you don't have the key, use the backup codes the service gave you or its account recovery process.")],
  "foot": "Codes are generated on your device. We never see your keys.",
  "privacyLink": "Privacy policy", "contactLink": "Contact", "guides": "Guides", "guidesPath": "/guides/", "guidesH": "2FA guides", "guidesLead": "Step-by-step help to set up, move and fix two-factor authentication.", "read": "Read guide →", "cta": "Have your secret key? Get your code now", "ctaBtn": "Open the 2FA generator", "updatedLbl": "Updated", "back": "← All guides",
  "pv": {
   "title": "Privacy Policy | Get2FA", "h1": "Privacy policy", "updated": "Last updated:",
   "body": [
    ("The short version", "Get2FA generates two-factor codes entirely in your browser. Your secret keys, codes and account names are never sent to our servers, stored, or shared with anyone."),
    ("What we don't collect", "We do not collect the 2FA secret keys, otpauth links, QR code images or account lines you enter. They are processed in your browser's memory and are discarded when you close or reload the page. Links in the form get2fa.online/#KEY keep the key after the # sign, a part of the address that browsers do not send to servers."),
    ("What is stored on your device", "We save two preferences in your browser's local storage: your light/dark theme and whether auto-copy is turned on. You can clear them at any time by clearing your browser's site data."),
    ("Hosting and logs", "Like any website, our hosting provider may record standard technical data such as IP address, browser type and the pages requested, for security and to keep the site running. These logs never contain your secret keys. We also use Cloudflare Web Analytics, a privacy-first service without cookies, to count page views; it does not read what you type."),
    ("Advertising", "We use Google AdSense to show ads. Google and its partners may use cookies to serve ads based on your visits to this and other websites. You can opt out of personalized advertising at <a href=\"https://adssettings.google.com\" rel=\"nofollow noopener\">Google Ads Settings</a> or <a href=\"https://www.aboutads.info/choices/\" rel=\"nofollow noopener\">aboutads.info</a>. Learn more about <a href=\"https://policies.google.com/technologies/partner-sites\" rel=\"nofollow noopener\">how Google uses data</a>. Where required by law (for example in the EEA, UK and Brazil), we ask for your consent before using advertising cookies."),
    ("Your rights", "Depending on where you live (including under the GDPR and Brazil's LGPD), you may have the right to access, correct or delete personal data and to withdraw consent. Because we don't collect your keys, there is no key data to request. For anything else, contact us."),
    ("Contact", "Questions about this policy: <a href=\"mailto:" + CONTACT + "\">" + CONTACT + "</a>.")]
  }
 },
 "pt": {
  "lang": "pt-BR", "path": "/pt/", "root": "/", "privacy": "/pt/privacidade",
  "title": "Gerador de Código 2FA – Pegue seu código do autenticador online | Get2FA",
  "desc": "Cole a chave secreta 2FA e receba na hora o código de 6 dígitos do autenticador. Funciona com Google, Facebook, Instagram, Microsoft e outros. 100% no seu navegador: sua chave nunca é enviada.",
  "h1": "Pegue seu código 2FA a partir da chave secreta",
  "sub": "Cole a chave 2FA, um link <code class=\"k\">otpauth://</code> ou um QR code e receba o mesmo código de 6 dígitos do seu app autenticador. Rápido, grátis e calculado só no seu aparelho.",
  "trust": ["Sua chave nunca sai do seu aparelho", "Várias chaves de uma vez", "Funciona offline"],
  "label": "Chave secreta 2FA", "labelSmall": "uma por linha",
  "placeholder": "Cole sua chave secreta, ex: JBSW Y3DP EHPK 3PXP\nou várias linhas como login|senha|CHAVE",
  "paste": "Colar", "qr": "Ler imagem do QR", "share": "Copiar link", "clear": "Limpar",
  "autocopy": "Copiar código automaticamente",
  "hint": "Dica: cole ou arraste um print do QR code em qualquer lugar da página. QR de exportação do Google Authenticator também funciona.",
  "shareNote": "Link copiado. A chave fica depois do <b>#</b>, parte que o navegador nunca envia a nenhum servidor, mas quem receber o link consegue gerar seus códigos.",
  "adv": "Configurações avançadas", "alg": "Algoritmo", "digits": "Dígitos", "period": "Período",
  "bulk": "Resultados (linha|código) — prontos para colar numa planilha", "copyAll": "Copiar tudo",
  "ad": "Publicidade",
  "i18n": {
    "copy": "Copiar", "copied": "Código copiado", "autoCopied": "Novo código copiado automaticamente", "copiedAll": "Todos os códigos copiados",
    "next": "Próximo:", "key": "Chave", "clickCopy": "Clique para copiar",
    "empty": "Seus códigos aparecem aqui assim que você colar uma chave.",
    "invalid": "Chave 2FA inválida:", "hotp": "Chaves baseadas em contador (HOTP) não são suportadas:",
    "noKey": "Cole uma chave primeiro", "linkCopied": "Link copiado",
    "pasteManual": "Aperte Ctrl+V (ou ⌘V) para colar",
    "qrUnsupported": "Não foi possível carregar o leitor de QR. Confira a conexão ou cole a chave em texto.",
    "qrNotFound": "Nenhum QR code de 2FA encontrado na imagem", "qrAdded": "Chave adicionada pelo QR code"
  },
  "langSwitch": ("English", "/"),
  "howH": "Como pegar seu código 2FA",
  "how": [("Encontre sua chave secreta", "Quando você ativa o 2FA, o site mostra um QR code e uma chave em texto (geralmente em “Não consegue escanear?”). Guarde essa chave."),
          ("Cole aqui em cima", "Cole a chave, o link otpauth:// ou uma imagem do QR code. Espaços e letras minúsculas não tem problema."),
          ("Copie o código", "Clique no código para copiar e use antes do círculo zerar. Um novo código aparece a cada 30 segundos.")],
  "featH": "Por que usar o Get2FA",
  "feat": [("Privado de verdade", "Os códigos são calculados com o Web Crypto do próprio navegador. Nenhuma chave, código ou nome de conta é enviado, registrado ou salvo."),
           ("Modo em massa", "Cole centenas de chaves ou linhas de conta como <code class=\"k\">login|senha|CHAVE</code>. Encontramos a chave em cada linha e entregamos uma lista pronta para copiar."),
           ("Código atual e o próximo", "Veja quantos segundos faltam e qual é o próximo código, para nunca digitar um que está prestes a expirar."),
           ("QR code e links otpauth", "Arraste ou cole o print de um QR code, ou cole um link otpauth://. Emissor, conta, dígitos e período são lidos automaticamente."),
           ("Links rápidos e privados", "Salve get2fa.online/pt/#SUACHAVE nos favoritos. O que vem depois do # fica no seu navegador e nunca chega ao nosso servidor."),
           ("Funciona em qualquer lugar", "Celular ou computador, modo claro ou escuro, e continua funcionando offline depois de carregado. SHA-1, SHA-256, SHA-512, 6 ou 8 dígitos.")],
  "cmpH": "Comparação",
  "cmpCols": ["", "Get2FA", "Sites de 2FA comuns"],
  "cmp": [("Chave processada só no seu aparelho", True, "Nem sempre fica claro"),
          ("Chave fora do endereço enviado ao servidor", True, "Muitas vezes no caminho (/tok/CHAVE)"),
          ("Várias chaves de uma vez", True, "Às vezes"),
          ("Mostra o próximo código e o tempo restante", True, "Raramente"),
          ("Imagem de QR e links otpauth://", True, "Raramente"),
          ("SHA-256/512, 8 dígitos, 60 s", True, "Raramente"),
          ("Lê o QR de exportação do Google Authenticator", True, "Não"),
          ("Funciona offline", True, "Não")],
  "safeH": "É seguro colar uma chave 2FA num site?",
  "safe": ["A chave secreta do 2FA é tão sensível quanto uma senha: quem tem a chave consegue gerar seus códigos. Por isso o Get2FA faz todo o cálculo dentro do seu navegador, com o algoritmo padrão (RFC 6238), e nunca envia a chave para lugar nenhum. Você mesmo pode conferir: abra as ferramentas de desenvolvedor do navegador, vá na aba Rede (Network) e cole uma chave. Nenhuma requisição contém a chave.",
           "Mesmo assim, um site não substitui um app autenticador. Para as contas que você usa todo dia, guarde a chave num app como Google Authenticator, Microsoft Authenticator, 2FAS, Aegis ou num gerenciador de senhas, e use o Get2FA quando estiver em outro aparelho, trocando de celular ou gerenciando muitas contas."],
  "whereH": "Onde encontrar sua chave secreta 2FA",
  "where": [("Google", "Conta do Google → Segurança → Verificação em duas etapas → Authenticator → Configurar → “Não consegue ler o código?”."),
            ("Facebook", "Central de Contas → Senha e segurança → Autenticação de dois fatores → App de autenticação. A chave aparece abaixo do QR code."),
            ("Instagram", "Configurações → Central de Contas → Senha e segurança → Autenticação de dois fatores → App de autenticação → “Copiar chave”."),
            ("Microsoft", "Segurança → Opções de segurança avançadas → Adicionar uma nova forma de entrar → App autenticador → “Quero usar outro app” → “Não consegue ler a imagem?”."),
            ("Discord, X/Twitter, Amazon, GitHub", "Ao configurar um app autenticador, procure “inserir chave manualmente” ou “não consegue escanear”. Esse texto é a sua chave secreta.")],
  "faqH": "Perguntas frequentes",
  "faq": [("O Get2FA é grátis?", "Sim. É grátis e não precisa de cadastro. O site é mantido por anúncios, que nunca aparecem dentro do gerador."),
          ("O código vai ser igual ao do Google Authenticator?", "Sim. Todo app que segue o padrão TOTP gera o mesmo código para a mesma chave no mesmo horário, incluindo Google Authenticator, Microsoft Authenticator, Authy e 2FAS."),
          ("Por que meu código não é aceito?", "O motivo mais comum é o relógio do aparelho errado. Os códigos TOTP dependem do horário exato, então ative data e hora automáticas. Confira também se copiou a chave inteira e se o site não usa 8 dígitos ou período de 60 segundos (veja Configurações avançadas)."),
          ("Vocês salvam minhas chaves?", "Não. As chaves existem só na memória desta aba e somem quando você fecha. Não usamos cookies nem armazenamento para chaves; só o tema e a opção de copiar automaticamente ficam salvos no seu aparelho."),
          ("Dá pra pegar códigos de várias contas de uma vez?", "Sim. Cole uma chave por linha, ou linhas completas como login|senha|CHAVE. Você recebe o código de cada uma e uma lista no formato linha|código para copiar de uma vez."),
          ("O que é a chave secreta do 2FA?", "É um código aleatório, normalmente com 16 a 32 letras de A a Z e números de 2 a 7 (Base32), que o site compartilha com o seu autenticador quando você ativa a verificação em duas etapas. O QR code é só essa chave em forma de imagem."),
          ("Perdi meu celular. O Get2FA recupera meus códigos?", "Só se você tiver guardado a chave secreta. O Get2FA não consegue ler chaves de outro aparelho. Se você não tem a chave, use os códigos de backup que o serviço forneceu ou o processo de recuperação de conta.")],
  "foot": "Os códigos são gerados no seu aparelho. Nunca vemos suas chaves.",
  "privacyLink": "Política de privacidade", "contactLink": "Contato", "guides": "Guias", "guidesPath": "/pt/guias/", "guidesH": "Guias de 2FA", "guidesLead": "Passo a passo para configurar, transferir e resolver problemas da verificação em duas etapas.", "read": "Ler guia →", "cta": "Já tem a chave secreta? Pegue seu código agora", "ctaBtn": "Abrir o gerador de 2FA", "updatedLbl": "Atualizado em", "back": "← Todos os guias",
  "pv": {
   "title": "Política de Privacidade | Get2FA", "h1": "Política de privacidade", "updated": "Atualizada em:",
   "body": [
    ("Resumo", "O Get2FA gera códigos de dois fatores inteiramente no seu navegador. Suas chaves secretas, códigos e nomes de conta nunca são enviados aos nossos servidores, salvos ou compartilhados com ninguém."),
    ("O que não coletamos", "Não coletamos as chaves secretas 2FA, links otpauth, imagens de QR code ou linhas de conta que você insere. Eles são processados na memória do seu navegador e descartados quando você fecha ou recarrega a página. Links no formato get2fa.online/#CHAVE mantêm a chave depois do sinal #, parte do endereço que os navegadores não enviam aos servidores."),
    ("O que fica salvo no seu aparelho", "Salvamos duas preferências no armazenamento local do navegador: o tema claro/escuro e se a cópia automática está ligada. Você pode apagá-las a qualquer momento limpando os dados do site no navegador."),
    ("Hospedagem e registros", "Como qualquer site, nosso provedor de hospedagem pode registrar dados técnicos padrão, como endereço IP, tipo de navegador e páginas acessadas, para segurança e funcionamento do site. Esses registros nunca contêm suas chaves secretas. Também usamos o Cloudflare Web Analytics, um serviço sem cookies, para contar visualizações de página; ele não lê o que você digita."),
    ("Publicidade", "Usamos o Google AdSense para exibir anúncios. O Google e seus parceiros podem usar cookies para exibir anúncios com base nas suas visitas a este e a outros sites. Você pode desativar a publicidade personalizada nas <a href=\"https://adssettings.google.com\" rel=\"nofollow noopener\">Configurações de anúncios do Google</a> ou em <a href=\"https://www.aboutads.info/choices/\" rel=\"nofollow noopener\">aboutads.info</a>. Saiba mais sobre <a href=\"https://policies.google.com/technologies/partner-sites?hl=pt-BR\" rel=\"nofollow noopener\">como o Google usa dados</a>. Quando exigido por lei (por exemplo, pela LGPD no Brasil e pelo GDPR na Europa), pedimos seu consentimento antes de usar cookies de publicidade."),
    ("Seus direitos", "Conforme a LGPD e outras leis aplicáveis, você pode ter direito de acessar, corrigir ou excluir dados pessoais e de revogar consentimento. Como não coletamos suas chaves, não há dados de chaves a solicitar. Para qualquer outra questão, fale conosco."),
    ("Contato", "Dúvidas sobre esta política: <a href=\"mailto:" + CONTACT + "\">" + CONTACT + "</a>.")]
  }
 }
}

THEME_JS = """<script>
(function(){var r=document.documentElement;document.getElementById('themeBtn').addEventListener('click',function(){var d=r.getAttribute('data-theme')?r.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme: dark)').matches;var n=d?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('q2fa.theme',n)}catch(e){}});})();
</script>"""

def hreflang(kind):
    if kind == "home":
        en, pt = SITE + "/", SITE + "/pt/"
    elif kind == "privacy":
        en, pt = SITE + "/privacy", SITE + "/pt/privacidade"
    else:
        en = SITE + kind[0]
        pt = SITE + kind[1] if kind[1] else None
    if not pt:
        return f'<link rel="alternate" hreflang="en" href="{en}">\n<link rel="alternate" hreflang="x-default" href="{en}">'
    return (f'<link rel="alternate" hreflang="en" href="{en}">\n'
            f'<link rel="alternate" hreflang="pt-BR" href="{pt}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{en}">')

def head(t, title, desc, canonical, kind, extra=""):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}" data-root="/">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{hreflang(kind)}
<meta name="referrer" content="no-referrer">
<meta name="theme-color" content="#2f5cff">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:locale" content="{'pt_BR' if t['lang']=='pt-BR' else 'en_US'}">
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

def header(t, alt=None):
    name, href = t["langSwitch"]
    if alt: href = alt
    home = t["path"]
    return f"""<header class="wrap top">
  <a class="brand" href="{home}">{LOGO}<span>{BRAND}</span></a>
  <nav class="nav">
    <a class="pill" href="{t['guidesPath']}">📘 <span class="t">{t['guides']}</span></a>
    <a class="pill" href="{href}" hreflang="{'pt-BR' if href.startswith('/pt/') else 'en'}" lang="{'pt-BR' if href.startswith('/pt/') else 'en'}">🌐 <span class="t">{name}</span></a>
    <button class="pill" id="themeBtn" type="button" aria-label="Theme">{ICON_MOON}</button>
  </nav>
</header>"""

def footer(t, alt=None):
    name, href = t["langSwitch"]
    if alt: href = alt
    return f"""<footer>
  <div class="wrap">
    <div>© 2026 {BRAND}. {t['foot']}</div>
    <nav><a href="{t['guidesPath']}">{t['guides']}</a><a href="{t['privacy']}">{t['privacyLink']}</a><a href="mailto:{CONTACT}">{t['contactLink']}</a><a href="{href}">{name}</a></nav>
  </div>
</footer>"""

def ad(t, slot):
    return f'<div class="ad-slot" data-label="{t["ad"]}" data-slot="{slot}"><!-- AdSense unit: {slot} --></div>'

from articles import ARTICLES

def gpath(code, a):
    return L[code]["guidesPath"] + a[code]["slug"] if a.get(code) else None

def other(code):
    return "pt" if code == "en" else "en"

def guide_cards(code):
    t = L[code]
    return "".join(f'<a class="feature" href="{gpath(code, a)}" style="text-decoration:none;color:inherit"><b>{a[code]["h1"]}</b><span>{a[code]["desc"]}</span><span style="display:block;margin-top:8px;color:var(--accent);font-weight:600">{t["read"]}</span></a>' for a in ARTICLES if a.get(code))

def page_guides(code):
    t = L[code]
    canonical = SITE + t["guidesPath"]
    o = other(code)
    title = f"{t['guidesH']} | {BRAND}"
    return head(t, title, t["guidesLead"], canonical, (L["en"]["guidesPath"], L["pt"]["guidesPath"])) + f"""<body>
{header(t, L[o]["guidesPath"])}
<main class="wrap content">
  <section class="hero"><h1>{t['guidesH']}</h1><p>{t['guidesLead']}</p></section>
  <div class="features">{guide_cards(code)}</div>
  {ad(t, 'guides-index')}
</main>
{footer(t, L[o]["guidesPath"])}
{THEME_JS}
</body>
</html>
"""

def page_article(code, a):
    t = L[code]; x = a[code]; o = other(code)
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
    alt = gpath(o, a) or L[o]["guidesPath"]
    return head(t, f"{x['title']} | {BRAND}", x["desc"], canonical, (gpath("en", a), gpath("pt", a)), extra) + f"""<body>
{header(t, alt)}
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
{footer(t, alt)}
{THEME_JS}
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
    return head(t, t["title"], t["desc"], canonical, "home", ld) + f"""<body>
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
<script src="/assets/app.js" defer></script>
</body>
</html>
"""

def page_privacy(code):
    t = L[code]; pv = t["pv"]
    canonical = SITE + t["privacy"]
    body = "".join(f"<h2>{a}</h2><p>{b}</p>" for a, b in pv["body"])
    return head(t, pv["title"], pv["body"][0][1], canonical, "privacy") + f"""<body>
{header(t)}
<main class="wrap legal content">
  <h1>{pv['h1']}</h1>
  <p class="lead">{pv['updated']} {UPDATED}</p>
  {body}
</main>
{footer(t)}
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
ASSET_V = {a: _ver("assets/" + a) for a in ("style.css", "app.js", "totp.js")}

def w(rel, content):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    if rel.endswith(".html"):
        for a, v in ASSET_V.items():
            content = content.replace('/assets/' + a + '"', '/assets/' + a + '?v=' + v + '"')
    open(p, "w", encoding="utf-8").write(content)

w("index.html", page_home("en"))
w("guides/index.html", page_guides("en"))
w("pt/guias/index.html", page_guides("pt"))
for a in ARTICLES:
    w("guides/" + a["en"]["slug"] + ".html", page_article("en", a))
    if a.get("pt"):
        w("pt/guias/" + a["pt"]["slug"] + ".html", page_article("pt", a))
w("pt/index.html", page_home("pt"))
w("privacy.html", page_privacy("en"))
w("pt/privacidade.html", page_privacy("pt"))
w("assets/icon.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
w("ads.txt", "# Replace with your AdSense line, e.g.:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")

urls = [("/", "/pt/", "1.0"), ("/guides/", "/pt/guias/", "0.8")] + [(gpath("en", a), gpath("pt", a), "0.7") for a in ARTICLES] + [("/privacy", "/pt/privacidade", "0.3")]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for en, pt, pr in urls:
    if not pt:
        sm.append(f'  <url><loc>{SITE}{en}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>')
        continue
    for loc in (en, pt):
        sm.append(f'  <url><loc>{SITE}{loc}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority>'
                  f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>'
                  f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}{pt}"/>'
                  f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/></url>')
sm.append('</urlset>')
w("sitemap.xml", "\n".join(sm) + "\n")

w("manifest.webmanifest", json.dumps({
  "name": "Get2FA – 2FA Code Generator", "short_name": BRAND, "start_url": "/", "scope": "/",
  "display": "standalone", "background_color": "#f6f7fb", "theme_color": "#2f5cff",
  "icons": [{"src": "/assets/icon.svg", "sizes": "any", "type": "image/svg+xml"},
            {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))

w("sw.js", """/* Get2FA offline cache. Only static files are cached; secrets are never involved. */
const V = 'q2fa-v2';
const FILES = ['/', '/pt/', '/assets/style.css', '/assets/totp.js', '/assets/app.js', '/assets/icon.svg'];
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
