from .base_page import BasePage
from selenium.webdriver.common.by import By


class AJAXDataPage(BasePage):
    
    BUTTON_AJAX_TRIGGER = (By.XPATH, '//*[@id="ajaxButton"]')
    AJAX_LOADED_DATA = (By.XPATH, '//*[@id="content"]/p')

    
    def trigger_ajax_request(self):
        element = self.driver.find_element(*self.BUTTON_AJAX_TRIGGER)
        element.click()

    def get_loaded_data(self):
        element = self.driver.find_element(*self.AJAX_LOADED_DATA)
        return element.text