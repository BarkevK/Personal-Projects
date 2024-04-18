// When the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('reminderForm');

    // Listen for the form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission action

        const websiteUrl = document.getElementById('websiteUrl').value;
        const reminderText = document.getElementById('reminderText').value;

        // Save the reminder data using Chrome's local storage API
        chrome.storage.local.set({[websiteUrl]: reminderText}, function() {
            console.log('Reminder set for ' + websiteUrl + ': ' + reminderText);
            // Clear the form
            form.reset();
            // Display a confirmation
            alert('Reminder set!');
        });
    });

    // Check the current tab's URL against stored reminders
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        let currentUrl = new URL(tabs[0].url);
        chrome.storage.local.get(null, function(reminders) {
            Object.keys(reminders).forEach(function(url) {
                if (currentUrl.href.includes(url)) {
                    alert('Reminder for this site: ' + reminders[url]);
                }
            });
        });
    });

    removeForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const removeUrl = document.getElementById('removeUrl').value;

        chrome.storage.local.remove(removeUrl, function() {
            console.log('Reminder removed for ' + removeUrl);
            alert('Reminder removed!');
            removeForm.reset();
        });
    });
});


