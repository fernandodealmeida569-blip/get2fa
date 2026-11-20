# -*- coding: utf-8 -*-
"""Guides added after the keyword research (Nov 2026)."""

WHAT_IS = {"key": "what-is",
"en": {
 "slug": "what-is-2fa",
 "title": "What Is 2FA? Two-Factor Authentication Explained Simply",
 "desc": "What 2FA means, how two-factor authentication works, the different types (SMS, authenticator app, security key) and why it protects your accounts.",
 "h1": "What is 2FA (two-factor authentication)?",
 "lead": "2FA, or two-factor authentication, means you need two different things to sign in: something you know, like a password, and something you have, like your phone. A stolen password alone is no longer enough.",
 "body": """
<h2>2FA meaning in one sentence</h2>
<p>Two-factor authentication adds a second check after your password, usually a short code that changes every few seconds, so only the person holding your second factor can get in.</p>
<h2>How 2FA works</h2>
<ol>
<li>You type your username and password as usual.</li>
<li>The site asks for a second proof: a 6-digit code, a tap on your phone or a security key.</li>
<li>Only when both are correct are you signed in.</li>
</ol>
<p>If someone steals or guesses your password, they still can't sign in without the second factor.</p>
<h2>Types of 2FA</h2>
<ul>
<li><strong>Authenticator app (TOTP):</strong> apps like Google Authenticator, Microsoft Authenticator or 2FAS make a new 6-digit code every 30 seconds from a secret key. It works offline and is the most common choice.</li>
<li><strong>SMS or email codes:</strong> easy, but weaker. Text messages can be intercepted or redirected with a SIM swap.</li>
<li><strong>Push notifications:</strong> you approve the sign-in on your phone.</li>
<li><strong>Security keys and passkeys:</strong> a physical key or your device's built-in passkey. The strongest option against phishing.</li>
</ul>
<h2>2FA vs MFA vs 2-step verification</h2>
<p>MFA (multi-factor authentication) means two <em>or more</em> factors, so 2FA is the most common kind of MFA. “2-step verification” is the name Google and others use for the same idea.</p>
<h2>Where does the 2FA code come from?</h2>
<p>With an authenticator app, the site gives you a <strong>secret key</strong> (shown as a QR code). Your app combines that key with the current time to calculate the code. Any app with the same key shows the same code, which is why you can also <a href="/">get a 2FA code online with Get2FA</a> if you saved the key. Learn <a href="find-2fa-secret-key">where to find your secret key</a>.</p>
<h2>Should you turn on 2FA?</h2>
<p>Yes, especially for email, banking, crypto, social media and gaming accounts. Turn it on, save the backup codes the site gives you, and keep a copy of the secret key in a password manager so a lost phone doesn't lock you out.</p>
"""},
"pt": {
 "slug": "o-que-e-2fa",
 "title": "O que é 2FA? Autenticação de dois fatores explicada de forma simples",
 "desc": "O que significa 2FA, como funciona a autenticação de dois fatores, os tipos (SMS, app autenticador, chave de segurança) e por que ela protege suas contas.",
 "h1": "O que é 2FA (autenticação de dois fatores)?",
 "lead": "2FA, ou autenticação de dois fatores, significa que você precisa de duas coisas diferentes para entrar: algo que você sabe, como a senha, e algo que você tem, como o celular. Só a senha roubada já não basta.",
 "body": """
<h2>O significado de 2FA em uma frase</h2>
<p>A autenticação de dois fatores acrescenta uma segunda verificação depois da senha, normalmente um código curto que muda a cada poucos segundos, para que só quem tem o segundo fator consiga entrar.</p>
<h2>Como o 2FA funciona</h2>
<ol>
<li>Você digita usuário e senha normalmente.</li>
<li>O site pede uma segunda prova: um código de 6 dígitos, uma confirmação no celular ou uma chave de segurança.</li>
<li>Só quando as duas estão certas você entra.</li>
</ol>
<p>Se alguém roubar ou adivinhar sua senha, ainda não consegue entrar sem o segundo fator.</p>
<h2>Tipos de 2FA</h2>
<ul>
<li><strong>App autenticador (TOTP):</strong> apps como Google Authenticator, Microsoft Authenticator ou 2FAS geram um código novo de 6 dígitos a cada 30 segundos a partir de uma chave secreta. Funciona sem internet e é a opção mais comum.</li>
<li><strong>Código por SMS ou e-mail:</strong> fácil, mas mais fraco. SMS pode ser interceptado ou desviado com clonagem de chip.</li>
<li><strong>Notificação no celular:</strong> você aprova o login no próprio aparelho.</li>
<li><strong>Chaves de segurança e passkeys:</strong> uma chave física ou a passkey do seu aparelho. É a opção mais forte contra golpes de phishing.</li>
</ul>
<h2>2FA, MFA e verificação em duas etapas</h2>
<p>MFA (autenticação multifator) significa dois <em>ou mais</em> fatores, então o 2FA é o tipo mais comum de MFA. “Verificação em duas etapas” é o nome que Google, gov.br e outros usam para a mesma ideia.</p>
<h2>De onde vem o código 2FA?</h2>
<p>Com um app autenticador, o site entrega uma <strong>chave secreta</strong> (em forma de QR code). O app junta essa chave com o horário atual para calcular o código. Qualquer app com a mesma chave mostra o mesmo código, por isso você também pode <a href="/pt/">pegar o código 2FA online no Get2FA</a> se guardou a chave. Veja <a href="onde-encontrar-chave-secreta-2fa">onde encontrar a chave secreta</a>.</p>
<h2>Vale a pena ativar o 2FA?</h2>
<p>Sim, principalmente em e-mail, banco, cripto, redes sociais e jogos. Ative, guarde os códigos de backup que o site oferece e mantenha uma cópia da chave secreta num gerenciador de senhas, para que perder o celular não te deixe trancado para fora.</p>
"""},
"es": {
 "slug": "que-es-2fa",
 "title": "¿Qué es 2FA? La autenticación en dos pasos explicada fácil",
 "desc": "Qué significa 2FA, cómo funciona la autenticación de dos factores, sus tipos (SMS, app de autenticación, llave de seguridad) y por qué protege tus cuentas.",
 "h1": "¿Qué es 2FA (autenticación de dos factores)?",
 "lead": "2FA, o autenticación de dos factores, significa que necesitas dos cosas distintas para entrar: algo que sabes, como la contraseña, y algo que tienes, como tu móvil. Una contraseña robada ya no basta.",
 "body": """
<h2>Qué significa 2FA en una frase</h2>
<p>La autenticación de dos factores añade una segunda comprobación después de la contraseña, normalmente un código corto que cambia cada pocos segundos, para que solo quien tenga el segundo factor pueda entrar.</p>
<h2>Cómo funciona 2FA</h2>
<ol>
<li>Escribes tu usuario y contraseña como siempre.</li>
<li>El sitio pide una segunda prueba: un código de 6 dígitos, una confirmación en el móvil o una llave de seguridad.</li>
<li>Solo si ambas son correctas entras.</li>
</ol>
<p>Si alguien roba o adivina tu contraseña, sigue sin poder entrar sin el segundo factor.</p>
<h2>Tipos de 2FA</h2>
<ul>
<li><strong>App de autenticación (TOTP):</strong> apps como Google Authenticator, Microsoft Authenticator o 2FAS generan un código nuevo de 6 dígitos cada 30 segundos a partir de una clave secreta. Funciona sin conexión y es la opción más común.</li>
<li><strong>Códigos por SMS o correo:</strong> fáciles, pero más débiles. Los SMS se pueden interceptar o desviar con un duplicado de SIM.</li>
<li><strong>Notificaciones push:</strong> apruebas el inicio de sesión en tu móvil.</li>
<li><strong>Llaves de seguridad y passkeys:</strong> una llave física o la passkey de tu dispositivo. La opción más fuerte contra el phishing.</li>
</ul>
<h2>2FA, MFA y verificación en dos pasos</h2>
<p>MFA (autenticación multifactor) significa dos <em>o más</em> factores, así que 2FA es el tipo de MFA más habitual. “Verificación en dos pasos” es el nombre que usan Google y otros para la misma idea.</p>
<h2>¿De dónde sale el código 2FA?</h2>
<p>Con una app de autenticación, el sitio te da una <strong>clave secreta</strong> (en forma de código QR). La app combina esa clave con la hora actual para calcular el código. Cualquier app con la misma clave muestra el mismo código, por eso también puedes <a href="/es/">obtener tu código 2FA online con Get2FA</a> si guardaste la clave. Mira <a href="donde-encontrar-clave-secreta-2fa">dónde encontrar la clave secreta</a>.</p>
<h2>¿Conviene activar 2FA?</h2>
<p>Sí, sobre todo en correo, banca, cripto, redes sociales y videojuegos. Actívalo, guarda los códigos de respaldo que te da el sitio y conserva una copia de la clave secreta en un gestor de contraseñas para que perder el móvil no te deje fuera.</p>
"""},
"vi": {
 "slug": "2fa-la-gi",
 "title": "2FA là gì? Xác thực 2 yếu tố giải thích dễ hiểu",
 "desc": "2FA là gì, xác thực hai yếu tố hoạt động thế nào, các loại 2FA (SMS, ứng dụng xác thực, khóa bảo mật) và vì sao nó bảo vệ tài khoản của bạn.",
 "h1": "2FA là gì (xác thực hai yếu tố)?",
 "lead": "2FA, hay xác thực hai yếu tố, nghĩa là bạn cần hai thứ khác nhau để đăng nhập: thứ bạn biết, như mật khẩu, và thứ bạn có, như điện thoại. Chỉ lộ mật khẩu thôi là chưa đủ để người khác vào được.",
 "body": """
<h2>2FA nghĩa là gì trong một câu</h2>
<p>Xác thực hai yếu tố thêm một bước kiểm tra sau mật khẩu, thường là một mã ngắn thay đổi sau vài giây, để chỉ người giữ yếu tố thứ hai mới đăng nhập được.</p>
<h2>2FA hoạt động thế nào</h2>
<ol>
<li>Bạn nhập tên đăng nhập và mật khẩu như bình thường.</li>
<li>Trang web yêu cầu thêm một bằng chứng: mã 6 số, xác nhận trên điện thoại hoặc khóa bảo mật.</li>
<li>Chỉ khi cả hai đều đúng bạn mới vào được.</li>
</ol>
<p>Nếu ai đó lấy cắp hoặc đoán được mật khẩu, họ vẫn không đăng nhập được nếu thiếu yếu tố thứ hai.</p>
<h2>Các loại 2FA</h2>
<ul>
<li><strong>Ứng dụng xác thực (TOTP):</strong> Google Authenticator, Microsoft Authenticator hay 2FAS tạo mã 6 số mới sau mỗi 30 giây từ một khóa bí mật. Dùng được khi không có mạng và phổ biến nhất.</li>
<li><strong>Mã qua SMS hoặc email:</strong> dễ dùng nhưng yếu hơn. SMS có thể bị chặn hoặc bị chiếm qua việc làm lại SIM.</li>
<li><strong>Thông báo đẩy:</strong> bạn bấm xác nhận đăng nhập trên điện thoại.</li>
<li><strong>Khóa bảo mật và passkey:</strong> khóa vật lý hoặc passkey có sẵn trên thiết bị. Mạnh nhất trước lừa đảo phishing.</li>
</ul>
<h2>Mã 2FA lấy từ đâu?</h2>
<p>Với ứng dụng xác thực, trang web đưa cho bạn một <strong>khóa bí mật</strong> (dạng mã QR). Ứng dụng kết hợp khóa này với thời gian hiện tại để tính ra mã. Ứng dụng nào có cùng khóa cũng hiện cùng một mã, vì vậy nếu đã lưu khóa, bạn có thể <a href="/vi/">lấy mã 2FA online bằng Get2FA</a>. Xem <a href="tim-khoa-bi-mat-2fa">cách tìm khóa bí mật</a>.</p>
<h2>2FA, MFA và xác minh 2 bước</h2>
<p>MFA (xác thực đa yếu tố) là từ hai yếu tố trở lên, nên 2FA là dạng MFA phổ biến nhất. “Xác minh 2 bước” là tên Google và nhiều dịch vụ dùng cho cùng ý tưởng này.</p>
<h2>Có nên bật 2FA không?</h2>
<p>Có, đặc biệt với email, ngân hàng, tiền mã hóa, mạng xã hội và tài khoản game. Hãy bật 2FA, lưu mã dự phòng mà trang web cung cấp và giữ một bản khóa bí mật trong trình quản lý mật khẩu để mất điện thoại không khiến bạn bị khóa tài khoản.</p>
"""},
"id": {
 "slug": "2fa-adalah",
 "title": "2FA Adalah? Arti Autentikasi Dua Faktor dan Cara Kerjanya",
 "desc": "2FA adalah autentikasi dua faktor. Pelajari artinya, cara kerjanya, jenis-jenisnya (SMS, aplikasi autentikator, kunci keamanan) dan mengapa melindungi akun Anda.",
 "h1": "2FA adalah apa? Penjelasan autentikasi dua faktor",
 "lead": "2FA atau autentikasi dua faktor berarti Anda butuh dua hal berbeda untuk masuk: sesuatu yang Anda ketahui, seperti kata sandi, dan sesuatu yang Anda miliki, seperti ponsel. Kata sandi yang dicuri saja tidak cukup lagi.",
 "body": """
<h2>Arti 2FA dalam satu kalimat</h2>
<p>Autentikasi dua faktor menambahkan pemeriksaan kedua setelah kata sandi, biasanya kode pendek yang berganti setiap beberapa detik, sehingga hanya pemegang faktor kedua yang bisa masuk.</p>
<h2>Cara kerja 2FA</h2>
<ol>
<li>Anda mengetik nama pengguna dan kata sandi seperti biasa.</li>
<li>Situs meminta bukti kedua: kode 6 digit, konfirmasi di ponsel, atau kunci keamanan.</li>
<li>Anda baru bisa masuk jika keduanya benar.</li>
</ol>
<p>Jika seseorang mencuri atau menebak kata sandi Anda, ia tetap tidak bisa masuk tanpa faktor kedua.</p>
<h2>Jenis-jenis 2FA</h2>
<ul>
<li><strong>Aplikasi autentikator (TOTP):</strong> Google Authenticator, Microsoft Authenticator, atau 2FAS membuat kode 6 digit baru setiap 30 detik dari sebuah kunci rahasia. Bisa offline dan paling umum dipakai.</li>
<li><strong>Kode lewat SMS atau email:</strong> mudah, tetapi lebih lemah. SMS bisa disadap atau dialihkan lewat penggantian SIM.</li>
<li><strong>Notifikasi push:</strong> Anda menyetujui login di ponsel.</li>
<li><strong>Kunci keamanan dan passkey:</strong> kunci fisik atau passkey bawaan perangkat. Pilihan terkuat melawan phishing.</li>
</ul>
<h2>2FA, MFA, dan verifikasi 2 langkah</h2>
<p>MFA (autentikasi multifaktor) berarti dua <em>atau lebih</em> faktor, jadi 2FA adalah jenis MFA yang paling umum. “Verifikasi 2 Langkah” adalah nama yang dipakai Google dan layanan lain untuk ide yang sama. Banyak orang juga menyebutnya “2FA auth”.</p>
<h2>Dari mana kode 2FA berasal?</h2>
<p>Dengan aplikasi autentikator, situs memberi Anda <strong>kunci rahasia</strong> (dalam bentuk kode QR). Aplikasi menggabungkan kunci itu dengan waktu saat ini untuk menghitung kode. Aplikasi mana pun dengan kunci yang sama menampilkan kode yang sama, jadi jika Anda menyimpan kuncinya, Anda juga bisa <a href="/id/">mendapatkan kode 2FA online di Get2FA</a>. Lihat <a href="cara-menemukan-kunci-rahasia-2fa">cara menemukan kunci rahasia</a>.</p>
<h2>Perlukah mengaktifkan 2FA?</h2>
<p>Ya, terutama untuk email, bank, kripto, media sosial, dan akun game. Aktifkan, simpan kode cadangan dari situs, dan simpan salinan kunci rahasia di pengelola kata sandi agar kehilangan ponsel tidak membuat Anda terkunci.</p>
"""},
"de": {
 "slug": "was-ist-2fa",
 "title": "Was ist 2FA? Zwei-Faktor-Authentifizierung einfach erklärt",
 "desc": "Was 2FA bedeutet, wie die Zwei-Faktor-Authentifizierung funktioniert, welche Arten es gibt (SMS, Authenticator-App, Sicherheitsschlüssel) und warum sie deine Konten schützt.",
 "h1": "Was ist 2FA (Zwei-Faktor-Authentifizierung)?",
 "lead": "2FA, die Zwei-Faktor-Authentifizierung, bedeutet: Du brauchst zwei verschiedene Dinge zum Anmelden, etwas, das du weißt, wie ein Passwort, und etwas, das du hast, wie dein Handy. Ein gestohlenes Passwort allein reicht dann nicht mehr.",
 "body": """
<h2>2FA in einem Satz</h2>
<p>Die Zwei-Faktor-Authentifizierung ergänzt das Passwort um eine zweite Prüfung, meist einen kurzen Code, der sich alle paar Sekunden ändert, damit nur die Person mit dem zweiten Faktor hineinkommt.</p>
<h2>So funktioniert 2FA</h2>
<ol>
<li>Du gibst wie gewohnt Benutzername und Passwort ein.</li>
<li>Die Website verlangt einen zweiten Nachweis: einen 6-stelligen Code, eine Bestätigung auf dem Handy oder einen Sicherheitsschlüssel.</li>
<li>Erst wenn beides stimmt, bist du angemeldet.</li>
</ol>
<p>Stiehlt oder errät jemand dein Passwort, kommt er ohne den zweiten Faktor trotzdem nicht hinein.</p>
<h2>Arten von 2FA</h2>
<ul>
<li><strong>Authenticator-App (TOTP):</strong> Apps wie Google Authenticator, Microsoft Authenticator oder 2FAS erzeugen alle 30 Sekunden aus einem geheimen Schlüssel einen neuen 6-stelligen Code. Funktioniert offline und ist am verbreitetsten.</li>
<li><strong>Codes per SMS oder E-Mail:</strong> einfach, aber schwächer. SMS können abgefangen oder per SIM-Swapping umgeleitet werden.</li>
<li><strong>Push-Benachrichtigungen:</strong> Du bestätigst die Anmeldung auf dem Handy.</li>
<li><strong>Sicherheitsschlüssel und Passkeys:</strong> ein physischer Schlüssel oder der Passkey deines Geräts. Der beste Schutz gegen Phishing.</li>
</ul>
<h2>2FA, MFA und Bestätigung in zwei Schritten</h2>
<p>MFA (Multi-Faktor-Authentifizierung) bedeutet zwei <em>oder mehr</em> Faktoren, 2FA ist also die häufigste Form von MFA. „Bestätigung in zwei Schritten“ nennt Google dasselbe Prinzip.</p>
<h2>Woher kommt der 2FA-Code?</h2>
<p>Bei einer Authenticator-App gibt dir die Website einen <strong>geheimen Schlüssel</strong> (als QR-Code). Die App kombiniert ihn mit der aktuellen Uhrzeit und berechnet daraus den Code. Jede App mit demselben Schlüssel zeigt denselben Code, deshalb kannst du auch <a href="/de/">deinen 2FA-Code online mit Get2FA abrufen</a>, wenn du den Schlüssel gespeichert hast. Siehe <a href="2fa-geheimen-schluessel-finden">wo du den geheimen Schlüssel findest</a>.</p>
<h2>Solltest du 2FA aktivieren?</h2>
<p>Ja, besonders für E-Mail, Banking, Krypto, soziale Netzwerke und Gaming-Konten. Aktiviere es, speichere die Backup-Codes der Website und bewahre eine Kopie des geheimen Schlüssels in einem Passwortmanager auf, damit ein verlorenes Handy dich nicht aussperrt.</p>
"""},
}

_F_EN = """
<h2>What is fortnite.com/2fa?</h2>
<p><strong>fortnite.com/2fa</strong> is the short link Epic Games uses for turning on two-factor authentication. It takes you to your Epic Games account, where 2FA is managed under <strong>Account → Password &amp; Security</strong>. Fortnite doesn't have its own 2FA: you protect the Epic Games account that your Fortnite progress is linked to.</p>
<h2>How to enable 2FA for Fortnite</h2>
<ol>
<li>Open <strong>fortnite.com/2fa</strong> (or epicgames.com) in a browser and sign in to your Epic Games account.</li>
<li>Go to <strong>Account → Password &amp; Security</strong> and scroll to <strong>Two-factor authentication</strong>.</li>
<li>Choose a method: <strong>authenticator app</strong> (recommended), SMS or email.</li>
<li>For the authenticator app, scan the QR code with Google Authenticator, Microsoft Authenticator or 2FAS and type the 6-digit code to confirm.</li>
<li>Save the backup codes Epic shows you.</li>
</ol>
<p>Playing on PlayStation, Xbox or Switch? Make sure the console account is linked to the same Epic Games account, then enable 2FA there.</p>
<h2>Fortnite 2FA rewards</h2>
<ul>
<li><strong>Battle Royale:</strong> the <strong>Boogie Down</strong> emote.</li>
<li><strong>Save the World:</strong> 50 Armory slots, 10 Backpack slots and a Legendary Troll Stash Llama.</li>
</ul>
<p>If the reward doesn't appear, restart Fortnite and check that 2FA is on for the account you actually play with. 2FA is also required to send gifts and to join many competitive events.</p>
<h2>Tip: save the setup key</h2>
<p>When Epic shows the QR code, also copy the text key under it and keep it in a password manager. If you lose or reset your phone, you can paste that key into <a href="/">Get2FA</a> to get a working code right away. See <a href="find-2fa-secret-key">where to find the secret key</a> and <a href="2fa-code-not-working">what to do if the code isn't working</a>.</p>
<h2>Watch out for scams</h2>
<p>Real 2FA pages are on epicgames.com or fortnite.com. Never type your code into a site promising free V-Bucks, and never share it with anyone, including people claiming to be Epic support.</p>
"""

FORTNITE = {"key": "fortnite",
"en": {"slug": "fortnite-2fa", "title": "Fortnite 2FA: How to Enable It at fortnite.com/2fa (and Get Boogie Down)",
 "desc": "How to turn on two-factor authentication for Fortnite at fortnite.com/2fa, on PC, PlayStation, Xbox or Switch, and the rewards you get: the Boogie Down emote and Save the World items.",
 "h1": "Fortnite 2FA: how to enable it at fortnite.com/2fa",
 "lead": "Turning on 2FA for your Epic Games account protects your skins and V-Bucks, unlocks the free Boogie Down emote and lets you gift items and join tournaments. It takes about two minutes.",
 "body": _F_EN},
"pt": {"slug": "fortnite-2fa", "title": "Fortnite 2FA: como ativar em fortnite.com/2fa (e ganhar o Boogie Down)",
 "desc": "Como ativar a autenticação de dois fatores no Fortnite em fortnite.com/2fa, no PC, PlayStation, Xbox ou Switch, e as recompensas: o gesto Boogie Down e itens do Salve o Mundo.",
 "h1": "Fortnite 2FA: como ativar em fortnite.com/2fa",
 "lead": "Ativar o 2FA na sua conta Epic Games protege suas skins e V-Bucks, libera o gesto Boogie Down de graça e permite presentear itens e entrar em torneios. Leva uns dois minutos.",
 "body": """
<h2>O que é fortnite.com/2fa?</h2>
<p><strong>fortnite.com/2fa</strong> é o link curto que a Epic Games usa para ativar a autenticação de dois fatores. Ele leva à sua conta Epic Games, onde o 2FA fica em <strong>Conta → Senha e segurança</strong>. O Fortnite não tem 2FA próprio: você protege a conta Epic Games ligada ao seu progresso.</p>
<h2>Como ativar o 2FA no Fortnite</h2>
<ol>
<li>Abra <strong>fortnite.com/2fa</strong> (ou epicgames.com) no navegador e entre na sua conta Epic Games.</li>
<li>Vá em <strong>Conta → Senha e segurança</strong> e desça até <strong>Autenticação de dois fatores</strong>.</li>
<li>Escolha o método: <strong>app autenticador</strong> (recomendado), SMS ou e-mail.</li>
<li>No app autenticador, escaneie o QR code com Google Authenticator, Microsoft Authenticator ou 2FAS e digite o código de 6 dígitos para confirmar.</li>
<li>Guarde os códigos de backup que a Epic mostrar.</li>
</ol>
<p>Joga no PlayStation, Xbox ou Switch? Confira se a conta do console está vinculada à mesma conta Epic Games e ative o 2FA nela.</p>
<h2>Recompensas do 2FA no Fortnite</h2>
<ul>
<li><strong>Battle Royale:</strong> o gesto <strong>Boogie Down</strong>.</li>
<li><strong>Salve o Mundo:</strong> 50 espaços no Arsenal, 10 espaços na Mochila e uma Lhama Lendária do Troll.</li>
</ul>
<p>Se a recompensa não aparecer, reinicie o Fortnite e confira se o 2FA está ativo na conta em que você joga. O 2FA também é exigido para presentear itens e para muitos eventos competitivos.</p>
<h2>Dica: guarde a chave de configuração</h2>
<p>Quando a Epic mostrar o QR code, copie também a chave em texto abaixo dele e guarde num gerenciador de senhas. Se perder ou formatar o celular, é só colar a chave no <a href="/pt/">Get2FA</a> para ter um código na hora. Veja <a href="onde-encontrar-chave-secreta-2fa">onde encontrar a chave secreta</a> e <a href="codigo-2fa-nao-funciona">o que fazer se o código não funciona</a>.</p>
<h2>Cuidado com golpes</h2>
<p>As páginas verdadeiras de 2FA ficam em epicgames.com ou fortnite.com. Nunca digite seu código em sites que prometem V-Bucks grátis e nunca passe o código para ninguém, nem para quem diz ser do suporte da Epic.</p>
"""},
"es": {"slug": "fortnite-2fa", "title": "Fortnite 2FA: cómo activarlo en fortnite.com/2fa (y conseguir Boogie Down)",
 "desc": "Cómo activar la autenticación en dos pasos de Fortnite en fortnite.com/2fa, en PC, PlayStation, Xbox o Switch, y las recompensas: el gesto Boogie Down y objetos de Salvar el mundo.",
 "h1": "Fortnite 2FA: cómo activarlo en fortnite.com/2fa",
 "lead": "Activar el 2FA en tu cuenta de Epic Games protege tus skins y paVos, desbloquea gratis el gesto Boogie Down y te permite regalar objetos y entrar en torneos. Tarda unos dos minutos.",
 "body": """
<h2>¿Qué es fortnite.com/2fa?</h2>
<p><strong>fortnite.com/2fa</strong> es el enlace corto que usa Epic Games para activar la autenticación en dos pasos. Te lleva a tu cuenta de Epic Games, donde el 2FA está en <strong>Cuenta → Contraseña y seguridad</strong>. Fortnite no tiene un 2FA propio: proteges la cuenta de Epic Games vinculada a tu progreso.</p>
<h2>Cómo activar 2FA en Fortnite</h2>
<ol>
<li>Abre <strong>fortnite.com/2fa</strong> (o epicgames.com) en el navegador e inicia sesión en tu cuenta de Epic Games.</li>
<li>Ve a <strong>Cuenta → Contraseña y seguridad</strong> y baja hasta <strong>Autenticación de dos factores</strong>.</li>
<li>Elige un método: <strong>app de autenticación</strong> (recomendado), SMS o correo.</li>
<li>Con la app, escanea el código QR con Google Authenticator, Microsoft Authenticator o 2FAS y escribe el código de 6 dígitos para confirmar.</li>
<li>Guarda los códigos de respaldo que te muestra Epic.</li>
</ol>
<p>¿Juegas en PlayStation, Xbox o Switch? Asegúrate de que la cuenta de la consola está vinculada a la misma cuenta de Epic Games y activa ahí el 2FA.</p>
<h2>Recompensas del 2FA en Fortnite</h2>
<ul>
<li><strong>Battle Royale:</strong> el gesto <strong>Boogie Down</strong>.</li>
<li><strong>Salvar el mundo:</strong> 50 espacios de arsenal, 10 de mochila y una llama legendaria del trol.</li>
</ul>
<p>Si no ves la recompensa, reinicia Fortnite y comprueba que el 2FA está activo en la cuenta con la que juegas. El 2FA también es obligatorio para regalar objetos y para muchos eventos competitivos.</p>
<h2>Consejo: guarda la clave de configuración</h2>
<p>Cuando Epic muestre el código QR, copia también la clave de texto que aparece debajo y guárdala en un gestor de contraseñas. Si pierdes o restableces el móvil, pega esa clave en <a href="/es/">Get2FA</a> y tendrás un código al momento. Mira <a href="donde-encontrar-clave-secreta-2fa">dónde encontrar la clave secreta</a> y <a href="codigo-2fa-no-funciona">qué hacer si el código no funciona</a>.</p>
<h2>Cuidado con las estafas</h2>
<p>Las páginas reales de 2FA están en epicgames.com o fortnite.com. Nunca escribas tu código en webs que prometen paVos gratis y nunca se lo des a nadie, ni siquiera a quien diga ser del soporte de Epic.</p>
"""},
"de": {"slug": "fortnite-2fa-aktivieren", "title": "Fortnite 2FA aktivieren unter fortnite.com/2fa (und Boogie Down erhalten)",
 "desc": "So aktivierst du die Zwei-Faktor-Authentifizierung für Fortnite unter fortnite.com/2fa, auf PC, PlayStation, Xbox oder Switch, und die Belohnungen: das Boogie-Down-Emote und Rette-die-Welt-Items.",
 "h1": "Fortnite 2FA aktivieren unter fortnite.com/2fa",
 "lead": "Mit 2FA auf deinem Epic-Games-Konto schützt du deine Skins und V-Bucks, schaltest kostenlos das Emote Boogie Down frei und kannst Geschenke senden und an Turnieren teilnehmen. Das dauert etwa zwei Minuten.",
 "body": """
<h2>Was ist fortnite.com/2fa?</h2>
<p><strong>fortnite.com/2fa</strong> ist der Kurzlink, über den Epic Games die Zwei-Faktor-Authentifizierung einrichten lässt. Er führt zu deinem Epic-Games-Konto, wo du 2FA unter <strong>Konto → Passwort und Sicherheit</strong> verwaltest. Fortnite hat kein eigenes 2FA: Du schützt das Epic-Games-Konto, mit dem dein Fortschritt verknüpft ist.</p>
<h2>So aktivierst du 2FA für Fortnite</h2>
<ol>
<li>Öffne <strong>fortnite.com/2fa</strong> (oder epicgames.com) im Browser und melde dich bei deinem Epic-Games-Konto an.</li>
<li>Gehe zu <strong>Konto → Passwort und Sicherheit</strong> und scrolle zu <strong>Zwei-Faktor-Authentifizierung</strong>.</li>
<li>Wähle eine Methode: <strong>Authenticator-App</strong> (empfohlen), SMS oder E-Mail.</li>
<li>Scanne bei der App den QR-Code mit Google Authenticator, Microsoft Authenticator oder 2FAS und gib zur Bestätigung den 6-stelligen Code ein.</li>
<li>Speichere die Backup-Codes, die Epic dir anzeigt.</li>
</ol>
<p>Du spielst auf PlayStation, Xbox oder Switch? Stelle sicher, dass dein Konsolenkonto mit demselben Epic-Games-Konto verknüpft ist, und aktiviere dort 2FA.</p>
<h2>Fortnite-2FA-Belohnungen</h2>
<ul>
<li><strong>Battle Royale:</strong> das Emote <strong>Boogie Down</strong>.</li>
<li><strong>Rette die Welt:</strong> 50 Arsenalplätze, 10 Rucksackplätze und ein legendäres Troll-Vorratslama.</li>
</ul>
<p>Erscheint die Belohnung nicht, starte Fortnite neu und prüfe, ob 2FA auf dem Konto aktiv ist, mit dem du spielst. 2FA ist außerdem Pflicht, um Geschenke zu senden und an vielen Wettbewerben teilzunehmen.</p>
<h2>Tipp: Einrichtungsschlüssel speichern</h2>
<p>Wenn Epic den QR-Code zeigt, kopiere auch den Textschlüssel darunter und bewahre ihn in einem Passwortmanager auf. Verlierst du dein Handy oder setzt es zurück, fügst du den Schlüssel einfach in <a href="/de/">Get2FA</a> ein und hast sofort einen Code. Siehe <a href="2fa-geheimen-schluessel-finden">wo du den geheimen Schlüssel findest</a> und <a href="2fa-code-funktioniert-nicht">was tun, wenn der Code nicht funktioniert</a>.</p>
<h2>Vorsicht vor Betrug</h2>
<p>Echte 2FA-Seiten liegen auf epicgames.com oder fortnite.com. Gib deinen Code nie auf Seiten ein, die kostenlose V-Bucks versprechen, und teile ihn mit niemandem, auch nicht mit angeblichem Epic-Support.</p>
"""},
}

GOVBR = {"key": "govbr", "en": None,
"pt": {"slug": "verificacao-duas-etapas-gov-br",
 "title": "Verificação em duas etapas do gov.br: como ativar, desativar e recuperar",
 "desc": "Como funciona o 2FA do gov.br, como ativar e desativar a verificação em duas etapas no app gov.br e como recuperar o acesso se perdeu ou trocou de celular.",
 "h1": "Verificação em duas etapas (2FA) do gov.br",
 "lead": "A verificação em duas etapas do gov.br pede, além da senha, um código gerado no aplicativo gov.br do seu celular. Veja como ativar, desativar e o que fazer se você trocou ou perdeu o aparelho.",
 "body": """
<h2>Como funciona o 2FA do gov.br</h2>
<p>Depois de ativada, a verificação em duas etapas pede um código de acesso de 6 dígitos sempre que você entra no gov.br por um navegador ou aparelho novo. Esse código é gerado <strong>exclusivamente no aplicativo gov.br</strong>, e apenas um celular fica vinculado à conta por vez. O recurso está disponível para contas nível prata e ouro.</p>
<div class="note warn">Importante: o gov.br não mostra uma chave secreta para usar em outros apps. Por isso, o código do gov.br <strong>não</strong> pode ser gerado no Google Authenticator nem no Get2FA, só no app oficial.</div>
<h2>Como ativar</h2>
<ol>
<li>Instale o aplicativo gov.br e entre com sua conta.</li>
<li>Abra <strong>Segurança da conta</strong> e ligue a <strong>Verificação em duas etapas</strong>.</li>
<li>Cadastre um <strong>e-mail de recuperação</strong> quando o app pedir. É ele que salva você se perder o celular.</li>
</ol>
<p>Ao entrar num navegador que você usa sempre, dá para marcar “Não solicitar verificação em duas etapas novamente neste navegador”.</p>
<h2>Como desativar</h2>
<p>No app gov.br, vá em <strong>Segurança da conta</strong> e desligue a verificação em duas etapas. Os aparelhos e navegadores autorizados também são gerenciados ali.</p>
<h2>Perdi ou troquei de celular: como recuperar</h2>
<ol>
<li>Na tela que pede o código, clique em <strong>“Estou com dificuldade para gerar o código”</strong>.</li>
<li>Faça o reconhecimento facial para confirmar sua identidade.</li>
<li>Digite o código enviado ao e-mail de recuperação cadastrado.</li>
</ol>
<p>Sem e-mail de recuperação cadastrado, procure o atendimento oficial em gov.br/atendimento.</p>
<h2>O código do app não é aceito?</h2>
<p>Assim como em qualquer 2FA, a data e a hora do celular precisam estar corretas. Ative data e hora automáticas e gere um novo código. Veja outras causas em <a href="codigo-2fa-nao-funciona">código 2FA não funciona</a>.</p>
<h2>E nas outras contas?</h2>
<p>Diferente do gov.br, a maioria dos sites (Google, Instagram, Facebook, Binance…) usa o padrão TOTP e mostra uma chave secreta ao ativar o 2FA. Guardando essa chave, você consegue <a href="/pt/">gerar o código no Get2FA</a> em qualquer aparelho. Veja <a href="onde-encontrar-chave-secreta-2fa">onde encontrar a chave</a>.</p>
"""},
}

NEW = [WHAT_IS, FORTNITE, GOVBR]

FB_CODE = {"key": "fb-code", "en": {
 "slug": "facebook-6-digit-login-code",
 "title": "“Enter a 6-digit login code generated by an authentication app” – What to Do",
 "desc": "Facebook or Instagram asks for a 6-digit login code generated by an authentication app? Here's where that code comes from and how to get it, even without your old phone.",
 "h1": "“Enter a 6-digit login code generated by an authentication app”: what to do",
 "lead": "This message means the account has two-factor authentication with an authenticator app. The code comes from the app (or from the secret key it was set up with), not from SMS.",
 "body": """
<h2>Where the 6-digit code comes from</h2>
<p>When 2FA was turned on, Facebook (or Instagram) gave a <strong>secret key</strong> that was added to an authenticator app such as Google Authenticator, Microsoft Authenticator, 2FAS or Duo. That app shows a new 6-digit code every 30 seconds. Type the code shown under the account's name.</p>
<h2>Option 1: you have the secret key</h2>
<p>If you saved the key (a code of 32 letters and numbers, sometimes split into groups of four), paste it into <a href="/">Get2FA</a>. You'll get the same 6-digit code the app would show, on any device. Many people who manage several accounts keep lines like <code class="k">user|password|KEY</code>; Get2FA finds the key in each line automatically.</p>
<h2>Option 2: you have the authenticator app</h2>
<p>Open the app on the phone where 2FA was set up and type the code under the right account. If it's rejected, check that the phone's date and time are set to automatic. More causes in <a href="2fa-code-not-working">2FA code not working</a>.</p>
<h2>Option 3: no app and no key</h2>
<ul>
<li>Tap <strong>“Try another way”</strong> on the login screen: Facebook may offer a confirmation on a device where you're already logged in, an SMS, or a <strong>recovery code</strong> (the 8-digit codes you could save when turning on 2FA).</li>
<li>If none works, follow Facebook's account recovery, which may ask for an ID or a video selfie.</li>
</ul>
<h2>Next time</h2>
<p>When you turn on 2FA, copy the key shown under the QR code and keep it in a password manager. See <a href="facebook-2fa-authentication-app">how to set up Facebook 2FA</a> and <a href="find-2fa-secret-key">where to find the secret key</a>.</p>
"""},
"vi": {
 "slug": "lay-code-facebook",
 "title": "Lấy code Facebook từ mã 2FA – Cách lấy mã đăng nhập 6 số",
 "desc": "Cách lấy code Facebook (mã đăng nhập 6 số) từ khóa 2FA, từ ứng dụng xác thực hoặc mã khôi phục. Lấy mã 2FA Facebook nhanh, miễn phí, ngay trên trình duyệt.",
 "h1": "Lấy code Facebook (mã 2FA 6 số)",
 "lead": "Khi Facebook yêu cầu “mã đăng nhập 6 chữ số do ứng dụng xác thực tạo ra”, bạn cần code 2FA của tài khoản. Code này đến từ khóa 2FA hoặc ứng dụng xác thực, không phải SMS.",
 "body": """
<h2>Code Facebook đến từ đâu?</h2>
<p>Khi bật xác thực 2 yếu tố, Facebook cấp một <strong>khóa 2FA</strong> (chuỗi 32 ký tự chữ và số, đôi khi chia thành nhóm 4 ký tự). Ứng dụng xác thực dùng khóa này để tạo mã 6 số mới sau mỗi 30 giây. Ai có khóa đều tạo ra đúng mã đó.</p>
<h2>Cách 1: lấy code Facebook bằng khóa 2FA (nhanh nhất)</h2>
<ol>
<li>Sao chép khóa 2FA của tài khoản.</li>
<li>Dán vào ô trên trang <a href="/vi/">Get2FA</a>.</li>
<li>Bấm vào mã 6 số để sao chép và nhập vào Facebook trước khi vòng tròn chạy hết.</li>
</ol>
<p>Có nhiều tài khoản dạng <code class="k">uid|mật khẩu|2FA</code>? Dán cả danh sách, mỗi dòng một tài khoản. Get2FA tự tìm khóa trong từng dòng và trả về danh sách <code class="k">dòng|mã</code> để sao chép một lần.</p>
<h2>Cách 2: dùng ứng dụng xác thực</h2>
<p>Mở Google Authenticator, Microsoft Authenticator, 2FAS… trên điện thoại đã thiết lập 2FA và nhập mã dưới tên tài khoản. Nếu Facebook báo mã sai, hãy bật ngày giờ tự động trên điện thoại. Xem thêm <a href="ma-2fa-khong-hoat-dong">mã 2FA không hoạt động</a>.</p>
<h2>Cách 3: không có khóa và không có ứng dụng</h2>
<ul>
<li>Chọn <strong>“Thử cách khác”</strong> ở màn hình đăng nhập: Facebook có thể cho xác nhận trên thiết bị đã đăng nhập, gửi SMS hoặc cho dùng <strong>mã khôi phục</strong> 8 số mà bạn đã lưu khi bật 2FA.</li>
<li>Nếu vẫn không được, làm theo quy trình khôi phục tài khoản của Facebook (có thể cần giấy tờ tùy thân hoặc video selfie).</li>
</ul>
<h2>Lưu ý an toàn</h2>
<p>Get2FA tính mã ngay trong trình duyệt, khóa không bao giờ được gửi đi. Đừng dán khóa 2FA vào trang không rõ nguồn gốc và không đưa khóa cho người khác: ai có khóa đều lấy được code Facebook của bạn. Xem <a href="tim-khoa-bi-mat-2fa">cách tìm khóa bí mật 2FA</a>.</p>
"""}}

TOTP = {"key": "totp", "en": {
 "slug": "what-is-totp",
 "title": "What Is TOTP? Meaning, How It Works and TOTP vs HOTP",
 "desc": "TOTP meaning explained: how time-based one-time passwords are generated from a secret key and the clock, TOTP vs HOTP, and how to generate a TOTP code.",
 "h1": "What is TOTP? (and TOTP vs HOTP)",
 "lead": "TOTP stands for Time-based One-Time Password. It's the algorithm behind the 6-digit codes in Google Authenticator and almost every authenticator app, defined in RFC 6238.",
 "body": """
<h2>TOTP meaning</h2>
<p>A <strong>time-based one-time password</strong> is a short code calculated from two inputs: a <strong>shared secret key</strong> and the <strong>current time</strong>. The server and your app both know the key and the time, so they calculate the same code without talking to each other.</p>
<h2>How a TOTP code is generated</h2>
<ol>
<li>Take the current Unix time and divide it by the period (usually 30 seconds). The whole number is the <em>counter</em>.</li>
<li>Calculate HMAC-SHA1 (or SHA-256/SHA-512) of the counter using the secret key.</li>
<li>Pick 4 bytes from the result (“dynamic truncation”) and turn them into a number.</li>
<li>Keep the last 6 (or 8) digits. That's the code.</li>
</ol>
<p>Because the counter changes every 30 seconds, the code does too. That's why a wrong device clock makes codes fail.</p>
<h2>TOTP vs HOTP</h2>
<div class="table-wrap"><table><thead><tr><th></th><th>TOTP</th><th>HOTP</th></tr></thead><tbody>
<tr><td>Moving factor</td><td>Time (every 30 s)</td><td>A counter that goes up on each use</td></tr>
<tr><td>Standard</td><td>RFC 6238</td><td>RFC 4226</td></tr>
<tr><td>Code expires</td><td>Yes, after the period</td><td>No, until the next one is used</td></tr>
<tr><td>Typical use</td><td>Authenticator apps, 2FA on websites</td><td>Hardware tokens with a button</td></tr>
</tbody></table></div>
<p>TOTP is really HOTP with the time as the counter, which makes codes short-lived and harder to reuse.</p>
<h2>TOTP secret and QR code</h2>
<p>The secret is usually a Base32 string (letters A–Z and digits 2–7). Sites share it as a QR code containing an <code class="k">otpauth://totp/…?secret=…</code> link, which can also set the algorithm, digits and period.</p>
<h2>Generate a TOTP code</h2>
<ul>
<li><a href="/">Get2FA</a>: paste a TOTP secret and get the current code (and the next one), right in your browser.</li>
<li><a href="/2fa-key-generator">TOTP key &amp; QR generator</a>: create a new secret and its QR code for testing.</li>
<li><a href="/check-2fa-code">Code checker</a>: see whether a code matches a key and whether your clock is off.</li>
</ul>
"""}}

MS_AUTH = {"key": "ms-auth", "en": {
 "slug": "microsoft-authenticator-not-showing-code",
 "title": "Microsoft Authenticator Not Showing a Code? How to Fix It",
 "desc": "Microsoft Authenticator only shows approval requests or no 6-digit code? Here's where to find the one-time code and how to fix missing or wrong codes.",
 "h1": "Microsoft Authenticator not showing a code? Here's the fix",
 "lead": "Microsoft Authenticator often uses “approve sign-in” notifications instead of codes, so the 6-digit code can seem to be missing. It's usually still there, one tap away.",
 "body": """
<h2>1. Tap the account to see the code</h2>
<p>For Microsoft accounts, the main screen may show only the account name. Tap it: the <strong>one-time password code</strong> appears on the account's page, with a timer. Codes for other services (Google, Facebook, etc.) are shown directly in the list.</p>
<h2>2. The sign-in expects a notification, not a code</h2>
<p>If the site asks you to approve a request, open the app and look for the pending notification. If notifications don't arrive, choose “I can't use my Microsoft Authenticator app right now” or “Use a verification code” on the sign-in page, then use the code from step 1.</p>
<h2>3. Notifications are blocked</h2>
<p>Allow notifications for Microsoft Authenticator in your phone settings, turn off battery optimization for the app and make sure it's updated.</p>
<h2>4. The code is rejected</h2>
<p>Turn on automatic date and time on the phone. Codes depend on the clock, and a difference of 30 seconds is enough to break them. You can test your clock with our <a href="/check-2fa-code">2FA code checker</a>.</p>
<h2>5. The account disappeared after changing phones</h2>
<p>Restore from the app's cloud backup (signed in with the same Microsoft account) on the new phone. For non-Microsoft accounts, you may need to set 2FA up again on each site. If you saved the secret keys, paste them into <a href="/">Get2FA</a> to get codes immediately. See <a href="lost-phone-2fa">lost your phone with the authenticator app</a>.</p>
<h2>Work or school accounts</h2>
<p>Company accounts are managed by your IT admin, who may require notifications only or number matching. If codes don't work, ask them to reset your sign-in methods.</p>
"""}}

NEW = [WHAT_IS, FB_CODE, FORTNITE, TOTP, MS_AUTH, GOVBR]
