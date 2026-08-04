from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class HomePage(BasePage):

    SEARCH_BOX = (
        By.NAME,
        "q"
    )

    SEARCH_BUTTON = (
        By.CLASS_NAME,
        "search-box__button--1oH7"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "div[data-qa-locator='product-item'] a"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "span.notranslate.pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl"
    )

    PRODUCT_TITLE = (
        By.TAG_NAME,
        "h1"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(ReadConfig.get_url())

    def search_product(self, product):
        self.type(self.SEARCH_BOX, product)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def get_current_page_title(self):
        return self.get_title()

    def get_current_page_url(self):
        return self.get_current_url()