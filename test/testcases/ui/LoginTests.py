import time
from main.pageobjects.pages.LoginPage import LoginPage
from main.providers.UserProvider import UserData
from main.pageobjects.locators import LoginPageLocators
from main.pageobjects.locators import CreateNewRecordPageLocators


def test_verifySwimLaneLogo(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)
    assert loginPage.isswimlanelogo_displayed()


def test_loginWithValidCredentials(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(CreateNewRecordPageLocators.CREATE_NEWRECORD_BUTTON)
    assert not loginPage.isswimlanelogo_displayed()

    loginPage.logout()


def test_loginWithInvalidUserName(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginpage()
    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginPage.get_errormessage().__contains__("Login failed")


def test_loginWithInvalidPassword(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginpage()
    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_BUTTON)

    loginPage.set_username(UserData().get_username())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginbutton()

    loginPage.wait_for_the_element(LoginPageLocators.LOGIN_ERROR_CONTAINER)
    assert loginPage.get_errormessage().__contains__("Login failed")
