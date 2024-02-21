import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By

from Pages.settingpage import SettingPageC


class InboxpageC:
    def __init__(self, driver):
        self.driver = driver

    header_grp = (By.XPATH, "//div[@data-rbd-droppable-id='/org/entity_1SE43R8S5D000/settings/']")
    #exp_but = (By.XPATH, "/div[@class='css-s84hkm']/")

    def settingclick(self):

        Wait = WebDriverWait(self.driver,10)
        #time.sleep(10)
        #first_cli = self.driver.find_element(*InboxpageC.exp_but).click()
        #still in progress
        Wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-rbd-droppable-id='/org/entity_1SE43R8S5D000/settings/']"))).click()

        #grp_1 = self.driver.find_element(*InboxpageC.header_grp).click()
        #grp_1[4].click()
        setpag = SettingPageC(self.driver)
        return setpag