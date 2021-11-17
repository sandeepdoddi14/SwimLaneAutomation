from main.providers.UserProvider import UserData
from main.swagger_client.apis.UserApi import Userapi
from main.swagger_client.models.UserLoginModel import UserPayloadProvider
from main.swagger_client.models.RecordModel import RecordPayloadProvider
from main.swagger_client.apis.RecordApi import Recordapi

RECORD_ID = ""
APP_ID = ""
recordapi = Recordapi()


def createrecord():
    """
    creates new record
    :return:
    """
    userapi = Userapi()
    loginmodel = UserPayloadProvider()

    payload = loginmodel.generate_loginpayload(
        UserData().get_username(), UserData.get_password()
    )
    response = userapi.post_userLogin(payload)
    global  APP_ID 
    APP_ID=response.json()["id"]

    createrecordpayload = RecordPayloadProvider.generate_createrecordayload()
    createrecordresponse = recordapi.post_addRecord(APP_ID, createrecordpayload)
    global  RECORD_ID
    RECORD_ID = createrecordresponse.json()["applicationId"]

    assert createrecordresponse.status_code == 200


def test_getrecord():
    """
    get record data
    :return:
    """
    getrecordresponse = recordapi.get_record(APP_ID, RECORD_ID)
    assert getrecordresponse.status_code == 200


def test_deleterecord():
    """
    delete record data
    :return:
    """
    deleterecordresponse = recordapi.delete_record(APP_ID, RECORD_ID)
    assert deleterecordresponse.status_code == 200
