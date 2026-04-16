from voice import listen, speak
from brain import think
from actions import perform

while True:
    command = listen()
    response = think(command)
    perform(response)