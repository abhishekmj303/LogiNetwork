import subprocess, shutil, os
from urllib import request
from zipfile import ZipFile

git_url = "https://github.com/abhishekmj303/LogiNetwork/archive/refs/heads/master.zip"
request.urlretrieve(git_url, "master.zip")

dname = os.path.join(os.environ['LOCALAPPDATA'], "LogiNetwork")
if os.path.exists(dname):
    dname_old = os.path.join(os.environ['LOCALAPPDATA'], "LogiNetwork_old")
    os.rename(dname, dname_old)
    shutil.rmtree(dname_old, ignore_errors=True)
os.mkdir(dname)

startup = os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
with ZipFile("master.zip", "r") as zip_ref:
    zip_ref.extract("loginet.py", dname)
    zip_ref.extract("icon.ico", dname)
    zip_ref.extract("win/hotkey.pyw", dname)
    zip_ref.extract("win/hotkey.pyw", startup)
    zip_ref.extract("requirements.txt")
    print("Installing pip dependencies...")
    subprocess.run("pip install -r requirements.txt", shell=True)

os.remove("master.zip")
os.remove("requirements.txt")

print("Installation complete")
print(">>> Use Ctrl+Alt+e to Login to College Network <<<")