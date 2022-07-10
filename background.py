import subprocess
import time
import os
import platform
import threading
from urllib import request, error

tries = 0
login_url = 'http://example.com/'
dest_urls = ['http://example.com/', 'https://example.com/']

OS = platform.system()
if OS == "Linux":
    is_active_cmd = "nmcli connection show --active"
    py = "/bin/python3"
    file_path = "/opt/LogiNetwork/loginet.py"
elif OS == "Windows":
    is_active_cmd = "netsh int show int"
    py = "pythonw"
    file_path = os.path.join(
        os.environ['USERPROFILE'], "LogiNetwork", "loginet.py")


def is_online():
    try:
        resp = request.urlopen(login_url)
        if resp.url in dest_urls:
            return True
    except error.URLError as e:
        if "[Errno" in str(e):
            return True
        return False


def on_change():
    global tries
    if tries <= 5:
        print("Network Changed")
        try:
            out = is_online()
            if (out == False):
                subprocess.run([py, file_path])
            else:
                tries += 1
                time.sleep(3)
                on_change()
        except subprocess.CalledProcessError as e:
            print(e)
            tries += 1
            time.sleep(3)
            on_change()


def active_network():
    return subprocess.check_output(is_active_cmd, shell=True).decode("utf-8")


def watch_network():
    while (True):
        state1 = active_network()
        # print(state1)
        time.sleep(3)
        state2 = active_network()
        # print(state2)

        global tries
        if state1 != state2:
            tries = 0
            on_change()

# Change the hotkey to whatever you want


def hotkey_linux():
    from pynput import keyboard

    def on_activate():
        subprocess.run([py, file_path])

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>+e'),
        on_activate)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()


def hotkey_win():
    import keyboard

    def on_activate():
        subprocess.run([py, file_path])

    # Change the hotkey to whatever you want
    keyboard.add_hotkey('ctrl+alt+e', on_activate)

    keyboard.wait()


if __name__ == "__main__":
    t1 = threading.Thread(target=watch_network)
    if OS == 'Linux':
        t2 = threading.Thread(target=hotkey_linux)
    elif OS == 'Windows':
        t2 = threading.Thread(target=hotkey_win)

    t1.start()
    t2.start()
    on_change()
