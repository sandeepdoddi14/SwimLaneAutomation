"""
Wrapper code which has common implementation for pages
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
    This class provides common helper methods for page objects
    """

    def get_web_element(self, element_locator, driver) -> WebElement:
        """
        returns web element
        :param element_locator: takes from locator file
        :param driver: webdriver instance
        :return: webelement
        """
        words = element_locator.split(",")
        locator_strategy = words[0]
        locator = words[1]
        if locator_strategy.__contains__("id"):
            return driver.find_element(By.ID, locator)
        if locator_strategy.__contains__("class"):
            return driver.find_element(By.CLASS_NAME, locator)
        if locator_strategy.__contains__("xpath"):
            return driver.find_element(By.XPATH, locator)

    def wait_for_the_element(self, element_locator, driver):
        """
        polls for existence of element
        :param element_locator: element locator string
        :param driver: driver instance
        :return: void
        """
        ispresent = False
        while not ispresent:
            try:
                self.get_web_element(element_locator, driver)
                ispresent = True
            except Exception as error:
                print("Exception cought while Get Element" + error)
