import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.hidden_layers_page import HiddenLayerPage

class HiddenLayer(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/hiddenlayers"

    def test_hidden_layer_button(self):
        driver = self.driver
        driver.get(self.base_url)
        hidden_layer_page = HiddenLayerPage(driver)
        hidden_layer_page.click_to_green_button()
        self.assertFalse(
            hidden_layer_page.click_to_green_button()
        ), "Green button was clicked twice"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    