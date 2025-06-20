from pages.contact_page import ContactPage

def test_contact_form_submission(driver):
    contact_page = ContactPage(driver)
    contact_page.load()
    contact_page.consent_button_click()
    contact_page.open_contact_us_form()
    contact_page.fill_contact_form("Tester1","tester1@example.com","Feedback","This is a test message. ")
    contact_page.submit_form()
    contact_page.accept_alert()
    assert contact_page.is_submission_successful()