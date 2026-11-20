# -*- coding: utf-8 -*-
H = "/vi/"
G = "/vi/huong-dan/"

TOOLS = {
"gen": {
 "path": "/vi/tao-khoa-2fa",
 "title": "Tạo khóa bí mật 2FA và mã QR (TOTP) – Miễn phí, ngay trên trình duyệt",
 "desc": "Tạo khóa bí mật 2FA ngẫu nhiên, liên kết otpauth:// và mã QR cho Google Authenticator và mọi ứng dụng TOTP. Tạo trên thiết bị của bạn bằng Web Crypto.",
 "h1": "Tạo khóa bí mật 2FA và mã QR",
 "sub": "Tạo khóa TOTP ngẫu nhiên, liên kết otpauth:// và mã QR mà mọi ứng dụng xác thực đều quét được. Phù hợp cho lập trình viên kiểm thử 2FA hoặc thiết lập ứng dụng riêng.",
 "card": "Tạo khóa và mã QR", "cardDesc": "Tạo khóa 2FA ngẫu nhiên và mã QR cho mọi ứng dụng xác thực.",
 "i18n": {"copied": "Đã sao chép"},
 "ui": {"aria": "Trình tạo khóa", "issuer": "Nhà phát hành (tên ứng dụng hoặc trang web)", "issuerPh": "UngDungCuaToi", "account": "Tài khoản (tên người dùng hoặc email)", "accountPh": "lan@vidu.com",
        "keyLen": "Độ dài khóa", "opt80": "80 bit (16 ký tự)", "opt160": "160 bit (32 ký tự, khuyến nghị)", "opt256": "256 bit (52 ký tự)",
        "newKey": "Khóa mới", "secret": "Khóa bí mật", "uri": "Liên kết otpauth://", "copy": "Sao chép", "copyLink": "Sao chép liên kết", "dl": "Tải mã QR (SVG)",
        "openGen": "Mở trong trình tạo mã", "current": "Mã hiện tại",
        "hint": "Khóa được tạo bằng bộ sinh số ngẫu nhiên an toàn của trình duyệt và không bao giờ rời khỏi trang này."},
 "content": """
    <h2>Cách sử dụng</h2>
    <ol class="steps"><li><b>Đặt tên</b>Nhập nhà phát hành (ứng dụng hoặc trang web) và tài khoản. Đây là tên hiển thị trong ứng dụng xác thực.</li><li><b>Quét hoặc sao chép</b>Quét mã QR bằng Google Authenticator, Microsoft Authenticator, 2FAS hoặc bất kỳ ứng dụng TOTP nào, hoặc sao chép liên kết otpauth://.</li><li><b>Kiểm tra mã</b>Mã hiện tại cập nhật trực tiếp để bạn xác nhận ứng dụng hiển thị cùng một số.</li></ol>
    <h2>Liên kết otpauth:// là gì?</h2>
    <p>Đây là định dạng chuẩn mà ứng dụng xác thực đọc từ mã QR: <code class="k">otpauth://totp/NhaPhatHanh:taikhoan?secret=KHOA&amp;issuer=NhaPhatHanh</code>. Các tham số tùy chọn đặt thuật toán, số chữ số và chu kỳ. Hầu hết dịch vụ dùng SHA-1, 6 chữ số và 30 giây, cũng là giá trị mặc định ở đây.</p>
    <h2>Tạo khóa online có an toàn không?</h2>
    <p>Khóa được tạo bằng <code class="k">crypto.getRandomValues</code> trong trình duyệt và không có gì được tải lên. Với hệ thống thật, hãy tạo khóa trên máy chủ của bạn và lưu dạng mã hóa; dùng công cụ này để thử nghiệm, làm mẫu hoặc cho tài khoản cá nhân.</p>
    <h2>Nên chọn độ dài khóa nào?</h2>
    <p>160 bit (32 ký tự Base32) là mức RFC 4226 khuyến nghị và được đa số dịch vụ dùng. 80 bit là mức tối thiểu một số ứng dụng cũ chấp nhận; 256 bit dùng được với ứng dụng hiện đại.</p>"""},
"check": {
 "path": "/vi/kiem-tra-ma-2fa",
 "title": "Check mã 2FA – Kiểm tra mã 2FA đúng hay sai và đồng hồ thiết bị",
 "desc": "Dán khóa 2FA và mã ứng dụng hiển thị để xem có khớp không, đồng thời kiểm tra đồng hồ thiết bị có bị lệch. Tìm ra lý do mã xác thực không hoạt động.",
 "h1": "Check mã 2FA và đồng hồ thiết bị",
 "sub": "Dán khóa bí mật và mã mà ứng dụng xác thực hiển thị. Chúng tôi cho bạn biết mã có khớp không, và đồng hồ thiết bị có phải là lý do mã bị từ chối.",
 "card": "Kiểm tra mã 2FA", "cardDesc": "Xem mã có khớp với khóa không và đồng hồ thiết bị có bị lệch không.",
 "i18n": {"copied": "Đã sao chép", "clockOk": "✓ Đồng hồ thiết bị của bạn chính xác (lệch dưới 2 giây).",
          "clockAhead": "⚠ Đồng hồ thiết bị đang nhanh khoảng {n} giây. Hãy bật ngày giờ tự động.",
          "clockBehind": "⚠ Đồng hồ thiết bị đang chậm khoảng {n} giây. Hãy bật ngày giờ tự động.",
          "clockUnknown": "Hiện không kiểm tra được đồng hồ của bạn.",
          "badKey": "Đây không giống khóa bí mật 2FA hợp lệ.", "badCode": "Nhập mã {n} chữ số từ ứng dụng của bạn.",
          "match": "✓ Mã khớp với mã hiện tại. Ứng dụng và khóa của bạn đều đúng.",
          "matchPast": "⚠ Mã khớp với mã của {s} giây trước. Có thể đồng hồ thiết bị đang chậm, hoặc mã đã cũ.",
          "matchFuture": "⚠ Mã khớp với mã của {s} giây sau. Thiết bị tạo mã có đồng hồ chạy nhanh.",
          "noMatch": "✗ Không khớp trong khoảng ±5 phút. Khóa, tài khoản hoặc cài đặt (số chữ số, chu kỳ, thuật toán) khác nhau.",
          "expected": "Mã hiện tại của khóa này:"},
 "ui": {"aria": "Kiểm tra mã", "checking": "Đang kiểm tra đồng hồ…", "secret": "Khóa bí mật", "code": "Mã từ ứng dụng", "check": "Kiểm tra mã"},
 "content": f"""
    <h2>Ý nghĩa kết quả</h2>
    <ul>
    <li><b>Khớp với mã hiện tại:</b> khóa và ứng dụng đều ổn. Nếu trang web vẫn từ chối, có thể họ dùng khóa khác (2FA đã được đặt lại) hoặc mã hết hạn khi bạn đang nhập.</li>
    <li><b>Khớp với mã trước hoặc sau:</b> một trong các đồng hồ bị lệch. Hãy bật ngày giờ tự động trên điện thoại chạy ứng dụng xác thực.</li>
    <li><b>Không khớp:</b> khóa thuộc tài khoản khác, bị sao chép thiếu, hoặc trang web dùng 8 chữ số, 60 giây hay SHA-256.</li>
    </ul>
    <h2>Cách kiểm tra đồng hồ hoạt động</h2>
    <p>Chúng tôi so sánh giờ trên thiết bị của bạn với giờ máy chủ báo về trong một yêu cầu tải trang thông thường. Mã TOTP đổi mỗi 30 giây, nên chỉ lệch vài giây cũng đủ làm mã bị từ chối.</p>
    <p>Vẫn chưa được? Đọc <a href="{G}ma-2fa-khong-hoat-dong">Mã 2FA không hoạt động: 7 nguyên nhân</a>.</p>"""},
"read": {
 "path": "/vi/doc-ma-qr-2fa",
 "title": "Đọc mã QR 2FA – Lấy khóa bí mật (kể cả mã xuất từ Google Authenticator)",
 "desc": "Tải lên hoặc dán ảnh chụp mã QR 2FA để lấy khóa bí mật và liên kết otpauth. Đọc được cả mã QR xuất từ Google Authenticator (otpauth-migration). Chạy trong trình duyệt.",
 "h1": "Đọc mã QR 2FA và lấy khóa bí mật",
 "sub": "Kéo, dán hoặc tải lên ảnh chụp mã QR 2FA. Bạn sẽ có khóa bí mật, nhà phát hành, tài khoản và cài đặt, kể cả từ mã xuất của Google Authenticator.",
 "card": "Đọc mã QR 2FA", "cardDesc": "Lấy khóa bí mật từ mọi mã QR 2FA, kể cả mã xuất từ Google Authenticator.",
 "i18n": {"copied": "Đã sao chép", "copy": "Sao chép", "copyUri": "Sao chép liên kết otpauth", "openGen": "Xem mã", "issuer": "Nhà phát hành", "account": "Tài khoản",
          "secret": "Khóa bí mật", "settings": "Cài đặt", "found": "Tìm thấy {n} tài khoản.", "reading": "Đang đọc ảnh…",
          "qrNotFound": "Không tìm thấy mã QR 2FA trong ảnh. Hãy thử ảnh chụp rõ hơn, hiển thị toàn bộ mã.",
          "qrUnsupported": "Không tải được trình đọc QR. Kiểm tra kết nối rồi thử lại."},
 "ui": {"aria": "Đọc mã QR", "dropB": "Kéo ảnh mã QR vào đây", "dropS": "hoặc bấm để chọn tệp · hoặc nhấn Ctrl+V để dán ảnh chụp",
        "link": "…hoặc dán liên kết otpauth:// hay otpauth-migration://", "hint": "Ảnh được đọc trên thiết bị của bạn và không bao giờ được tải lên."},
 "content": f"""
    <h2>Khi nào công cụ này hữu ích?</h2>
    <ul>
    <li>Bạn có ảnh chụp mã QR 2FA và muốn lưu khóa vào trình quản lý mật khẩu.</li>
    <li>Bạn đã xuất tài khoản từ Google Authenticator và muốn lấy khóa thật, không chỉ chuyển sang điện thoại khác.</li>
    <li>Bạn là lập trình viên và muốn xem mã QR của ứng dụng thực sự chứa gì.</li>
    </ul>
    <h2>Mã xuất từ Google Authenticator</h2>
    <p>Màn hình <em>Chuyển tài khoản → Xuất tài khoản</em> tạo mã QR theo định dạng đặc biệt <code class="k">otpauth-migration://</code> chứa nhiều tài khoản. Công cụ này giải mã và liệt kê từng tài khoản kèm khóa. Xem <a href="{G}chuyen-google-authenticator-sang-dien-thoai-moi">cách chuyển Google Authenticator</a>.</p>
    <h2>Quyền riêng tư</h2>
    <p>Việc giải mã dùng trình đọc mã vạch có sẵn của trình duyệt hoặc một thư viện mã nguồn mở tải từ chính trang này. Hãy xóa ảnh chụp sau khi xong: ai có ảnh đều tạo được mã của bạn.</p>"""},
}

GUIDES = {
"find-key": {
 "slug": "tim-khoa-bi-mat-2fa",
 "title": "Tìm khóa bí mật 2FA ở đâu (Google, Facebook, Instagram, Microsoft)",
 "desc": "Khóa bí mật 2FA là gì và tìm nó ở đâu khi bật xác minh 2 bước trên Google, Facebook, Instagram, Microsoft và các trang khác.",
 "h1": "Tìm khóa bí mật 2FA ở đâu",
 "lead": "Khóa bí mật là phiên bản dạng chữ của mã QR bạn quét khi bật xác minh 2 bước. Lưu nó một lần là bạn có thể tạo lại mã trên bất kỳ thiết bị nào.",
 "body": """
<h2>Khóa bí mật 2FA là gì?</h2>
<p>Khi bạn chọn “ứng dụng xác thực” làm phương thức 2FA, trang web tạo ra một chuỗi bí mật ngẫu nhiên và chia sẻ với ứng dụng của bạn. Ứng dụng kết hợp chuỗi đó với thời gian hiện tại để tạo mã 6 số mới sau mỗi 30 giây. Phương thức này gọi là TOTP (mật khẩu dùng một lần theo thời gian).</p>
<p>Chuỗi bí mật thường hiển thị theo hai cách: <strong>mã QR</strong> và <strong>khóa dạng chữ</strong> dài 16–32 ký tự, gồm chữ A–Z và số 2–7, ví dụ <code class="k">JBSW Y3DP EHPK 3PXP</code>. Cả hai chứa đúng cùng một thông tin.</p>
<h2>Mỗi trang hiển thị khóa ở đâu</h2>
<p>Đa số trang giấu khóa dạng chữ sau một liên kết bên dưới mã QR. Hãy tìm các cụm như <em>“Không quét được?”</em>, <em>“Nhập khóa thủ công”</em>, <em>“Sao chép khóa”</em> hoặc <em>“Khóa thiết lập”</em>.</p>
<h3>Google</h3>
<p>Mở Tài khoản Google, vào <strong>Bảo mật → Xác minh 2 bước → Authenticator</strong> và chọn thiết lập ứng dụng xác thực. Bên dưới mã QR, chạm <strong>“Không quét được mã?”</strong> để xem khóa.</p>
<h3>Facebook</h3>
<p>Vào <strong>Cài đặt và quyền riêng tư → Cài đặt → Trung tâm tài khoản → Mật khẩu và bảo mật → Xác thực 2 yếu tố</strong>, chọn tài khoản rồi chọn <strong>Ứng dụng xác thực</strong>. Khóa hiển thị cùng nút <strong>Sao chép khóa</strong> cạnh mã QR.</p>
<h3>Instagram</h3>
<p>Trong ứng dụng, mở trang cá nhân, chạm menu rồi vào <strong>Trung tâm tài khoản → Mật khẩu và bảo mật → Xác thực 2 yếu tố</strong>, chọn tài khoản và chọn <strong>Ứng dụng xác thực</strong>. Chạm <strong>Sao chép khóa</strong>. Instagram chỉ cho bật phương thức này từ ứng dụng Android hoặc iPhone.</p>
<h3>Microsoft</h3>
<p>Khi thêm ứng dụng xác thực, chọn dùng ứng dụng khác rồi chọn <strong>“Không quét được hình ảnh?”</strong>. Microsoft hiển thị mã bí mật trên trang đó.</p>
<h3>Các trang khác (Discord, X, Amazon, GitHub…)</h3>
<p>Quy trình gần như giống nhau: chọn tùy chọn ứng dụng xác thực rồi tìm liên kết cho phép nhập khóa thủ công.</p>
<h2>Đã bật 2FA mà chưa lưu khóa?</h2>
<p>Đa số trang không hiển thị lại khóa. Nếu cần, hãy tắt rồi bật lại phương thức ứng dụng (hoặc dùng “thêm thiết bị khác”) và lần này lưu khóa mới. Nhớ cập nhật cả ứng dụng xác thực, vì khóa cũ sẽ ngừng hoạt động.</p>
<h2>Cách lưu khóa an toàn</h2>
<ul>
<li>Lưu trong trình quản lý mật khẩu (Bitwarden, 1Password…) cùng mục với tài khoản.</li>
<li>Không bao giờ gửi khóa qua email hay tin nhắn, và không đăng ảnh chụp mã QR.</li>
<li>Ai có khóa đều tạo được mã của bạn, nên hãy coi nó như mật khẩu.</li>
</ul>
"""},
"transfer": {
 "slug": "chuyen-google-authenticator-sang-dien-thoai-moi",
 "title": "Cách chuyển Google Authenticator sang điện thoại mới (và lấy khóa bí mật)",
 "desc": "Chuyển mã Google Authenticator sang điện thoại mới bằng đồng bộ đám mây hoặc mã QR Xuất tài khoản, và lấy khóa bí mật từ mã QR xuất bằng Get2FA.",
 "h1": "Cách chuyển Google Authenticator sang điện thoại mới",
 "lead": "Có hai cách chuyển mã: đăng nhập Google để đồng bộ, hoặc xuất bằng mã QR. Get2FA còn đọc được mã QR xuất đó và hiển thị từng khóa bí mật.",
 "body": f"""
<h2>Cách 1: đồng bộ đám mây (dễ nhất)</h2>
<ol>
<li>Trên điện thoại cũ, mở Google Authenticator và chạm vào biểu tượng hồ sơ.</li>
<li>Đăng nhập Tài khoản Google và bật đồng bộ. Biểu tượng đám mây nhỏ xác nhận đã sao lưu.</li>
<li>Trên điện thoại mới, cài Google Authenticator và đăng nhập cùng Tài khoản Google. Mã sẽ tự hiện ra.</li>
</ol>
<p>Đồng bộ rất tiện, nhưng khóa 2FA khi đó được lưu trong Tài khoản Google. Hãy bảo vệ tài khoản đó thật kỹ.</p>
<h2>Cách 2: Xuất tài khoản (không cần mạng)</h2>
<ol>
<li>Trên điện thoại cũ, mở menu và vào <strong>Chuyển tài khoản → Xuất tài khoản</strong>.</li>
<li>Chọn các tài khoản rồi chạm <strong>Tiếp theo</strong>. Ứng dụng hiển thị một hoặc nhiều mã QR.</li>
<li>Trên điện thoại mới, vào <strong>Chuyển tài khoản → Nhập tài khoản → Quét mã QR</strong> và quét từng mã.</li>
</ol>
<p>Cách xuất hoạt động giữa Android và iPhone theo cả hai chiều.</p>
<h2>Lấy khóa bí mật từ mã QR xuất</h2>
<p>Mã QR xuất dùng định dạng đặc biệt (<code class="k">otpauth-migration://</code>) mà nhiều ứng dụng khác không đọc được. <a href="{H}">Get2FA</a> thì đọc được: chụp màn hình mã QR (trên điện thoại bạn tin tưởng), rồi dán hoặc kéo ảnh vào Get2FA. Mỗi tài khoản hiện ra kèm tên và mã trực tiếp, danh sách hiển thị đầy đủ liên kết <code class="k">otpauth://</code> có khóa. Hãy lưu chúng vào trình quản lý mật khẩu.</p>
<p>Mọi thứ được giải mã trong trình duyệt; ảnh và khóa không bao giờ bị tải lên. Xóa ảnh chụp sau đó.</p>
<h2>Đừng xóa điện thoại cũ quá sớm</h2>
<p>Hãy thử đăng nhập vài tài khoản trên điện thoại mới trước khi đặt lại điện thoại cũ. Nếu có sự cố khi không còn điện thoại cũ, bạn sẽ cần mã dự phòng hoặc quy trình khôi phục của từng trang.</p>
"""},
"not-working": {
 "slug": "ma-2fa-khong-hoat-dong",
 "title": "Mã 2FA không hoạt động? 7 nguyên nhân và cách khắc phục",
 "desc": "Mã xác thực liên tục bị từ chối? Tìm hiểu các nguyên nhân phổ biến, từ đồng hồ thiết bị lệch đến sai khóa, và cách xử lý từng trường hợp.",
 "h1": "Mã 2FA không hoạt động? Đây là cách khắc phục",
 "lead": "Khi trang web báo mã 2FA không hợp lệ, nguyên nhân gần như luôn là một trong số này. Hãy bắt đầu từ mục đầu tiên: nó giải quyết phần lớn trường hợp.",
 "body": f"""
<h2>1. Đồng hồ thiết bị bị lệch</h2>
<p>Mã TOTP được tính từ thời gian hiện tại. Nếu đồng hồ điện thoại hoặc máy tính lệch quá khoảng 30 giây, mã sẽ không khớp. Bật <strong>ngày giờ tự động</strong> (và múi giờ tự động) trong cài đặt rồi thử mã mới. Bạn có thể kiểm tra bằng <a href="{H}kiem-tra-ma-2fa">công cụ kiểm tra mã 2FA</a>.</p>
<h2>2. Mã hết hạn khi bạn đang nhập</h2>
<p>Mỗi mã chỉ có hiệu lực 30 giây và một số trang từ chối mã ở những giây cuối. Hãy chờ mã mới. Get2FA hiển thị số giây còn lại và mã kế tiếp để bạn chọn đúng lúc.</p>
<h2>3. Dùng sai khóa hoặc sai tài khoản</h2>
<p>Nếu bạn đã thiết lập 2FA nhiều lần, chỉ khóa cuối cùng còn hiệu lực. Hãy chắc chắn mục trong ứng dụng thuộc đúng tài khoản (xem tên và email) và bạn đã sao chép đủ khóa.</p>
<h2>4. Trang web dùng cài đặt khác</h2>
<p>Hầu hết trang dùng 6 chữ số, 30 giây và SHA-1. Một số dùng 8 chữ số, 60 giây hoặc SHA-256. Nếu mã QR có các cài đặt này, ứng dụng sẽ tự đọc. Với khóa dạng chữ, hãy chỉnh trong <em>Cài đặt nâng cao</em> của Get2FA.</p>
<h2>5. Nhập sai khóa</h2>
<p>Khóa bí mật chỉ dùng chữ A–Z và số 2–7. Các số 0, 1, 8 và 9 không bao giờ xuất hiện, nên “0” thực ra là chữ O và “1” là chữ I hoặc L. Hãy sao chép và dán thay vì gõ tay khi có thể.</p>
<h2>6. Mã đã được dùng</h2>
<p>Một số trang chỉ chấp nhận mỗi mã một lần. Nếu vừa dùng một mã, hãy chờ mã tiếp theo.</p>
<h2>7. 2FA đã bị đặt lại trên trang</h2>
<p>Nếu bạn (hoặc bộ phận hỗ trợ) đã tắt rồi bật lại 2FA, khóa cũ không còn dùng được. Hãy đăng nhập bằng mã dự phòng và thiết lập lại ứng dụng xác thực.</p>
<h2>Vẫn không vào được?</h2>
<p>Dùng mã dự phòng hoặc mã khôi phục mà trang đã cấp, hoặc bắt đầu quy trình khôi phục tài khoản. Xem <a href="mat-dien-thoai-ung-dung-xac-thuc">phải làm gì khi mất điện thoại</a>.</p>
"""},
"lost-phone": {
 "slug": "mat-dien-thoai-ung-dung-xac-thuc",
 "title": "Mất điện thoại có ứng dụng xác thực? Cần làm gì ngay",
 "desc": "Điện thoại chứa mã 2FA bị mất, bị trộm hoặc bị đặt lại? Cách vào lại tài khoản bằng khóa đã lưu, mã dự phòng, đồng bộ đám mây hoặc khôi phục tài khoản.",
 "h1": "Mất điện thoại có ứng dụng xác thực? Cần làm gì",
 "lead": "Mất điện thoại chứa mã 2FA rất căng thẳng, nhưng thường vẫn có cách vào lại. Hãy thử lần lượt các cách sau.",
 "body": f"""
<h2>1. Bạn có lưu khóa bí mật không?</h2>
<p>Nếu bạn còn giữ các khóa thiết lập (trong trình quản lý mật khẩu, ghi chú hoặc bản in), bạn rất may mắn: dán từng khóa vào <a href="{H}">Get2FA</a> là có mã dùng được ngay trên mọi thiết bị. Sau đó thêm khóa vào ứng dụng xác thực trên điện thoại mới.</p>
<h2>2. Bạn có bật đồng bộ đám mây không?</h2>
<p>Google Authenticator (khi đã đăng nhập), Microsoft Authenticator, 2FAS và nhiều ứng dụng khác có thể sao lưu mã. Cài cùng ứng dụng trên điện thoại mới và đăng nhập cùng tài khoản để khôi phục.</p>
<h2>3. Dùng mã dự phòng</h2>
<p>Hầu hết trang cấp mã dự phòng hoặc mã khôi phục dùng một lần khi bạn bật 2FA (Google, Facebook, Instagram và GitHub đều có). Mỗi mã cho bạn đăng nhập một lần. Sau khi vào được, hãy thiết lập lại 2FA trên điện thoại mới.</p>
<h2>4. Dùng phương thức 2FA khác</h2>
<p>Nếu bạn đã thêm SMS, khóa bảo mật, passkey hoặc thiết bị tin cậy khác, hãy dùng nó để đăng nhập.</p>
<h2>5. Bắt đầu khôi phục tài khoản</h2>
<p>Cách cuối cùng là dùng tùy chọn “Không truy cập được mã?” hoặc khôi phục tài khoản của trang. Việc này có thể mất vài ngày và thường cần chứng minh danh tính, nên hãy bắt đầu sớm.</p>
<h2>Sau khi vào lại được</h2>
<ul>
<li>Thiết lập lại 2FA và lần này <strong>lưu từng khóa mới</strong> vào trình quản lý mật khẩu.</li>
<li>Lưu mã dự phòng mới ở nơi khác ngoài điện thoại.</li>
<li>Nếu điện thoại bị trộm, hãy đổi mật khẩu các tài khoản quan trọng và gỡ thiết bị cũ khỏi tài khoản.</li>
</ul>
"""},
}
