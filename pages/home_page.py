# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class HomePage:

#     SEARCH_BOX = (By.NAME, "q")

#     def __init__(self, driver):
#         self.driver = driver

#     def open(self):
#         self.driver.get("https://www.daraz.com.bd/")

#     def search_product(self, product):
#         self.driver.find_element(*self.SEARCH_BOX).send_keys(product)
#         self.driver.find_element(*self.SEARCH_BOX).send_keys(Keys.ENTER)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box__button--1oH7")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-qa-locator='product-item'] a")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.daraz.com.bd/")

    def search_product(self, product):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_title(self):
        return self.driver.title

    def click_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )
        self.driver.find_element(*self.FIRST_PRODUCT).click()