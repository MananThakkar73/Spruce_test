import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Pages.Inboxpage import InboxpageC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    Emal = (By.NAME,"username")
    pswd = (By.NAME, "password")
    logiin = (By.XPATH, "//button[@type='submit']")

    def logindetails(self, eml, paswd):

        time.sleep(10)
        self.driver.find_element(*LoginPage.Emal).send_keys(eml)
        self.driver.find_element(*LoginPage.pswd).send_keys(paswd)
        self.driver.find_element(*LoginPage.logiin).click()
        inboxpage = InboxpageC(self.driver)
        return inboxpage