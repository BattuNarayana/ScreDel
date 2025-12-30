# 📦 S C R E D E L
### Smart Screenshot Cleanup & Storage Saver for Windows

**Scredel** is a lightweight background utility that monitors screenshots in real-time, reminds you daily to clean them, and tracks how much storage space you have saved over time.

> **Perfect for developers, students, and anyone who regularly screenshots debugging issues, code references, or notes.**

---

## 🚀 Features
Real-time screenshot tracking
Daily reminder popup       
One-click delete today’s screenshots 
Storage space saved tracking (MB/GB) 
Dashboard with statistics 
Screenshot history with scroll
System tray background mode 
Auto-start on system boot 
**EXE build – no Python needed to run** 

---

## 🔧 How it Works

1. **Logs Automatically:** Every screenshot taken is logged automatically by Scredel.
2. **Daily Reminder:** At a configured time (default **9 PM**), you receive a reminder popup.
3. **One-Click Action:** Click ❌ **Delete All** to instantly clean today’s screenshots.
4. **Track Savings:** The Dashboard shows Total Storage Saved + History.

Stop piling screenshots forever — let **Scredel** maintain your storage.

---

## 📥 Installation & Usage

### Method 1 – Direct Run (Easiest)
1. Download `Scredel.exe` from the [Releases](#) page.
2. Double-click to start.
3. An icon will appear in the system tray; the tool runs silently.

### Method 2 – Run at System Startup (Recommended)
1. Right-click `Scredel.exe` → **Create Shortcut**.
2. Press <kbd>Win</kbd> + <kbd>R</kbd> on your keyboard.
3. Type `shell:startup` and hit Enter.
4. Move the shortcut inside the opened **Startup** folder.
5. Now Scredel runs 24/7 automatically.

---

## 🛠 Developer Setup

If you want to run the source code or build it yourself:

1. **Clone the repository**
   ```bash
   git clone <your-repo-url-here>
   cd Scredel

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the application**
   ```bash
   python main.py

4. **Build EXE**
   ```bash
   pyinstaller --noconsole --onefile main.py

## 🎯 Why this project exists?
Modern workflow = Screenshots everywhere. Errors, docs, chats, notes → saved → never deleted → storage suffers.

Scredel solves it by:

✔ Tracking screenshots silently
✔ Reminding instead of forgetting
✔ Cleaning with one click
✔ Showing actual storage you saved

A tiny tool that protects your time & storage.