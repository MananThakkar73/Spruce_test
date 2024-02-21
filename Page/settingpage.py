import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

#from Pages.Inboxpage import InboxpageC


class SettingPageC:
    def __init__(self, driver):
        self.driver = driver

    tmmate = (By.XPATH, "//a[text()='Teammates']")
    tmmate_grp = (By.XPATH, "//div[@class='css-1bxnwe5']")
    p_to_ad = (By.XPATH, "//div[@class='css-19isju1'][text()='Promote to Admin']")
    adm_con = (By.XPATH,"//div[@class='css-19isju1'][text()='Promote']")
    tm_ad_nam = (By.XPATH,"//div[@class='css-134rf3e'][text()='clinic tm 002, tm']")

    def tmclick(self):

        time.sleep(5)
        self.driver.find_element(*SettingPageC.tmmate).click()

        tm_grp = self.driver.find_elements(*SettingPageC.tmmate_grp)
        tm_grp[1].click()

        self.driver.find_element(*SettingPageC.p_to_ad).click()

        time.sleep(5)

        self.driver.find_element(*SettingPageC.adm_con).click()

        tm_nam = self.driver.find_element(*SettingPageC.tm_ad_nam).text


        return print(tm_nam,"is now an admin")

    org_pro = (By.XPATH,"//a[text()='Organization Profile']")
    edit_pro = (By.XPATH,"//div[@data-test-id='UI.Settings.ClinicProfile.Button']")
    fir_fra = (By.XPATH,"//div[@class='css-yn0ymo']")
    cli_nam_inp = (By.NAME,"displayName")
    sav_cli = (By.XPATH,"//div[text()='Save']")

    def clinamup(self, orgnam):

        time.sleep(5)

        self.driver.find_element(*SettingPageC.org_pro).click()

        time.sleep(5)

        self.driver.find_element(*SettingPageC.edit_pro).click()

        #self.driver.switch_to_frame(*SettingPageC.fir_fra)

        time.sleep(5)

        self.driver.find_element(*SettingPageC.cli_nam_inp).click()


        self.driver.find_element(*SettingPageC.cli_nam_inp).send_keys(orgnam)

        time.sleep(5)

        self.driver.find_element(*SettingPageC.sav_cli).click()

        return print("Organization name has been updated")





