import yaml
class UserData:
    path = "../resources/testdata/User.yaml"

    def __init__(self):
        with open(self.path, 'r') as file:
          self.prime_service = yaml.safe_load(file)

    def  get_userName(self):
        self.prime_service['user']['username']

    def get_password(self):
        self.prime_service['user']['password']