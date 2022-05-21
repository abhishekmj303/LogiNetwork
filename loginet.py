from selenium import webdriver
from selenium.webdriver.common.by import By
import os, platform
from plyer import notification
from datetime import datetime

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def store():
    rln = input("Roll no. not found!!!\n   Enter your Roll no. : ")
    pwd = input("   Enter your password: ")
    with open("roll.txt", "w") as f:
        f.write(rln+","+pwd)
    log("Roll no. and password stored successfully!!")

def log(msg):
    print(msg)

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(dt_string+": "+msg+"\n")
    
def send_notif(msg, timeout=5):
    notification.notify(title="LogiNetwork", message=msg, app_icon="./icon.png", timeout=timeout)

def login(username, password):
    driver.get("http://fixwifi.it/")
    if driver.current_url != "http://fixwifi.it/":
        global tries
        if tries >= 3:
            send_notif("Login Unsuccessful: INCORRECT PASSWORD")
            log("Too many tries. Exiting...")
            return
        
        log("Trying to login with your Roll no...")
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="Form1"]/table/tbody/tr[4]/th/div/table/tbody/tr[2]/th/div/p[3]/input').click()

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
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
elif OS == "Darwin":
    driver = webdriver.Safari()

try:
    with open("roll.txt", "r+") as f:
        data = f.read()
        rln, pwd = data.split(",")
except FileNotFoundError or ValueError:
    store()

tries = 0
login(rln, pwd)
log("Final URL: "+driver.current_url)

driver.quit()
log("\t---x---x---x---x---x---")