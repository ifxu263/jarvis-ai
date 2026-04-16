def think(command):
    if "youtube" in command:
        return "open_youtube"
    elif "shutdown" in command:
        return "shutdown"
    else:
        return "unknown"