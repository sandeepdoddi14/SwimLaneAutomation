import requests
from main.utility.ConfigReader import ConfigReader


class Userapi:
    url_userlogin = ConfigReader().getApplicationUrl() + "api/user/login"

    def post_userLogin(self, payload):
        return requests.post(self.url_userlogin, json=payload)
