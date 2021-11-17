"""
User Payload Provider Module
"""
class UserPayloadProvider:
    """
    This Class wraps the user payloads
    """

    def generate_loginpayload(self, username, password):
        """
        wraps login payload
        :param username: username
        :param password: password
        :return: login payload
        """
        payload = {"userName": username, "password": password}
        return payload
