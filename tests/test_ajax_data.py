import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.ajax_data_page import AJAXDataPage

class AJAXData(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(16)
        self.base_url = "http://uitestingplayground.com/ajax"

    def test_page_ajax_delay(self):
        driver = self.driver
        driver.get(self.base_url)
        ajax_data_page = AJAXDataPage(driver)
        ajax_data_page.trigger_ajax_request()
        self.assertIsNotNone(
            ajax_data_page.get_loaded_data()
        ), "AJAX data didn't download"


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()