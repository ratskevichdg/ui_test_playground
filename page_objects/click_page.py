from .base_page import BasePage
from selenium.webdriver.common.by import By


class ClickPage(BasePage):
    
    BAD_BUTTON = (By.XPATH, '//*[@id="badButton"]')

    def click_the_button(self):
        element = self.driver.find_element(*self.BAD_BUTTON)
        element.click()

    def get_button_color(self):
        return self.driver.find_element(
            *self.BAD_BUTTON
        ).value_of_css_property("background-color")