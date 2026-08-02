from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box__button--1oH7")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-qa-locator='product-item'] a")

    def __init__(self, driver):
        super().__init__(driver)

    # Open Daraz Website
    def open(self):
        self.driver.get(ReadConfig.get_url())

    # Search Product
    def search_product(self, product):
        self.type(self.SEARCH_BOX, product)

    # Click Search Button
    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    # Click First Product
    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    # Get Search Page Title
    def get_title(self):
        return self.driver.title

    # Get Product Page Title
    def get_product_title(self):
        return self.driver.title

    # Get Current URL
    def get_current_url(self):
        return self.driver.current_url

    # Take Screenshot
    def take_screenshot(self):
        self.driver.save_screenshot("screenshots/product.png")