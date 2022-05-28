from pynput import keyboard
import os, platform

def on_activate():
    OS = platform.system()
    if OS == "Linux":
        os.system('/bin/python3 /opt/LogiNetwork/loginet.py')
    elif OS == "Windows":
        os.system("python C:\\Program Files\\LogiNetwork\\loginet.py")

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<shift>+<ctrl>+<alt>+l'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()