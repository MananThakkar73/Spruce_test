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
    r = requests.get("https://app.spruce-staging.com/login")
    print(r.status_code)


    Wait = WebDriverWait(driver,10)

    email = Wait.until(EC.presence_of_element_located((By.NAME,"username")))
    email.send_keys("lsspl.sprucepatient+beta17@gmail.com")

    paswd = Wait.until(EC.presence_of_element_located((By.NAME,"password")))
    paswd.send_keys("asdf12")
    paswd.send_keys(Keys.ENTER)

    sett = Wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-test-id='UI.MainNavigation.Settings']"))).click()

    time.sleep(3)

    sett_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(sett_links))

    '''
    urls = []
    for e in sett_links:
        href = e.get_attribute("href")
        urls.append(href)

    print(urls)

    '''
    #bill = Wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Billing']"))).click()
    #bill_links = driver.find_elements(By.TAG_NAME,"a")
    url_rescode = []
    not_200url = []
    urls = []
    for url in sett_links:
        href = url.get_attribute('href')
        urls.append(href)
        r1 = requests.get(str(href)).status_code
        if r1 != 200:
            not_200url.append(href)

        url_rescode.append(r1)
    print(url_rescode)
    print(not_200url)
    print(urls)



    print(driver.title)

    time.sleep(5)

    driver.quit()

except Exception as e:
    print(e)