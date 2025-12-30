from watcher import watch_screenshots
from cleaner import log_screenshot
from scheduler import schedule_reminder
from native_notify import send_notification
from notifier import show_popup
from settings import open_settings
from tray import create_icon


import threading

def screenshot_detected(path):
    print(f"Screenshot detected: {path}")
    log_screenshot(path)

# --- Thread-1: Live Screenshot Watcher ---
t1 = threading.Thread(target=watch_screenshots, args=(screenshot_detected,))
t1.daemon = True
t1.start()


# --- Reminder Trigger -> Notification + UI Popup ---
def reminder_trigger():
    send_notification()
    show_popup()


# --- Thread-2: Daily Reminder Scheduler ---
t2 = threading.Thread(target=schedule_reminder, args=(reminder_trigger,))
t2.daemon = True
t2.start()


# Thread-3: System Tray Icon
t3 = threading.Thread(target=create_icon)
t3.daemon = True
t3.start()


print("Scredel is running... Watching screenshots & waiting for reminder...")

while True:
    pass
