import speech_recognition as sr
import sounddevice as sd
import numpy as np

recognizer = sr.Recognizer()

def take_command():
    try:
        samplerate = 16000
        duration = 4  # seconds

        print("Listening...")
        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )
        sd.wait()

        audio_data = sr.AudioData(
            audio.tobytes(),
            samplerate,
            2
        )

        text = recognizer.recognize_google(audio_data)
        text = text.lower()
        print("You said:", text)
        return text

    except Exception as e:
        print("Speech error:", e)
        return ""
