import os
import json
from datetime import datetime

LOG_DIR = "logs"
STATS_FILE = "storage_stats.json"

def get_file_size(file_path):
    return os.path.getsize(file_path) if os.path.exists(file_path) else 0

def update_storage_stats(bytes_saved):
    data = json.load(open(STATS_FILE))
    data["total_saved_bytes"] += bytes_saved
    json.dump(data, open(STATS_FILE, "w"), indent=4)


def log_screenshot(path):
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{today}.json")

    # If log doesn't exist -> create
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            json.dump([], f)

    # Append entry
    with open(log_file, "r") as f:
        data = json.load(f)

    data.append(path)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)


def delete_today_screenshots():
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{today}.json")

    if not os.path.exists(log_file):
        return "No screenshots logged today."

    with open(log_file, "r") as f:
        data = json.load(f)

    bytes_saved = 0

    for file_path in data:
        if os.path.exists(file_path):
            bytes_saved += get_file_size(file_path)
            os.remove(file_path)

    update_storage_stats(bytes_saved)

    os.remove(log_file)
    mb = bytes_saved / (1024*1024)
    return f"Deleted {len(data)} screenshots → Freed {mb:.2f} MB"

