import shutil
import os
import sys

py_ver = ".".join((str(sys.version_info[i]) for i in (0, 1)))
progs = ["pythonw", "pythonw"+py_ver]
for p in progs:
    os.system("taskkill /f /im "+p+".exe")

dname = os.path.join(os.environ['USERPROFILE'], "LogiNetwork")
driver_dir = os.path.join(os.environ['USERPROFILE'], ".wdm")
startup = os.path.join(os.environ['APPDATA'], "Microsoft", "Windows",
                       "Start Menu", "Programs", "Startup", "loginet_bg.pyw")
if os.path.exists(dname):
    shutil.rmtree(dname, ignore_errors=True)
if os.path.exists(startup):
    os.remove(startup)
if os.path.exists(driver_dir):
    shutil.rmtree(driver_dir, ignore_errors=True)
