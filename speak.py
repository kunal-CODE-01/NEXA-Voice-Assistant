import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# try to select female voice
for v in voices:
    if "female" in v.name.lower() or "zira" in v.name.lower():
        engine.setProperty('voice', v.id)
        break

engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()
