from .base_page import BasePage
from selenium.webdriver.common.by import By


class ClassAttributePage(BasePage):
    
    PRIMARY_BUTTON = (
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]",
    )
    SUCCESS_BUTTON = (
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-success ')]",        
    )
    WARNING_BUTTON = (
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-warning ')]",        
    )
    ALERT_TEXT = "Primary button pressed"


    def click_to_primary_button(self):
        element = self.driver.find_element(*self.PRIMARY_BUTTON)
        element.click()

    def click_to_success_button(self):
        element = self.driver.find_element(*self.SUCCESS_BUTTON)
        element.click()

    def click_to_warning_button(self):
        element = self.driver.find_element(*self.WARNING_BUTTON)
        element.click()
    
    def get_alert_text(self):
        alert = self.driver.switch_to_alert()
        return alert.text
        
    def accept_alert(self):
        self.driver.switch_to_alert().accept()