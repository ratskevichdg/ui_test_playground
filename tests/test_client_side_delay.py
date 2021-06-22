import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest

from page_objects.client_side_delay_page import ClientSideDelayPage

class ClientSideDelay(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/clientdelay"

    def test_page_ajax_delay(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        client_side_delay_page = ClientSideDelayPage(driver)
        client_side_delay_page.trigger_client_logic_request()
        self.assertIsNotNone(
            client_side_delay_page.get_loaded_data()
        ), "Data from client side wasn't download"

if __name__ == "__main__":
    unittest.main()