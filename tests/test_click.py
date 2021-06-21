import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.click_page import ClickPage

class ClickData(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/click"

    def test_button_colors(self):
        driver = self.driver
        driver.get(self.base_url)
        click_page = ClickPage(driver)
        initial_color = click_page.get_button_color()
        click_page.click_the_button()
        # Enter a 0.5 sec sleep to give a time to response
        sleep(0.5)
        color_after_clicking = click_page.get_button_color()
        self.assertNotEqual(
            initial_color, color_after_clicking
        ), "Button didn't change the color"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()