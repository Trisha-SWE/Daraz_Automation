from configparser import ConfigParser


class ReadConfig:
    """
    Read values from config.ini
    """

    config = ConfigParser()
    config.read("config/config.ini")

    @staticmethod
    def get_url():
        return ReadConfig.config.get("common", "baseURL")

    @staticmethod
    def get_product():
        return ReadConfig.config.get("common", "product")

    @staticmethod
    def get_email():
        return ReadConfig.config.get("common", "email")

    @staticmethod
    def get_password():
        return ReadConfig.config.get("common", "password")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")

    @staticmethod
    def get_timeout():
        return ReadConfig.config.getint("common", "timeout")