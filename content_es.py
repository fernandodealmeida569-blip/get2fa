# -*- coding: utf-8 -*-
H = "/es/"
G = "/es/guias/"

TOOLS = {
"gen": {
 "path": "/es/generador-de-clave-2fa",
 "title": "Generador de clave 2FA y código QR (TOTP) – Gratis, en tu navegador",
 "desc": "Genera una clave secreta 2FA aleatoria, su enlace otpauth:// y el código QR para Google Authenticator y cualquier app TOTP. Creada en tu dispositivo con Web Crypto.",
 "h1": "Generador de clave 2FA y código QR",
 "sub": "Crea una clave TOTP aleatoria, el enlace otpauth:// y un código QR que cualquier app de autenticación puede escanear. Ideal para desarrolladores que prueban 2FA o configuran su propia app.",
 "card": "Generador de clave y QR", "cardDesc": "Crea una clave 2FA aleatoria y su código QR para cualquier app de autenticación.",
 "i18n": {"copied": "Copiado"},
 "ui": {"aria": "Generador", "issuer": "Emisor (nombre de la app o del sitio)", "issuerPh": "MiApp", "account": "Cuenta (usuario o correo)", "accountPh": "ana@ejemplo.com",
        "keyLen": "Longitud de la clave", "opt80": "80 bits (16 caracteres)", "opt160": "160 bits (32 caracteres, recomendado)", "opt256": "256 bits (52 caracteres)",
        "newKey": "Nueva clave", "secret": "Clave secreta", "uri": "Enlace otpauth://", "copy": "Copiar", "copyLink": "Copiar enlace", "dl": "Descargar QR (SVG)",
        "openGen": "Abrir en el generador", "current": "Código actual",
        "hint": "La clave se crea con el generador aleatorio seguro de tu navegador y nunca sale de esta página."},
 "content": """
    <h2>Cómo usarlo</h2>
    <ol class="steps"><li><b>Ponle nombre</b>Escribe el emisor (tu app o sitio) y la cuenta. Son el nombre que se verá en la app de autenticación.</li><li><b>Escanea o copia</b>Escanea el código QR con Google Authenticator, Microsoft Authenticator, 2FAS o cualquier app TOTP, o copia el enlace otpauth://.</li><li><b>Comprueba el código</b>El código actual se actualiza en vivo, para que confirmes que la app muestra el mismo número.</li></ol>
    <h2>¿Qué es un enlace otpauth://?</h2>
    <p>Es el formato estándar que las apps de autenticación leen del código QR: <code class="k">otpauth://totp/Emisor:cuenta?secret=CLAVE&amp;issuer=Emisor</code>. Hay parámetros opcionales para el algoritmo, los dígitos y el periodo. Casi todos los servicios usan SHA-1, 6 dígitos y 30 segundos, que son los valores por defecto aquí.</p>
    <h2>¿Es seguro generar claves online?</h2>
    <p>Las claves se crean con <code class="k">crypto.getRandomValues</code> en tu navegador y no se sube nada. En sistemas en producción, genera las claves en tu propio servidor y guárdalas cifradas; usa esta herramienta para pruebas, prototipos o cuentas personales.</p>
    <h2>¿Qué longitud de clave elegir?</h2>
    <p>160 bits (32 caracteres Base32) es lo que recomienda la RFC 4226 y lo que usan la mayoría de servicios. 80 bits es el mínimo que aceptan algunas apps antiguas; 256 bits funciona en las apps modernas.</p>"""},
"check": {
 "path": "/es/comprobar-codigo-2fa",
 "title": "Comprobar código 2FA – ¿Por qué mi código no funciona? | Prueba de reloj",
 "desc": "Pega tu clave 2FA y el código de tu app para ver si coinciden, y comprueba si el reloj de tu dispositivo está desfasado. Descubre por qué falla el código del autenticador.",
 "h1": "Comprobar un código 2FA y tu reloj",
 "sub": "Pega tu clave secreta y el código que muestra tu autenticador. Te decimos si coincide y si el reloj de tu dispositivo es la causa de que rechacen los códigos.",
 "card": "Comprobador de código 2FA", "cardDesc": "Mira si un código coincide con tu clave y si el reloj de tu dispositivo está desfasado.",
 "i18n": {"copied": "Copiado", "clockOk": "✓ El reloj de tu dispositivo es correcto (menos de 2 segundos de diferencia).",
          "clockAhead": "⚠ El reloj de tu dispositivo va unos {n} s adelantado. Activa la fecha y hora automáticas.",
          "clockBehind": "⚠ El reloj de tu dispositivo va unos {n} s atrasado. Activa la fecha y hora automáticas.",
          "clockUnknown": "No se pudo comprobar tu reloj ahora mismo.",
          "badKey": "Eso no parece una clave secreta 2FA válida.", "badCode": "Escribe el código de {n} dígitos de tu app.",
          "match": "✓ El código coincide con el actual. Tu app y tu clave son correctas.",
          "matchPast": "⚠ El código coincide con uno de hace {s} s. Probablemente el reloj de tu dispositivo va atrasado o el código era antiguo.",
          "matchFuture": "⚠ El código coincide con uno de dentro de {s} s. El dispositivo que lo generó tiene el reloj adelantado.",
          "noMatch": "✗ No hay coincidencia en ±5 minutos. La clave, la cuenta o la configuración (dígitos, periodo, algoritmo) son distintas.",
          "expected": "Código actual para esta clave:"},
 "ui": {"aria": "Comprobador", "checking": "Comprobando tu reloj…", "secret": "Clave secreta", "code": "Código de tu app", "check": "Comprobar código"},
 "content": f"""
    <h2>Qué significa el resultado</h2>
    <ul>
    <li><b>Coincide con el código actual:</b> tu clave y tu app están bien. Si el sitio aún lo rechaza, puede tener otra clave (se reinició el 2FA) o el código caducó mientras lo escribías.</li>
    <li><b>Coincide con un código anterior o posterior:</b> algún reloj está desfasado. Activa la fecha y hora automáticas en el móvil donde está el autenticador.</li>
    <li><b>No coincide:</b> la clave es de otra cuenta, se copió incompleta, o el sitio usa 8 dígitos, 60 segundos o SHA-256.</li>
    </ul>
    <h2>Cómo funciona la prueba del reloj</h2>
    <p>Comparamos la hora de tu dispositivo con la hora que indica nuestro servidor en una petición normal de la página. Los códigos TOTP cambian cada 30 segundos, así que unos pocos segundos de diferencia bastan para que fallen.</p>
    <p>¿Sigues con problemas? Lee <a href="{G}codigo-2fa-no-funciona">El código 2FA no funciona: 7 causas</a>.</p>"""},
"read": {
 "path": "/es/leer-codigo-qr-2fa",
 "title": "Leer código QR 2FA – Extraer la clave secreta (también exportación de Google Authenticator)",
 "desc": "Sube o pega una captura de un código QR 2FA para extraer la clave secreta y el enlace otpauth. También lee los QR de exportación de Google Authenticator (otpauth-migration). Funciona en tu navegador.",
 "h1": "Leer un código QR 2FA y obtener la clave secreta",
 "sub": "Arrastra, pega o sube una captura de un código QR de 2FA. Obtendrás la clave secreta, el emisor, la cuenta y la configuración, incluso de códigos de exportación de Google Authenticator.",
 "card": "Lector de código QR 2FA", "cardDesc": "Extrae la clave secreta de cualquier QR 2FA, incluidas las exportaciones de Google Authenticator.",
 "i18n": {"copied": "Copiado", "copy": "Copiar", "copyUri": "Copiar enlace otpauth", "openGen": "Ver códigos", "issuer": "Emisor", "account": "Cuenta",
          "secret": "Clave secreta", "settings": "Configuración", "found": "{n} cuenta(s) encontrada(s).", "reading": "Leyendo la imagen…",
          "qrNotFound": "No se encontró ningún código QR de 2FA en la imagen. Prueba con una captura más nítida que muestre el código entero.",
          "qrUnsupported": "No se pudo cargar el lector de QR. Revisa tu conexión e inténtalo de nuevo."},
 "ui": {"aria": "Lector de QR", "dropB": "Arrastra aquí la imagen del código QR", "dropS": "o haz clic para elegir un archivo · o pulsa Ctrl+V para pegar una captura",
        "link": "…o pega un enlace otpauth:// u otpauth-migration://", "hint": "La imagen se lee en tu dispositivo y nunca se sube."},
 "content": f"""
    <h2>¿Cuándo es útil?</h2>
    <ul>
    <li>Tienes una captura de un código QR de 2FA y quieres guardar la clave en un gestor de contraseñas.</li>
    <li>Exportaste cuentas de Google Authenticator y quieres las claves reales, no solo pasarlas a otro móvil.</li>
    <li>Eres desarrollador y quieres ver qué contiene realmente el código QR de tu app.</li>
    </ul>
    <h2>Códigos de exportación de Google Authenticator</h2>
    <p>La pantalla <em>Transferir cuentas → Exportar cuentas</em> genera códigos QR en un formato especial, <code class="k">otpauth-migration://</code>, con varias cuentas. Este lector lo decodifica y muestra cada cuenta con su clave. Mira <a href="{G}transferir-google-authenticator-nuevo-movil">cómo transferir Google Authenticator</a>.</p>
    <h2>Privacidad</h2>
    <p>La lectura usa el lector de códigos de barras del propio navegador o una biblioteca de código abierto servida desde este sitio. Borra la captura al terminar: quien la tenga puede generar tus códigos.</p>"""},
}

GUIDES = {
"find-key": {
 "slug": "donde-encontrar-clave-secreta-2fa",
 "title": "Dónde encontrar la clave secreta 2FA (Google, Facebook, Instagram, Microsoft)",
 "desc": "Qué es la clave secreta 2FA y dónde encontrarla al activar la verificación en dos pasos en Google, Facebook, Instagram, Microsoft y otros sitios.",
 "h1": "Dónde encontrar tu clave secreta 2FA",
 "lead": "La clave secreta es la versión en texto del código QR que escaneas al activar la verificación en dos pasos. Si la guardas una vez, podrás recrear tus códigos en cualquier dispositivo.",
 "body": """
<h2>¿Qué es una clave secreta 2FA?</h2>
<p>Cuando eliges “app de autenticación” como método 2FA, el sitio crea un secreto aleatorio y lo comparte con tu app. La app combina ese secreto con la hora actual para generar un código nuevo de 6 dígitos cada 30 segundos. Este método se llama TOTP (contraseña de un solo uso basada en el tiempo).</p>
<p>El secreto suele mostrarse de dos formas: como <strong>código QR</strong> y como <strong>clave de texto</strong> de 16 a 32 caracteres, con letras A–Z y números 2–7, por ejemplo <code class="k">JBSW Y3DP EHPK 3PXP</code>. Ambos contienen exactamente la misma información.</p>
<h2>Dónde muestra la clave cada sitio</h2>
<p>La mayoría de sitios esconden la clave de texto tras un enlace bajo el código QR. Busca frases como <em>“¿No puedes escanearlo?”</em>, <em>“Introducir clave manualmente”</em>, <em>“Copiar clave”</em> o <em>“Clave de configuración”</em>.</p>
<h3>Google</h3>
<p>Abre tu Cuenta de Google, ve a <strong>Seguridad → Verificación en dos pasos → Authenticator</strong> y elige configurar una app de autenticación. Bajo el código QR, toca <strong>“¿No puedes escanearlo?”</strong> para ver la clave.</p>
<h3>Facebook</h3>
<p>Ve a <strong>Configuración y privacidad → Configuración → Centro de cuentas → Contraseña y seguridad → Autenticación en dos pasos</strong>, elige tu cuenta y selecciona <strong>App de autenticación</strong>. La clave aparece con un botón <strong>Copiar clave</strong> junto al código QR.</p>
<h3>Instagram</h3>
<p>En la app, abre tu perfil, toca el menú y entra en <strong>Centro de cuentas → Contraseña y seguridad → Autenticación en dos pasos</strong>, elige tu cuenta y selecciona <strong>App de autenticación</strong>. Toca <strong>Copiar clave</strong>. Instagram solo permite activar este método desde la app de Android o iPhone.</p>
<h3>Microsoft</h3>
<p>Al añadir una app de autenticación, elige usar otra app y después <strong>“¿No puedes escanear la imagen?”</strong>. Microsoft muestra el código secreto en esa página.</p>
<h3>Otros sitios (Discord, X, Amazon, GitHub…)</h3>
<p>El proceso casi siempre es igual: elige la opción de app de autenticación y busca el enlace para introducir la clave manualmente.</p>
<h2>¿Activaste 2FA sin guardar la clave?</h2>
<p>La mayoría de sitios no vuelven a mostrarla. Si la necesitas, desactiva y vuelve a activar el método de app (o usa “añadir otro dispositivo”) y esta vez guarda la nueva clave. Actualiza también tu app de autenticación, porque la clave antigua deja de funcionar.</p>
<h2>Cómo guardar la clave de forma segura</h2>
<ul>
<li>Guárdala en un gestor de contraseñas (Bitwarden, 1Password, etc.) junto a la cuenta.</li>
<li>No la envíes nunca por correo o chat, ni publiques capturas del código QR.</li>
<li>Quien tenga la clave puede generar tus códigos: trátala como una contraseña.</li>
</ul>
"""},
"transfer": {
 "slug": "transferir-google-authenticator-nuevo-movil",
 "title": "Cómo transferir Google Authenticator a un móvil nuevo (y extraer las claves)",
 "desc": "Pasa los códigos de Google Authenticator a un móvil nuevo con la sincronización en la nube o el QR de Exportar cuentas, y extrae las claves secretas del QR con Get2FA.",
 "h1": "Cómo transferir Google Authenticator a un móvil nuevo",
 "lead": "Hay dos formas de mover tus códigos: iniciar sesión en Google para sincronizarlos o exportarlos con un código QR. Get2FA también puede leer ese QR de exportación y mostrar cada clave secreta.",
 "body": f"""
<h2>Opción 1: sincronización en la nube (la más fácil)</h2>
<ol>
<li>En el móvil antiguo, abre Google Authenticator y toca el icono de tu perfil.</li>
<li>Inicia sesión con tu Cuenta de Google y activa la sincronización. Un pequeño icono de nube confirma la copia.</li>
<li>En el móvil nuevo, instala Google Authenticator e inicia sesión con la misma cuenta. Tus códigos aparecerán solos.</li>
</ol>
<p>Es cómodo, pero tus claves 2FA quedan guardadas en tu Cuenta de Google. Protégela bien.</p>
<h2>Opción 2: Exportar cuentas (sin conexión)</h2>
<ol>
<li>En el móvil antiguo, abre el menú y ve a <strong>Transferir cuentas → Exportar cuentas</strong>.</li>
<li>Selecciona las cuentas y toca <strong>Siguiente</strong>. La app muestra uno o varios códigos QR.</li>
<li>En el móvil nuevo, ve a <strong>Transferir cuentas → Importar cuentas → Escanear código QR</strong> y escanea cada código.</li>
</ol>
<p>La exportación funciona entre Android e iPhone en ambos sentidos.</p>
<h2>Obtén las claves secretas del QR de exportación</h2>
<p>El QR de exportación usa un formato especial (<code class="k">otpauth-migration://</code>) que otras apps a menudo no leen. <a href="{H}">Get2FA</a> sí: haz una captura del QR (en un móvil de confianza) y pégala o arrástrala en Get2FA. Cada cuenta aparece con su nombre y su código en vivo, y la lista muestra el enlace <code class="k">otpauth://</code> completo con la clave. Guárdalas en tu gestor de contraseñas.</p>
<p>Todo se decodifica en tu navegador; la imagen y las claves nunca se suben. Borra la captura después.</p>
<h2>No borres el móvil antiguo demasiado pronto</h2>
<p>Prueba a iniciar sesión en algunas cuentas desde el móvil nuevo antes de restablecer el antiguo. Si algo falla cuando ya no tengas el móvil antiguo, necesitarás los códigos de respaldo o el proceso de recuperación de cada sitio.</p>
"""},
"not-working": {
 "slug": "codigo-2fa-no-funciona",
 "title": "¿El código 2FA no funciona? 7 causas y cómo solucionarlas",
 "desc": "¿Te rechazan el código del autenticador una y otra vez? Conoce las causas más comunes, desde el reloj del dispositivo hasta una clave equivocada, y cómo arreglar cada una.",
 "h1": "¿El código 2FA no funciona? Así se soluciona",
 "lead": "Cuando un sitio dice que tu código 2FA no es válido, la causa casi siempre es una de estas. Empieza por la primera: resuelve la mayoría de casos.",
 "body": f"""
<h2>1. El reloj de tu dispositivo está desfasado</h2>
<p>Los códigos TOTP se calculan a partir de la hora actual. Si el reloj de tu móvil u ordenador se desvía más de unos 30 segundos, el código no coincidirá. Activa la <strong>fecha y hora automáticas</strong> (y la zona horaria automática) en los ajustes y prueba con un código nuevo. Puedes comprobarlo con el <a href="{H}comprobar-codigo-2fa">comprobador de código 2FA</a>.</p>
<h2>2. El código caducó mientras lo escribías</h2>
<p>Cada código dura 30 segundos y algunos sitios lo rechazan justo al final. Espera a uno nuevo. Get2FA muestra los segundos restantes y el siguiente código, para que elijas el momento.</p>
<h2>3. Usas la clave o la cuenta equivocada</h2>
<p>Si configuraste 2FA más de una vez, solo vale la última clave. Asegúrate de que la entrada de tu app pertenece a la misma cuenta (mira el nombre y el correo) y de que copiaste la clave completa.</p>
<h2>4. El sitio usa otra configuración</h2>
<p>Casi todos los sitios usan 6 dígitos, 30 segundos y SHA-1. Algunos usan 8 dígitos, 60 segundos o SHA-256. Si el QR incluye estos ajustes, las apps los leen solas. Con una clave de texto, ajústalos en la <em>Configuración avanzada</em> de Get2FA.</p>
<h2>5. La clave se escribió mal</h2>
<p>Las claves solo usan letras A–Z y números 2–7. Los dígitos 0, 1, 8 y 9 nunca aparecen, así que un “0” es en realidad la letra O y un “1” es la I o la L. Copia y pega siempre que puedas.</p>
<h2>6. El código ya se usó</h2>
<p>Algunos sitios aceptan cada código una sola vez. Si acabas de usar uno, espera al siguiente.</p>
<h2>7. Se reinició el 2FA en el sitio</h2>
<p>Si tú (o el soporte) desactivasteis y volvisteis a activar el 2FA, la clave antigua ya no sirve. Entra con un código de respaldo y vuelve a configurar el autenticador.</p>
<h2>¿Sigues sin poder entrar?</h2>
<p>Usa los códigos de respaldo o recuperación que te dio el sitio, o inicia su proceso de recuperación de cuenta. Mira <a href="perdi-el-movil-autenticador">qué hacer si perdiste el móvil</a>.</p>
"""},
"lost-phone": {
 "slug": "perdi-el-movil-autenticador",
 "title": "¿Perdiste el móvil con la app de autenticación? Qué hacer ahora",
 "desc": "¿Móvil perdido, robado o restablecido con tus códigos 2FA? Cómo volver a entrar en tus cuentas con claves guardadas, códigos de respaldo, sincronización o recuperación.",
 "h1": "¿Perdiste el móvil con el autenticador? Qué hacer",
 "lead": "Perder el móvil con tus códigos 2FA es estresante, pero casi siempre hay una forma de volver a entrar. Revisa estas opciones en orden.",
 "body": f"""
<h2>1. ¿Guardaste las claves secretas?</h2>
<p>Si conservaste las claves de configuración (en un gestor de contraseñas, una nota o impresas), estás de suerte: pega cada clave en <a href="{H}">Get2FA</a> y tendrás códigos válidos al momento, en cualquier dispositivo. Luego añade las claves a un autenticador en tu móvil nuevo.</p>
<h2>2. ¿Tenías la sincronización activada?</h2>
<p>Google Authenticator (con sesión iniciada), Microsoft Authenticator, 2FAS y otras apps pueden hacer copia de tus códigos. Instala la misma app en el móvil nuevo e inicia sesión con la misma cuenta para recuperarlos.</p>
<h2>3. Usa códigos de respaldo</h2>
<p>La mayoría de sitios te dan códigos de respaldo o recuperación de un solo uso al activar 2FA (Google, Facebook, Instagram y GitHub lo hacen). Cada código te deja entrar una vez. Después, vuelve a configurar el 2FA en el móvil nuevo.</p>
<h2>4. Usa otro método 2FA</h2>
<p>Si también añadiste SMS, una llave de seguridad, una passkey u otro dispositivo de confianza, úsalo para entrar.</p>
<h2>5. Inicia la recuperación de la cuenta</h2>
<p>Como último recurso, usa la opción “¿No puedes acceder a tus códigos?” o la recuperación de cuenta del sitio. Puede tardar días y suele pedir pruebas de identidad, así que empieza cuanto antes.</p>
<h2>Cuando vuelvas a entrar</h2>
<ul>
<li>Configura de nuevo el 2FA y esta vez <strong>guarda cada clave nueva</strong> en un gestor de contraseñas.</li>
<li>Guarda los nuevos códigos de respaldo fuera del móvil.</li>
<li>Si te robaron el móvil, cambia las contraseñas de tus cuentas importantes y elimina el dispositivo antiguo de ellas.</li>
</ul>
"""},
}
