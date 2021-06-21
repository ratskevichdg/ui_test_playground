import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.scrollbars_page import ScrollbarsPage

class Scrollbars(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/scrollbars"

    def test_find_a_button(self):
        driver = self.driver
        driver.get(self.base_url)
        scrollbars_page = ScrollbarsPage(driver)
        scrollbars_page.execute_js_script()
        sleep(1)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()