from pages.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


def test_search(driver):

    logger.info("========== Search Test Started ==========")

    home = HomePage(driver)

    logger.info("Opening Daraz Website")
    home.open()

    product = ReadConfig.get_product()

    logger.info(f"Searching Product: {product}")
    home.search_product(product)

    logger.info("Clicking Search Button")
    home.click_search()

    logger.info("Opening First Product")
    home.click_first_product()

    logger.info("Getting Product Information")

    product_title = home.get_product_title()
    product_price = home.get_product_price()
    product_url = home.get_current_url()

    print(f"\nProduct Title : {product_title}")
    print(f"Product Price : {product_price}")
    print(f"Product URL   : {product_url}")

    logger.info(f"Product Title : {product_title}")
    logger.info(f"Product Price : {product_price}")
    logger.info(f"Product URL : {product_url}")

    home.take_screenshot("screenshots/search_result.png")

    assert product_title != "", "Product title is empty."
    assert product_price != "", "Product price is empty."

    logger.info("Search Test Passed")
    logger.info("========== Search Test Finished ==========")

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