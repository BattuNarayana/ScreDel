import tkinter as tk
import os, json
from datetime import datetime
import subprocess

LOG_DIR = "logs"
STATS_FILE = "storage_stats.json"


def load_today():
    today = datetime.now().strftime("%Y-%m-%d")
    file = os.path.join(LOG_DIR, f"{today}.json")
    if not os.path.exists(file):
        return []
    return json.load(open(file, "r"))


def open_screenshot_folder():
    cfg = json.load(open("config.json", "r"))
    path = cfg["screenshot_folder"]

    if os.path.exists(path):
        os.startfile(path)  # Windows native open
    else:
        print("Screenshot folder not found.")


def open_today_log():
    today = datetime.now().strftime("%Y-%m-%d")
    file = os.path.join(LOG_DIR, f"{today}.json")

    if os.path.exists(file):
        os.startfile(file)  # opens in default editor (Notepad/VSCode)
    else:
        print("No log for today.")

def load_history():
    history = []
    for file in os.listdir(LOG_DIR):
        if file.endswith(".json"):
            date = file.replace(".json", "")
            count = len(json.load(open(os.path.join(LOG_DIR, file))))
            history.append((date, count))
    history.sort(reverse=True)  # latest on top
    return history


def dashboard():
    shots = load_today()
    count = len(shots)

    # Load total space saved analytics
    if os.path.exists(STATS_FILE):
        stats = json.load(open(STATS_FILE))
        total_saved = stats.get("total_saved_bytes", 0) / (1024 * 1024)  # convert to MB
    else:
        total_saved = 0.0

    win = tk.Tk()
    win.title("Scredel Dashboard")
    win.geometry("350x230")
    win.resizable(False, False)

    tk.Label(win, text="S C R E D E L", font=("Arial", 16, "bold")).pack(pady=5)
    tk.Label(win, text=f"Today's Screenshots: {count}", font=("Arial", 12)).pack(pady=5)
    tk.Label(win, text=f"Total Space Saved: {total_saved:.2f} MB", font=("Arial", 11)).pack(pady=5)
    
    # ------------------ Scrollable History Section ------------------
    tk.Label(win, text="Recent Screenshot History", font=("Arial", 11, "bold")).pack(pady=5)

    history_frame = tk.Frame(win)
    history_frame.pack(padx=10, pady=5, fill="both", expand=True)

    canvas = tk.Canvas(history_frame, height=120)  # Visible scroll height — adjust if needed
    scrollbar = tk.Scrollbar(history_frame, orient="vertical", command=canvas.yview)

    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    history = load_history()

    if not history:
        tk.Label(scrollable_frame, text="No history available").pack(anchor="w")
    else:
        for date, count in history:
            tk.Label(scrollable_frame, text=f"{date}  →  {count} shots", font=("Arial", 10)).pack(anchor="w", pady=2)


    tk.Button(win, text="Open Screenshot Folder", width=22,
              command=open_screenshot_folder).pack(pady=6)

    tk.Button(win, text="View Today Log", width=22,
              command=open_today_log).pack(pady=6)

    tk.Button(win, text="Close", width=22, command=win.destroy).pack(pady=12)

    win.mainloop()
