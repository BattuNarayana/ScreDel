from plyer import notification
from cleaner import delete_today_screenshots

def send_notification():
    notification.notify(
        title="Scredel Reminder",
        message="Click here to open cleanup window.",
        timeout=10
    )
    print("Notification sent. (Click will be handled by popup)")
