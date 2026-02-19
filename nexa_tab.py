import tkinter as tk

nexa_window = None

def open_nexa_tab():
    global nexa_window

    if nexa_window is not None:
        return

    nexa_window = tk.Tk()
    nexa_window.title("NEXA Assistant")
    nexa_window.geometry("320x180")
    nexa_window.resizable(False, False)

    label = tk.Label(
        nexa_window,
        text="NEXA is Active\nListening for commands...",
        font=("Arial", 12),
        pady=30
    )
    label.pack()

    nexa_window.protocol("WM_DELETE_WINDOW", close_nexa_tab)
    nexa_window.mainloop()


def close_nexa_tab():
    global nexa_window
    if nexa_window is not None:
        nexa_window.destroy()
        nexa_window = None
