import string

from main.utility.BasePage import BasePage
from main.pageobjects.locators import LoginPageLocators
from main.utility.ConfigReader import ConfigReader

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def set_userName(self, userName):
        self.getWebElement(LoginPageLocators.userName, self.driver).clear()
        self.getWebElement(LoginPageLocators.userName, self.driver).send_keys(userName)

    def set_password(self, password):
        self.getWebElement(LoginPageLocators.password, self.driver).clear()
        self.getWebElement(LoginPageLocators.password, self.driver).send_keys(password)

    def click_loginButton(self):
        self.getWebElement(LoginPageLocators.loginButton, self.driver).click()

    def get_errorMessage(self)->string:
        return self.getWebElement(LoginPageLocators.loginErrorContainer, self.driver).text

    def navigateto_loginPage(self):
        self.driver.get(ConfigReader().getApplicationUrl()+"login")

    def logout(self):
        self.driver.get(ConfigReader().getApplicationUrl()+"logout")

    def isSwimLaneLogoDisplayed(self):
        return self.getWebElement(LoginPageLocators.swimlaneLogo, self.driver).is_displayed()
