"""
PAGE OBJECT
"""
from pageobjects.locators import createnewrecord_locator
from utility.basepage import BasePage


class CreateRecordpage(BasePage):
    """
    Page object for new record creation
    """

    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self, firstname):
        """
        sets first name
        :param firstname: string
        :return: void
        """
        self.get_web_element(createnewrecord_locator.FIRST_NAME,self.driver).clear()
        self.get_web_element(createnewrecord_locator.FIRST_NAME,self.driver). \
            send_keys(firstname)

    def set_lastname(self, lastname):
        """
        sets last name
        :param lastname:string
        :return: void
        """
        self.get_web_element(createnewrecord_locator.LAST_NAME,self.driver).clear()
        self.get_web_element(createnewrecord_locator.LAST_NAME,self.driver). \
            send_keys(lastname)

    def set_city(self, city):
        """
        sets text city
        :param city: string
        :return: void
        """
        self.get_web_element(createnewrecord_locator.CITY,self.driver).clear()
        self.get_web_element(createnewrecord_locator.CITY,self.driver). \
            send_keys(city)

    def click_savebutton(self):
        """
        clicks on save button
        :return: void
        """
        self.get_web_element(createnewrecord_locator.SAVE_BUTTON,self.driver). \
            click()

    def click_savetimespent(self):
        """
        clicks on button
        """
        self.get_web_element(createnewrecord_locator.SAVE_TIME_SPENTBUTTON,self.driver). \
            click()

    def goto_newrecord_page(self):
        """
        Navigate to new record craetion page
        :return: void
        """
        self.get_web_element(createnewrecord_locator.CREATE_NEWRECORD_BUTTON,self.driver). \
            click()

    def is_savebutton_enabled(self):
        """
        checks for existance
        :return: boolean
        """
        return self.get_web_element(createnewrecord_locator.SAVE_BUTTON,self.driver). \
            is_displayed()
