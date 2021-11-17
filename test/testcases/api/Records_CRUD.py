from main.providers.UserProvider import UserData
from main.swagger_client.apis.UserApi import Userapi
from main.swagger_client.models.UserLoginModel import UserPayloadProvider
from main.swagger_client.models.RecordModel import RecordPayloadProvider
from main.swagger_client.apis.RecordApi import Recordapi

global recordID
global appID
recordapi = Recordapi()


def createRecord():
    userApi = Userapi()
    loginModel = UserPayloadProvider()

    payload = loginModel.generate_loginPayload(
        UserData().get_userName(), UserData.get_password()
    )
    response = userApi.post_userLogin(payload)
    appID = response.json()["id"]

    createRecordPayload = RecordPayloadProvider.generate_createRecordPayload()
    createRecordResponse = recordapi.post_addRecord(appID, createRecordPayload)
    recordID = createRecordResponse.json()["applicationId"]

    assert createRecordResponse.status_code == 200


def test_getRecord():
    getRecordResponse = recordapi.get_record(appID, recordID)
    assert getRecordResponse.status_code == 200


def test_deleteRecord():
    deleteRecordResponse = recordapi.delete_record(appID, recordID)
    assert deleteRecordResponse.status_code == 200
