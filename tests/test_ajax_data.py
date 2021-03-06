import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest


from page_objects.ajax_data_page import AJAXDataPage

class AJAXData(BaseTestClass):

    BASE_URL= "http://uitestingplayground.com/ajax"

    def test_page_ajax_delay(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        ajax_data_page = AJAXDataPage(driver)
        ajax_data_page.trigger_ajax_request()
        self.assertIsNotNone(
            ajax_data_page.get_loaded_data()
        ), "AJAX data didn't download"


if __name__ == "__main__":
    unittest.main()