# -*- coding: utf-8 -*-
"""Comparison guide: Get2FA as an alternative to 2fa.live.
Only states what each site's own page shows (checked November 2026)."""

ALT = {"key": "alt-2fa-live",
"en": {"slug": "2fa-live-alternative",
 "title": "2fa.live Alternative: Get2FA, an Open-Source 2FA Code Generator",
 "desc": "Looking for an alternative to 2fa.live? Get2FA gives the same 6-digit 2FA code from a secret key, calculated in your browser, with open source code, QR reading, a Chrome extension and 17 languages.",
 "h1": "2fa.live alternative: how Get2FA compares",
 "lead": "Both sites turn a 2FA secret key into the 6-digit login code. This page sets out what differs, so you can pick the one that fits how you work.",
 "body": """
<h2>What both tools do</h2>
<p>2fa.live and Get2FA are web pages where you paste a 2FA secret key and get the current code, the same one an authenticator app would show. Both follow the TOTP standard, so for the same key at the same moment they give the same code.</p>

<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Get2FA</th><th>2fa.live</th></tr></thead>
<tbody>
<tr><td>Code from a secret key</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>Where the code is calculated</td><td>In your browser. The page says so and the source code is public</td><td>Not stated on the page</td></tr>
<tr><td>Privacy policy</td><td class="yes">✓</td><td>None found on the page</td></tr>
<tr><td>Open source</td><td class="yes">✓ (GitHub)</td><td>Not published</td></tr>
<tr><td>Next code and seconds left</td><td class="yes">✓</td><td>Not shown</td></tr>
<tr><td>Read a QR code image, otpauth:// links</td><td class="yes">✓</td><td>Not offered</td></tr>
<tr><td>Interface languages</td><td>17</td><td>English</td></tr>
<tr><td>Browser extension</td><td class="yes">✓ (Chrome)</td><td>None listed on the page</td></tr>
<tr><td>Works offline after loading</td><td class="yes">✓</td><td>Not stated</td></tr>
</tbody></table></div>
<p class="hint">The 2fa.live column describes what its public page showed in November 2026. Sites change, so check for yourself if a point matters to you.</p>

<h2>Why “calculated in your browser” matters</h2>
<p>A 2FA secret key is as sensitive as a password: whoever has it can produce your codes. With Get2FA the key never leaves your device. You can confirm it: open your browser's developer tools, go to the Network tab and paste a key. No request carries it. The code is also on <a href="https://github.com/fernandodealmeida569-blip/get2fa" rel="noopener">GitHub</a> for anyone to read.</p>
<p>With any 2FA site that doesn't say where the calculation happens, you can run the same Network-tab check before trusting it with a real key.</p>

<h2>Moving over takes nothing</h2>
<p>There is no account and nothing to import. Paste the same secret key into <a href="/">Get2FA</a> and you get the same code. If you handle many accounts, paste all the lines at once, or use the <a href="/account-line-splitter">account line splitter</a> to pick columns and add the code to each line.</p>

<h2>When a website is the wrong tool</h2>
<p>For accounts you use every day, keep the key in an authenticator app or a password manager, and use a web generator when you are on another device or managing many accounts. See <a href="what-is-2fa">what 2FA is</a> and <a href="find-2fa-secret-key">where to find your secret key</a>.</p>
"""},
"vi": {"slug": "thay-the-2fa-live",
 "title": "Thay thế 2fa.live: Get2FA, công cụ lấy mã 2FA mã nguồn mở",
 "desc": "Đang tìm công cụ thay thế 2fa.live? Get2FA cho cùng mã 2FA 6 số từ khóa bí mật, tính ngay trên trình duyệt, mã nguồn mở, đọc mã QR, có tiện ích Chrome và giao diện tiếng Việt.",
 "h1": "Thay thế 2fa.live: Get2FA khác gì?",
 "lead": "Cả hai trang đều đổi khóa bí mật 2FA thành mã đăng nhập 6 số. Trang này nêu những điểm khác nhau để bạn chọn công cụ hợp với cách làm việc của mình.",
 "body": """
<h2>Hai công cụ giống nhau ở đâu</h2>
<p>2fa.live và Get2FA đều là trang web để bạn dán khóa bí mật 2FA và nhận mã hiện tại, giống mã mà ứng dụng xác thực hiển thị. Cả hai đều theo chuẩn TOTP, nên với cùng một khóa tại cùng một thời điểm, hai trang cho cùng một mã.</p>

<h2>So sánh</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Get2FA</th><th>2fa.live</th></tr></thead>
<tbody>
<tr><td>Lấy mã từ khóa bí mật</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>Mã được tính ở đâu</td><td>Trên trình duyệt của bạn. Trang ghi rõ và mã nguồn công khai</td><td>Trang không nêu</td></tr>
<tr><td>Chính sách quyền riêng tư</td><td class="yes">✓</td><td>Không thấy trên trang</td></tr>
<tr><td>Mã nguồn mở</td><td class="yes">✓ (GitHub)</td><td>Không công bố</td></tr>
<tr><td>Mã kế tiếp và số giây còn lại</td><td class="yes">✓</td><td>Không hiển thị</td></tr>
<tr><td>Đọc ảnh mã QR, liên kết otpauth://</td><td class="yes">✓</td><td>Không có</td></tr>
<tr><td>Ngôn ngữ giao diện</td><td>17, có tiếng Việt</td><td>Tiếng Anh</td></tr>
<tr><td>Tiện ích trình duyệt</td><td class="yes">✓ (Chrome)</td><td>Trang không nêu</td></tr>
<tr><td>Dùng được khi mất mạng sau khi tải trang</td><td class="yes">✓</td><td>Trang không nêu</td></tr>
</tbody></table></div>
<p class="hint">Cột 2fa.live mô tả những gì trang công khai của họ hiển thị vào tháng 11/2026. Trang web có thể thay đổi, bạn nên tự kiểm tra nếu điểm nào đó quan trọng với bạn.</p>

<h2>Vì sao “tính trên trình duyệt” lại quan trọng</h2>
<p>Khóa bí mật 2FA nhạy cảm như mật khẩu: ai có khóa là tạo được mã của bạn. Với Get2FA, khóa không rời khỏi thiết bị. Bạn có thể tự kiểm chứng: mở công cụ dành cho nhà phát triển của trình duyệt, vào thẻ Network rồi dán một khóa. Không có yêu cầu nào chứa khóa. Mã nguồn cũng có trên <a href="https://github.com/fernandodealmeida569-blip/get2fa" rel="noopener">GitHub</a> để ai cũng đọc được.</p>
<p>Với bất kỳ trang 2FA nào không nói rõ việc tính toán diễn ra ở đâu, bạn có thể làm đúng phép kiểm tra đó trước khi dán khóa thật.</p>

<h2>Chuyển sang không cần làm gì thêm</h2>
<p>Không cần tài khoản, không cần nhập dữ liệu. Dán cùng khóa bí mật vào <a href="/vi/">Get2FA</a> là có cùng mã. Nếu bạn quản lý nhiều tài khoản, hãy dán tất cả các dòng cùng lúc, hoặc dùng công cụ <a href="/vi/cat-chuoi-tai-khoan">cắt chuỗi tài khoản</a> để chọn cột và thêm mã vào từng dòng.</p>

<h2>Khi nào không nên dùng trang web</h2>
<p>Với tài khoản dùng hằng ngày, hãy giữ khóa trong ứng dụng xác thực hoặc trình quản lý mật khẩu, và chỉ dùng công cụ web khi bạn ở thiết bị khác hoặc quản lý nhiều tài khoản. Xem <a href="2fa-la-gi">2FA là gì</a> và <a href="tim-khoa-bi-mat-2fa">cách tìm khóa bí mật 2FA</a>.</p>
"""},
}
