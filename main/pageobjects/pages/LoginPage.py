import string

from main.utility.BasePage import BasePage
from main.pageobjects.locators import LoginPageLocators
from main.utility.ConfigReader import ConfigReader


class LoginPage(BasePage):
    """
    page object for user login page
    """
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, userName):
        """
        sets user name
        :param userName: string
        :return: void
        """
        self.get_web_element(LoginPageLocators.userName, self.driver).clear()
        self.get_web_element(LoginPageLocators.userName, self.driver).\
            send_keys(userName)

    def set_password(self, password):
        """
        sets password
        :param password:
        :return: void
        """
        self.get_web_element(LoginPageLocators.password, self.driver).clear()
        self.get_web_element(LoginPageLocators.password, self.driver).\
            send_keys(password)

    def click_loginbutton(self):
        """
        clicks on login button
        :return: void
        """
        self.get_web_element(LoginPageLocators.loginButton, self.driver).click()

    def get_errormessage(self) -> string:
        """
        retrives error message container
        :return: string
        """
        return self.get_web_element(
            LoginPageLocators.loginErrorContainer, self.driver
        ).text

    def navigateto_loginpage(self):
        """
        navigate to login page
        :return: void
        """
        self.driver.get(ConfigReader().getApplicationUrl() + "login")

    def logout(self):
        """
        user log out
        :return: void
        """
        self.driver.get(ConfigReader().getApplicationUrl() + "logout")

    def isswimlanelogo_displayed(self):
        """
        checks if logo is displayed
        :return: boolean
        """
        return self.get_web_element(
            LoginPageLocators.swimlaneLogo, self.driver
        ).is_displayed()
