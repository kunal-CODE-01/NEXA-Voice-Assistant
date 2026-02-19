import tkinter as tk
from PIL import Image, ImageTk

window = None

def open_nexa_tab():
    global window

    if window:
        return

    window = tk.Tk()
    window.title("NEXA AI")
    window.geometry("900x550")
    window.resizable(False, False)

    bg_img = Image.open("assets/nexa_bg.png")
    bg_img = bg_img.resize((900, 550))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0)

    logo_img = Image.open("assets/nexa_logo.png")
    logo_img = logo_img.resize((180, 180))
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(window, image=logo_photo, bg="black")
    logo_label.image = logo_photo
    logo_label.place(x=360, y=120)

    title = tk.Label(
        window,
        text="NEXA AI SYSTEM ONLINE",
        fg="#ffaa33",
        bg="black",
        font=("Orbitron", 16)
    )
    title.place(x=290, y=320)

    window.after(100, window.update)
