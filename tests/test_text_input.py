import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.text_input_page import TextInputPage

class ClickData(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/textinput"

    def test_text_input_with_empty_string(self):
        driver = self.driver
        driver.get(self.base_url)
        text_input_page = TextInputPage(driver)
        initial_button_text = text_input_page.get_button_text()
        text_input_page.click_the_button()
        button_text_after_click = text_input_page.get_button_text()
        self.assertEqual(
            initial_button_text, button_text_after_click
        ), "Button text was changed"

    
    def test_text_input_with_random_string(self):
        driver = self.driver
        driver.get(self.base_url)
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


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()