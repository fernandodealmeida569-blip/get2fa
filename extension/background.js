/* Get2FA extension: context menu "scan QR code on this page".
   Takes a screenshot of the visible tab only after the user clicks the menu
   (activeTab), keeps it in session memory and opens the scanner page. */
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'g2fa-scan',
    title: chrome.i18n.getMessage('scanMenu'),
    contexts: ['page', 'image']
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId !== 'g2fa-scan' || !tab) return;
  try {
    const shot = await chrome.tabs.captureVisibleTab(tab.windowId, { format: 'jpeg', quality: 92 }) /* JPEG keeps big screens under the session-storage limit */;
    await chrome.storage.session.set({ shot });
  } catch (e) {
    await chrome.storage.session.set({ shot: null, shotError: String(e && e.message || e) });
  }
  chrome.tabs.create({ url: chrome.runtime.getURL('popup.html?scan=1'), index: tab.index + 1 });
});
