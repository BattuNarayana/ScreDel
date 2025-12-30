import pystray
from PIL import Image, ImageDraw
from settings import open_settings
from cleaner import delete_today_screenshots
from dashboard import dashboard

import threading

def create_icon():
    # Create simple icon dynamically (black circle)
    img = Image.new('RGB', (64,64), "white")
    draw = ImageDraw.Draw(img)
    draw.ellipse((8,8,56,56), fill="black")

    def on_settings(icon, item):
        threading.Thread(target=open_settings).start()

    def on_delete(icon, item):
        print(delete_today_screenshots())

    def on_exit(icon, item):
        icon.stop()

    menu = pystray.Menu(
        pystray.MenuItem("Dashboard", lambda icon,item: threading.Thread(target=dashboard).start()),
        pystray.MenuItem("Settings", on_settings),
        pystray.MenuItem("Delete Today", on_delete),
        pystray.MenuItem("Exit", on_exit)
    )

    icon = pystray.Icon("Scredel", img, "Scredel Running", menu)
    icon.run()
