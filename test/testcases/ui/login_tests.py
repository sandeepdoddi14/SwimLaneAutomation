"""
TESTS FOR LOGIN PAGE
"""

from pageobjects.locators import loginpage_locator, createnewrecord_locator
from pageobjects.pages.login_pom import LoginPage
from providers.user_provider import UserData


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

    loginpage.wait_for_the_element(createnewrecord_locator.CREATE_NEWRECORD_BUTTON)
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
    loginpage.wait_for_the_element(loginpage_locator.LOGIN_BUTTON)

    loginpage.set_username(UserData().get_username())
    loginpage.set_password(UserData().get_password())
    loginpage.click_loginbutton()

    loginpage.wait_for_the_element(loginpage_locator.LOGIN_ERROR_CONTAINER)
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
    loginpage.wait_for_the_element(loginpage_locator.LOGIN_BUTTON)

    loginpage.set_username(UserData().get_username())
    loginpage.set_password(UserData().get_password())
    loginpage.click_loginbutton()

    loginpage.wait_for_the_element(loginpage_locator.LOGIN_ERROR_CONTAINER)
    assert loginpage.get_errormessage().__contains__("Login failed")
