import os
import webbrowser
import pyautogui
from speak import speak
from speech import take_command
from nexa_ui import open_nexa_tab

active = False

# Open NEXA UI
open_nexa_tab()

speak("Hello Kunal. NEXA is online. Say hey nexa to activate.")

while True:
    command = take_command()

    if not command:
        continue

    print("HEARD:", command, "| ACTIVE:", active)

    # ACTIVATE
    if not active and "hey nexa" in command:
        active = True
        speak("Activated. How can I help you?")
        continue

    # DEACTIVATE
    if active and ("sleep nexa" in command or "stop nexa" in command):
        active = False
        speak("Going to sleep.")
        continue

    if not active:
        continue

    # ---- COMMANDS ----

    if "open chrome" in command:
        speak("Opening Google Chrome")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif "open file explorer" in command:
        speak("Opening file explorer")
        os.system("explorer")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command.startswith("type"):
        text = command.replace("type", "", 1).strip()
        speak("Typing now")
        pyautogui.write(text, interval=0.05)

    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "who are you" in command:
        speak("I am NEXA. Your personal AI assistant.")

    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 1")

    elif "exit" in command:
        speak("Goodbye Kunal")
        break

    else:
        speak("Command not recognized")
