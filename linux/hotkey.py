from pynput import keyboard
import os

def on_activate():
    os.system('/bin/python3 /opt/LogiNetwork/loginet.py')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

# Change the hotkey to whatever you want
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+e'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()