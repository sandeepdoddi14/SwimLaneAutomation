"""
Module to wrap config data
"""
import configparser


class ConfigReader:
    """
    Reader to get configuration data
    """

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read("configuration.properties")

    def get_application_url(self):
        """
        get application url
        :return: url as string
        """
        return self.config.get("applicationDetails", "applicationUrl")
