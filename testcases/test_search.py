# def test_open_browser(driver):
#     driver.get("https://www.daraz.com.bd/")



from pages.home_page import HomePage

def test_search(driver):
    home = HomePage(driver)

    home.open()
    home.search_product("Laptop")
    home.click_search()
    home.click_first_product()

    assert "Laptop" in home.get_title()