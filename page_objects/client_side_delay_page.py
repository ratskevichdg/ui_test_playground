from .base_page import BasePage
from selenium.webdriver.common.by import By


class ClientSideDelayPage(BasePage):
    
    BUTTON_TRIGGER = (By.XPATH, '//*[@id="ajaxButton"]')
    CLIENT_SIDE_LOADED_DATA = (By.XPATH, '//*[@id="content"]/p')

    
    def trigger_client_logic_request(self):
        element = self.driver.find_element(*self.BUTTON_TRIGGER)
        element.click()

    def get_loaded_data(self):
        element = self.driver.find_element(*self.CLIENT_SIDE_LOADED_DATA)
        return element.text