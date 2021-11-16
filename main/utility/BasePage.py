from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def getWebElement(self, element_locator, driver) -> WebElement:
        words = element_locator.split(",")
        locatorStrategy = words[0]
        locator = words[1]
        if (locatorStrategy.__contains__("id")):
            return driver.find_element(By.ID, locator)
        if (locatorStrategy.__contains__("class")):
            return driver.find_element(By.CLASS_NAME, locator)
        elif locatorStrategy.__contains__("xpath"):
            return driver.find_element(By.XPATH, locator)

    def waitForTheElement(self,element_locator,driver):
        elementExists=False
        while(elementExists==False):
            try:
               self.getWebElement(element_locator,driver)
               elementExists=True
            except Exception as e:
                print("Exception cought while Get Element"+e.with_traceback())


