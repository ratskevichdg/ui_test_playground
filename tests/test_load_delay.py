import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest

from page_objects.load_delay_page import LoadDelayPage

class LoadDelay(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com"

    def test_page_switch_with_delay(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        load_delay_page = LoadDelayPage(driver)
        load_delay_page.switch_to_load_dealy_page()
        self.assertEqual(
            driver.title, load_delay_page.PAGE_TITLE
        ), "there wasn't page changeover"

if __name__ == "__main__":
    unittest.main()