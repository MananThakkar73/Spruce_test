import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"],scope="class")
def startup(request):
    if request.param == "chrome":
        #option = webdriver.ChromeOptions()
        #driver = webdriver.Chrome(executable_path="E:\\Drivers\\chromedriver")
        #driver = webdriver.Chrome(executable_path="/Users/mt00821132/drivers/chromedriver")
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield
    driver.close()