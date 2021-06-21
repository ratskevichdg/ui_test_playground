from .base_page import BasePage
from selenium.webdriver.common.by import By

from random import choice
from string import ascii_letters


class TextInputPage(BasePage):
    
    INPUT_BUTTON_NAME = (By.XPATH, '//*[@id="newButtonName"]')
    BUTTON_WITH_EDITABLE_NAME = (By.XPATH, '//*[@id="updatingButton"]')
    

    def click_the_button(self):
        element = self.driver.find_element(*self.BUTTON_WITH_EDITABLE_NAME)
        element.click()

    def get_button_text(self):
        return self.driver.find_element(*self.BUTTON_WITH_EDITABLE_NAME).text

    def enter_text(self, searchtext):
        self.driver.find_element(*self.INPUT_BUTTON_NAME).send_keys(searchtext)

    @staticmethod
    def random_string():  
        result = ''.join((choice(ascii_letters) for x in range(10))) 
        return result  