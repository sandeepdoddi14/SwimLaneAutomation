import time
from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from main.utility.ConfigReader import ConfigReader


@fixture(scope="module", autouse=True)
def launch_driver():
    ser = Service("../resources/drivers/chromedriver_mac")
    driver = webdriver.Chrome(service=ser)
    driver.get(ConfigReader().getApplicationUrl())
    driver.maximize_window()
    time.sleep(10)
    yield driver
    driver.quit()
