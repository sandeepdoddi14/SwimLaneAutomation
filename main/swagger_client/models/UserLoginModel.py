class UserPayloadProvider:
    def generate_loginPayload(self, username, password):
        payload = {"userName": username, "password": password}
        return payload
