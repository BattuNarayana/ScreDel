import tkinter as tk
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def save_config(data):
    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

def open_settings():
    config = load_config()

    window = tk.Tk()
    window.title("Scredel Settings")
    window.geometry("300x150")

    tk.Label(window, text="Reminder Time (24hr format)").pack(pady=10)

    time_entry = tk.Entry(window, width=10)
    time_entry.insert(0, config.get("reminder_time", "21:00"))
    time_entry.pack()

    def save_time():
        config["reminder_time"] = time_entry.get()
        save_config(config)
        print("Reminder time updated.")
        window.destroy()

    tk.Button(window, text="Save", command=save_time).pack(pady=10)

    window.mainloop()
