# -*- coding: utf-8 -*-
H = "/id/"
G = "/id/panduan/"

TOOLS = {
"gen": {
 "path": "/id/generator-kunci-2fa",
 "title": "Generator Kunci Rahasia 2FA & Kode QR (TOTP) – Gratis, di Browser Anda",
 "desc": "Buat kunci rahasia 2FA acak, tautan otpauth://, dan kode QR untuk Google Authenticator dan aplikasi TOTP apa pun. Dibuat di perangkat Anda dengan Web Crypto.",
 "h1": "Generator kunci rahasia 2FA & kode QR",
 "sub": "Buat kunci TOTP acak, tautan otpauth://, dan kode QR yang bisa dipindai aplikasi autentikator apa pun. Cocok untuk developer yang menguji 2FA atau menyiapkan aplikasinya sendiri.",
 "card": "Generator kunci & QR", "cardDesc": "Buat kunci 2FA acak dan kode QR-nya untuk aplikasi autentikator apa pun.",
 "i18n": {"copied": "Disalin"},
 "ui": {"aria": "Generator", "issuer": "Penerbit (nama aplikasi atau situs)", "issuerPh": "AplikasiSaya", "account": "Akun (nama pengguna atau email)", "accountPh": "budi@contoh.com",
        "keyLen": "Panjang kunci", "opt80": "80 bit (16 karakter)", "opt160": "160 bit (32 karakter, disarankan)", "opt256": "256 bit (52 karakter)",
        "newKey": "Kunci baru", "secret": "Kunci rahasia", "uri": "Tautan otpauth://", "copy": "Salin", "copyLink": "Salin tautan", "dl": "Unduh QR (SVG)",
        "openGen": "Buka di generator", "current": "Kode saat ini",
        "hint": "Kunci dibuat dengan pembangkit acak aman milik browser dan tidak pernah keluar dari halaman ini."},
 "content": """
    <h2>Cara menggunakan</h2>
    <ol class="steps"><li><b>Beri nama</b>Ketik penerbit (aplikasi atau situs Anda) dan akunnya. Keduanya menjadi label yang terlihat di aplikasi autentikator.</li><li><b>Pindai atau salin</b>Pindai kode QR dengan Google Authenticator, Microsoft Authenticator, 2FAS, atau aplikasi TOTP lain, atau salin tautan otpauth://.</li><li><b>Cek kodenya</b>Kode saat ini diperbarui langsung, jadi Anda bisa memastikan aplikasi menampilkan angka yang sama.</li></ol>
    <h2>Apa itu tautan otpauth://?</h2>
    <p>Itu format standar yang dibaca aplikasi autentikator dari kode QR: <code class="k">otpauth://totp/Penerbit:akun?secret=KUNCI&amp;issuer=Penerbit</code>. Parameter opsional mengatur algoritma, digit, dan periode. Kebanyakan layanan memakai SHA-1, 6 digit, dan 30 detik, yang juga menjadi bawaan di sini.</p>
    <h2>Amankah membuat kunci secara online?</h2>
    <p>Kunci dibuat dengan <code class="k">crypto.getRandomValues</code> di browser Anda dan tidak ada yang diunggah. Untuk sistem produksi, buat kunci di server Anda sendiri dan simpan dalam bentuk terenkripsi; gunakan alat ini untuk uji coba, prototipe, atau akun pribadi.</p>
    <h2>Panjang kunci mana yang dipakai?</h2>
    <p>160 bit (32 karakter Base32) adalah rekomendasi RFC 4226 dan dipakai sebagian besar layanan. 80 bit adalah batas minimum beberapa aplikasi lama; 256 bit bisa dipakai di aplikasi modern.</p>"""},
"check": {
 "path": "/id/cek-kode-2fa",
 "title": "Cek Kode 2FA – Mengapa Kode Autentikator Salah? | Cek Jam",
 "desc": "Tempel kunci 2FA dan kode dari aplikasi untuk melihat apakah cocok, lalu cek apakah jam perangkat Anda meleset. Cari tahu mengapa kode autentikator tidak berfungsi.",
 "h1": "Cek kode 2FA dan jam perangkat",
 "sub": "Tempel kunci rahasia dan kode yang ditampilkan autentikator Anda. Kami beri tahu apakah cocok, dan apakah jam perangkat menjadi penyebab kode ditolak.",
 "card": "Pengecek kode 2FA", "cardDesc": "Lihat apakah kode cocok dengan kunci dan apakah jam perangkat meleset.",
 "i18n": {"copied": "Disalin", "clockOk": "✓ Jam perangkat Anda tepat (selisih kurang dari 2 detik).",
          "clockAhead": "⚠ Jam perangkat Anda lebih cepat sekitar {n} detik. Aktifkan tanggal dan waktu otomatis.",
          "clockBehind": "⚠ Jam perangkat Anda lebih lambat sekitar {n} detik. Aktifkan tanggal dan waktu otomatis.",
          "clockUnknown": "Saat ini jam Anda tidak bisa dicek.",
          "badKey": "Itu tidak terlihat seperti kunci rahasia 2FA yang valid.", "badCode": "Ketik kode {n} digit dari aplikasi Anda.",
          "match": "✓ Kode cocok dengan kode saat ini. Aplikasi dan kunci Anda sudah benar.",
          "matchPast": "⚠ Kode cocok dengan kode {s} detik yang lalu. Kemungkinan jam perangkat lambat, atau kodenya sudah lama.",
          "matchFuture": "⚠ Kode cocok dengan kode {s} detik ke depan. Perangkat yang membuatnya punya jam yang terlalu cepat.",
          "noMatch": "✗ Tidak ada yang cocok dalam ±5 menit. Kunci, akun, atau pengaturannya (digit, periode, algoritma) berbeda.",
          "expected": "Kode saat ini untuk kunci ini:"},
 "ui": {"aria": "Pengecek", "checking": "Mengecek jam Anda…", "secret": "Kunci rahasia", "code": "Kode dari aplikasi", "check": "Cek kode"},
 "content": f"""
    <h2>Arti hasilnya</h2>
    <ul>
    <li><b>Cocok dengan kode saat ini:</b> kunci dan aplikasi Anda baik-baik saja. Jika situs masih menolak, mungkin situs memakai kunci lain (2FA diatur ulang) atau kode kedaluwarsa saat Anda mengetik.</li>
    <li><b>Cocok dengan kode sebelum atau sesudahnya:</b> salah satu jam meleset. Aktifkan tanggal dan waktu otomatis di ponsel yang menjalankan autentikator.</li>
    <li><b>Tidak cocok:</b> kunci milik akun lain, tersalin tidak lengkap, atau situs memakai 8 digit, 60 detik, atau SHA-256.</li>
    </ul>
    <h2>Cara kerja cek jam</h2>
    <p>Kami membandingkan waktu perangkat Anda dengan waktu yang dilaporkan server kami dalam permintaan halaman biasa. Kode TOTP berganti setiap 30 detik, jadi selisih beberapa detik saja sudah cukup membuat kode gagal.</p>
    <p>Masih bermasalah? Baca <a href="{G}kode-2fa-tidak-berfungsi">Kode 2FA tidak berfungsi: 7 penyebab</a>.</p>"""},
"read": {
 "path": "/id/baca-kode-qr-2fa",
 "title": "Baca Kode QR 2FA – Ambil Kunci Rahasia (Termasuk Ekspor Google Authenticator)",
 "desc": "Unggah atau tempel tangkapan layar kode QR 2FA untuk mengambil kunci rahasia dan tautan otpauth. Bisa membaca QR ekspor Google Authenticator (otpauth-migration). Berjalan di browser.",
 "h1": "Baca kode QR 2FA dan dapatkan kunci rahasia",
 "sub": "Seret, tempel, atau unggah tangkapan layar kode QR 2FA. Anda akan mendapat kunci rahasia, penerbit, akun, dan pengaturannya, bahkan dari kode ekspor Google Authenticator.",
 "card": "Pembaca kode QR 2FA", "cardDesc": "Ambil kunci rahasia dari kode QR 2FA apa pun, termasuk ekspor Google Authenticator.",
 "i18n": {"copied": "Disalin", "copy": "Salin", "copyUri": "Salin tautan otpauth", "openGen": "Lihat kode", "issuer": "Penerbit", "account": "Akun",
          "secret": "Kunci rahasia", "settings": "Pengaturan", "found": "Ditemukan {n} akun.", "reading": "Membaca gambar…",
          "qrNotFound": "Tidak ada kode QR 2FA di gambar ini. Coba tangkapan layar yang lebih tajam dan menampilkan seluruh kode.",
          "qrUnsupported": "Gagal memuat pembaca QR. Periksa koneksi lalu coba lagi."},
 "ui": {"aria": "Pembaca QR", "dropB": "Seret gambar kode QR ke sini", "dropS": "atau klik untuk memilih file · atau tekan Ctrl+V untuk menempel tangkapan layar",
        "link": "…atau tempel tautan otpauth:// atau otpauth-migration://", "hint": "Gambar dibaca di perangkat Anda dan tidak pernah diunggah."},
 "content": f"""
    <h2>Kapan ini berguna?</h2>
    <ul>
    <li>Anda punya tangkapan layar kode QR 2FA dan ingin menyimpan kuncinya di pengelola kata sandi.</li>
    <li>Anda mengekspor akun dari Google Authenticator dan ingin kunci aslinya, bukan sekadar memindahkannya ke ponsel lain.</li>
    <li>Anda developer yang ingin melihat isi sebenarnya dari kode QR aplikasi Anda.</li>
    </ul>
    <h2>Kode ekspor Google Authenticator</h2>
    <p>Layar <em>Transfer akun → Ekspor akun</em> membuat kode QR dalam format khusus, <code class="k">otpauth-migration://</code>, yang memuat beberapa akun. Pembaca ini mendekodenya dan menampilkan setiap akun beserta kuncinya. Lihat <a href="{G}pindah-google-authenticator-ke-hp-baru">cara memindahkan Google Authenticator</a>.</p>
    <h2>Privasi</h2>
    <p>Dekode memakai pembaca barcode bawaan browser atau pustaka sumber terbuka yang dimuat dari situs ini. Hapus tangkapan layarnya setelah selesai: siapa pun yang memilikinya bisa membuat kode Anda.</p>"""},
}

GUIDES = {
"find-key": {
 "slug": "cara-menemukan-kunci-rahasia-2fa",
 "title": "Di Mana Menemukan Kunci Rahasia 2FA (Google, Facebook, Instagram, Microsoft)",
 "desc": "Pelajari apa itu kunci rahasia 2FA dan di mana menemukannya saat mengaktifkan verifikasi dua langkah di Google, Facebook, Instagram, Microsoft, dan situs lain.",
 "h1": "Di mana menemukan kunci rahasia 2FA",
 "lead": "Kunci rahasia adalah versi teks dari kode QR yang Anda pindai saat mengaktifkan verifikasi dua langkah. Simpan sekali, dan Anda bisa membuat ulang kode di perangkat mana pun.",
 "body": """
<h2>Apa itu kunci rahasia 2FA?</h2>
<p>Saat Anda memilih “aplikasi autentikasi” sebagai metode 2FA, situs membuat rahasia acak dan membagikannya ke aplikasi Anda. Aplikasi menggabungkan rahasia itu dengan waktu saat ini untuk membuat kode 6 digit baru setiap 30 detik. Metode ini disebut TOTP (kata sandi sekali pakai berbasis waktu).</p>
<p>Rahasia biasanya ditampilkan dengan dua cara: sebagai <strong>kode QR</strong> dan sebagai <strong>kunci teks</strong> sepanjang 16–32 karakter, berisi huruf A–Z dan angka 2–7, misalnya <code class="k">JBSW Y3DP EHPK 3PXP</code>. Keduanya berisi informasi yang persis sama.</p>
<h2>Di mana setiap situs menampilkan kunci</h2>
<p>Kebanyakan situs menyembunyikan kunci teks di balik tautan di bawah kode QR. Cari tulisan seperti <em>“Tidak bisa memindai?”</em>, <em>“Masukkan kunci secara manual”</em>, <em>“Salin kunci”</em>, atau <em>“Kunci penyiapan”</em>.</p>
<h3>Google</h3>
<p>Buka Akun Google, masuk ke <strong>Keamanan → Verifikasi 2 Langkah → Authenticator</strong>, lalu pilih untuk menyiapkan aplikasi autentikator. Di bawah kode QR, ketuk <strong>“Tidak bisa memindai?”</strong> untuk melihat kunci.</p>
<h3>Facebook</h3>
<p>Buka <strong>Pengaturan &amp; privasi → Pengaturan → Pusat Akun → Kata sandi dan keamanan → Autentikasi dua faktor</strong>, pilih akun Anda, lalu pilih <strong>Aplikasi autentikasi</strong>. Kunci muncul dengan tombol <strong>Salin kunci</strong> di samping kode QR.</p>
<h3>Instagram</h3>
<p>Di aplikasi, buka profil, ketuk menu, lalu <strong>Pusat Akun → Kata sandi dan keamanan → Autentikasi dua faktor</strong>, pilih akun dan pilih <strong>Aplikasi autentikasi</strong>. Ketuk <strong>Salin kunci</strong>. Instagram hanya mengizinkan metode ini diaktifkan dari aplikasi Android atau iPhone.</p>
<h3>Microsoft</h3>
<p>Saat menambahkan aplikasi autentikator, pilih untuk memakai aplikasi lain lalu <strong>“Tidak bisa memindai gambar?”</strong>. Microsoft menampilkan kode rahasia di halaman itu.</p>
<h3>Situs lain (Discord, X, Amazon, GitHub…)</h3>
<p>Alurnya hampir selalu sama: pilih opsi aplikasi autentikator, lalu cari tautan untuk memasukkan kunci secara manual.</p>
<h2>Sudah mengaktifkan 2FA tanpa menyimpan kunci?</h2>
<p>Kebanyakan situs tidak menampilkan kunci lagi. Jika Anda membutuhkannya, nonaktifkan lalu aktifkan lagi metode aplikasi (atau gunakan “tambah perangkat lain”), dan kali ini simpan kunci barunya. Perbarui juga aplikasi autentikator, karena kunci lama berhenti berfungsi.</p>
<h2>Cara menyimpan kunci dengan aman</h2>
<ul>
<li>Simpan di pengelola kata sandi (Bitwarden, 1Password, dll.) di entri yang sama dengan akunnya.</li>
<li>Jangan pernah mengirimnya lewat email atau chat, dan jangan unggah tangkapan layar kode QR.</li>
<li>Siapa pun yang memiliki kunci bisa membuat kode Anda, jadi perlakukan seperti kata sandi.</li>
</ul>
"""},
"transfer": {
 "slug": "pindah-google-authenticator-ke-hp-baru",
 "title": "Cara Memindahkan Google Authenticator ke HP Baru (dan Mengambil Kuncinya)",
 "desc": "Pindahkan kode Google Authenticator ke HP baru dengan sinkronisasi cloud atau kode QR Ekspor akun, lalu ambil kunci rahasia dari QR ekspor dengan Get2FA.",
 "h1": "Cara memindahkan Google Authenticator ke HP baru",
 "lead": "Ada dua cara memindahkan kode: masuk ke akun Google agar tersinkron, atau ekspor dengan kode QR. Get2FA juga bisa membaca QR ekspor itu dan menampilkan setiap kunci rahasia.",
 "body": f"""
<h2>Cara 1: sinkronisasi cloud (paling mudah)</h2>
<ol>
<li>Di HP lama, buka Google Authenticator dan ketuk ikon profil.</li>
<li>Masuk dengan Akun Google dan aktifkan sinkronisasi. Ikon awan kecil menandakan cadangan berhasil.</li>
<li>Di HP baru, pasang Google Authenticator dan masuk dengan Akun Google yang sama. Kode Anda muncul otomatis.</li>
</ol>
<p>Sinkronisasi memang praktis, tetapi kunci 2FA Anda jadi tersimpan di Akun Google. Lindungi akun itu dengan baik.</p>
<h2>Cara 2: Ekspor akun (offline)</h2>
<ol>
<li>Di HP lama, buka menu lalu <strong>Transfer akun → Ekspor akun</strong>.</li>
<li>Pilih akun-akunnya dan ketuk <strong>Berikutnya</strong>. Aplikasi menampilkan satu atau beberapa kode QR.</li>
<li>Di HP baru, buka <strong>Transfer akun → Impor akun → Pindai kode QR</strong> dan pindai setiap kode.</li>
</ol>
<p>Ekspor ini bisa dipakai antara Android dan iPhone, dua arah.</p>
<h2>Ambil kunci rahasia dari QR ekspor</h2>
<p>QR ekspor memakai format khusus (<code class="k">otpauth-migration://</code>) yang sering tidak terbaca aplikasi lain. <a href="{H}">Get2FA</a> bisa membacanya: ambil tangkapan layar QR ekspor (di ponsel yang Anda percaya), lalu tempel atau seret gambarnya ke Get2FA. Setiap akun muncul dengan nama dan kode langsungnya, dan daftar menampilkan tautan <code class="k">otpauth://</code> lengkap dengan kuncinya. Simpan di pengelola kata sandi.</p>
<p>Semua didekode di browser Anda; gambar dan kunci tidak pernah diunggah. Hapus tangkapan layarnya setelah itu.</p>
<h2>Jangan reset HP lama terlalu cepat</h2>
<p>Coba masuk ke beberapa akun di HP baru sebelum mereset HP lama. Jika ada masalah setelah HP lama hilang, Anda butuh kode cadangan atau proses pemulihan dari setiap situs.</p>
"""},
"not-working": {
 "slug": "kode-2fa-tidak-berfungsi",
 "title": "Kode 2FA Tidak Berfungsi? 7 Penyebab dan Cara Mengatasinya",
 "desc": "Kode autentikator terus ditolak? Pelajari penyebab paling umum, dari jam perangkat yang salah hingga kunci yang keliru, dan cara mengatasi masing-masing.",
 "h1": "Kode 2FA tidak berfungsi? Begini cara mengatasinya",
 "lead": "Saat situs menyebut kode 2FA Anda tidak valid, penyebabnya hampir selalu salah satu dari daftar ini. Mulailah dari yang pertama: itu menyelesaikan sebagian besar kasus.",
 "body": f"""
<h2>1. Jam perangkat Anda meleset</h2>
<p>Kode TOTP dihitung dari waktu saat ini. Jika jam ponsel atau komputer meleset lebih dari sekitar 30 detik, kode tidak akan cocok. Aktifkan <strong>tanggal dan waktu otomatis</strong> (dan zona waktu otomatis) di pengaturan, lalu coba kode baru. Anda bisa mengeceknya dengan <a href="{H}cek-kode-2fa">pengecek kode 2FA</a>.</p>
<h2>2. Kode kedaluwarsa saat Anda mengetik</h2>
<p>Setiap kode berlaku 30 detik dan beberapa situs menolaknya tepat di akhir. Tunggu kode baru. Get2FA menampilkan sisa detik dan kode berikutnya, jadi Anda bisa memilih waktu yang tepat.</p>
<h2>3. Kunci atau akunnya salah</h2>
<p>Jika Anda menyiapkan 2FA lebih dari sekali, hanya kunci terakhir yang berlaku. Pastikan entri di aplikasi milik akun yang sama (lihat nama dan email) dan kunci tersalin lengkap.</p>
<h2>4. Situs memakai pengaturan berbeda</h2>
<p>Hampir semua situs memakai 6 digit, 30 detik, dan SHA-1. Beberapa memakai 8 digit, 60 detik, atau SHA-256. Jika kode QR memuat pengaturan ini, aplikasi membacanya otomatis. Untuk kunci teks, atur di <em>Pengaturan lanjutan</em> Get2FA.</p>
<h2>5. Kunci salah ketik</h2>
<p>Kunci rahasia hanya memakai huruf A–Z dan angka 2–7. Angka 0, 1, 8, dan 9 tidak pernah muncul, jadi “0” sebenarnya huruf O dan “1” adalah huruf I atau L. Salin dan tempel jika memungkinkan.</p>
<h2>6. Kode sudah dipakai</h2>
<p>Beberapa situs hanya menerima setiap kode sekali. Jika baru saja memakai sebuah kode, tunggu kode berikutnya.</p>
<h2>7. 2FA diatur ulang di situs</h2>
<p>Jika Anda (atau tim dukungan) mematikan lalu menyalakan lagi 2FA, kunci lama tidak berlaku. Masuk dengan kode cadangan dan siapkan ulang autentikator.</p>
<h2>Masih tidak bisa masuk?</h2>
<p>Gunakan kode cadangan atau kode pemulihan yang diberikan situs, atau mulai proses pemulihan akun. Lihat <a href="hp-hilang-aplikasi-autentikator">apa yang harus dilakukan jika HP hilang</a>.</p>
"""},
"lost-phone": {
 "slug": "hp-hilang-aplikasi-autentikator",
 "title": "HP dengan Aplikasi Autentikator Hilang? Ini yang Harus Dilakukan",
 "desc": "HP berisi kode 2FA hilang, dicuri, atau direset? Cara kembali masuk ke akun dengan kunci yang disimpan, kode cadangan, sinkronisasi cloud, atau pemulihan akun.",
 "h1": "HP dengan autentikator hilang? Ini yang harus dilakukan",
 "lead": "Kehilangan HP yang menyimpan kode 2FA memang bikin panik, tetapi biasanya masih ada jalan masuk. Coba opsi-opsi ini secara berurutan.",
 "body": f"""
<h2>1. Apakah Anda menyimpan kunci rahasia?</h2>
<p>Jika Anda menyimpan kunci penyiapan (di pengelola kata sandi, catatan, atau cetakan), Anda beruntung: tempel setiap kunci ke <a href="{H}">Get2FA</a> dan kode langsung bisa dipakai, di perangkat mana pun. Lalu tambahkan kunci ke autentikator di HP baru.</p>
<h2>2. Apakah sinkronisasi cloud aktif?</h2>
<p>Google Authenticator (saat masuk akun), Microsoft Authenticator, 2FAS, dan lainnya bisa mencadangkan kode. Pasang aplikasi yang sama di HP baru dan masuk dengan akun yang sama untuk memulihkannya.</p>
<h2>3. Gunakan kode cadangan</h2>
<p>Kebanyakan situs memberi kode cadangan atau pemulihan sekali pakai saat Anda mengaktifkan 2FA (Google, Facebook, Instagram, dan GitHub semuanya begitu). Setiap kode bisa dipakai masuk sekali. Setelah masuk, siapkan lagi 2FA di HP baru.</p>
<h2>4. Gunakan metode 2FA lain</h2>
<p>Jika Anda juga menambahkan SMS, kunci keamanan, passkey, atau perangkat tepercaya lain, gunakan itu untuk masuk.</p>
<h2>5. Mulai pemulihan akun</h2>
<p>Sebagai upaya terakhir, gunakan opsi “Tidak bisa mengakses kode?” atau pemulihan akun dari situs. Prosesnya bisa memakan waktu beberapa hari dan biasanya butuh bukti identitas, jadi mulailah lebih awal.</p>
<h2>Setelah berhasil masuk</h2>
<ul>
<li>Siapkan lagi 2FA dan kali ini <strong>simpan setiap kunci baru</strong> di pengelola kata sandi.</li>
<li>Simpan kode cadangan baru di luar HP.</li>
<li>Jika HP dicuri, ganti kata sandi akun-akun penting dan hapus perangkat lama dari akun Anda.</li>
</ul>
"""},
}
