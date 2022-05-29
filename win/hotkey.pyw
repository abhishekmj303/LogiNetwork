import keyboard, subprocess, os

def on_activate():
    py_file = os.path.join(os.environ['LOCALAPPDATA'], "LogiNetwork", "loginet.py")
    subprocess.run(["pythonw", py_file])

# Change the hotkey to whatever you want
keyboard.add_hotkey('ctrl+alt+e', on_activate)

keyboard.wait()