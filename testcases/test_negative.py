from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


# =========================================================
# TEST 1: INVALID PASSWORD
# =========================================================

def test_invalid_password(driver):

    logger.info(
        "========== INVALID PASSWORD TEST STARTED =========="
    )

    login = LoginPage(driver)

    # =========================
    # STEP 1: OPEN DARAZ
    # =========================

    logger.info(
        "STEP 1: Opening Daraz"
    )

    login.open()

    # =========================
    # STEP 2: CLICK LOGIN
    # =========================

    logger.info(
        "STEP 2: Clicking Login"
    )

    login.click_login()

    # =========================
    # STEP 3: ENTER VALID EMAIL
    # =========================

    logger.info(
        "STEP 3: Entering valid email"
    )

    email = ReadConfig.get_email()

    login.enter_email(
        email
    )

    # =========================
    # STEP 4: ENTER INVALID PASSWORD
    # =========================

    logger.info(
        "STEP 4: Entering invalid password"
    )

    invalid_password = "WrongPassword123456"

    login.enter_password(
        invalid_password
    )

    # =========================
    # STEP 5: CLICK LOGIN
    # =========================

    logger.info(
        "STEP 5: Clicking Login"
    )

    login.click_login_button()

    # =========================
    # STEP 6: TAKE SCREENSHOT
    # =========================

    logger.info(
        "STEP 6: Taking Screenshot"
    )

    login.take_screenshot(
        "screenshots/invalid_password.png"
    )

    # =========================
    # STEP 7: VERIFY LOGIN FAILED
    # =========================

    logger.info(
        "STEP 7: Verifying Invalid Password"
    )

    login_failed = login.is_login_failed()

    print(
        "\n========== INVALID PASSWORD RESULT =========="
    )

    print(
        "Login failed:",
        login_failed
    )

    # Invalid password দিয়ে login করা উচিত নয়
    assert login_failed, (
        "BUG: User was able to login with an invalid password."
    )

    logger.info(
        "Invalid Password Test Passed"
    )

    logger.info(
        "========== INVALID PASSWORD TEST FINISHED =========="
    )


# =========================================================
# TEST 2: INVALID EMAIL FORMAT
# =========================================================

def test_invalid_email_format(driver):

    logger.info(
        "========== INVALID EMAIL TEST STARTED =========="
    )

    login = LoginPage(driver)

    # =========================
    # STEP 1: OPEN DARAZ
    # =========================

    logger.info(
        "STEP 1: Opening Daraz"
    )

    login.open()

    # =========================
    # STEP 2: CLICK LOGIN
    # =========================

    logger.info(
        "STEP 2: Clicking Login"
    )

    login.click_login()

    # =========================
    # STEP 3: ENTER INVALID EMAIL
    # =========================

    logger.info(
        "STEP 3: Entering invalid email"
    )

    invalid_email = "invalid-email"

    login.enter_email(
        invalid_email
    )

    # =========================
    # STEP 4: ENTER PASSWORD
    # =========================

    logger.info(
        "STEP 4: Entering password"
    )

    password = ReadConfig.get_password()

    login.enter_password(
        password
    )

    # =========================
    # STEP 5: CLICK LOGIN
    # =========================

    logger.info(
        "STEP 5: Clicking Login"
    )

    login.click_login_button()

    # =========================
    # STEP 6: TAKE SCREENSHOT
    # =========================

    logger.info(
        "STEP 6: Taking Screenshot"
    )

    login.take_screenshot(
        "screenshots/invalid_email.png"
    )

    # =========================
    # STEP 7: VERIFY LOGIN FAILED
    # =========================

    logger.info(
        "STEP 7: Verifying Invalid Email"
    )

    login_failed = login.is_login_failed()

    print(
        "\n========== INVALID EMAIL RESULT =========="
    )

    print(
        "Login failed:",
        login_failed
    )

    # Invalid email দিয়ে login করা উচিত নয়
    assert login_failed, (
        "BUG: User was able to login with an invalid email."
    )

    logger.info(
        "Invalid Email Test Passed"
    )

    logger.info(
        "========== INVALID EMAIL TEST FINISHED =========="
    )


# =========================================================
# TEST 3: WHITESPACE-ONLY SEARCH (BUG-01)
# =========================================================

def test_whitespace_only_search_is_rejected(driver):

    logger.info(
        "========== WHITESPACE-ONLY SEARCH TEST STARTED =========="
    )

    home = HomePage(driver)

    # =========================
    # STEP 1: OPEN DARAZ
    # =========================

    logger.info(
        "STEP 1: Opening Daraz"
    )

    home.open()

    # =========================
    # STEP 2: ENTER WHITESPACE-ONLY SEARCH
    # =========================

    logger.info(
        "STEP 2: Entering whitespace-only search input"
    )

    home.search_product(" ")

    # =========================
    # STEP 3: CLICK SEARCH
    # =========================

    logger.info(
        "STEP 3: Clicking Search"
    )

    home.click_search()

    # =========================
    # STEP 4: TAKE SCREENSHOT
    # =========================

    logger.info(
        "STEP 4: Taking Screenshot"
    )

    home.take_screenshot(
        "screenshots/BUG-01_whitespace_search.png"
    )

    # =========================
    # STEP 5: VERIFY SEARCH WAS REJECTED
    # =========================

    logger.info(
        "STEP 5: Verifying whitespace-only search was rejected"
    )

    current_url = home.get_current_page_url()

    print(
        "\n========== WHITESPACE-ONLY SEARCH RESULT =========="
    )

    print(
        "Current URL:",
        current_url
    )

    # Whitespace-only search গ্রহণ করা উচিত নয়
    assert "q=%20" not in current_url, (
        f"BUG-01: Whitespace-only search was accepted by the system. "
        f"Actual URL: {current_url}"
    )

    logger.info(
        "Whitespace-Only Search Test Passed"
    )

    logger.info(
        "========== WHITESPACE-ONLY SEARCH TEST FINISHED =========="
    )