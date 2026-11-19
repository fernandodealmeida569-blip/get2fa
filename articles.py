# -*- coding: utf-8 -*-
"""Guides for Get2FA. Each article has an EN and a PT version."""

ARTICLES = [
# ---------------------------------------------------------------- 1
{
  "key": "find-key",
 "en": {
  "slug": "find-2fa-secret-key",
  "title": "Where to Find Your 2FA Secret Key (Google, Facebook, Instagram, Microsoft)",
  "desc": "Learn what a 2FA secret key is and exactly where to find it when you turn on two-factor authentication on Google, Facebook, Instagram, Microsoft and other sites.",
  "h1": "Where to find your 2FA secret key",
  "lead": "The secret key is the text version of the QR code you scan when you turn on two-factor authentication. Save it once and you can rebuild your codes on any device.",
  "body": """
<h2>What is a 2FA secret key?</h2>
<p>When you choose “authentication app” as your 2FA method, the site creates a random secret and shares it with your app. The app combines that secret with the current time to make a new 6-digit code every 30 seconds. This method is called TOTP (time-based one-time password).</p>
<p>The secret is usually shown in two ways: as a <strong>QR code</strong> and as a <strong>text key</strong> of 16 to 32 characters, made of letters A–Z and numbers 2–7, for example <code class="k">JBSW Y3DP EHPK 3PXP</code>. Both contain exactly the same information.</p>

<h2>Where each site shows the key</h2>
<p>Most sites hide the text key behind a link under the QR code. Look for words like <em>“Can't scan it?”</em>, <em>“Enter key manually”</em>, <em>“Copy key”</em> or <em>“Setup key”</em>.</p>
<h3>Google</h3>
<p>Open your Google Account, go to <strong>Security → 2-Step Verification → Authenticator</strong> and choose to set up an authenticator app. Under the QR code, tap <strong>“Can't scan it?”</strong> to see the key.</p>
<h3>Facebook</h3>
<p>Go to <strong>Settings &amp; privacy → Settings → Accounts Center → Password and security → Two-factor authentication</strong>, pick your account and choose <strong>Authentication app</strong>. The key appears with a <strong>Copy key</strong> button next to the QR code.</p>
<h3>Instagram</h3>
<p>In the app, open your profile, tap the menu, then <strong>Accounts Center → Password and security → Two-factor authentication</strong>, select your account and choose <strong>Authentication app</strong>. Tap <strong>Copy key</strong>. Instagram only lets you turn on the authentication app method from the Android or iPhone app.</p>
<h3>Microsoft</h3>
<p>When adding an authenticator app, choose to use a different app and then <strong>“Can't scan the image?”</strong>. Microsoft shows the secret code on that page.</p>
<h3>Other sites (Discord, X, Amazon, GitHub…)</h3>
<p>The flow is almost always the same: choose the authenticator app option, then look for the link that lets you enter the key manually.</p>

<h2>Already set up 2FA without saving the key?</h2>
<p>Most sites never show the key again. If you need it, turn the authenticator method off and on again (or use “add another device”), and this time save the new key. Remember to update your authenticator app too, because the old key stops working.</p>

<h2>How to store the key safely</h2>
<ul>
<li>Keep it in a password manager (Bitwarden, 1Password, etc.) in the same entry as the account.</li>
<li>Never send it by email or chat, and never post a screenshot of the QR code.</li>
<li>Anyone with the key can generate your codes, so treat it like a password.</li>
</ul>
"""
 },
 "pt": {
  "slug": "onde-encontrar-chave-secreta-2fa",
  "title": "Onde encontrar a chave secreta do 2FA (Google, Facebook, Instagram, Microsoft)",
  "desc": "Entenda o que é a chave secreta do 2FA e onde encontrá-la ao ativar a verificação em duas etapas no Google, Facebook, Instagram, Microsoft e outros sites.",
  "h1": "Onde encontrar a chave secreta do 2FA",
  "lead": "A chave secreta é a versão em texto do QR code que você escaneia ao ativar a verificação em duas etapas. Guardando ela uma vez, você recria seus códigos em qualquer aparelho.",
  "body": """
<h2>O que é a chave secreta do 2FA?</h2>
<p>Quando você escolhe “app de autenticação” como método de 2FA, o site cria um segredo aleatório e compartilha com o seu app. O app junta esse segredo com o horário atual e gera um código novo de 6 dígitos a cada 30 segundos. Esse método se chama TOTP (senha única baseada em tempo).</p>
<p>O segredo costuma aparecer de duas formas: como <strong>QR code</strong> e como <strong>chave em texto</strong> de 16 a 32 caracteres, com letras de A a Z e números de 2 a 7, por exemplo <code class="k">JBSW Y3DP EHPK 3PXP</code>. Os dois têm exatamente a mesma informação.</p>

<h2>Onde cada site mostra a chave</h2>
<p>A maioria dos sites esconde a chave em texto num link abaixo do QR code. Procure por <em>“Não consegue escanear?”</em>, <em>“Inserir chave manualmente”</em>, <em>“Copiar chave”</em> ou <em>“Chave de configuração”</em>.</p>
<h3>Google</h3>
<p>Abra sua Conta do Google, vá em <strong>Segurança → Verificação em duas etapas → Authenticator</strong> e escolha configurar um app autenticador. Abaixo do QR code, toque em <strong>“Não consegue ler o código?”</strong> para ver a chave.</p>
<h3>Facebook</h3>
<p>Vá em <strong>Configurações e privacidade → Configurações → Central de Contas → Senha e segurança → Autenticação de dois fatores</strong>, escolha sua conta e selecione <strong>App de autenticação</strong>. A chave aparece com um botão <strong>Copiar chave</strong> ao lado do QR code.</p>
<h3>Instagram</h3>
<p>No app, abra seu perfil, toque no menu e vá em <strong>Central de Contas → Senha e segurança → Autenticação de dois fatores</strong>, escolha sua conta e selecione <strong>App de autenticação</strong>. Toque em <strong>Copiar chave</strong>. O Instagram só deixa ativar o método por app de autenticação pelo aplicativo de Android ou iPhone.</p>
<h3>Microsoft</h3>
<p>Ao adicionar um app autenticador, escolha usar outro app e depois <strong>“Não consegue ler a imagem?”</strong>. A Microsoft mostra o código secreto nessa página.</p>
<h3>Outros sites (Discord, X, Amazon, GitHub…)</h3>
<p>O caminho é quase sempre o mesmo: escolha a opção de app autenticador e procure o link para inserir a chave manualmente.</p>

<h2>Já ativou o 2FA sem guardar a chave?</h2>
<p>A maioria dos sites não mostra a chave de novo. Se precisar dela, desative e ative de novo o método por app (ou use “adicionar outro aparelho”) e, dessa vez, guarde a nova chave. Lembre de atualizar o seu app autenticador também, porque a chave antiga para de funcionar.</p>

<h2>Como guardar a chave com segurança</h2>
<ul>
<li>Guarde num gerenciador de senhas (Bitwarden, 1Password etc.), junto com a conta.</li>
<li>Nunca envie por e-mail ou chat, e nunca publique print do QR code.</li>
<li>Quem tem a chave consegue gerar seus códigos, então trate como uma senha.</li>
</ul>
"""
 }
},
# ---------------------------------------------------------------- 2
{
  "key": "instagram",
 "en": {
  "slug": "instagram-2fa-authentication-app",
  "title": "How to Turn On Instagram 2FA with an Authentication App (and Get the Key)",
  "desc": "Step-by-step guide to turning on Instagram two-factor authentication with an authenticator app, copying the setup key and using it on more than one device.",
  "h1": "How to turn on Instagram 2FA with an authentication app",
  "lead": "An authentication app is the safest 2FA method on Instagram. Here's how to turn it on, where to find the setup key and how to use the same key on several devices.",
  "body": """
<h2>Before you start</h2>
<ul>
<li>You need the Instagram app for Android or iPhone. The authentication app method can only be turned on from the mobile app.</li>
<li>Install an authenticator app (Google Authenticator, Microsoft Authenticator, 2FAS, Aegis…) or keep Get2FA open.</li>
</ul>

<h2>Step by step</h2>
<ol>
<li>Open Instagram and tap your profile picture in the bottom right.</li>
<li>Tap the menu (three lines) in the top right.</li>
<li>Tap <strong>Accounts Center</strong>, then <strong>Password and security</strong>.</li>
<li>Tap <strong>Two-factor authentication</strong> and select your Instagram account.</li>
<li>Choose <strong>Authentication app</strong> and tap <strong>Next</strong>.</li>
<li>Tap <strong>Copy key</strong> (or view the QR code). <strong>Save this key</strong> in a safe place before going on.</li>
<li>Add the key to your authenticator app, or paste it into <a href="/">Get2FA</a> to see the code.</li>
<li>Type the 6-digit code into Instagram and tap <strong>Next</strong>.</li>
</ol>
<p>Instagram's key is usually 32 characters long. Spaces don't matter: Get2FA and most apps remove them automatically.</p>

<h2>Using 2FA on more than one device</h2>
<p>The same key works on every device you add it to, so a team member or a second phone can generate the same codes. In Instagram, other devices are added from the same <em>Authentication app</em> screen with <strong>Copy key</strong> or <strong>View QR code</strong>.</p>

<h2>Save your backup codes</h2>
<p>After turning on 2FA, Instagram offers one-time backup codes. They're different from the setup key: each one works only once and is meant for when you can't get a code. Save them together with the key.</p>

<h2>Common problems</h2>
<ul>
<li><strong>“The code isn't valid”</strong>: check that your device's date and time are set to automatic. See <a href="2fa-code-not-working">why 2FA codes don't work</a>.</li>
<li><strong>Option missing</strong>: update the Instagram app. Older versions show 2FA under Settings → Security.</li>
</ul>
"""
 },
 "pt": {
  "slug": "instagram-autenticacao-dois-fatores",
  "title": "Como ativar o 2FA do Instagram com app de autenticação (e pegar a chave)",
  "desc": "Passo a passo para ativar a autenticação de dois fatores do Instagram com app autenticador, copiar a chave e usar em mais de um aparelho.",
  "h1": "Como ativar o 2FA do Instagram com app de autenticação",
  "lead": "O app de autenticação é o método de 2FA mais seguro do Instagram. Veja como ativar, onde encontrar a chave e como usar a mesma chave em vários aparelhos.",
  "body": """
<h2>Antes de começar</h2>
<ul>
<li>Você precisa do app do Instagram no Android ou iPhone. O método por app de autenticação só pode ser ativado pelo aplicativo.</li>
<li>Instale um app autenticador (Google Authenticator, Microsoft Authenticator, 2FAS, Aegis…) ou deixe o Get2FA aberto.</li>
</ul>

<h2>Passo a passo</h2>
<ol>
<li>Abra o Instagram e toque na sua foto de perfil, no canto inferior direito.</li>
<li>Toque no menu (três linhas) no canto superior direito.</li>
<li>Toque em <strong>Central de Contas</strong> e depois em <strong>Senha e segurança</strong>.</li>
<li>Toque em <strong>Autenticação de dois fatores</strong> e escolha sua conta do Instagram.</li>
<li>Selecione <strong>App de autenticação</strong> e toque em <strong>Avançar</strong>.</li>
<li>Toque em <strong>Copiar chave</strong> (ou veja o QR code). <strong>Guarde essa chave</strong> num lugar seguro antes de continuar.</li>
<li>Adicione a chave no seu app autenticador, ou cole no <a href="/pt/">Get2FA</a> para ver o código.</li>
<li>Digite o código de 6 dígitos no Instagram e toque em <strong>Avançar</strong>.</li>
</ol>
<p>A chave do Instagram costuma ter 32 caracteres. Espaços não fazem diferença: o Get2FA e a maioria dos apps tiram automaticamente.</p>

<h2>Usando o 2FA em mais de um aparelho</h2>
<p>A mesma chave funciona em todos os aparelhos onde você adicioná-la, então outra pessoa da equipe ou um segundo celular podem gerar os mesmos códigos. No Instagram, outros aparelhos são adicionados pela mesma tela de <em>App de autenticação</em>, com <strong>Copiar chave</strong> ou <strong>Ver QR code</strong>.</p>

<h2>Guarde os códigos de backup</h2>
<p>Depois de ativar o 2FA, o Instagram oferece códigos de backup de uso único. Eles são diferentes da chave: cada um funciona só uma vez e serve para quando você não consegue gerar um código. Guarde junto com a chave.</p>

<h2>Problemas comuns</h2>
<ul>
<li><strong>“O código não é válido”</strong>: confira se a data e hora do aparelho estão no automático. Veja <a href="codigo-2fa-nao-funciona">por que o código 2FA não funciona</a>.</li>
<li><strong>A opção não aparece</strong>: atualize o app do Instagram. Versões antigas mostram o 2FA em Configurações → Segurança.</li>
</ul>
"""
 }
},
# ---------------------------------------------------------------- 3
{
  "key": "facebook",
 "en": {
  "slug": "facebook-2fa-authentication-app",
  "title": "How to Set Up Facebook 2FA with an Authenticator App (Copy Key)",
  "desc": "Turn on Facebook two-factor authentication with an authenticator app on a computer or phone, copy the key, and save the 10 recovery codes.",
  "h1": "How to set up Facebook 2FA with an authenticator app",
  "lead": "Facebook supports text messages, security keys and authenticator apps for 2FA. An app is safer than SMS and keeps working without signal. Here's how to set it up and keep the key.",
  "body": """
<h2>On a computer</h2>
<ol>
<li>Sign in at facebook.com and click your profile picture in the top right.</li>
<li>Go to <strong>Settings &amp; privacy → Settings</strong>.</li>
<li>Open <strong>Accounts Center</strong>, then <strong>Password and security</strong>.</li>
<li>Click <strong>Two-factor authentication</strong> and choose your Facebook account.</li>
<li>Choose <strong>Authentication app</strong>.</li>
<li>Facebook shows a QR code and a key with a <strong>Copy key</strong> button. Copy and <strong>save the key</strong>.</li>
<li>Add it to your authenticator app, or paste it into <a href="/">Get2FA</a>, and type the 6-digit code to confirm.</li>
</ol>

<h2>On the app (Android or iPhone)</h2>
<p>Open the menu (or your profile picture on iPhone), then <strong>Settings &amp; privacy → Settings → Accounts Center → Password and security → Two-factor authentication</strong>. Pick the account, choose <strong>Authentication app</strong> and tap <strong>Copy key</strong>.</p>

<h2>Save the 10 recovery codes</h2>
<p>Once 2FA is on, Facebook can give you 10 recovery codes. Each one works once, in place of an authenticator code. Find them later in <em>Password and security → Two-factor authentication</em>. Store them with your key, outside your phone.</p>

<h2>Why keep the key?</h2>
<p>If your phone is lost, stolen or reset, the key lets you get your codes back in minutes on a new device or on Get2FA, without going through Facebook's account recovery.</p>

<h2>If the option isn't there</h2>
<p>Facebook moved 2FA into Accounts Center. If you don't see it, update the app or open facebook.com/settings in a browser. You can only add a 2FA method while you still have access to the account; if you're locked out, you'll need Facebook's recovery process.</p>
"""
 },
 "pt": {
  "slug": "facebook-autenticacao-dois-fatores",
  "title": "Como ativar o 2FA do Facebook com app autenticador (copiar chave)",
  "desc": "Ative a autenticação de dois fatores do Facebook com app autenticador no computador ou no celular, copie a chave e guarde os 10 códigos de recuperação.",
  "h1": "Como ativar o 2FA do Facebook com app autenticador",
  "lead": "O Facebook aceita SMS, chave de segurança e app autenticador no 2FA. O app é mais seguro que o SMS e funciona sem sinal. Veja como ativar e guardar a chave.",
  "body": """
<h2>No computador</h2>
<ol>
<li>Entre em facebook.com e clique na sua foto de perfil, no canto superior direito.</li>
<li>Vá em <strong>Configurações e privacidade → Configurações</strong>.</li>
<li>Abra a <strong>Central de Contas</strong> e depois <strong>Senha e segurança</strong>.</li>
<li>Clique em <strong>Autenticação de dois fatores</strong> e escolha sua conta do Facebook.</li>
<li>Selecione <strong>App de autenticação</strong>.</li>
<li>O Facebook mostra um QR code e uma chave com o botão <strong>Copiar chave</strong>. Copie e <strong>guarde a chave</strong>.</li>
<li>Adicione no seu app autenticador, ou cole no <a href="/pt/">Get2FA</a>, e digite o código de 6 dígitos para confirmar.</li>
</ol>

<h2>No app (Android ou iPhone)</h2>
<p>Abra o menu (ou sua foto de perfil no iPhone) e vá em <strong>Configurações e privacidade → Configurações → Central de Contas → Senha e segurança → Autenticação de dois fatores</strong>. Escolha a conta, selecione <strong>App de autenticação</strong> e toque em <strong>Copiar chave</strong>.</p>

<h2>Guarde os 10 códigos de recuperação</h2>
<p>Com o 2FA ativado, o Facebook pode gerar 10 códigos de recuperação. Cada um funciona uma vez, no lugar do código do app. Depois você encontra eles em <em>Senha e segurança → Autenticação de dois fatores</em>. Guarde junto com a chave, fora do celular.</p>

<h2>Por que guardar a chave?</h2>
<p>Se o celular for perdido, roubado ou formatado, a chave permite recuperar seus códigos em minutos num aparelho novo ou no Get2FA, sem passar pela recuperação de conta do Facebook.</p>

<h2>Se a opção não aparecer</h2>
<p>O Facebook levou o 2FA para a Central de Contas. Se não encontrar, atualize o app ou abra facebook.com/settings no navegador. Só dá para adicionar um método de 2FA enquanto você ainda tem acesso à conta; se ficou trancado fora, vai precisar do processo de recuperação do Facebook.</p>
"""
 }
},
# ---------------------------------------------------------------- 4
{
  "key": "transfer",
 "en": {
  "slug": "transfer-google-authenticator-new-phone",
  "title": "How to Transfer Google Authenticator to a New Phone (and Extract the Keys)",
  "desc": "Move Google Authenticator codes to a new phone with cloud sync or the Export accounts QR code, and extract the secret keys from the export QR with Get2FA.",
  "h1": "How to transfer Google Authenticator to a new phone",
  "lead": "There are two ways to move your codes: sign in to Google so they sync, or export them with a QR code. Get2FA can also read that export QR and show each secret key.",
  "body": """
<h2>Option 1: cloud sync (easiest)</h2>
<ol>
<li>On the old phone, open Google Authenticator and tap your profile icon.</li>
<li>Sign in with your Google Account and turn on sync. A small cloud icon confirms the backup.</li>
<li>On the new phone, install Google Authenticator and sign in with the same Google Account. Your codes appear automatically.</li>
</ol>
<p>Sync is convenient, but your 2FA keys are then stored in your Google Account. Protect that account well.</p>

<h2>Option 2: Export accounts (offline)</h2>
<ol>
<li>On the old phone, open the menu and go to <strong>Transfer accounts → Export accounts</strong>.</li>
<li>Select the accounts and tap <strong>Next</strong>. The app shows one or more QR codes.</li>
<li>On the new phone, go to <strong>Transfer accounts → Import accounts → Scan QR code</strong> and scan each code.</li>
</ol>
<p>The export works between Android and iPhone in both directions.</p>

<h2>Get the secret keys from the export QR</h2>
<p>The export QR code uses a special format (<code class="k">otpauth-migration://</code>) that other apps often can't read. <a href="/">Get2FA</a> can: take a screenshot of the export QR (on a phone you trust), then paste or drop the image on Get2FA. Each account appears with its name and live code, and the list shows the full <code class="k">otpauth://</code> link with the key. Save them in your password manager.</p>
<p>Everything is decoded in your browser; the image and the keys are never uploaded. Delete the screenshot afterwards.</p>

<h2>Don't wipe the old phone too soon</h2>
<p>Test a few logins on the new phone before resetting the old one. If something goes wrong after the old phone is gone, you'll need each site's backup codes or recovery process.</p>
"""
 },
 "pt": {
  "slug": "transferir-google-authenticator-novo-celular",
  "title": "Como transferir o Google Authenticator para outro celular (e extrair as chaves)",
  "desc": "Passe os códigos do Google Authenticator para um celular novo com sincronização na nuvem ou pelo QR de exportação, e extraia as chaves com o Get2FA.",
  "h1": "Como transferir o Google Authenticator para outro celular",
  "lead": "Dá para passar seus códigos de dois jeitos: entrando com a conta Google para sincronizar, ou exportando por QR code. O Get2FA também lê esse QR de exportação e mostra cada chave.",
  "body": """
<h2>Opção 1: sincronização na nuvem (mais fácil)</h2>
<ol>
<li>No celular antigo, abra o Google Authenticator e toque no ícone do seu perfil.</li>
<li>Entre com sua Conta do Google e ative a sincronização. Um pequeno ícone de nuvem confirma o backup.</li>
<li>No celular novo, instale o Google Authenticator e entre com a mesma conta. Os códigos aparecem sozinhos.</li>
</ol>
<p>A sincronização é prática, mas suas chaves de 2FA passam a ficar na sua Conta do Google. Proteja bem essa conta.</p>

<h2>Opção 2: Exportar contas (offline)</h2>
<ol>
<li>No celular antigo, abra o menu e vá em <strong>Transferir contas → Exportar contas</strong>.</li>
<li>Escolha as contas e toque em <strong>Avançar</strong>. O app mostra um ou mais QR codes.</li>
<li>No celular novo, vá em <strong>Transferir contas → Importar contas → Ler QR code</strong> e escaneie cada código.</li>
</ol>
<p>A exportação funciona entre Android e iPhone nos dois sentidos.</p>

<h2>Pegue as chaves secretas do QR de exportação</h2>
<p>O QR de exportação usa um formato especial (<code class="k">otpauth-migration://</code>) que muitos apps não leem. O <a href="/pt/">Get2FA</a> lê: tire um print do QR de exportação (num aparelho de confiança) e cole ou arraste a imagem no Get2FA. Cada conta aparece com nome e código atual, e a lista mostra o link <code class="k">otpauth://</code> completo com a chave. Guarde no seu gerenciador de senhas.</p>
<p>Tudo é lido no seu navegador; a imagem e as chaves nunca são enviadas. Apague o print depois.</p>

<h2>Não formate o celular antigo cedo demais</h2>
<p>Teste alguns logins no celular novo antes de resetar o antigo. Se algo der errado depois que o antigo já foi apagado, você vai precisar dos códigos de backup ou da recuperação de cada site.</p>
"""
 }
},
# ---------------------------------------------------------------- 5
{
  "key": "not-working",
 "en": {
  "slug": "2fa-code-not-working",
  "title": "2FA Code Not Working? 7 Reasons and How to Fix Them",
  "desc": "Your authenticator code keeps being rejected? Learn the most common causes, from a wrong device clock to the wrong key, and how to fix each one.",
  "h1": "2FA code not working? Here's how to fix it",
  "lead": "When a site says your 2FA code is invalid, the cause is almost always one of these. Start with the first: it solves most cases.",
  "body": """
<h2>1. Your device's clock is off</h2>
<p>TOTP codes are calculated from the current time. If your phone or computer clock is wrong by more than about 30 seconds, the code won't match. Turn on <strong>automatic date and time</strong> (and automatic time zone) in your device settings, then try a new code.</p>

<h2>2. The code expired while you typed it</h2>
<p>Each code lasts 30 seconds and some sites reject it right at the end. Wait for a fresh code. Get2FA shows the seconds left and the next code, so you can choose the right moment.</p>

<h2>3. You're using the wrong key or account</h2>
<p>If you set up 2FA more than once, only the last key is valid. Make sure the entry in your app belongs to the same account (look at the name and email) and that you copied the whole key without missing characters.</p>

<h2>4. The site uses different settings</h2>
<p>Almost every site uses 6 digits, 30 seconds and SHA-1. A few use 8 digits, 60 seconds or SHA-256. If the QR code has these settings, apps read them automatically. With a text key, set them in Get2FA's <em>Advanced settings</em>.</p>

<h2>5. The key was typed wrong</h2>
<p>Secret keys only use letters A–Z and numbers 2–7. The digits 0, 1, 8 and 9 never appear, so a “0” is really the letter O and a “1” is the letter I or L. Copy and paste instead of typing whenever you can.</p>

<h2>6. The code was already used</h2>
<p>Some sites accept each code only once. If you just used a code, wait for the next one.</p>

<h2>7. 2FA was reset on the site</h2>
<p>If you (or a support agent) turned 2FA off and on again, the old key no longer works. Use a backup code to sign in and set up the authenticator again.</p>

<h2>Still locked out?</h2>
<p>Use the backup or recovery codes the site gave you, or start the site's account recovery. See <a href="lost-phone-2fa">what to do if you lost your phone</a>.</p>
"""
 },
 "pt": {
  "slug": "codigo-2fa-nao-funciona",
  "title": "Código 2FA não funciona? 7 motivos e como resolver",
  "desc": "O código do autenticador é sempre recusado? Veja as causas mais comuns, do relógio errado à chave errada, e como resolver cada uma.",
  "h1": "Código 2FA não funciona? Veja como resolver",
  "lead": "Quando o site diz que o código 2FA é inválido, a causa quase sempre é uma destas. Comece pela primeira: ela resolve a maioria dos casos.",
  "body": """
<h2>1. O relógio do aparelho está errado</h2>
<p>Os códigos TOTP são calculados a partir do horário. Se o relógio do celular ou do computador estiver errado em mais de uns 30 segundos, o código não bate. Ative <strong>data e hora automáticas</strong> (e fuso horário automático) nas configurações e tente um código novo.</p>

<h2>2. O código expirou enquanto você digitava</h2>
<p>Cada código dura 30 segundos e alguns sites recusam bem no final. Espere um código novo. O Get2FA mostra os segundos restantes e o próximo código, para você escolher o momento certo.</p>

<h2>3. Chave ou conta errada</h2>
<p>Se você configurou o 2FA mais de uma vez, só a última chave vale. Confira se a entrada no app é da mesma conta (veja nome e e-mail) e se você copiou a chave inteira, sem faltar caractere.</p>

<h2>4. O site usa outras configurações</h2>
<p>Quase todo site usa 6 dígitos, 30 segundos e SHA-1. Alguns usam 8 dígitos, 60 segundos ou SHA-256. Se o QR code tiver essas configurações, os apps leem sozinhos. Com chave em texto, ajuste nas <em>Configurações avançadas</em> do Get2FA.</p>

<h2>5. A chave foi digitada errada</h2>
<p>Chaves secretas só usam letras de A a Z e números de 2 a 7. Os números 0, 1, 8 e 9 nunca aparecem, então um “0” na verdade é a letra O e um “1” é a letra I ou L. Sempre que puder, copie e cole em vez de digitar.</p>

<h2>6. O código já foi usado</h2>
<p>Alguns sites aceitam cada código uma única vez. Se você acabou de usar um, espere o próximo.</p>

<h2>7. O 2FA foi redefinido no site</h2>
<p>Se você (ou o suporte) desativou e ativou o 2FA de novo, a chave antiga não funciona mais. Use um código de backup para entrar e configure o autenticador outra vez.</p>

<h2>Ainda sem acesso?</h2>
<p>Use os códigos de backup ou de recuperação que o site forneceu, ou inicie a recuperação de conta do site. Veja <a href="perdi-celular-autenticador">o que fazer se perdeu o celular</a>.</p>
"""
 }
},
# ---------------------------------------------------------------- 6
{
  "key": "lost-phone",
 "en": {
  "slug": "lost-phone-2fa",
  "title": "Lost Your Phone with the Authenticator App? What to Do Now",
  "desc": "Lost, stolen or reset phone with your 2FA codes? Here's how to get back into your accounts with saved keys, backup codes, cloud sync or account recovery.",
  "h1": "Lost your phone with the authenticator app? What to do",
  "lead": "Losing the phone that holds your 2FA codes is stressful, but there's usually a way back in. Go through these options in order.",
  "body": """
<h2>1. Did you save the secret keys?</h2>
<p>If you kept the setup keys (in a password manager, a note or a printout), you're in luck: paste each key into <a href="/">Get2FA</a> and you'll have working codes immediately, on any device. Then add the keys to an authenticator on your new phone.</p>

<h2>2. Was cloud sync on?</h2>
<p>Google Authenticator (when signed in), Microsoft Authenticator, 2FAS and others can back up your codes. Install the same app on the new phone and sign in with the same account to restore them.</p>

<h2>3. Use backup codes</h2>
<p>Most sites give you one-time backup or recovery codes when you turn on 2FA (Google, Facebook, Instagram and GitHub all do). Each code gets you in once. After signing in, set up 2FA again on your new phone.</p>

<h2>4. Use another 2FA method</h2>
<p>If you also added SMS, a security key, a passkey or another trusted device, use it to sign in.</p>

<h2>5. Start account recovery</h2>
<p>As a last resort, use the site's “Can't access your codes?” or account recovery option. It can take days and usually needs proof of identity, so start early.</p>

<h2>After you're back in</h2>
<ul>
<li>Set up 2FA again and, this time, <strong>save each new key</strong> in a password manager.</li>
<li>Save the new backup codes outside your phone.</li>
<li>If the phone was stolen, change the passwords of your important accounts and remove the old device from your accounts.</li>
</ul>
"""
 },
 "pt": {
  "slug": "perdi-celular-autenticador",
  "title": "Perdi o celular com o autenticador: o que fazer agora",
  "desc": "Perdeu, foi roubado ou formatou o celular com os códigos 2FA? Veja como voltar às suas contas com chaves salvas, códigos de backup, nuvem ou recuperação de conta.",
  "h1": "Perdi o celular com o autenticador: o que fazer",
  "lead": "Perder o celular com os códigos 2FA assusta, mas quase sempre existe um caminho de volta. Siga estas opções na ordem.",
  "body": """
<h2>1. Você guardou as chaves secretas?</h2>
<p>Se você guardou as chaves de configuração (num gerenciador de senhas, numa nota ou impressas), ótimo: cole cada chave no <a href="/pt/">Get2FA</a> e você terá códigos funcionando na hora, em qualquer aparelho. Depois adicione as chaves num autenticador no celular novo.</p>

<h2>2. A sincronização na nuvem estava ligada?</h2>
<p>O Google Authenticator (com conta conectada), o Microsoft Authenticator, o 2FAS e outros fazem backup dos códigos. Instale o mesmo app no celular novo e entre com a mesma conta para restaurar.</p>

<h2>3. Use os códigos de backup</h2>
<p>A maioria dos sites oferece códigos de backup ou de recuperação de uso único ao ativar o 2FA (Google, Facebook, Instagram e GitHub oferecem). Cada código deixa você entrar uma vez. Depois de entrar, configure o 2FA de novo no celular novo.</p>

<h2>4. Use outro método de 2FA</h2>
<p>Se você também cadastrou SMS, chave de segurança, passkey ou outro aparelho confiável, use para entrar.</p>

<h2>5. Peça a recuperação de conta</h2>
<p>Em último caso, use a opção “Não consegue acessar seus códigos?” ou a recuperação de conta do site. Pode levar dias e geralmente exige comprovar identidade, então comece logo.</p>

<h2>Depois de recuperar o acesso</h2>
<ul>
<li>Configure o 2FA de novo e, dessa vez, <strong>guarde cada chave nova</strong> num gerenciador de senhas.</li>
<li>Guarde os novos códigos de backup fora do celular.</li>
<li>Se o celular foi roubado, troque as senhas das contas importantes e remova o aparelho antigo das suas contas.</li>
</ul>
"""
 }
},
]

# ---------------------------------------------------------------- US-focused, English only
def _us(slug, title, desc, h1, lead, body):
    return {"key": slug, "en": {"slug": slug, "title": title, "desc": desc, "h1": h1, "lead": lead, "body": body}, "pt": None}

_KEEP = """
<h2>Keep a copy of the key</h2>
<p>Before you scan the QR code, look for the option to see the key as text and save it in your password manager. If your phone is lost or replaced, you can paste that key into <a href="/">Get2FA</a> or a new authenticator app and get your codes back in seconds. Never share the key or a screenshot of the QR code: anyone who has it can generate your codes.</p>
"""

ARTICLES += [
_us("amazon-2fa-authenticator-app",
 "How to Set Up Amazon Two-Step Verification with an Authenticator App",
 "Turn on Amazon Two-Step Verification (2SV) with an authenticator app instead of text messages, step by step, and keep a backup so you never get locked out.",
 "How to set up Amazon Two-Step Verification with an authenticator app",
 "Amazon calls 2FA “Two-Step Verification” (2SV). Using an authenticator app is safer than text messages and works without cell signal. Here's how to set it up.",
 """
<h2>Step by step (computer)</h2>
<ol>
<li>Sign in to Amazon, open <strong>Account &amp; Lists</strong> and choose <strong>Your Account</strong>.</li>
<li>Click <strong>Login &amp; security</strong>.</li>
<li>Next to <strong>Two-Step Verification (2SV) Settings</strong>, click <strong>Edit</strong> (or <strong>Turn on</strong>), then <strong>Get Started</strong>.</li>
<li>Select <strong>Authenticator App</strong>. Amazon shows a QR code; use the link below it to see the key as text if you want to save it.</li>
<li>Add the key to your authenticator app (or paste it into <a href="/">Get2FA</a>), type the 6-digit code into Amazon and click <strong>Verify OTP and continue</strong>.</li>
<li>Add a backup method when asked. Amazon requires one, usually a phone number.</li>
<li>Click <strong>Got it. Turn on Two-Step Verification</strong> to finish.</li>
</ol>
<p>The Amazon Shopping app reaches the same <em>Login &amp; security</em> page, so the steps are the same on iPhone and Android.</p>

<h2>Switching from text messages to an app</h2>
<p>If you already use 2SV with SMS, go to <em>Login &amp; security → Two-Step Verification (2SV) Settings → Edit</em>, add an authenticator app and set it as your preferred method.</p>

<h2>One account, all Amazon sites</h2>
<p>Your Amazon login is also used by Audible, Prime Video and other Amazon services, so the same 2SV protects all of them.</p>
""" + _KEEP),

_us("paypal-2fa-authenticator-app",
 "How to Turn On PayPal 2-Step Verification with an Authenticator App",
 "Set up PayPal 2-step verification with Google Authenticator, Microsoft Authenticator or any TOTP app. Web browser steps, tips and what to do if you lose your phone.",
 "How to turn on PayPal 2-step verification with an authenticator app",
 "PayPal supports authenticator apps like Google Authenticator and Microsoft Authenticator for 2-step verification. Setup is done from a web browser, not the PayPal app.",
 """
<h2>Step by step</h2>
<ol>
<li>Log in to PayPal <strong>in a web browser</strong> (the setting isn't available in the PayPal app).</li>
<li>Click the <strong>Settings</strong> icon next to “Log out”.</li>
<li>Open the <strong>Security</strong> tab.</li>
<li>Click <strong>Set Up</strong> (or <strong>Update</strong>) next to <strong>2-step verification</strong>.</li>
<li>Choose <strong>Use an authenticator app</strong> and click <strong>Set it Up</strong>.</li>
<li>Scan the QR code or use the option to enter the key manually. Save the key.</li>
<li>Type the 6-digit code from your app (or from <a href="/">Get2FA</a>) to confirm.</li>
</ol>

<h2>Good to know</h2>
<ul>
<li>PayPal notes that if you turn off text-message 2-step verification, you may not be able to turn the text option on again. An authenticator app is the safer choice anyway.</li>
<li>To turn it off later: <em>Settings → Security → Update next to 2-step verification → Turn Off</em>.</li>
<li>Payment accounts are a top target for phishing. PayPal will never ask for your 2FA code by phone, email or chat.</li>
</ul>
""" + _KEEP),

_us("coinbase-2fa-authenticator-app",
 "How to Set Up Coinbase 2FA with an Authenticator App (TOTP)",
 "Add an authenticator app to Coinbase 2-step verification from a web browser, understand Coinbase's other 2FA methods, and keep a safe backup of your key.",
 "How to set up Coinbase 2FA with an authenticator app",
 "Coinbase requires 2-step verification and supports any TOTP authenticator app, along with passkeys, security keys and push prompts. Here's how to add an authenticator app.",
 """
<h2>Step by step</h2>
<ol>
<li>Install an authenticator app on your phone (Google Authenticator, Microsoft Authenticator, Duo, 2FAS…).</li>
<li>Sign in to Coinbase <strong>from a web browser</strong>. You can't change your 2-step method from the Coinbase mobile app.</li>
<li>Open the security settings page and select the <strong>2FA settings</strong> tab.</li>
<li>Under <strong>Available methods</strong>, click <strong>Set up</strong> next to <strong>Authenticator app</strong>. You'll be asked to confirm with your current method.</li>
<li>Scan the QR code or copy the key, then enter the 6-digit code to finish.</li>
</ol>

<h2>Which 2FA method is best on Coinbase?</h2>
<p>Coinbase lists security keys and passkeys as its strongest methods and lets you turn on several methods at once as backups. Your account is only as secure as the weakest method you leave on, so if you add an authenticator app, consider turning off text messages.</p>

<h2>Extra care for crypto accounts</h2>
<ul>
<li>Coinbase may ask for a code when you sign in from a new device or send crypto, so keep your app (or saved key) handy.</li>
<li>Store the key offline or in a password manager, never in your email or photos.</li>
<li>No real Coinbase employee will ever ask for your 2FA code.</li>
</ul>
""" + _KEEP),

_us("discord-2fa-authenticator-app",
 "How to Enable Discord 2FA with an Authenticator App (and Save Backup Codes)",
 "Turn on Discord two-factor authentication on desktop or mobile, scan the QR code or enter the key manually, and save your backup codes so you never lose your account.",
 "How to enable Discord 2FA with an authenticator app",
 "Discord's 2FA uses an authenticator app as the main method, with SMS only as a backup. Some servers require 2FA for moderators, so it's worth setting up properly.",
 """
<h2>On desktop or in the browser</h2>
<ol>
<li>Click the <strong>gear icon</strong> (User Settings) next to your name.</li>
<li>Open <strong>My Account</strong> and find <strong>Password and Authentication</strong>.</li>
<li>Click <strong>Enable Two-Factor Auth</strong> and enter your password.</li>
<li>Scan the QR code with your authenticator app, or type the 2FA key manually. Save the key.</li>
<li>Enter the 6-digit code from your app (or from <a href="/">Get2FA</a>) and confirm.</li>
<li>When Discord shows your <strong>backup codes</strong>, download them and store them safely.</li>
</ol>

<h2>On iPhone or Android</h2>
<p>Tap your profile picture, open <strong>My Account</strong> (in Account settings) and tap <strong>Enable Two-Factor Auth</strong>. The rest of the steps are the same.</p>

<h2>Backup codes and SMS</h2>
<ul>
<li>Each backup code works once instead of an app code. You can see them later in <em>My Account → View Backup Codes</em> and generate new ones there.</li>
<li>After enabling the app, Discord offers SMS as a backup. It's convenient but less secure.</li>
</ul>
""" + _KEEP),

_us("x-twitter-2fa-authenticator-app",
 "How to Set Up X (Twitter) 2FA with an Authentication App",
 "Protect your X (Twitter) account with an authentication app instead of SMS. Step-by-step setup on web and mobile, plus backup codes and recovery tips.",
 "How to set up X (Twitter) 2FA with an authentication app",
 "X offers three 2FA methods: authentication app, security key and text message, and text messages are limited to Premium subscribers. For most people an authentication app is the way to go.",
 """
<h2>On the web</h2>
<ol>
<li>Click <strong>More</strong> in the left menu, then <strong>Settings and privacy</strong>.</li>
<li>Go to <strong>Security and account access → Security → Two-factor authentication</strong>.</li>
<li>Turn on <strong>Authentication app</strong>, enter your password and click <strong>Get started</strong>.</li>
<li>Scan the QR code, or choose to link the app manually to see the key as text. Save it.</li>
<li>Enter the 6-digit code from your app (or from <a href="/">Get2FA</a>) and confirm.</li>
<li>Save the <strong>backup code</strong> X shows you.</li>
</ol>

<h2>On iPhone or Android</h2>
<p>Tap your profile picture, then <strong>Settings and Support → Settings and privacy → Security and account access → Security → Two-factor authentication</strong>, and turn on <strong>Authentication app</strong>.</p>

<h2>Why not SMS?</h2>
<p>Besides being limited to Premium accounts, text-message codes can be intercepted through SIM-swap attacks. An authentication app or security key is much harder to steal.</p>
""" + _KEEP),
]

# ---------------------------------------------------------------- batch 3 (EN + PT)
_KEEP_PT = """
<h2>Guarde uma cópia da chave</h2>
<p>Antes de escanear o QR code, procure a opção de ver a chave em texto e guarde num gerenciador de senhas. Se o celular for perdido ou trocado, basta colar essa chave no <a href="/pt/">Get2FA</a> ou num app autenticador novo para ter os códigos de volta. Nunca compartilhe a chave nem prints do QR code: quem tem a chave consegue gerar seus códigos.</p>
"""

def _pair(eid, en, pt):
    return {"key": eid, "en": en, "pt": pt}

ARTICLES += [
_pair("tiktok",
 {"slug": "tiktok-2fa-authenticator-app",
  "title": "How to Set Up TikTok 2-Step Verification with an Authenticator App",
  "desc": "Turn on TikTok 2-step verification with an authenticator app in Settings and privacy, save the setup key and avoid getting locked out.",
  "h1": "How to set up TikTok 2-step verification with an authenticator app",
  "lead": "TikTok asks you to pick at least two verification methods. Choosing an authenticator app as one of them protects your account even if someone gets your password or your SMS.",
  "body": """
<h2>Step by step (TikTok app)</h2>
<ol>
<li>Open TikTok and tap <strong>Profile</strong> in the bottom right.</li>
<li>Tap the menu (three lines) and choose <strong>Settings and privacy</strong>.</li>
<li>Open <strong>Security &amp; permissions</strong> (called <em>Security</em> in some versions) and tap <strong>2-step verification</strong>.</li>
<li>Select <strong>Authenticator app</strong> and one more method (email, phone or password). TikTok requires at least two.</li>
<li>Tap <strong>Turn on</strong> and confirm your identity when asked.</li>
<li>TikTok shows a QR code and a <strong>key</strong>. Copy and save the key before going on.</li>
<li>Add the key to your authenticator app (or paste it into <a href="/">Get2FA</a>) and enter the 6-digit code.</li>
</ol>

<h2>Business and ads accounts</h2>
<p>TikTok for Business (Ads Manager) has its own 2-step verification under <em>User settings → Account Security</em>, and it also accepts third-party authenticator apps. It's a separate setting from your personal TikTok account.</p>

<h2>Code not accepted?</h2>
<p>Set your phone's date and time to automatic and use a fresh code. See <a href="2fa-code-not-working">why 2FA codes don't work</a> or test it with the <a href="/check-2fa-code">2FA code checker</a>.</p>
""" + _KEEP},
 {"slug": "tiktok-verificacao-duas-etapas",
  "title": "Como ativar a verificação em duas etapas do TikTok com app autenticador",
  "desc": "Ative a verificação em duas etapas do TikTok com app autenticador em Configurações e privacidade, guarde a chave e evite perder o acesso.",
  "h1": "Como ativar a verificação em duas etapas do TikTok com app autenticador",
  "lead": "O TikTok pede para escolher pelo menos dois métodos de verificação. Usar um app autenticador como um deles protege a conta mesmo se alguém descobrir sua senha ou interceptar o SMS.",
  "body": """
<h2>Passo a passo (app do TikTok)</h2>
<ol>
<li>Abra o TikTok e toque em <strong>Perfil</strong>, no canto inferior direito.</li>
<li>Toque no menu (três linhas) e escolha <strong>Configurações e privacidade</strong>.</li>
<li>Abra <strong>Segurança e permissões</strong> (em algumas versões, só <em>Segurança</em>) e toque em <strong>Verificação em duas etapas</strong>.</li>
<li>Selecione <strong>App autenticador</strong> e mais um método (e-mail, telefone ou senha). O TikTok exige pelo menos dois.</li>
<li>Toque em <strong>Ativar</strong> e confirme sua identidade quando pedir.</li>
<li>O TikTok mostra um QR code e uma <strong>chave</strong>. Copie e guarde a chave antes de continuar.</li>
<li>Adicione a chave no seu app autenticador (ou cole no <a href="/pt/">Get2FA</a>) e digite o código de 6 dígitos.</li>
</ol>

<h2>Contas de anúncios e empresas</h2>
<p>O TikTok for Business (Gerenciador de Anúncios) tem a própria verificação em duas etapas, em <em>Configurações do usuário → Segurança da conta</em>, e também aceita apps autenticadores. É uma configuração separada da sua conta pessoal.</p>

<h2>O código não é aceito?</h2>
<p>Deixe data e hora do celular no automático e use um código novo. Veja <a href="codigo-2fa-nao-funciona">por que o código 2FA não funciona</a> ou teste no <a href="/pt/verificar-codigo-2fa">verificador de código 2FA</a>.</p>
""" + _KEEP_PT}),

_pair("microsoft",
 {"slug": "microsoft-account-2fa-authenticator-app",
  "title": "How to Use Any Authenticator App with Your Microsoft Account (Outlook, Xbox)",
  "desc": "Set up two-step verification on a personal Microsoft account (Outlook, Xbox, OneDrive) with Google Authenticator or any TOTP app instead of Microsoft Authenticator.",
  "h1": "How to use any authenticator app with your Microsoft account",
  "lead": "You don't have to use Microsoft Authenticator. Microsoft accounts work with any TOTP app, including Google Authenticator, 2FAS and Get2FA. The trick is a small link during setup.",
  "body": """
<h2>Step by step</h2>
<ol>
<li>Sign in at <strong>account.microsoft.com/security</strong>.</li>
<li>Select <strong>Manage how I sign in</strong> (or <em>Advanced security options</em>).</li>
<li>Choose <strong>Add a new way to sign in or verify</strong>, then <strong>Use an app</strong>.</li>
<li>When Microsoft offers to install Microsoft Authenticator, select <strong>Set up a different Authenticator app</strong> / <strong>I want to use a different authenticator app</strong>.</li>
<li>Microsoft shows a QR code. Use <strong>“I can't scan the bar code”</strong> to see the secret key and save it.</li>
<li>Add the key to your app (or <a href="/">Get2FA</a>) and type the code to confirm.</li>
<li>Back in security settings, turn on <strong>Two-step verification</strong> if it isn't on yet.</li>
</ol>

<h2>Before you turn it on</h2>
<ul>
<li>Microsoft recommends having three pieces of security info (for example an app, a phone number and an email) so you don't lose access.</li>
<li>Some older apps and devices can't ask for a code. For those, Microsoft uses <strong>app passwords</strong>, created in the same security page.</li>
</ul>

<h2>Work or school accounts</h2>
<p>For accounts managed by a company or school, setup happens at your organization's sign-in page and your administrator decides which apps are allowed.</p>
""" + _KEEP},
 {"slug": "conta-microsoft-autenticador",
  "title": "Como usar qualquer app autenticador na conta Microsoft (Outlook, Xbox)",
  "desc": "Ative a verificação em duas etapas na conta Microsoft pessoal (Outlook, Xbox, OneDrive) com Google Authenticator ou qualquer app TOTP, sem o Microsoft Authenticator.",
  "h1": "Como usar qualquer app autenticador na conta Microsoft",
  "lead": "Você não é obrigado a usar o Microsoft Authenticator. A conta Microsoft funciona com qualquer app TOTP, como Google Authenticator, 2FAS e Get2FA. O segredo é um link durante a configuração.",
  "body": """
<h2>Passo a passo</h2>
<ol>
<li>Entre em <strong>account.microsoft.com/security</strong>.</li>
<li>Selecione <strong>Gerenciar como eu entro</strong> (ou <em>Opções de segurança avançadas</em>).</li>
<li>Escolha <strong>Adicionar uma nova forma de entrar ou verificar</strong> e depois <strong>Usar um aplicativo</strong>.</li>
<li>Quando a Microsoft sugerir instalar o Microsoft Authenticator, selecione <strong>Configurar um aplicativo autenticador diferente</strong> / <strong>Quero usar outro aplicativo</strong>.</li>
<li>A Microsoft mostra um QR code. Use <strong>“Não consigo ler o código de barras”</strong> para ver a chave secreta e guarde.</li>
<li>Adicione a chave no seu app (ou no <a href="/pt/">Get2FA</a>) e digite o código para confirmar.</li>
<li>Nas configurações de segurança, ative a <strong>Verificação em duas etapas</strong> se ainda não estiver ligada.</li>
</ol>

<h2>Antes de ativar</h2>
<ul>
<li>A Microsoft recomenda ter três formas de verificação (por exemplo, app, telefone e e-mail) para não perder o acesso.</li>
<li>Alguns apps e aparelhos antigos não pedem código. Para eles, a Microsoft usa <strong>senhas de aplicativo</strong>, criadas na mesma página de segurança.</li>
</ul>

<h2>Contas de trabalho ou escola</h2>
<p>Em contas gerenciadas por empresa ou escola, a configuração é feita na página de login da organização, e o administrador define quais apps são permitidos.</p>
""" + _KEEP_PT}),

_pair("github",
 {"slug": "github-2fa-totp-app",
  "title": "How to Set Up GitHub 2FA with a TOTP App (Setup Key and Recovery Codes)",
  "desc": "Configure GitHub two-factor authentication with any TOTP app, find the setup key, save recovery codes and add the same key to more than one device.",
  "h1": "How to set up GitHub 2FA with a TOTP app",
  "lead": "GitHub requires 2FA for everyone who contributes code. It works with any TOTP app and shows the exact settings it uses, so it's one of the easiest services to set up.",
  "body": """
<h2>Step by step</h2>
<ol>
<li>Click your profile picture → <strong>Settings</strong>.</li>
<li>In the <em>Access</em> section, open <strong>Password and authentication</strong>.</li>
<li>Click <strong>Enable two-factor authentication</strong>.</li>
<li>Under the QR code, click <strong>setup key</strong> to see the TOTP secret. Save it.</li>
<li>Add the key to your TOTP app (or <a href="/">Get2FA</a>) and type the code under <em>Verify the code from the app</em>.</li>
<li>Download your <strong>recovery codes</strong> and store them safely, then click <strong>I have saved my recovery codes</strong>.</li>
</ol>

<h2>The settings GitHub uses</h2>
<p>If you set up an app manually, GitHub's documentation lists: type TOTP, issuer GitHub, label <code class="k">GitHub:your-username</code>, algorithm SHA1, 6 digits and a 30-second period. These are the defaults in Get2FA.</p>

<h2>More than one device</h2>
<p>To use 2FA on several devices, scan the QR code with each of them during setup, or save the setup key and add it later. If 2FA is already on, you have to reconfigure the TOTP app in your security settings to see a new key.</p>

<h2>Extra protection</h2>
<p>After the TOTP app, you can add a security key, a passkey or GitHub Mobile as extra methods, so losing one device doesn't lock you out.</p>
""" + _KEEP},
 {"slug": "github-2fa-app-totp",
  "title": "Como ativar o 2FA do GitHub com app TOTP (chave e códigos de recuperação)",
  "desc": "Configure a autenticação de dois fatores do GitHub com qualquer app TOTP, encontre a chave de configuração, guarde os códigos de recuperação e use em mais de um aparelho.",
  "h1": "Como ativar o 2FA do GitHub com app TOTP",
  "lead": "O GitHub exige 2FA de todos que contribuem com código. Ele funciona com qualquer app TOTP e mostra exatamente as configurações que usa, então é um dos serviços mais fáceis de configurar.",
  "body": """
<h2>Passo a passo</h2>
<ol>
<li>Clique na sua foto de perfil → <strong>Settings</strong>.</li>
<li>Na seção <em>Access</em>, abra <strong>Password and authentication</strong>.</li>
<li>Clique em <strong>Enable two-factor authentication</strong>.</li>
<li>Abaixo do QR code, clique em <strong>setup key</strong> para ver a chave TOTP. Guarde.</li>
<li>Adicione a chave no seu app TOTP (ou no <a href="/pt/">Get2FA</a>) e digite o código em <em>Verify the code from the app</em>.</li>
<li>Baixe os <strong>recovery codes</strong> (códigos de recuperação), guarde em lugar seguro e clique em <strong>I have saved my recovery codes</strong>.</li>
</ol>

<h2>As configurações que o GitHub usa</h2>
<p>Para configurar um app manualmente, a documentação do GitHub informa: tipo TOTP, emissor GitHub, rótulo <code class="k">GitHub:seu-usuario</code>, algoritmo SHA1, 6 dígitos e período de 30 segundos. São os padrões do Get2FA.</p>

<h2>Mais de um aparelho</h2>
<p>Para usar o 2FA em vários aparelhos, escaneie o QR code com todos durante a configuração, ou guarde a chave e adicione depois. Se o 2FA já estiver ativo, é preciso reconfigurar o app TOTP nas configurações de segurança para ver uma chave nova.</p>

<h2>Proteção extra</h2>
<p>Depois do app TOTP, dá para adicionar chave de segurança, passkey ou o GitHub Mobile como métodos extras, para não perder o acesso se um aparelho sumir.</p>
""" + _KEEP_PT}),

_pair("binance",
 {"slug": "binance-2fa-authenticator-app",
  "title": "How to Enable Binance 2FA with an Authenticator App (Website and App)",
  "desc": "Turn on Binance two-factor authentication with Google Authenticator or any TOTP app, save the setup key and fix codes that don't work.",
  "h1": "How to enable Binance 2FA with an authenticator app",
  "lead": "On a crypto exchange, 2FA is not optional: Binance requires it for withdrawals. An authenticator app is far safer than SMS. Here's how to set it up and keep a backup.",
  "body": """
<h2>On the Binance website</h2>
<ol>
<li>Log in, hover over the <strong>Profile</strong> icon and click <strong>Account</strong>.</li>
<li>Go to <strong>Security</strong> and click <strong>Manage</strong> next to <strong>Authenticator App</strong>.</li>
<li>Click <strong>Enable Authenticator App</strong>.</li>
<li>Binance shows a QR code and a <strong>setup key</strong>. Don't click <em>Next</em> until you've saved the key.</li>
<li>Add the key to your authenticator app (or <a href="/">Get2FA</a>), then enter the 6-digit code to finish.</li>
</ol>

<h2>On the Binance app</h2>
<p>Tap the <strong>Account</strong> icon, tap the profile section at the top, go to <strong>Security</strong> and tap <strong>Authenticator App → Enable</strong>. The rest is the same.</p>

<h2>Tips for crypto accounts</h2>
<ul>
<li>Binance suggests setting up Google Authenticator without linking it to your Google account, so a hacked Google account doesn't expose your exchange codes.</li>
<li>If codes are rejected, Binance's own help points to the phone's date and time: set it to automatic.</li>
<li>Store the key offline. Nobody from support will ever ask for it or for a 2FA code.</li>
</ul>
""" + _KEEP},
 {"slug": "binance-2fa-app-autenticador",
  "title": "Como ativar o 2FA da Binance com app autenticador (site e app)",
  "desc": "Ative a autenticação de dois fatores da Binance com Google Authenticator ou qualquer app TOTP, guarde a chave e resolva códigos que não funcionam.",
  "h1": "Como ativar o 2FA da Binance com app autenticador",
  "lead": "Em corretora de cripto, o 2FA não é opcional: a Binance exige para saques. O app autenticador é muito mais seguro que SMS. Veja como ativar e guardar um backup.",
  "body": """
<h2>No site da Binance</h2>
<ol>
<li>Entre na conta, passe o mouse no ícone de <strong>Perfil</strong> e clique em <strong>Conta</strong>.</li>
<li>Vá em <strong>Segurança</strong> e clique em <strong>Gerenciar</strong> ao lado de <strong>App autenticador</strong>.</li>
<li>Clique em <strong>Ativar app autenticador</strong>.</li>
<li>A Binance mostra um QR code e uma <strong>chave de configuração</strong>. Não clique em <em>Próximo</em> antes de guardar a chave.</li>
<li>Adicione a chave no seu app autenticador (ou no <a href="/pt/">Get2FA</a>) e digite o código de 6 dígitos para concluir.</li>
</ol>

<h2>No app da Binance</h2>
<p>Toque no ícone de <strong>Conta</strong>, toque na área do perfil no topo, vá em <strong>Segurança</strong> e toque em <strong>App autenticador → Ativar</strong>. O resto é igual.</p>

<h2>Dicas para contas de cripto</h2>
<ul>
<li>A Binance sugere configurar o Google Authenticator sem vincular à sua conta Google, para que uma conta Google invadida não exponha os códigos da corretora.</li>
<li>Se os códigos forem recusados, a própria ajuda da Binance aponta o relógio do celular: deixe data e hora no automático.</li>
<li>Guarde a chave offline. Ninguém do suporte vai pedir a chave nem um código 2FA.</li>
</ul>
""" + _KEEP_PT}),
]
