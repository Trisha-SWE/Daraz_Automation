from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class LoginPage(BasePage):

    LOGIN_LINK = (By.LINK_TEXT, "LOGIN")

    EMAIL = (
        By.XPATH,
        "//input[@placeholder='Please enter your Phone or Email']"
    )

    PASSWORD = (
        By.XPATH,
        "//input[@placeholder='Please enter your password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'LOGIN')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(ReadConfig.get_url())

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)