import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.client_side_delay_page import ClientSideDelayPage

class ClientSideDelay(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(16)
        self.base_url = "http://uitestingplayground.com/clientdelay"

    def test_page_ajax_delay(self):
        driver = self.driver
        driver.get(self.base_url)
        client_side_delay_page = ClientSideDelayPage(driver)
        client_side_delay_page.trigger_client_logic_request()
        self.assertIsNotNone(
            client_side_delay_page.get_loaded_data()
        ), "Data from client side wasn't download"


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()