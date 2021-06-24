import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest
import allure
from time import sleep

from page_objects.text_input_page import TextInputPage

class ClickData(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/textinput"

    @allure.feature("Entering text into an edit field may not have effect")
    @allure.story("Record empty text into the input field and pressing the button.")
    @allure.severity("normal")
    def test_text_input_with_empty_string(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        text_input_page = TextInputPage(driver)
        initial_button_text = text_input_page.get_button_text()
        text_input_page.click_the_button()
        button_text_after_click = text_input_page.get_button_text()
        self.assertEqual(
            initial_button_text, button_text_after_click
        ), "Button text was changed"

    @allure.feature("Entering text into an edit field may not have effect")
    @allure.story("Record setting text into the input field and pressing the button.")
    @allure.severity("normal")
    def test_text_input_with_random_string(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        text_input_page = TextInputPage(driver)
        text_to_enter = text_input_page.random_string()
        text_input_page.enter_text(text_to_enter)
        text_input_page.click_the_button()
        # Enter a 0.5 sec sleep to give a time to response
        sleep(0.5)
        button_text_after_click = text_input_page.get_button_text()
        self.assertEqual(
            text_to_enter, button_text_after_click
        ), "Button text was changed"

if __name__ == "__main__":
    unittest.main()