from .base_page import BasePage
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementClickInterceptedException


class HiddenLayerPage(BasePage):
    
    GREEN_BUTTON = (By.ID, "greenButton")

    def click_to_green_button(self):
        try:
            element = self.driver.find_element(*self.GREEN_BUTTON)
            element.click()
        except ElementClickInterceptedException:
            return False