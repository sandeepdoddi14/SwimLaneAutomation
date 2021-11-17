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
    loginPage = LoginPage(driver)
    assert loginPage.isswimlanelogo_displayed()


def test_loginwithvalidcredentials(launch_driver):
    """
    login withn valid data
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(CreateNewRecordPageLocators.CREATE_NEWRECORD_BUTTON)
    assert not loginPage.isswimlanelogo_displayed()

    loginPage.logout()


def test_loginwithinvalidusername(launch_driver):
    """
    negitive test case
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginpage()
    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginPage.get_errormessage().__contains__("Login failed")


def test_loginwith_invalidpassword(launch_driver):
    """
    negitive test case
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginpage()
    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginPage.get_errormessage().__contains__("Login failed")
