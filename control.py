import os
import webbrowser
import pyautogui
import time

def open_chrome():
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

def open_file_explorer():
    os.system("explorer")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

def type_text(text):
    time.sleep(1)
    pyautogui.write(text, interval=0.05)

def press_enter():
    pyautogui.press("enter")
