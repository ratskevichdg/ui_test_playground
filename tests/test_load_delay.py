import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.load_delay_page import LoadDelayPage

class LoadDelay(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/"

    def test_page_switch_with_delay(self):
        driver = self.driver
        driver.get(self.base_url)
        load_delay_page = LoadDelayPage(driver)
        load_delay_page.switch_to_load_dealy_page()
        self.assertEqual(
            driver.title, load_delay_page.PAGE_TITLE
        ), "there wasn't page changeover"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()