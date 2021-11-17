"""
RECORD API REQUESTS
"""
import requests
from main.utility.ConfigReader import ConfigReader


class Recordapi:
    """
    this wrapps record api requests
    """
    url_postRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_getRecord = ConfigReader().getApplicationUrl() + "api/app/"
    url_deleteRecord = ConfigReader().getApplicationUrl() + "api/app/"

    def post_addRecord(self, app_id, payload):
        """

         :param app_id: applicant id
        :param recordID: record unique id
        :return: response of add record
        """
        return requests.post(self.url_postRecord + app_id + "/record",
                             json=payload)

    def get_record(self, app_id, record_id):
        """

        :param app_id: applicant id
        :param record_id: record unique id
        :return: response of get record
        """
        return requests.get(self.url_getRecord + app_id + "/record/" +
                            record_id)

    def delete_record(self, app_id, record_id):
        """

        :param app_id: applicant id
        :param record_id: record unique id
        :return: response of delete record
        """
        return requests.delete(self.url_deleteRecord + app_id + "/record" +
                               record_id)
