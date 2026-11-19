# -*- coding: utf-8 -*-
H = "/de/"
G = "/de/anleitungen/"

TOOLS = {
"gen": {
 "path": "/de/2fa-schluessel-generator",
 "title": "2FA-Schlüssel- und QR-Code-Generator (TOTP) – kostenlos im Browser",
 "desc": "Erzeuge einen zufälligen geheimen 2FA-Schlüssel, den otpauth://-Link und den QR-Code für Google Authenticator und jede TOTP-App. Erstellt auf deinem Gerät mit Web Crypto.",
 "h1": "2FA-Schlüssel- und QR-Code-Generator",
 "sub": "Erstelle einen zufälligen TOTP-Schlüssel, den otpauth://-Link und einen QR-Code, den jede Authenticator-App scannen kann. Ideal für Entwickler, die 2FA testen oder ihre eigene App einrichten.",
 "card": "Schlüssel- und QR-Generator", "cardDesc": "Erstelle einen zufälligen 2FA-Schlüssel und seinen QR-Code für jede Authenticator-App.",
 "i18n": {"copied": "Kopiert"},
 "ui": {"aria": "Generator", "issuer": "Anbieter (Name der App oder Website)", "issuerPh": "MeineApp", "account": "Konto (Benutzername oder E-Mail)", "accountPh": "anna@beispiel.de",
        "keyLen": "Schlüssellänge", "opt80": "80 Bit (16 Zeichen)", "opt160": "160 Bit (32 Zeichen, empfohlen)", "opt256": "256 Bit (52 Zeichen)",
        "newKey": "Neuer Schlüssel", "secret": "Geheimer Schlüssel", "uri": "otpauth://-Link", "copy": "Kopieren", "copyLink": "Link kopieren", "dl": "QR herunterladen (SVG)",
        "openGen": "Im Generator öffnen", "current": "Aktueller Code",
        "hint": "Der Schlüssel wird mit dem sicheren Zufallsgenerator deines Browsers erstellt und verlässt diese Seite nie."},
 "content": """
    <h2>So funktioniert es</h2>
    <ol class="steps"><li><b>Namen vergeben</b>Gib den Anbieter (deine App oder Website) und das Konto ein. Daraus wird die Bezeichnung in der Authenticator-App.</li><li><b>Scannen oder kopieren</b>Scanne den QR-Code mit Google Authenticator, Microsoft Authenticator, 2FAS oder einer anderen TOTP-App, oder kopiere den otpauth://-Link.</li><li><b>Code prüfen</b>Der aktuelle Code wird live aktualisiert, damit du prüfen kannst, ob die App dieselbe Zahl zeigt.</li></ol>
    <h2>Was ist ein otpauth://-Link?</h2>
    <p>Das ist das Standardformat, das Authenticator-Apps aus einem QR-Code lesen: <code class="k">otpauth://totp/Anbieter:konto?secret=SCHLUESSEL&amp;issuer=Anbieter</code>. Optionale Parameter legen Algorithmus, Stellen und Intervall fest. Die meisten Dienste nutzen SHA-1, 6 Stellen und 30 Sekunden, die hier auch voreingestellt sind.</p>
    <h2>Ist es sicher, Schlüssel online zu erzeugen?</h2>
    <p>Schlüssel werden mit <code class="k">crypto.getRandomValues</code> in deinem Browser erstellt, nichts wird hochgeladen. Für Produktivsysteme solltest du Schlüssel auf deinem eigenen Server erzeugen und verschlüsselt speichern; nutze dieses Tool zum Testen, für Prototypen oder private Konten.</p>
    <h2>Welche Schlüssellänge sollte ich wählen?</h2>
    <p>160 Bit (32 Base32-Zeichen) empfiehlt RFC 4226, und die meisten Dienste verwenden sie. 80 Bit ist das Minimum, das manche ältere Apps akzeptieren; 256 Bit funktioniert mit modernen Apps.</p>"""},
"check": {
 "path": "/de/2fa-code-pruefen",
 "title": "2FA-Code prüfen – Warum ist mein Authenticator-Code falsch? | Uhrzeit-Check",
 "desc": "Füge deinen 2FA-Schlüssel und den Code aus der App ein, um zu sehen, ob sie übereinstimmen, und prüfe, ob die Uhr deines Geräts falsch geht. Finde heraus, warum dein Code nicht funktioniert.",
 "h1": "2FA-Code und Geräteuhr prüfen",
 "sub": "Füge deinen geheimen Schlüssel und den Code aus deiner Authenticator-App ein. Wir sagen dir, ob er passt und ob die Uhr deines Geräts der Grund für abgelehnte Codes ist.",
 "card": "2FA-Code-Prüfer", "cardDesc": "Prüfe, ob ein Code zu deinem Schlüssel passt und ob deine Geräteuhr falsch geht.",
 "i18n": {"copied": "Kopiert", "clockOk": "✓ Die Uhr deines Geräts stimmt (Abweichung unter 2 Sekunden).",
          "clockAhead": "⚠ Die Uhr deines Geräts geht etwa {n} s vor. Aktiviere automatisches Datum und Uhrzeit.",
          "clockBehind": "⚠ Die Uhr deines Geräts geht etwa {n} s nach. Aktiviere automatisches Datum und Uhrzeit.",
          "clockUnknown": "Deine Uhr konnte gerade nicht geprüft werden.",
          "badKey": "Das sieht nicht nach einem gültigen geheimen 2FA-Schlüssel aus.", "badCode": "Gib den {n}-stelligen Code aus deiner App ein.",
          "match": "✓ Der Code stimmt mit dem aktuellen Code überein. App und Schlüssel sind korrekt.",
          "matchPast": "⚠ Der Code passt zu einem Code von vor {s} s. Wahrscheinlich geht deine Geräteuhr nach, oder der Code war alt.",
          "matchFuture": "⚠ Der Code passt zu einem Code in {s} s. Das Gerät, das ihn erzeugt hat, geht vor.",
          "noMatch": "✗ Keine Übereinstimmung innerhalb von ±5 Minuten. Schlüssel, Konto oder Einstellungen (Stellen, Intervall, Algorithmus) sind verschieden.",
          "expected": "Aktueller Code für diesen Schlüssel:"},
 "ui": {"aria": "Prüfer", "checking": "Uhr wird geprüft…", "secret": "Geheimer Schlüssel", "code": "Code aus deiner App", "check": "Code prüfen"},
 "content": f"""
    <h2>Was das Ergebnis bedeutet</h2>
    <ul>
    <li><b>Passt zum aktuellen Code:</b> Schlüssel und App sind in Ordnung. Lehnt die Website ihn trotzdem ab, hat sie vielleicht einen anderen Schlüssel (2FA wurde zurückgesetzt) oder der Code ist beim Eintippen abgelaufen.</li>
    <li><b>Passt zu einem älteren oder neueren Code:</b> Eine der Uhren geht falsch. Aktiviere automatisches Datum und Uhrzeit auf dem Handy mit der Authenticator-App.</li>
    <li><b>Keine Übereinstimmung:</b> Der Schlüssel gehört zu einem anderen Konto, wurde unvollständig kopiert, oder die Website nutzt 8 Stellen, 60 Sekunden oder SHA-256.</li>
    </ul>
    <h2>So funktioniert der Uhrzeit-Check</h2>
    <p>Wir vergleichen die Zeit deines Geräts mit der Zeit, die unser Server bei einem normalen Seitenaufruf meldet. TOTP-Codes wechseln alle 30 Sekunden, daher reichen schon wenige Sekunden Abweichung, damit Codes scheitern.</p>
    <p>Klappt es immer noch nicht? Lies <a href="{G}2fa-code-funktioniert-nicht">2FA-Code funktioniert nicht: 7 Gründe</a>.</p>"""},
"read": {
 "path": "/de/2fa-qr-code-lesen",
 "title": "2FA-QR-Code lesen – geheimen Schlüssel auslesen (auch Google-Authenticator-Export)",
 "desc": "Lade einen Screenshot eines 2FA-QR-Codes hoch oder füge ihn ein, um den geheimen Schlüssel und den otpauth-Link auszulesen. Liest auch Export-QR-Codes von Google Authenticator (otpauth-migration). Läuft im Browser.",
 "h1": "2FA-QR-Code lesen und geheimen Schlüssel erhalten",
 "sub": "Ziehe, füge ein oder lade einen Screenshot eines 2FA-QR-Codes hoch. Du erhältst den geheimen Schlüssel, Anbieter, Konto und Einstellungen, sogar aus Export-Codes von Google Authenticator.",
 "card": "2FA-QR-Code-Leser", "cardDesc": "Lies den geheimen Schlüssel aus jedem 2FA-QR-Code aus, auch aus Google-Authenticator-Exporten.",
 "i18n": {"copied": "Kopiert", "copy": "Kopieren", "copyUri": "otpauth-Link kopieren", "openGen": "Codes anzeigen", "issuer": "Anbieter", "account": "Konto",
          "secret": "Geheimer Schlüssel", "settings": "Einstellungen", "found": "{n} Konto/Konten gefunden.", "reading": "Bild wird gelesen…",
          "qrNotFound": "Kein 2FA-QR-Code im Bild gefunden. Versuche einen schärferen Screenshot, der den ganzen Code zeigt.",
          "qrUnsupported": "Der QR-Leser konnte nicht geladen werden. Prüfe deine Verbindung und versuche es erneut."},
 "ui": {"aria": "QR-Leser", "dropB": "QR-Code-Bild hierher ziehen", "dropS": "oder klicken, um eine Datei zu wählen · oder Strg+V drücken, um einen Screenshot einzufügen",
        "link": "…oder einen otpauth://- oder otpauth-migration://-Link einfügen", "hint": "Das Bild wird auf deinem Gerät gelesen und nie hochgeladen."},
 "content": f"""
    <h2>Wann ist das nützlich?</h2>
    <ul>
    <li>Du hast einen Screenshot eines 2FA-QR-Codes und willst den Schlüssel in einem Passwortmanager speichern.</li>
    <li>Du hast Konten aus Google Authenticator exportiert und willst die eigentlichen Schlüssel, nicht nur eine Übertragung aufs neue Handy.</li>
    <li>Du bist Entwickler und willst prüfen, was der QR-Code deiner App wirklich enthält.</li>
    </ul>
    <h2>Export-Codes von Google Authenticator</h2>
    <p>Der Bildschirm <em>Konten übertragen → Konten exportieren</em> erzeugt QR-Codes in einem speziellen Format, <code class="k">otpauth-migration://</code>, das mehrere Konten enthält. Dieser Leser dekodiert es und listet jedes Konto mit seinem Schlüssel auf. Siehe <a href="{G}google-authenticator-auf-neues-handy-uebertragen">Google Authenticator übertragen</a>.</p>
    <h2>Datenschutz</h2>
    <p>Das Dekodieren nutzt den eingebauten Barcode-Leser deines Browsers oder eine Open-Source-Bibliothek, die von dieser Website geladen wird. Lösche den Screenshot danach: Wer ihn hat, kann deine Codes erzeugen.</p>"""},
}

GUIDES = {
"find-key": {
 "slug": "2fa-geheimen-schluessel-finden",
 "title": "Wo du deinen geheimen 2FA-Schlüssel findest (Google, Facebook, Instagram, Microsoft)",
 "desc": "Was ein geheimer 2FA-Schlüssel ist und wo du ihn beim Aktivieren der Zwei-Faktor-Authentifizierung bei Google, Facebook, Instagram, Microsoft und anderen findest.",
 "h1": "Wo du deinen geheimen 2FA-Schlüssel findest",
 "lead": "Der geheime Schlüssel ist die Textversion des QR-Codes, den du beim Aktivieren der Zwei-Faktor-Authentifizierung scannst. Speicherst du ihn einmal, kannst du deine Codes auf jedem Gerät wiederherstellen.",
 "body": """
<h2>Was ist ein geheimer 2FA-Schlüssel?</h2>
<p>Wählst du „Authentifizierungs-App“ als 2FA-Methode, erzeugt die Website ein zufälliges Geheimnis und teilt es mit deiner App. Die App kombiniert dieses Geheimnis mit der aktuellen Uhrzeit und erzeugt alle 30 Sekunden einen neuen 6-stelligen Code. Dieses Verfahren heißt TOTP (zeitbasiertes Einmalpasswort).</p>
<p>Das Geheimnis wird meist auf zwei Arten angezeigt: als <strong>QR-Code</strong> und als <strong>Textschlüssel</strong> mit 16 bis 32 Zeichen aus den Buchstaben A–Z und den Ziffern 2–7, zum Beispiel <code class="k">JBSW Y3DP EHPK 3PXP</code>. Beide enthalten genau dieselbe Information.</p>
<h2>Wo die einzelnen Websites den Schlüssel zeigen</h2>
<p>Die meisten Websites verstecken den Textschlüssel hinter einem Link unter dem QR-Code. Achte auf Formulierungen wie <em>„Scannen nicht möglich?“</em>, <em>„Schlüssel manuell eingeben“</em>, <em>„Schlüssel kopieren“</em> oder <em>„Einrichtungsschlüssel“</em>.</p>
<h3>Google</h3>
<p>Öffne dein Google-Konto, gehe zu <strong>Sicherheit → Bestätigung in zwei Schritten → Authenticator</strong> und richte eine Authenticator-App ein. Tippe unter dem QR-Code auf <strong>„Scannen nicht möglich?“</strong>, um den Schlüssel zu sehen.</p>
<h3>Facebook</h3>
<p>Gehe zu <strong>Einstellungen und Privatsphäre → Einstellungen → Kontenübersicht → Passwort und Sicherheit → Zweistufige Authentifizierung</strong>, wähle dein Konto und dann <strong>Authentifizierungs-App</strong>. Der Schlüssel erscheint mit einer Schaltfläche <strong>Schlüssel kopieren</strong> neben dem QR-Code.</p>
<h3>Instagram</h3>
<p>Öffne in der App dein Profil, tippe auf das Menü und dann auf <strong>Kontenübersicht → Passwort und Sicherheit → Zweistufige Authentifizierung</strong>, wähle dein Konto und <strong>Authentifizierungs-App</strong>. Tippe auf <strong>Schlüssel kopieren</strong>. Instagram erlaubt diese Methode nur über die Android- oder iPhone-App.</p>
<h3>Microsoft</h3>
<p>Wähle beim Hinzufügen einer Authenticator-App, dass du eine andere App verwenden möchtest, und dann <strong>„Bild kann nicht gescannt werden?“</strong>. Microsoft zeigt dort den geheimen Code an.</p>
<h3>Andere Websites (Discord, X, Amazon, GitHub…)</h3>
<p>Der Ablauf ist fast immer gleich: Wähle die Option für eine Authenticator-App und suche dann den Link, um den Schlüssel manuell einzugeben.</p>
<h2>2FA schon aktiviert, ohne den Schlüssel zu speichern?</h2>
<p>Die meisten Websites zeigen den Schlüssel nicht noch einmal an. Brauchst du ihn, deaktiviere die App-Methode und aktiviere sie erneut (oder nutze „weiteres Gerät hinzufügen“) und speichere diesmal den neuen Schlüssel. Aktualisiere auch deine Authenticator-App, denn der alte Schlüssel funktioniert dann nicht mehr.</p>
<h2>So bewahrst du den Schlüssel sicher auf</h2>
<ul>
<li>Speichere ihn in einem Passwortmanager (Bitwarden, 1Password usw.) im selben Eintrag wie das Konto.</li>
<li>Schicke ihn nie per E-Mail oder Chat und veröffentliche nie einen Screenshot des QR-Codes.</li>
<li>Wer den Schlüssel hat, kann deine Codes erzeugen. Behandle ihn wie ein Passwort.</li>
</ul>
"""},
"transfer": {
 "slug": "google-authenticator-auf-neues-handy-uebertragen",
 "title": "Google Authenticator auf ein neues Handy übertragen (und die Schlüssel auslesen)",
 "desc": "Übertrage Google-Authenticator-Codes per Cloud-Synchronisierung oder Export-QR-Code auf ein neues Handy und lies die geheimen Schlüssel mit Get2FA aus dem Export-QR aus.",
 "h1": "Google Authenticator auf ein neues Handy übertragen",
 "lead": "Es gibt zwei Wege, deine Codes umzuziehen: bei Google anmelden, damit sie synchronisiert werden, oder per QR-Code exportieren. Get2FA kann diesen Export-QR auch lesen und jeden geheimen Schlüssel anzeigen.",
 "body": f"""
<h2>Weg 1: Cloud-Synchronisierung (am einfachsten)</h2>
<ol>
<li>Öffne auf dem alten Handy Google Authenticator und tippe auf dein Profilbild.</li>
<li>Melde dich mit deinem Google-Konto an und aktiviere die Synchronisierung. Ein kleines Wolkensymbol bestätigt die Sicherung.</li>
<li>Installiere auf dem neuen Handy Google Authenticator und melde dich mit demselben Google-Konto an. Deine Codes erscheinen automatisch.</li>
</ol>
<p>Die Synchronisierung ist bequem, aber deine 2FA-Schlüssel liegen dann in deinem Google-Konto. Schütze dieses Konto gut.</p>
<h2>Weg 2: Konten exportieren (offline)</h2>
<ol>
<li>Öffne auf dem alten Handy das Menü und gehe zu <strong>Konten übertragen → Konten exportieren</strong>.</li>
<li>Wähle die Konten aus und tippe auf <strong>Weiter</strong>. Die App zeigt einen oder mehrere QR-Codes.</li>
<li>Gehe auf dem neuen Handy zu <strong>Konten übertragen → Konten importieren → QR-Code scannen</strong> und scanne jeden Code.</li>
</ol>
<p>Der Export funktioniert zwischen Android und iPhone in beide Richtungen.</p>
<h2>Geheime Schlüssel aus dem Export-QR auslesen</h2>
<p>Der Export-QR-Code nutzt ein spezielles Format (<code class="k">otpauth-migration://</code>), das andere Apps oft nicht lesen können. <a href="{H}">Get2FA</a> kann es: Mache einen Screenshot des Export-QR (auf einem Handy, dem du vertraust) und füge das Bild in Get2FA ein oder ziehe es hinein. Jedes Konto erscheint mit Namen und Live-Code, und die Liste zeigt den vollständigen <code class="k">otpauth://</code>-Link mit dem Schlüssel. Speichere sie in deinem Passwortmanager.</p>
<p>Alles wird in deinem Browser dekodiert; Bild und Schlüssel werden nie hochgeladen. Lösche den Screenshot danach.</p>
<h2>Das alte Handy nicht zu früh zurücksetzen</h2>
<p>Teste einige Anmeldungen auf dem neuen Handy, bevor du das alte zurücksetzt. Geht etwas schief, wenn das alte Handy weg ist, brauchst du die Backup-Codes oder die Kontowiederherstellung der jeweiligen Website.</p>
"""},
"not-working": {
 "slug": "2fa-code-funktioniert-nicht",
 "title": "2FA-Code funktioniert nicht? 7 Gründe und Lösungen",
 "desc": "Dein Authenticator-Code wird immer wieder abgelehnt? Die häufigsten Ursachen, von der falschen Geräteuhr bis zum falschen Schlüssel, und wie du sie behebst.",
 "h1": "2FA-Code funktioniert nicht? So behebst du es",
 "lead": "Wenn eine Website deinen 2FA-Code als ungültig meldet, ist fast immer einer dieser Gründe schuld. Fang mit dem ersten an: Er löst die meisten Fälle.",
 "body": f"""
<h2>1. Die Uhr deines Geräts geht falsch</h2>
<p>TOTP-Codes werden aus der aktuellen Uhrzeit berechnet. Weicht die Uhr deines Handys oder Computers um mehr als etwa 30 Sekunden ab, passt der Code nicht. Aktiviere <strong>automatisches Datum und Uhrzeit</strong> (und automatische Zeitzone) in den Einstellungen und probiere einen neuen Code. Prüfen kannst du das mit dem <a href="{H}2fa-code-pruefen">2FA-Code-Prüfer</a>.</p>
<h2>2. Der Code ist beim Eintippen abgelaufen</h2>
<p>Jeder Code gilt 30 Sekunden, und manche Websites lehnen ihn kurz vor Ablauf ab. Warte auf einen neuen Code. Get2FA zeigt die verbleibenden Sekunden und den nächsten Code, damit du den richtigen Moment wählst.</p>
<h2>3. Falscher Schlüssel oder falsches Konto</h2>
<p>Hast du 2FA mehrmals eingerichtet, gilt nur der letzte Schlüssel. Achte darauf, dass der Eintrag in deiner App zum selben Konto gehört (Name und E-Mail prüfen) und dass du den ganzen Schlüssel kopiert hast.</p>
<h2>4. Die Website nutzt andere Einstellungen</h2>
<p>Fast alle Websites nutzen 6 Stellen, 30 Sekunden und SHA-1. Einige nutzen 8 Stellen, 60 Sekunden oder SHA-256. Enthält der QR-Code diese Einstellungen, lesen Apps sie automatisch. Bei einem Textschlüssel stellst du sie in den <em>Erweiterten Einstellungen</em> von Get2FA ein.</p>
<h2>5. Der Schlüssel wurde falsch eingetippt</h2>
<p>Geheime Schlüssel enthalten nur die Buchstaben A–Z und die Ziffern 2–7. Die Ziffern 0, 1, 8 und 9 kommen nie vor, eine „0“ ist also eigentlich der Buchstabe O und eine „1“ ein I oder L. Kopieren und einfügen statt abtippen, wann immer möglich.</p>
<h2>6. Der Code wurde schon benutzt</h2>
<p>Manche Websites akzeptieren jeden Code nur einmal. Hast du gerade einen Code verwendet, warte auf den nächsten.</p>
<h2>7. 2FA wurde auf der Website zurückgesetzt</h2>
<p>Hast du (oder der Support) 2FA aus- und wieder eingeschaltet, funktioniert der alte Schlüssel nicht mehr. Melde dich mit einem Backup-Code an und richte die Authenticator-App neu ein.</p>
<h2>Immer noch ausgesperrt?</h2>
<p>Nutze die Backup- oder Wiederherstellungscodes der Website oder starte die Kontowiederherstellung. Siehe <a href="handy-verloren-authenticator">was zu tun ist, wenn du dein Handy verloren hast</a>.</p>
"""},
"lost-phone": {
 "slug": "handy-verloren-authenticator",
 "title": "Handy mit Authenticator-App verloren? Das musst du jetzt tun",
 "desc": "Handy mit deinen 2FA-Codes verloren, gestohlen oder zurückgesetzt? So kommst du mit gespeicherten Schlüsseln, Backup-Codes, Cloud-Sync oder Kontowiederherstellung wieder in deine Konten.",
 "h1": "Handy mit Authenticator verloren? Das ist zu tun",
 "lead": "Das Handy mit deinen 2FA-Codes zu verlieren ist stressig, aber meist gibt es einen Weg zurück. Geh diese Möglichkeiten der Reihe nach durch.",
 "body": f"""
<h2>1. Hast du die geheimen Schlüssel gespeichert?</h2>
<p>Hast du die Einrichtungsschlüssel aufbewahrt (im Passwortmanager, in einer Notiz oder ausgedruckt), hast du Glück: Füge jeden Schlüssel in <a href="{H}">Get2FA</a> ein und du hast sofort funktionierende Codes, auf jedem Gerät. Füge die Schlüssel dann einer Authenticator-App auf deinem neuen Handy hinzu.</p>
<h2>2. War die Cloud-Synchronisierung aktiv?</h2>
<p>Google Authenticator (wenn angemeldet), Microsoft Authenticator, 2FAS und andere können deine Codes sichern. Installiere dieselbe App auf dem neuen Handy und melde dich mit demselben Konto an, um sie wiederherzustellen.</p>
<h2>3. Backup-Codes verwenden</h2>
<p>Die meisten Websites geben dir beim Aktivieren von 2FA einmalige Backup- oder Wiederherstellungscodes (Google, Facebook, Instagram und GitHub tun das alle). Jeder Code bringt dich einmal hinein. Richte danach 2FA auf deinem neuen Handy neu ein.</p>
<h2>4. Eine andere 2FA-Methode nutzen</h2>
<p>Hast du auch SMS, einen Sicherheitsschlüssel, einen Passkey oder ein anderes vertrauenswürdiges Gerät hinzugefügt, melde dich damit an.</p>
<h2>5. Kontowiederherstellung starten</h2>
<p>Als letzten Ausweg nutze die Option „Kein Zugriff auf deine Codes?“ oder die Kontowiederherstellung der Website. Das kann Tage dauern und erfordert meist einen Identitätsnachweis, also fang früh an.</p>
<h2>Wenn du wieder drin bist</h2>
<ul>
<li>Richte 2FA neu ein und <strong>speichere diesmal jeden neuen Schlüssel</strong> in einem Passwortmanager.</li>
<li>Bewahre die neuen Backup-Codes außerhalb deines Handys auf.</li>
<li>Wurde das Handy gestohlen, ändere die Passwörter deiner wichtigen Konten und entferne das alte Gerät aus deinen Konten.</li>
</ul>
"""},
}
