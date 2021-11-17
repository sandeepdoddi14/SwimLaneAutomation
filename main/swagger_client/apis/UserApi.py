import requests
from main.utility.ConfigReader import ConfigReader


class Userapi:
    """
    Class contains requests wrapped for user api
    """
    url_userlogin = ConfigReader().getApplicationUrl() + "api/user/login"

    def post_userLogin(self, payload):
        """
        posts the payload information
        :param payload: user login payload with data
        :return: response of user login
        """
        return requests.post(self.url_userlogin, json=payload)
