from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


def test_login(driver):

    logger.info("========== Login Test Started ==========")

    login = LoginPage(driver)

    logger.info("Opening Daraz")
    login.open()

    logger.info("Click Login")
    login.click_login()

    logger.info("Entering Email")
    login.enter_email(ReadConfig.get_email())

    logger.info("Entering Password")
    login.enter_password(ReadConfig.get_password())

    logger.info("Click Login Button")
    login.click_login_button()

    logger.info("Taking Screenshot")
    login.take_screenshot("screenshots/login_result.png")

    # Login Verify
    assert login.is_login_successful(), "Login Failed"

    logger.info("Login Successful")
    logger.info("========== Login Test Passed ==========")