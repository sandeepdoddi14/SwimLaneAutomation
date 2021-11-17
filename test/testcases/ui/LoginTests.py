import time
from main.pageobjects.pages.LoginPage import LoginPage
from main.providers.UserProvider import UserData
from main.pageobjects.locators import LoginPageLocators
from main.pageobjects.locators import CreateNewRecordPageLocators


def test_verifyswimlanelogo(launch_driver):
    """
    logo verification
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginpage = LoginPage(driver)
    assert loginpage.isswimlanelogo_displayed()


def test_loginwithvalidcredentials(launch_driver):
    """
    login withn valid data
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginpage = LoginPage(driver)

    loginpage.set_username(UserData().get_username())
    loginpage.set_password(UserData().get_password())
    loginpage.click_loginbutton()

    loginpage.wait_for_the_element(CreateNewRecordPageLocators.CREATE_NEWRECORD_BUTTON)
    assert not loginpage.isswimlanelogo_displayed()

    loginpage.logout()


def test_loginwithinvalidusername(launch_driver):
    """
    negitive test case
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginpage = LoginPage(driver)

    loginpage.navigateto_loginpage()
    loginpage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginpage.set_username(UserData().get_username())
    loginpage.set_password(UserData().get_password())
    loginpage.click_loginbutton()

    loginpage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginpage.get_errormessage().__contains__("Login failed")


def test_loginwith_invalidpassword(launch_driver):
    """
    negitive test case
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginpage = LoginPage(driver)

    loginpage.navigateto_loginpage()
    loginpage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginpage.set_username(UserData().get_username())
    loginpage.set_password(UserData().get_password())
    loginpage.click_loginbutton()

    loginpage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginpage.get_errormessage().__contains__("Login failed")
