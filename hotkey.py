from asyncio import subprocess
import keyboard, subprocess, platform

def login(os):
    if os == "Linux":
        subprocess.run(["python3", "/opt/LogiNetwork/loginet.py"])
    elif os == "Windows":
        subprocess.run(["python", "C:\\Program Files\\LogiNetwork\\loginet.py"])

os = platform.system()

keyboard.add_hotkey("ctrl+alt+shift+l", login(os))

keyboard.wait()