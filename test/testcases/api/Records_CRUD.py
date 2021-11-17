from main.providers.UserProvider import UserData
from main.swagger_client.apis.UserApi import Userapi
from main.swagger_client.models.UserLoginModel import UserPayloadProvider
from main.swagger_client.models.RecordModel import RecordPayloadProvider
from main.swagger_client.apis.RecordApi import Recordapi

global record_id
global app_id
recordapi = Recordapi()


def createrecord():
    """
    creates new record
    :return:
    """
    userApi = Userapi()
    loginModel = UserPayloadProvider()

    payload = loginModel.generate_loginpayload(
        UserData().get_username(), UserData.get_password()
    )
    response = userApi.post_userLogin(payload)
    app_id = response.json()["id"]

    createRecordPayload = RecordPayloadProvider.generate_createrecordayload()
    createRecordResponse = recordapi.post_addRecord(app_id, createRecordPayload)
    record_id = createRecordResponse.json()["applicationId"]

    assert createRecordResponse.status_code == 200


def test_getrecord():
    """
    get record data
    :return:
    """
    getRecordResponse = recordapi.get_record(app_id, record_id)
    assert getRecordResponse.status_code == 200


def test_deleterecord():
    """
    delete record data
    :return:
    """
    deleteRecordResponse = recordapi.delete_record(app_id, record_id)
    assert deleteRecordResponse.status_code == 200
