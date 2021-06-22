import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest

from page_objects.hidden_layers_page import HiddenLayerPage

class HiddenLayer(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/hiddenlayers"

    def test_hidden_layer_button(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        hidden_layer_page = HiddenLayerPage(driver)
        hidden_layer_page.click_to_green_button()
        self.assertFalse(
            hidden_layer_page.click_to_green_button()
        ), "Green button was clicked twice"

if __name__ == "__main__":
    unittest.main()

    