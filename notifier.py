import tkinter as tk

#from jupyter_server_terminals import msg
from cleaner import delete_today_screenshots

def show_popup():
    window = tk.Tk()
    window.title("Scredel Reminder")
    window.geometry("300x150")
    window.resizable(False, False)

    label = tk.Label(window, text="Delete today's screenshots?", font=("Arial", 12))
    label.pack(pady=15)

    def delete_action():
        result = delete_today_screenshots()
        print(result)

        msg = tk.Label(window, text=result, font=("Arial", 10))
        msg.pack(pady=5)      

        window.after(2000, window.destroy)  # auto close after 2 sec

    def keep_action():
        print("Screenshots kept.")
        window.destroy()

    tk.Button(window, text="Delete All", width=12, command=delete_action).pack(pady=5)
    tk.Button(window, text="Keep", width=12, command=keep_action).pack()

    window.mainloop()
