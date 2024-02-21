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

    driver.get("https://app.spruce-staging.com/login")

    Wait = WebDriverWait(driver, 10)

    email = Wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email.send_keys("lsspl.sprucepatient+17tm@gmail.com")

    paswd = Wait.until(EC.presence_of_element_located((By.NAME, "password")))
    paswd.send_keys("asdf12")
    paswd.send_keys(Keys.ENTER)

    sett = Wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='UI.MainNavigation.Settings']"))).click()

    tm_page = Wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Teammates'][@class='css-7nfrpy']"))).click()

    time.sleep(3)
    btn = driver.find_element(By.XPATH,"//div[@class='css-qx3oo9']")
    print(btn.is_displayed())


except Exception as e:
    print(e)
