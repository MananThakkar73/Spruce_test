import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:

    driver.get("https://app.spruce-staging.com/login")

    Wait = WebDriverWait(driver,10)

    email = Wait.until(EC.presence_of_element_located((By.NAME,"username")))
    email.send_keys("lsspl.sprucepatient+beta17@gmail.com")

    paswd = Wait.until(EC.presence_of_element_located((By.NAME,"password")))
    paswd.send_keys("asdf12")
    paswd.send_keys(Keys.ENTER)
    r = requests.get("https://app.spruce-staging.com/settings/fax/claim").status_code
    print(r)

except Exception as e:
    print(e)