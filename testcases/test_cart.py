from pages.cart_page import CartPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


def test_add_to_cart(driver):

    logger.info("********** Cart Test Started **********")

    cart = CartPage(driver)

    logger.info("Opening Daraz Website")
    cart.open()

    logger.info("Searching Product")
    cart.search_product(ReadConfig.get_product())

    logger.info("Clicking Search Button")
    cart.click_search()

    logger.info("Clicking First Product")
    cart.click_first_product()

    logger.info("Switching to Product Tab")
    cart.switch_to_new_tab()

    logger.info("Clicking Add To Cart")
    cart.click_add_to_cart()

    print("Product added to cart successfully.")

    cart.take_screenshot("screenshots/cart.png")

    logger.info("Screenshot Taken")

    logger.info("********** Cart Test Passed **********")