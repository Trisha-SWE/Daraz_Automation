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

    logger.info("Getting Product Information")

    title = home.get_product_title()
    price = home.get_product_price()
    url = home.get_current_url()

    print("Product Title:", title)
    print("Product Price:", price)
    print("Product URL:", url)

    logger.info("Verifying Product Title")
    assert ReadConfig.get_product().lower() in title.lower()

    logger.info("Verifying Product Price")
    assert len(price) > 0

    logger.info("Taking Screenshot")
    home.take_screenshot("screenshots/product.png")

    logger.info("********** Test Passed **********")