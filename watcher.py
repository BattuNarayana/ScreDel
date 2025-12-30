import os
import time
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def watch_screenshots(callback):
    config = load_config()
    folder = config["screenshot_folder"]

    existing_files = set(os.listdir(folder))

    while True:
        current_files = set(os.listdir(folder))
        new_files = current_files - existing_files

        if new_files:
            for file in new_files:
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    callback(os.path.abspath(os.path.join(folder, file)))


        existing_files = current_files
        time.sleep(2)   # checks every 2 seconds
