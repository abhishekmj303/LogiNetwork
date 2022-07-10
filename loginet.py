from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import platform
from pynotifier import Notification
from datetime import datetime
from urllib import request, error

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
login_url = 'http://example.com/'
dest_urls = ['http://example.com/', 'https://example.com/']


def store():
    send_notif("Login Credentials Required")
    rln = input("Roll no. not found!!!\n   Enter your Roll no. : ")
    pwd = input("   Enter your password: ")
    with open("roll.txt", "w") as f:
        f.write(rln+","+pwd)
    log("Roll no. and password stored successfully!!")
    return rln, pwd


def log(msg):
    print(msg)

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(dt_string+": "+msg+"\n")


def send_notif(msg, timeout=5):
    icon_path = os.path.join(dname, "icon.ico")
    Notification(title="LogiNetwork", description=msg,
                 icon_path=icon_path, duration=timeout).send()


def is_online():
    try:
        resp = request.urlopen(login_url)
        if resp.url in dest_urls:
            return True
    except error.URLError as e:
        if "[Errno -2]" in str(e):
            return True
        return False


def login(username, password):
    try:
        driver.get(login_url)
        if driver.current_url not in dest_urls:
            global tries
            if tries >= 3:
                send_notif("Login Unsuccessful: INCORRECT PASSWORD")
                log("Too many tries. Exiting...")
                return

            log("Trying to login with your Roll no...")

            driver.find_element(
                By.XPATH, '//*[@id="ft_un"]').send_keys(username)
            driver.find_element(
                By.XPATH, '//*[@id="ft_pd"]').send_keys(password)
            driver.find_element(
                By.XPATH, '//*[@id="Form1"]/table/tbody/tr[4]/th/div/table/tbody/tr[2]/th/div/p[3]/input').click()

            tries += 1
            login(username, password)
        else:
            send_notif("Login Successful")
            log("Network logged in successfully!!")

        if (OS == "Windows"):
            dr_mngr().install()

    except Exception as e:
        print(e)


send_notif("Connecting to Network...", timeout=1)
if (is_online() == True):
    send_notif("Network is already online")
    log("Network is already online")
    log("\t---x---x---x---x---x---")
    exit()

OS = platform.system()

if OS == "Linux":
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
elif OS == "Windows":
    from selenium.webdriver.edge.options import Options
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager as dr_mngr
    from subprocess import CREATE_NO_WINDOW
    import subprocess

    os.environ['WDM_SSL_VERIFY'] = '0'
    cmd = "where /r " + \
        os.path.join(os.environ['USERPROFILE'], ".wdm") + " msedgedriver.exe"
    exe_path = subprocess.check_output(
        cmd, shell=True).decode("utf-8").split("\r\n")[-2]
    service = Service(exe_path)
    service.creationflags = CREATE_NO_WINDOW
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Edge(options=options, service=service)
elif OS == "Darwin":
    driver = webdriver.Safari()

try:
    with open("roll.txt", "r+") as f:
        data = f.read()
        rln, pwd = data.split(",")
except FileNotFoundError or ValueError:
    rln, pwd = store()

tries = 0
try:
    login(rln, pwd)
    log("Final URL: "+driver.current_url)
except Exception as e:
    print(e)
driver.quit()
log("\t---x---x---x---x---x---")
