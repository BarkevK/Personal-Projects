chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    // Check if the URL of the tab has been updated
    if (changeInfo.url) {
        checkReminders(changeInfo.url);
    }
});

function checkReminders(url) {
    chrome.storage.local.get(null, function(reminders) {
        Object.keys(reminders).forEach(function(reminderUrl) {
            if (url.includes(reminderUrl)) {
                chrome.notifications.create({
                    type: 'basic',
                    iconUrl: 'icon48.png',
                    title: 'Reminder',
                    message: reminders[reminderUrl],
                    priority: 2
                });
            }
        });
    });
}
