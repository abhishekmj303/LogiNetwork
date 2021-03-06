from selenium import webdriver
from selenium.webdriver.common.by import By
import os, platform
from pynotifier import Notification
from datetime import datetime

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def store():
    send_notif("Login Credentials Required")
    rln = input("Roll no. not found!!!\n   Enter your Roll no. : ")
    pwd = input("   Enter your password: ")
    with open("roll.txt", "w") as f:
        f.write(rln+","+pwd)
    log("Roll no. and password stored successfully!!")
    return rln, pwd;

def log(msg):
    print(msg)

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(dt_string+": "+msg+"\n")
    
def send_notif(msg, timeout=5):
    icon_path = os.path.join(dname, "icon.ico")
    Notification(title="LogiNetwork", description=msg, icon_path=icon_path, duration=timeout).send()

def login(username, password):
    driver.get("http://fixwifi.it/")
    if driver.current_url != "http://fixwifi.it/":
        global tries
        if tries >= 3:
            send_notif("Login Unsuccessful: INCORRECT PASSWORD")
            log("Too many tries. Exiting...")
            return
        
        log("Trying to login with your Roll no...")
        try:
            driver.find_element(By.XPATH, '//*[@id="ft_un"]').send_keys(username)
            driver.find_element(By.XPATH, '//*[@id="ft_pd"]').send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="Form1"]/table/tbody/tr[4]/th/div/table/tbody/tr[2]/th/div/p[3]/input').click()
        except Exception as e:
            print(e)

        tries += 1
        login(username, password)
    else:
        send_notif("Login Successful")
        log("Network logged in successfully!!")


send_notif("Connecting to Network...", timeout=1)

OS = platform.system()

if OS == "Linux":
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
elif OS == "Windows":
    from selenium.webdriver.edge.options import Options
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from subprocess import CREATE_NO_WINDOW

    service = Service(EdgeChromiumDriverManager().install())
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
login(rln, pwd)
log("Final URL: "+driver.current_url)

driver.quit()
log("\t---x---x---x---x---x---")
