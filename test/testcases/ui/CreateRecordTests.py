from main.pageobjects.pages.CreateRecordPage import CreateRecordpage


def test_create_newrecord(launch_driver):
    driver = launch_driver
    createRecordPage = CreateRecordpage(driver)

    createRecordPage.goto_newrecord_page()
    createRecordPage.set_firstname("sandeep")
    createRecordPage.set_lastname("kumar")
    createRecordPage.set_city("vizag")
    createRecordPage.click_savebutton()
    createRecordPage.click_savetimespent()

    assert not createRecordPage.is_savebutton_enabled()
