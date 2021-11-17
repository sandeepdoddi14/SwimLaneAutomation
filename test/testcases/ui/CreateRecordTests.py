from main.pageobjects.pages.CreateRecordPage import CreateRecordpage


def test_createNewRecord(launch_driver):
    driver = launch_driver
    createRecordPage = CreateRecordpage(driver)

    createRecordPage.goToCreateNewRecordPage()
    createRecordPage.set_firstName("sandeep")
    createRecordPage.set_lastName("kumar")
    createRecordPage.set_city("vizag")
    createRecordPage.click_saveButton()
    createRecordPage.click_saveTimeSpent()

    assert createRecordPage.isSaveButtonEnabled() == False
