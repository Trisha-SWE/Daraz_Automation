from pages.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen

logger = LogGen.loggen()


def test_product_price(driver):

    logger.info("========== Product Price Test Started ==========")

    home = HomePage(driver)

    home.open()

    home.search_product(ReadConfig.get_product())

    home.click_search()

    home.click_first_product()

    home.switch_to_new_tab()

    price = home.get_product_price()

    print("Product Price:", price)

    assert price != ""

    home.take_screenshot("screenshots/product_price.png")

    logger.info("========== Product Price Test Passed ==========")