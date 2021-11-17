from main.utility.BasePage import BasePage
from main.pageobjects.locators import CreateNewRecordPageLocators


class CreateRecordpage(BasePage):
    """
    Page object for new record creation
    """
    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self, firstName):
        """
        sets first name
        :param firstName: string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.FIRST_NAME).clear()
        self.get_web_element(CreateNewRecordPageLocators.FIRST_NAME).\
            send_keys(firstName)

    def set_lastname(self, lastName):
        """
        sets last name
        :param lastName:string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.LAST_NAME).clear()
        self.get_web_element(CreateNewRecordPageLocators.LAST_NAME).\
            send_keys(lastName)

    def set_city(self, city):
        """
        sets text city
        :param city: string
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.CITY).clear()
        self.get_web_element(CreateNewRecordPageLocators.CITY).\
            send_keys(city)

    def click_savebutton(self):
        """
        clicks on save button
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.SAVE_BUTTON).\
            click()

    def click_savetimespent(self):
        """
        clicks on button
        """
        self.get_web_element(CreateNewRecordPageLocators.SAVE_TIME_SPENTBUTTON).\
            click()

    def goto_newrecord_page(self):
        """
        Navigate to new record craetion page
        :return: void
        """
        self.get_web_element(CreateNewRecordPageLocators.CREATE_NEWRECORD_BUTTON).\
            click()

    def is_savebutton_enabled(self):
        """
        checks for existance
        :return: boolean
        """
        return self.get_web_element(CreateNewRecordPageLocators.SAVE_BUTTON).\
            is_displayed()
