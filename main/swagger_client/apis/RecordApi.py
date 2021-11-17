import requests
from main.utility.ConfigReader import ConfigReader


class Recordapi:
    """
    this wrapps record api requests
    """
    url_postRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_getRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_deleteRecord = ConfigReader().getApplicationUrl() + "api/app/"

    def post_addRecord(self, appID, payload):
        """

         :param appID: applicant id
        :param recordID: record unique id
        :return: response of add record
        """
        return requests.post(self.url_postRecord + appID + "/record",
                             json=payload)

    def get_record(self, appID, recordID):
        """

        :param appID: applicant id
        :param recordID: record unique id
        :return: response of get record
        """
        return requests.get(self.url_getRecord + appID + "/record/" +
                            recordID)

    def delete_record(self, appID, recordID):
        """

        :param appID: applicant id
        :param recordID: record unique id
        :return: response of delete record
        """
        return requests.delete(self.url_deleteRecord + appID + "/record" +
                               recordID)
