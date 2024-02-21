from Pages.Inboxpage import InboxpageC
from Pages.Loginpage import LoginPage
from Pages.settingpage import SettingPageC
from Utilities.BaseClass import Baseclass


class TestTMadmin(Baseclass):

    #@pytest.mark.skip("one test skipped")
    def test_tmtoadm(self):

        self.driver.get("https://app.spruce-dev.com/login")

        zero_sp = LoginPage(self.driver)
        first_sp = LoginPage.logindetails(self,"lsspl.sprucepatient+devadmin1@gmail.com","asdf12")
        sec_sp = InboxpageC.settingclick(self)
        thrd_sp = SettingPageC.tmclick(self)


    def test_upcliname(self):
        #self.driver.get("https://app.spruce-dev.com/login")

        #LoginPage(self.driver)
        #LoginPage.logindetails(self, "lsspl.sprucepatient+devadmin1@gmail.com", "asdf12")
        #InboxpageC.settingclick(self)

        sec_run = SettingPageC.clinamup(self,"Automated Org")