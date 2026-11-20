# -*- coding: utf-8 -*-
"""Account line splitter tool (all languages)."""

def tpl_split(t, u, adv_html):
    d = u["d"]
    opts_in = "".join(f'<option value="{k}">{v}</option>' for k, v in [("auto", u["auto"]), ("pipe", "| " + d["pipe"]), ("colon", ": " + d["colon"]), ("semi", "; " + d["semi"]), ("comma", ", " + d["comma"]), ("tab", d["tab"]), ("space", d["space"])])
    opts_out = "".join(f'<option value="{k}">{v}</option>' for k, v in [("pipe", "| " + d["pipe"]), ("same", u["same"]), ("colon", ": " + d["colon"]), ("semi", "; " + d["semi"]), ("comma", ", " + d["comma"]), ("tab", d["tab"]), ("space", d["space"])])
    return f"""
  <section class="tool" aria-label="{u['aria']}">
    <label class="lbl" for="sIn">{u['input']}</label>
    <textarea id="sIn" spellcheck="false" autocomplete="off" rows="7" placeholder="{u['inputPh']}"></textarea>
    <div class="grid2">
      <label class="fld">{u['delim']}<select id="sDelim">{opts_in}</select></label>
      <label class="fld">{u['outDelim']}<select id="sOutDelim">{opts_out}</select></label>
    </div>
    <div class="lbl">{u['cols']} <small>{u['colsHint']}</small></div>
    <div class="chips" id="sPrev"></div>
    <label class="fld"><input id="sCols" type="text" spellcheck="false" autocomplete="off" placeholder="{u['colsPh']}"></label>
    <div class="checks">
      <label><input type="checkbox" id="sTrim" checked> {u['trim']}</label>
      <label><input type="checkbox" id="sDedup"> {u['dedup']}</label>
      <label><input type="checkbox" id="sCode"> {u['addCode']}</label>
    </div>
    {adv_html(t)}
    <div class="row"><label class="lbl" for="sOut" style="margin:0">{u['output']}</label><span class="spacer"></span><small class="hint" id="sStat"></small></div>
    <textarea id="sOut" readonly spellcheck="false" rows="7"></textarea>
    <div class="row">
      <button class="btn primary" id="sCopy" type="button">{u['copy']}</button>
      <button class="btn" id="sDl" type="button">{u['dl']}</button>
      <span class="spacer"></span>
      <button class="btn ghost" id="sClear" type="button">{u['clear']}</button>
    </div>
    <div class="hint">{u['hint']}</div>
  </section>"""

PH = "uid1|pass1|JBSWY3DPEHPK3PXP|mail1@example.com\nuid2|pass2|KRSXG5CTMVRXEZLU|mail2@example.com"

SPLIT = {
"en": {"path": "/account-line-splitter",
 "title": "Account Line Splitter – Split user|pass|2FA Lines and Add 2FA Codes",
 "desc": "Split account lines like user|pass|2FA|email, pick and reorder columns, change the separator, remove duplicates and add the current 2FA code to every line. Free, in your browser.",
 "h1": "Account line splitter (user|pass|2FA)",
 "sub": "Paste account lines, pick the columns you need, change the separator and add the live 2FA code to each line. Nothing is uploaded.",
 "card": "Account line splitter", "cardDesc": "Split user|pass|2FA lines, pick columns and add the current 2FA code.",
 "i18n": {"copied": "Copied", "stat": "{n} lines · {c} columns", "detected": "separator"},
 "ui": {"aria": "Line splitter", "input": "Account lines", "inputPh": PH, "delim": "Input separator", "auto": "Detect automatically", "outDelim": "Output separator", "same": "Same as input",
        "cols": "Columns", "colsHint": "click to include or remove · 🔑 = 2FA key", "colsPh": "e.g. 1,3 or 1-2,4 (empty = all)",
        "trim": "Trim spaces", "dedup": "Remove duplicates", "addCode": "Add current 2FA code column", "output": "Result",
        "copy": "Copy result", "dl": "Download .txt", "clear": "Clear", "hint": "Lines are processed on your device and never uploaded. Codes refresh every few seconds while “add 2FA code” is on.",
        "d": {"pipe": "(pipe)", "colon": "(colon)", "semi": "(semicolon)", "comma": "(comma)", "tab": "Tab", "space": "Space"}},
 "content": """
    <h2>How to use it</h2>
    <ol class="steps"><li><b>Paste the lines</b>One account per line, in any format: <code class="k">user|pass|2FA</code>, <code class="k">email:pass</code>, CSV…</li><li><b>Pick the columns</b>Click the column chips or type the order you want, like <code class="k">3,1</code>.</li><li><b>Copy or download</b>Choose the output separator and, if you want, add the current 2FA code to each line.</li></ol>
    <h2>What can it do?</h2>
    <ul>
    <li>Keep only some columns, for example just the 2FA keys or just the emails.</li>
    <li>Reorder columns and convert between separators (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, comma, tab).</li>
    <li>Remove duplicate and empty lines.</li>
    <li>Find the 2FA key in each line automatically and append the 6-digit code that works right now.</li>
    </ul>
    <h2>Privacy</h2>
    <p>Account lines often contain passwords. This tool runs entirely in your browser: nothing you paste is sent, logged or stored. Close the tab when you're done. Need the codes only? Use the <a href="/">2FA code generator</a>, which also accepts whole lines.</p>"""},
"pt": {"path": "/pt/separar-linhas-de-contas",
 "title": "Separador de linhas de contas – Divida login|senha|2FA e adicione o código 2FA",
 "desc": "Separe linhas de contas como login|senha|2FA|email, escolha e reordene colunas, troque o separador, remova duplicadas e adicione o código 2FA atual em cada linha. Grátis, no navegador.",
 "h1": "Separador de linhas de contas (login|senha|2FA)",
 "sub": "Cole as linhas das contas, escolha as colunas, troque o separador e adicione o código 2FA ao vivo em cada linha. Nada é enviado.",
 "card": "Separador de contas", "cardDesc": "Divida linhas login|senha|2FA, escolha colunas e adicione o código 2FA atual.",
 "i18n": {"copied": "Copiado", "stat": "{n} linhas · {c} colunas", "detected": "separador"},
 "ui": {"aria": "Separador de linhas", "input": "Linhas das contas", "inputPh": PH, "delim": "Separador de entrada", "auto": "Detectar automaticamente", "outDelim": "Separador de saída", "same": "Igual à entrada",
        "cols": "Colunas", "colsHint": "clique para incluir ou remover · 🔑 = chave 2FA", "colsPh": "ex.: 1,3 ou 1-2,4 (vazio = todas)",
        "trim": "Remover espaços", "dedup": "Remover duplicadas", "addCode": "Adicionar coluna com o código 2FA atual", "output": "Resultado",
        "copy": "Copiar resultado", "dl": "Baixar .txt", "clear": "Limpar", "hint": "As linhas são processadas no seu aparelho e nunca são enviadas. Com “código 2FA” ligado, os códigos se atualizam a cada poucos segundos.",
        "d": {"pipe": "(barra)", "colon": "(dois-pontos)", "semi": "(ponto e vírgula)", "comma": "(vírgula)", "tab": "Tab", "space": "Espaço"}},
 "content": """
    <h2>Como usar</h2>
    <ol class="steps"><li><b>Cole as linhas</b>Uma conta por linha, em qualquer formato: <code class="k">login|senha|2FA</code>, <code class="k">email:senha</code>, CSV…</li><li><b>Escolha as colunas</b>Clique nas colunas ou digite a ordem desejada, como <code class="k">3,1</code>.</li><li><b>Copie ou baixe</b>Escolha o separador de saída e, se quiser, adicione o código 2FA atual em cada linha.</li></ol>
    <h2>O que dá para fazer?</h2>
    <ul>
    <li>Manter só algumas colunas, por exemplo só as chaves 2FA ou só os e-mails.</li>
    <li>Reordenar colunas e converter entre separadores (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, vírgula, tab).</li>
    <li>Remover linhas duplicadas e vazias.</li>
    <li>Encontrar a chave 2FA em cada linha automaticamente e acrescentar o código de 6 dígitos válido agora.</li>
    </ul>
    <h2>Privacidade</h2>
    <p>Linhas de contas costumam ter senhas. Esta ferramenta roda inteira no seu navegador: nada do que você cola é enviado, registrado ou guardado. Feche a aba ao terminar. Só precisa dos códigos? Use o <a href="/pt/">gerador de código 2FA</a>, que também aceita linhas inteiras.</p>"""},
"es": {"path": "/es/separar-lineas-de-cuentas",
 "title": "Separador de líneas de cuentas – Divide usuario|contraseña|2FA y añade el código 2FA",
 "desc": "Separa líneas como usuario|contraseña|2FA|correo, elige y reordena columnas, cambia el separador, quita duplicados y añade el código 2FA actual a cada línea. Gratis, en tu navegador.",
 "h1": "Separador de líneas de cuentas (usuario|contraseña|2FA)",
 "sub": "Pega las líneas de las cuentas, elige las columnas, cambia el separador y añade el código 2FA en vivo a cada línea. No se sube nada.",
 "card": "Separador de cuentas", "cardDesc": "Divide líneas usuario|contraseña|2FA, elige columnas y añade el código 2FA actual.",
 "i18n": {"copied": "Copiado", "stat": "{n} líneas · {c} columnas", "detected": "separador"},
 "ui": {"aria": "Separador de líneas", "input": "Líneas de cuentas", "inputPh": PH, "delim": "Separador de entrada", "auto": "Detectar automáticamente", "outDelim": "Separador de salida", "same": "Igual que la entrada",
        "cols": "Columnas", "colsHint": "haz clic para incluir o quitar · 🔑 = clave 2FA", "colsPh": "ej.: 1,3 o 1-2,4 (vacío = todas)",
        "trim": "Quitar espacios", "dedup": "Quitar duplicados", "addCode": "Añadir columna con el código 2FA actual", "output": "Resultado",
        "copy": "Copiar resultado", "dl": "Descargar .txt", "clear": "Borrar", "hint": "Las líneas se procesan en tu dispositivo y nunca se suben. Con “código 2FA” activado, los códigos se actualizan cada pocos segundos.",
        "d": {"pipe": "(barra)", "colon": "(dos puntos)", "semi": "(punto y coma)", "comma": "(coma)", "tab": "Tabulador", "space": "Espacio"}},
 "content": """
    <h2>Cómo usarlo</h2>
    <ol class="steps"><li><b>Pega las líneas</b>Una cuenta por línea, en cualquier formato: <code class="k">usuario|contraseña|2FA</code>, <code class="k">correo:contraseña</code>, CSV…</li><li><b>Elige las columnas</b>Haz clic en las columnas o escribe el orden que quieras, como <code class="k">3,1</code>.</li><li><b>Copia o descarga</b>Elige el separador de salida y, si quieres, añade el código 2FA actual a cada línea.</li></ol>
    <h2>¿Qué puede hacer?</h2>
    <ul>
    <li>Quedarte solo con algunas columnas, por ejemplo solo las claves 2FA o solo los correos.</li>
    <li>Reordenar columnas y convertir entre separadores (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, coma, tabulador).</li>
    <li>Quitar líneas duplicadas y vacías.</li>
    <li>Encontrar la clave 2FA de cada línea y añadir el código de 6 dígitos válido ahora mismo.</li>
    </ul>
    <h2>Privacidad</h2>
    <p>Las líneas de cuentas suelen tener contraseñas. Esta herramienta funciona entera en tu navegador: nada de lo que pegas se envía, registra ni guarda. Cierra la pestaña al terminar. ¿Solo necesitas los códigos? Usa el <a href="/es/">generador de códigos 2FA</a>, que también acepta líneas completas.</p>"""},
"vi": {"path": "/vi/cat-chuoi-tai-khoan",
 "title": "Cắt chuỗi tài khoản – Tách uid|pass|2FA và lấy mã 2FA hàng loạt",
 "desc": "Cắt chuỗi tài khoản dạng uid|pass|2FA|mail: chọn và sắp xếp cột, đổi ký tự phân cách, xóa dòng trùng và thêm mã 2FA hiện tại vào từng dòng. Miễn phí, chạy trên trình duyệt.",
 "h1": "Cắt chuỗi tài khoản (uid|pass|2FA)",
 "sub": "Dán danh sách tài khoản, chọn cột cần lấy, đổi ký tự phân cách và thêm mã 2FA trực tiếp vào từng dòng. Không có gì được tải lên.",
 "card": "Cắt chuỗi tài khoản", "cardDesc": "Tách dòng uid|pass|2FA, chọn cột và thêm mã 2FA hiện tại.",
 "i18n": {"copied": "Đã sao chép", "stat": "{n} dòng · {c} cột", "detected": "phân cách"},
 "ui": {"aria": "Cắt chuỗi", "input": "Danh sách tài khoản", "inputPh": PH, "delim": "Ký tự phân cách đầu vào", "auto": "Tự động nhận diện", "outDelim": "Ký tự phân cách đầu ra", "same": "Giống đầu vào",
        "cols": "Cột", "colsHint": "bấm để chọn hoặc bỏ · 🔑 = khóa 2FA", "colsPh": "vd: 1,3 hoặc 1-2,4 (để trống = tất cả)",
        "trim": "Xóa khoảng trắng", "dedup": "Xóa dòng trùng", "addCode": "Thêm cột mã 2FA hiện tại", "output": "Kết quả",
        "copy": "Sao chép kết quả", "dl": "Tải .txt", "clear": "Xóa", "hint": "Dữ liệu được xử lý trên thiết bị của bạn và không bao giờ được tải lên. Khi bật “mã 2FA”, mã tự cập nhật sau vài giây.",
        "d": {"pipe": "(gạch đứng)", "colon": "(hai chấm)", "semi": "(chấm phẩy)", "comma": "(dấu phẩy)", "tab": "Tab", "space": "Dấu cách"}},
 "content": """
    <h2>Cách dùng</h2>
    <ol class="steps"><li><b>Dán danh sách</b>Mỗi dòng một tài khoản, định dạng bất kỳ: <code class="k">uid|pass|2FA</code>, <code class="k">mail:pass</code>, CSV…</li><li><b>Chọn cột</b>Bấm vào các cột hoặc nhập thứ tự mong muốn, ví dụ <code class="k">3,1</code>.</li><li><b>Sao chép hoặc tải về</b>Chọn ký tự phân cách đầu ra và, nếu cần, thêm mã 2FA hiện tại vào từng dòng.</li></ol>
    <h2>Công cụ làm được gì?</h2>
    <ul>
    <li>Chỉ giữ một số cột, ví dụ chỉ lấy khóa 2FA hoặc chỉ lấy mail.</li>
    <li>Đổi thứ tự cột và chuyển ký tự phân cách (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, dấu phẩy, tab).</li>
    <li>Xóa dòng trùng và dòng trống.</li>
    <li>Tự tìm khóa 2FA trong từng dòng và thêm mã 6 số đang có hiệu lực.</li>
    </ul>
    <h2>Quyền riêng tư</h2>
    <p>Danh sách tài khoản thường chứa mật khẩu. Công cụ này chạy hoàn toàn trong trình duyệt: không có gì bạn dán vào bị gửi đi, ghi lại hay lưu trữ. Đóng tab khi xong. Chỉ cần lấy mã? Dùng <a href="/vi/">công cụ lấy mã 2FA</a>, cũng nhận cả dòng tài khoản.</p>"""},
"id": {"path": "/id/pemisah-baris-akun",
 "title": "Pemisah Baris Akun – Pisahkan user|pass|2FA dan Tambahkan Kode 2FA",
 "desc": "Pisahkan baris akun seperti user|pass|2FA|email, pilih dan urutkan kolom, ganti pemisah, hapus duplikat, dan tambahkan kode 2FA saat ini di setiap baris. Gratis, di browser.",
 "h1": "Pemisah baris akun (user|pass|2FA)",
 "sub": "Tempel baris akun, pilih kolom yang dibutuhkan, ganti pemisah, dan tambahkan kode 2FA langsung di setiap baris. Tidak ada yang diunggah.",
 "card": "Pemisah baris akun", "cardDesc": "Pisahkan baris user|pass|2FA, pilih kolom, dan tambahkan kode 2FA saat ini.",
 "i18n": {"copied": "Disalin", "stat": "{n} baris · {c} kolom", "detected": "pemisah"},
 "ui": {"aria": "Pemisah baris", "input": "Baris akun", "inputPh": PH, "delim": "Pemisah input", "auto": "Deteksi otomatis", "outDelim": "Pemisah output", "same": "Sama dengan input",
        "cols": "Kolom", "colsHint": "klik untuk memilih atau menghapus · 🔑 = kunci 2FA", "colsPh": "mis.: 1,3 atau 1-2,4 (kosong = semua)",
        "trim": "Hapus spasi", "dedup": "Hapus duplikat", "addCode": "Tambah kolom kode 2FA saat ini", "output": "Hasil",
        "copy": "Salin hasil", "dl": "Unduh .txt", "clear": "Hapus", "hint": "Baris diproses di perangkat Anda dan tidak pernah diunggah. Saat “kode 2FA” aktif, kode diperbarui setiap beberapa detik.",
        "d": {"pipe": "(garis tegak)", "colon": "(titik dua)", "semi": "(titik koma)", "comma": "(koma)", "tab": "Tab", "space": "Spasi"}},
 "content": """
    <h2>Cara menggunakan</h2>
    <ol class="steps"><li><b>Tempel baris</b>Satu akun per baris, format apa pun: <code class="k">user|pass|2FA</code>, <code class="k">email:pass</code>, CSV…</li><li><b>Pilih kolom</b>Klik kolomnya atau ketik urutan yang diinginkan, misalnya <code class="k">3,1</code>.</li><li><b>Salin atau unduh</b>Pilih pemisah output dan, jika perlu, tambahkan kode 2FA saat ini di setiap baris.</li></ol>
    <h2>Apa saja yang bisa dilakukan?</h2>
    <ul>
    <li>Menyimpan kolom tertentu saja, misalnya hanya kunci 2FA atau hanya email.</li>
    <li>Mengurutkan ulang kolom dan mengganti pemisah (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, koma, tab).</li>
    <li>Menghapus baris duplikat dan kosong.</li>
    <li>Menemukan kunci 2FA di setiap baris secara otomatis dan menambahkan kode 6 digit yang berlaku sekarang.</li>
    </ul>
    <h2>Privasi</h2>
    <p>Baris akun biasanya berisi kata sandi. Alat ini berjalan sepenuhnya di browser Anda: apa pun yang Anda tempel tidak dikirim, dicatat, atau disimpan. Tutup tab setelah selesai. Hanya butuh kodenya? Gunakan <a href="/id/">generator kode 2FA</a>, yang juga menerima baris lengkap.</p>"""},
"de": {"path": "/de/kontozeilen-trennen",
 "title": "Kontozeilen trennen – user|pass|2FA aufteilen und 2FA-Codes hinzufügen",
 "desc": "Trenne Kontozeilen wie user|pass|2FA|E-Mail, wähle und sortiere Spalten, ändere das Trennzeichen, entferne Duplikate und füge jeder Zeile den aktuellen 2FA-Code hinzu. Kostenlos im Browser.",
 "h1": "Kontozeilen trennen (user|pass|2FA)",
 "sub": "Füge Kontozeilen ein, wähle die benötigten Spalten, ändere das Trennzeichen und hänge jeder Zeile den aktuellen 2FA-Code an. Nichts wird hochgeladen.",
 "card": "Kontozeilen trennen", "cardDesc": "Teile user|pass|2FA-Zeilen auf, wähle Spalten und füge den aktuellen 2FA-Code hinzu.",
 "i18n": {"copied": "Kopiert", "stat": "{n} Zeilen · {c} Spalten", "detected": "Trennzeichen"},
 "ui": {"aria": "Zeilen trennen", "input": "Kontozeilen", "inputPh": PH, "delim": "Trennzeichen (Eingabe)", "auto": "Automatisch erkennen", "outDelim": "Trennzeichen (Ausgabe)", "same": "Wie Eingabe",
        "cols": "Spalten", "colsHint": "klicken zum Aus- oder Abwählen · 🔑 = 2FA-Schlüssel", "colsPh": "z. B. 1,3 oder 1-2,4 (leer = alle)",
        "trim": "Leerzeichen entfernen", "dedup": "Duplikate entfernen", "addCode": "Spalte mit aktuellem 2FA-Code hinzufügen", "output": "Ergebnis",
        "copy": "Ergebnis kopieren", "dl": ".txt herunterladen", "clear": "Leeren", "hint": "Die Zeilen werden auf deinem Gerät verarbeitet und nie hochgeladen. Mit „2FA-Code“ aktualisieren sich die Codes alle paar Sekunden.",
        "d": {"pipe": "(senkrechter Strich)", "colon": "(Doppelpunkt)", "semi": "(Semikolon)", "comma": "(Komma)", "tab": "Tab", "space": "Leerzeichen"}},
 "content": """
    <h2>So funktioniert es</h2>
    <ol class="steps"><li><b>Zeilen einfügen</b>Ein Konto pro Zeile, beliebiges Format: <code class="k">user|pass|2FA</code>, <code class="k">email:pass</code>, CSV…</li><li><b>Spalten wählen</b>Klicke auf die Spalten oder gib die gewünschte Reihenfolge ein, z. B. <code class="k">3,1</code>.</li><li><b>Kopieren oder herunterladen</b>Wähle das Trennzeichen für die Ausgabe und füge bei Bedarf jeder Zeile den aktuellen 2FA-Code hinzu.</li></ol>
    <h2>Was kann das Tool?</h2>
    <ul>
    <li>Nur bestimmte Spalten behalten, etwa nur die 2FA-Schlüssel oder nur die E-Mails.</li>
    <li>Spalten umsortieren und zwischen Trennzeichen wechseln (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, Komma, Tab).</li>
    <li>Doppelte und leere Zeilen entfernen.</li>
    <li>Den 2FA-Schlüssel in jeder Zeile automatisch finden und den gerade gültigen 6-stelligen Code anhängen.</li>
    </ul>
    <h2>Datenschutz</h2>
    <p>Kontozeilen enthalten oft Passwörter. Dieses Tool läuft komplett in deinem Browser: Nichts, was du einfügst, wird gesendet, protokolliert oder gespeichert. Schließe den Tab, wenn du fertig bist. Brauchst du nur die Codes? Nutze den <a href="/de/">2FA-Code-Generator</a>, der auch ganze Zeilen versteht.</p>"""},
"th": {"path": "/th/yaek-khomun-banchi",
 "title": "แยกข้อมูลบัญชี – แยกบรรทัด user|pass|2FA และเพิ่มรหัส 2FA",
 "desc": "แยกบรรทัดบัญชีแบบ user|pass|2FA|อีเมล เลือกและเรียงคอลัมน์ เปลี่ยนตัวคั่น ลบรายการซ้ำ และเพิ่มรหัส 2FA ปัจจุบันในทุกบรรทัด ฟรี ทำงานในเบราว์เซอร์",
 "h1": "แยกข้อมูลบัญชี (user|pass|2FA)",
 "sub": "วางบรรทัดบัญชี เลือกคอลัมน์ที่ต้องการ เปลี่ยนตัวคั่น และเพิ่มรหัส 2FA สดๆ ในแต่ละบรรทัด ไม่มีการอัปโหลดใดๆ",
 "card": "แยกข้อมูลบัญชี", "cardDesc": "แยกบรรทัด user|pass|2FA เลือกคอลัมน์ และเพิ่มรหัส 2FA ปัจจุบัน",
 "i18n": {"copied": "คัดลอกแล้ว", "stat": "{n} บรรทัด · {c} คอลัมน์", "detected": "ตัวคั่น"},
 "ui": {"aria": "แยกบรรทัด", "input": "บรรทัดบัญชี", "inputPh": PH, "delim": "ตัวคั่นขาเข้า", "auto": "ตรวจจับอัตโนมัติ", "outDelim": "ตัวคั่นขาออก", "same": "เหมือนขาเข้า",
        "cols": "คอลัมน์", "colsHint": "คลิกเพื่อเลือกหรือเอาออก · 🔑 = คีย์ 2FA", "colsPh": "เช่น 1,3 หรือ 1-2,4 (ว่าง = ทั้งหมด)",
        "trim": "ตัดช่องว่าง", "dedup": "ลบรายการซ้ำ", "addCode": "เพิ่มคอลัมน์รหัส 2FA ปัจจุบัน", "output": "ผลลัพธ์",
        "copy": "คัดลอกผลลัพธ์", "dl": "ดาวน์โหลด .txt", "clear": "ล้าง", "hint": "ข้อมูลถูกประมวลผลบนอุปกรณ์ของคุณและไม่ถูกอัปโหลด เมื่อเปิด “รหัส 2FA” รหัสจะอัปเดตทุกไม่กี่วินาที",
        "d": {"pipe": "(ขีดตั้ง)", "colon": "(ทวิภาค)", "semi": "(อัฒภาค)", "comma": "(จุลภาค)", "tab": "แท็บ", "space": "ช่องว่าง"}},
 "content": """
    <h2>วิธีใช้</h2>
    <ol class="steps"><li><b>วางบรรทัด</b>บรรทัดละหนึ่งบัญชี รูปแบบใดก็ได้: <code class="k">user|pass|2FA</code>, <code class="k">email:pass</code>, CSV…</li><li><b>เลือกคอลัมน์</b>คลิกที่คอลัมน์ หรือพิมพ์ลำดับที่ต้องการ เช่น <code class="k">3,1</code></li><li><b>คัดลอกหรือดาวน์โหลด</b>เลือกตัวคั่นขาออก และถ้าต้องการ ให้เพิ่มรหัส 2FA ปัจจุบันในแต่ละบรรทัด</li></ol>
    <h2>ทำอะไรได้บ้าง?</h2>
    <ul>
    <li>เก็บเฉพาะบางคอลัมน์ เช่น เฉพาะคีย์ 2FA หรือเฉพาะอีเมล</li>
    <li>เรียงคอลัมน์ใหม่และเปลี่ยนตัวคั่น (<code class="k">|</code>, <code class="k">:</code>, <code class="k">;</code>, จุลภาค, แท็บ)</li>
    <li>ลบบรรทัดซ้ำและบรรทัดว่าง</li>
    <li>หาคีย์ 2FA ในแต่ละบรรทัดอัตโนมัติ และเพิ่มรหัส 6 หลักที่ใช้ได้ตอนนี้</li>
    </ul>
    <h2>ความเป็นส่วนตัว</h2>
    <p>บรรทัดบัญชีมักมีรหัสผ่าน เครื่องมือนี้ทำงานในเบราว์เซอร์ทั้งหมด สิ่งที่คุณวางจะไม่ถูกส่ง บันทึก หรือจัดเก็บ ปิดแท็บเมื่อใช้เสร็จ ต้องการแค่รหัส? ใช้ <a href="/th/">ตัวสร้างรหัส 2FA</a> ซึ่งรับทั้งบรรทัดได้เหมือนกัน</p>"""},
}

# Text for the "view in your language" hint, written in the target language.
SUGGEST = {"en": "View this page in English", "pt": "Ver esta página em Português", "es": "Ver esta página en Español",
           "vi": "Xem trang này bằng Tiếng Việt", "id": "Lihat halaman ini dalam Bahasa Indonesia", "de": "Diese Seite auf Deutsch ansehen",
           "th": "ดูหน้านี้เป็นภาษาไทย"}
