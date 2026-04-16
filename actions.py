import os
from voice import speak

def perform(action):
    if action == "open_youtube":
        speak("Opening YouTube")
        os.system("start https://youtube.com")

    elif action == "shutdown":
        speak("Shutting down")
        os.system("shutdown /s /t 5")

    else:
        speak("Sorry, I don't understand")