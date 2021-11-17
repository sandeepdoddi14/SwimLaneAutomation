"""
USER DATA PROVIDER
"""
import yaml


class UserData:
    """
    retrieve data from yaml
    """
    path = "../resources/testdata/User.yaml"

    def __init__(self):
        with open(self.path, 'r') as file:
            self.prime_service = yaml.safe_load(file)

    def get_username(self):
        """

        :return: user name
        """
        return self.prime_service['user']['username']

    def get_password(self):
        """

        :return: password
        """
        return self.prime_service['user']['password']
