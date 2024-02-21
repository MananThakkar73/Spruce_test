import selenium
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("https://www.espn.in/cricket/series/22002/game/1389399/india-vs-england-1st-test-england-in-india-2023-24")

    time.sleep(10)
    '''Wait = WebDriverWait(driver,10)

    email = Wait.until(EC.presence_of_element_located((By.NAME,"username")))
    email.send_keys("lsspl.sprucepatient+beta17@gmail.com")

    paswd = Wait.until(EC.presence_of_element_located((By.NAME,"password")))
    paswd.send_keys("asdf12")
    paswd.send_keys(Keys.ENTER)'''

    immg = driver.find_elements(By.TAG_NAME,"img")
    print(len(immg))
    broimmglst = []
    r_code = []
    time.sleep(5)

    for image in range(10,20):
        broimg = immg[image].get_attribute("src")
        broimmglst.append(broimg)
        r = requests.get(broimg).status_code
        r_code.append(r)


    print(broimmglst,r_code)



    driver.quit()


except Exception as e:
    print(e)



