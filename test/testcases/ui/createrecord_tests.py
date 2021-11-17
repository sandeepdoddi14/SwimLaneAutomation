"""
TESTS FOR CREATE NEW RECORD
"""
from pageobjects.pages.createrecord_pom import CreateRecordpage


def test_create_newrecord(launch_driver):
    """
    creates new record and verifies save button availablity
    :param launch_driver:
    :return:
    """
    driver = launch_driver
    createrecordpage = CreateRecordpage(driver)

    createrecordpage.goto_newrecord_page()
    createrecordpage.set_firstname("sandeep")
    createrecordpage.set_lastname("kumar")
    createrecordpage.set_city("vizag")
    createrecordpage.click_savebutton()
    createrecordpage.click_savetimespent()

    assert not createrecordpage.is_savebutton_enabled()
