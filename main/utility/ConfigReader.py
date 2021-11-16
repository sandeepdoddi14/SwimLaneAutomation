import configparser

class ConfigReader:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read('configuration.properties')

    def getApplicationUrl(self):
        return self.config.get('applicationDetails', 'applicationUrl')
