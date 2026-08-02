from pages.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen

logger = LogGen.loggen()


def test_search(driver):

    logger.info("********** Test Started **********")

    home = HomePage(driver)

    logger.info("Opening Daraz Website")
    home.open()

    logger.info("Searching Product")
    home.search_product(ReadConfig.get_product())

    logger.info("Clicking Search Button")
    home.click_search()

    logger.info("Clicking First Product")
    home.click_first_product()

    logger.info("Verifying Product Title")
    print(home.get_product_title())

    assert ReadConfig.get_product().lower() in home.get_product_title().lower()

    logger.info("Taking Screenshot")
    home.take_screenshot()

    logger.info("********** Test Passed **********")