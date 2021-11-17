import requests
from main.utility.ConfigReader import ConfigReader


class Recordapi:
    url_postRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_getRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_deleteRecord = ConfigReader().getApplicationUrl() + "api/app/"

    def post_addRecord(self, appID, payload):
        return requests.post(self.url_postRecord + appID + "/record",
                             json=payload)

    def get_record(self, appID, recordID):
        return requests.get(self.url_getRecord + appID + "/record/" +
                            recordID)

    def delete_record(self, appID, recordID):
        return requests.delete(self.url_deleteRecord + appID + "/record" +
                               recordID)
