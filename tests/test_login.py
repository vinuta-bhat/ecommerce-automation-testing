from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.consent_button_click()
    login_page.login("test_user@testing.com","test@123")
    assert "Logged in as" in driver.page_source

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.consent_button_click()
    login_page.login("test_user1@testing.com","test@123")
    assert login_page.is_login_error_displayed()