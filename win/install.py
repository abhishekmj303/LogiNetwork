import subprocess, shutil, os
from urllib import request

dname = os.path.join(os.environ['USERPROFILE'], "LogiNetwork")
print(dname)
if os.path.exists(dname):
    dname_old = os.path.join(os.environ['USERPROFILE'], "LogiNetwork_old")
    os.rename(dname, dname_old)
    shutil.rmtree(dname_old, ignore_errors=True)
os.mkdir(dname)

req_files = ["loginet.py", "icon.ico", "win/hotkey.pyw", "requirements.txt"]
base_url = "https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/"
for f in req_files:
    print(base_url + f)
    request.urlretrieve(base_url + f, os.path.join(dname, f.split("/")[-1]))

os.chdir(dname)
print(os.getcwd())

print("Installing pip dependencies...")
subprocess.run("pip install -r requirements.txt", shell=True)

startup = os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
hotkey = os.path.join(startup, "hotkey.pyw")
request.urlretrieve(base_url + req_files[2], hotkey)

subprocess.Popen(["pythonw", hotkey], stdin=None, stdout=None, stderr=None).pid

print()
print()
print()
print("Installation complete")
print(">>> Use Ctrl+Alt+e to Login to College Network <<<")