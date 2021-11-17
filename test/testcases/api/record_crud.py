"""
TESTS
"""
from providers.user_provider import UserData
from swagger_client.apis.record_api import Recordapi
from swagger_client.apis.user_api import Userapi
from swagger_client.models.record_model import RecordPayloadProvider
from swagger_client.models.userlogin_model import UserPayloadProvider

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
