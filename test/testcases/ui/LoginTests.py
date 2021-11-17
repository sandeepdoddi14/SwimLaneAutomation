import time
from main.pageobjects.pages.LoginPage import LoginPage
from main.providers.UserProvider import UserData
from main.pageobjects.locators import LoginPageLocators
from main.pageobjects.locators import CreateNewRecordPageLocators


def test_verifySwimLaneLogo(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)
    assert loginPage.isSwimLaneLogoDisplayed() == True


def test_loginWithValidCredentials(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.set_userName(UserData().get_userName())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginButton()

    loginPage.waitForTheElement(CreateNewRecordPageLocators.createNewRecordButton)
    assert loginPage.isSwimLaneLogoDisplayed() == False

    loginPage.logout()


def test_loginWithInvalidUserName(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginPage()
    loginPage.waitForTheElement(LoginPageLocators.loginButton)

    loginPage.set_userName(UserData().get_userName())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginButton()

    loginPage.waitForTheElement(LoginPageLocators.loginErrorContainer)
    assert loginPage.get_errorMessage().__contains__("Login failed")


def test_loginWithInvalidPassword(launch_driver):
    driver = launch_driver
    loginPage = LoginPage(driver)

    loginPage.navigateto_loginPage()
    loginPage.waitForTheElement(LoginPageLocators.loginButton)

    loginPage.set_userName(UserData().get_userName())
    loginPage.set_password(UserData().get_password())
    loginPage.click_loginButton()

    loginPage.waitForTheElement(LoginPageLocators.loginErrorContainer)
    assert loginPage.get_errorMessage().__contains__("Login failed")
