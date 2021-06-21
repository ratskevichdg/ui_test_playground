from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoadDelayPage(BasePage):
    
    LOAD_DELAY = (By.LINK_TEXT, "Load Delay")
    PAGE_TITLE = "Load Delays"
    
    def switch_to_load_dealy_page(self):
        element = self.driver.find_element(*self.LOAD_DELAY)
        element.click()

    