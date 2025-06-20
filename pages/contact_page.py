from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    def __init__(self,driver):
        self.driver = driver
        self.contact_link = (By.XPATH,"//a[@href='/contact_us' and contains(text(),' Contact us')]")
        self.name_input = (By.NAME,"name")
        self.email_input = (By.NAME,"email")
        self.subject_input = (By.NAME,"subject")
        self.your_message_input = (By.ID,"message")
        self.submit_button = (By.NAME,"submit")
        self.sucess_message = (By.XPATH,"//div[contains(text(),'Success! Your details have been submitted successfully.')]")
        self.consent_button_locator = (By.XPATH, "//button[./p[@class='fc-button-label' and text()='Consent']]")
        self.consent_popup_container_locator = (By.CLASS_NAME,"fc-dialog-container")

    def load(self):
        self.driver.get("https://automationexercise.com/login")

    def open_contact_us_form(self):
        self.driver.find_element(*self.contact_link).click()
    
    def fill_contact_form(self,name,email,subject,message):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.subject_input).send_keys(subject)
        self.driver.find_element(*self.your_message_input).send_keys(message)
    
    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def is_submission_successful(self):
        return self.driver.find_element(*self.sucess_message).is_displayed()
    
    def consent_button_click(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.consent_popup_container_locator))
        consent_element = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.consent_button_locator))
        consent_element.click()
        WebDriverWait(self.driver,15).until(EC.invisibility_of_element_located(self.consent_popup_container_locator))

    def accept_alert(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


        
        
