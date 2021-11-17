"""
PAGE OBJECT
"""
import string

from testcases.ui.login_tests import LoginPageLocators
from utility.configreader import ConfigReader
from utility import basepage


class LoginPage(basepage):
    """
    page object for user login page
    """
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        """
        sets user name
        :param username: string
        :return: void
        """
        self.get_web_element(LoginPageLocators.USER_NAME, self.driver).clear()
        self.get_web_element(LoginPageLocators.USER_NAME, self.driver).\
            send_keys(username)

    def set_password(self, password):
        """
        sets password
        :param password:
        :return: void
        """
        self.get_web_element(LoginPageLocators.PASSWORD, self.driver).clear()
        self.get_web_element(LoginPageLocators.PASSWORD, self.driver).\
            send_keys(password)

    def click_loginbutton(self):
        """
        clicks on login button
        :return: void
        """
        self.get_web_element(LoginPageLocators.LOGIN_BUTTON, self.driver).click()

    def get_errormessage(self) -> string:
        """
        retrives error message container
        :return: string
        """
        return self.get_web_element(
            LoginPageLocators.LOGIN_ERROR_CONTAINER, self.driver
        ).TEXT

    def navigateto_loginpage(self):
        """
        navigate to login page
        :return: void
        """
        self.driver.get(ConfigReader().get_application_url() + "login")

    def logout(self):
        """
        user log out
        :return: void
        """
        self.driver.get(ConfigReader().get_application_url() + "logout")

    def isswimlanelogo_displayed(self):
        """
        checks if logo is displayed
        :return: boolean
        """
        return self.get_web_element(
            LoginPageLocators.SWIMLANE_LOGO, self.driver
        ).is_displayed()
