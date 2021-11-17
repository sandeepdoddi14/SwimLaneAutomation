from main.utility.BasePage import BasePage
from main.pageobjects.locators import CreateNewRecordPageLocators


class CreateRecordpage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def set_firstName(self, firstName):
        self.getWebElement(CreateNewRecordPageLocators.firstName).clear()
        self.getWebElement(CreateNewRecordPageLocators.firstName).send_keys(firstName)

    def set_lastName(self, lastName):
        self.getWebElement(CreateNewRecordPageLocators.lastName).clear()
        self.getWebElement(CreateNewRecordPageLocators.lastName).send_keys(lastName)

    def set_city(self, city):
        self.getWebElement(CreateNewRecordPageLocators.city).clear()
        self.getWebElement(CreateNewRecordPageLocators.city).send_keys(city)

    def click_saveButton(self):
        self.getWebElement(CreateNewRecordPageLocators.saveButton).click()

    def click_saveTimeSpent(self):
        self.getWebElement(CreateNewRecordPageLocators.saveTimeSpentButton).click()

    def goToCreateNewRecordPage(self):
        self.getWebElement(CreateNewRecordPageLocators.createNewRecordButton).click()

    def isSaveButtonEnabled(self):
        return self.getWebElement(CreateNewRecordPageLocators.saveButton).is_displayed()
