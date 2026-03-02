import tkinter as tk
from datetime import datetime

LOG_FILE = "keylog.txt"

def format_key(event):
    if event.keysym == "space":
        return " "
    elif event.keysym == "Return":
        return "\n"
    elif len(event.char) == 1:
        return event.char
    else:
        return f"[{event.keysym}]"

def on_key(event):
    key = format_key(event)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key)

def clear_log():
    open(LOG_FILE, "w").close()

root = tk.Tk()
root.title("Keyboard Logger Demo (Lab Only)")
root.geometry("400x200")

tk.Label(root, text="Type inside this window to log keys").pack(pady=20)
tk.Button(root, text="Clear Log File", command=clear_log).pack()

root.bind("<Key>", on_key)

root.mainloop()