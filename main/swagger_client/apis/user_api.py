"""
USER API REQUESTS
"""
import requests
from utility.configreader import ConfigReader


class Userapi:
    """
    Class contains requests wrapped for user api
    """
    url_userlogin = ConfigReader().get_application_url() + "api/user/login"

    def post_userlogin(self, payload):
        """
        posts the payload information
        :param payload: user login payload with data
        :return: response of user login
        """
        return requests.post(self.url_userlogin, json=payload)
