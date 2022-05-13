from selenium import webdriver
from selenium.webdriver.common.by import By
import platform

os = platform.system()

if os == "Linux":
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
elif os == "Windows":
    from selenium.webdriver.edge.options import Options
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
elif os == "Darwin":
    driver = webdriver.Safari()

tries = 0

def login(username, password):
    driver.get("http://fixwifi.it/")
    if driver.current_url != "http://fixwifi.it/":
        global tries
        if tries >= 3:
            print("Too many tries. Exiting...")
            return
        
        print("Trying to login with your Roll no...")
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="Form1"]/table/tbody/tr[4]/th/div/table/tbody/tr[2]/th/div/p[3]/input').click()

        tries += 1
        login(username, password)
    else:
        print("Network logged in successfully!!")

try:
    with open("roll.txt", "r+") as f:
        data = f.read()
        if len(data) == 9 :
            rln = data
        else:
            rln = input("Roll no. not found!!!\n   Enter your Roll no. : ")
            f.write(rln)
except FileNotFoundError:
    rln = input("Roll no. not found!!!\n   Enter your Roll no. : ")
    with open("roll.txt", "w") as f:
        f.write(rln)

pwd = (rln[-4:]) + str(int(rln[-4:])+1)

login(rln, pwd)

print("Final URL: "+driver.current_url)
driver.quit()