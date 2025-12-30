import json
import schedule
import time
from cleaner import delete_today_screenshots

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def schedule_reminder(action_callback):
    config = load_config()
    remind_time = config["reminder_time"]    # "21:00"

    # Schedule exact time daily
    schedule.every().day.at(remind_time).do(action_callback)

    while True:
        schedule.run_pending()
        time.sleep(1)
