import configparser

config = configparser.RawConfigParser()
config.read("./config/config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_product():
        return config.get("common info", "productName")

    @staticmethod
    def get_browser():
        return config.get("common info", "browser")