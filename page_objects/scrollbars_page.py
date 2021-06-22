from .base_page import BasePage
from selenium.webdriver.common.by import By

class ScrollbarsPage(BasePage):

    HIDDING_BUTTON = "hidingButton"
    
    def execute_js_script(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'})",
            self.driver.find_element_by_id(self.HIDDING_BUTTON)
        )
    
    def find_a_button(self):
        self.driver.find_element_by_id(self.HIDDING_BUTTON)
