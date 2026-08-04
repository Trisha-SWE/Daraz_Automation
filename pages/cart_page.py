from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class CartPage(BasePage):

    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box__button--1oH7")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-qa-locator='product-item'] a")

    ADD_TO_CART = (
        By.XPATH,
        "//*[@id='module_add_to_cart']//button[contains(@class,'pdp-button_theme_bluedaraz')]"
    )

    PRODUCT_NAME = (
        By.XPATH,
        "//h1"
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
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)