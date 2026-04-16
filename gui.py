import tkinter as tk
from voice import listen, speak
from brain import think
from actions import perform

def start_listening():
    status_label.config(text="Listening...")
    window.update()

    command = listen()
    user_text.config(text=f"You: {command}")

    response = think(command)
    perform(response)

    status_label.config(text="Idle")

# Window setup
window = tk.Tk()
window.title("Irfan AI")
window.geometry("300x200")
window.configure(bg="#0f172a")

# Remove border (floating look)
window.overrideredirect(True)

# Always on top
window.attributes("-topmost", True)

# Status label
status_label = tk.Label(window, text="Idle", fg="white", bg="#0f172a", font=("Arial", 12))
status_label.pack(pady=10)

# User text
user_text = tk.Label(window, text="Say something...", fg="white", bg="#0f172a")
user_text.pack(pady=10)

# Mic button
mic_button = tk.Button(window, text="🎤", font=("Arial", 20), command=start_listening)
mic_button.pack(pady=20)

window.mainloop()