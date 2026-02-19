from speak import speak
from speech import take_command
import os
import webbrowser

listening = False

def start_listening():
    global listening
    listening = True
    speak("Nexa is active. Please say your command")

    while listening:
        command = take_command()

        if command == "":
            continue

        if "open file explorer" in command:
            speak("Opening file explorer")
            os.system("explorer")

        elif "open chrome" in command:
            speak("Opening Chrome")
            os.startfile(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            )

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "nexa stop" in command:
            speak("Stopping Nexa")
            stop_listening()

        else:
            speak("Command not recognized")

def stop_listening():
    global listening
    listening = False
