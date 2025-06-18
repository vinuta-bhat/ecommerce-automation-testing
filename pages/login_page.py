from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.email_input = (By.NAME,"email")
        self.password_input = (By.NAME,"password")
        self.login_button = (By.XPATH,"//button[text()='Login']")
        self.consent_button_locator = (By.XPATH, "//button[./p[@class='fc-button-label' and text()='Consent']]")
        self.consent_popup_container_locator = (By.CLASS_NAME,"fc-dialog-container")
        self.logout_button = (By.XPATH,"//a[@href='/logout' and contains(text(),' Logout')]")
        self.error_message = (By.XPATH,"//p[contains(text(),'Your email or password is incorrect!')]")

   

    def load(self):
        self.driver.get("https://automationexercise.com/login")

    def enter_email(self,email):
        self.driver.find_element(*self.email_input).send_keys(email)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def consent_button_click(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.consent_popup_container_locator))
        consent_element = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.consent_button_locator))
        consent_element.click()
        WebDriverWait(self.driver,15).until(EC.invisibility_of_element_located(self.consent_popup_container_locator))

    def login(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()

    def is_login_error_displayed(self):
        return self.driver.find_element(*self.error_message).is_displayed()
