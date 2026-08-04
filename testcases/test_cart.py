from pages.cart_page import CartPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


def test_add_to_cart(driver):

    logger.info("========== Cart Test Started ==========")

    cart = CartPage(driver)

    cart.open()

    cart.search_product(ReadConfig.get_product())

    cart.click_search()

    cart.click_first_product()

    cart.switch_to_new_tab()

    product_name = cart.get_product_name()

    cart.click_add_to_cart()

    cart.take_screenshot("screenshots/cart.png")

    assert product_name != ""

    logger.info("========== Cart Test Passed ==========")