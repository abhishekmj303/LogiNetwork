from webdriver_manager.microsoft import EdgeChromiumDriverManager
import subprocess
import shutil
import os
from urllib import request, error

print("LogiNetwork:")
print("    Completely automate the College Wifi/LAN")
print("    https//github.com/abhishekmj303/LogiNetwork\n")
dname = os.path.join(os.environ['USERPROFILE'], "LogiNetwork")

if os.path.exists(dname):
    dname_old = os.path.join(os.environ['USERPROFILE'], "LogiNetwork_old")
    os.rename(dname, dname_old)
    shutil.rmtree(dname_old, ignore_errors=True)
os.mkdir(dname)

print("Downloading LogiNetwork...")
req_files = ["loginet.py", "icon.ico", "background.py",
             "requirements.txt", "win/uninstall.py"]
base_url = "https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/"
try:
    for f in req_files:
        print(base_url + f)
        request.urlretrieve(
            base_url + f, os.path.join(dname, f.split("/")[-1]))
except error.URLError:
    print("Please check your internet connection and try again.")
    print("Exiting...")
    exit()

os.chdir(dname)
print(os.getcwd())

print("Installing python dependencies... (This may take a while)")
subprocess.run("pip install -r requirements.txt", shell=True)

print("Installing MSEdge-webdriver... (This may take a while)")
EdgeChromiumDriverManager().install()

print("Installing Application...")
print("  -Installation folder: " + dname)
startup = os.path.join(
    os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
hotkey = os.path.join(startup, "loginet_bg.pyw")
request.urlretrieve(base_url + req_files[2], hotkey)
print("  -Creating startup file: " + hotkey)

with open("roll.txt", "w") as roll:
    print("\n\nLogin Credentials")
    rln = input("\tUsername: ")
    pwd = input("\tPassword: ")
    roll.write(rln + "," + pwd)

subprocess.Popen(["pythonw", hotkey], stdin=None, stdout=None, stderr=None).pid


print("  -Installation complete")
print()
print("College WiFi/LAN login is now automatically done")
print("You can also explicitly use Ctrl+Alt+e to login (if not working properly)")
