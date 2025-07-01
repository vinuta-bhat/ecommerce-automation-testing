from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
        self.dropdown = (By.ID, "select-demo")
        self.result_text = (By.CLASS_NAME, "selected-value")

    def load(self):
        self.driver.get(self.dropdown_url)

    def select_day(self, day):
        dropdown_element = self.driver.find_element(*self.dropdown)
        select = Select(dropdown_element)
        select.select_by_visible_text(day)

    def get_result_text(self):
        return self.driver.find_element(*self.result_text).text
