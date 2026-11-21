# Get2FA browser extension – Privacy policy

_Last updated: November 21, 2026_

The Get2FA extension generates two-factor authentication (TOTP) codes inside your browser.

**What we collect:** nothing. The extension has no server, no analytics and no tracking. It never sends your secret keys, codes, account names or screenshots anywhere.

**What is stored on your device:** only the 2FA keys you choose to save with the "Save" button, kept in your browser profile (`chrome.storage.local`). You can delete them at any time with the × button or by removing the extension. Keys you paste without saving disappear when the popup closes.

**Screenshots for QR scanning:** when you click "Scan QR" or the right-click menu item, the extension takes one screenshot of the visible tab (permission `activeTab`) to find a QR code. The image is decoded locally, kept only in temporary session memory and discarded right away.

**Permissions:**
- `storage` – keep the keys you save on this device.
- `activeTab` – capture the visible tab only after you click "Scan QR" or the menu item.
- `contextMenus` – add the "scan 2FA QR code on this page" menu item.

**Open source:** https://github.com/fernandodealmeida569-blip/get2fa

**Contact:** contact@get2fa.online
