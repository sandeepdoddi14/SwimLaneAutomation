from main.utility.BasePage import BasePage
from main.pageobjects.locators import CreateNewRecordPageLocators


class CreateRecordpage(BasePage):
    """
    Page object for new record creation
    """
    def __init__(self, driver):
        self.driver = driver

    def set_firstName(self, firstName):
        """
        sets first name
        :param firstName: string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.firstName).clear()
        self.get_web_element(CreateNewRecordPageLocators.firstName).\
            send_keys(firstName)

    def set_lastName(self, lastName):
        """
        sets last name
        :param lastName:string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.lastName).clear()
        self.get_web_element(CreateNewRecordPageLocators.lastName).\
            send_keys(lastName)

    def set_city(self, city):
        """
        sets text city
        :param city: string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.city).clear()
        self.get_web_element(CreateNewRecordPageLocators.city).\
            send_keys(city)

    def click_saveButton(self):
        """
        clicks on save button
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.saveButton).\
            click()

    def click_saveTimeSpent(self):
        """
        clicks on button
        """
        self.get_web_element(CreateNewRecordPageLocators.saveTimeSpentButton).\
            click()

    def goToCreateNewRecordPage(self):
        """
        Navigate to new record craetion page
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.createNewRecordButton).\
            click()

    def isSaveButtonEnabled(self):
        """
        checks for existance
        :return: boolean
        """
        return self.get_web_element(CreateNewRecordPageLocators.saveButton).\
            is_displayed()
