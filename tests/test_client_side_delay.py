import sys
import os.path

libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from base_test_class import BaseTestClass
import unittest
import allure

from page_objects.client_side_delay_page import ClientSideDelayPage


class ClientSideDelay(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/clientdelay"

    @allure.feature(
        "Some elements may appear after client-side time consuming JavaScript calculations"
    )
    @allure.story(
        "Record the following steps. Press the button below and wait for data to appear ",
        "(15 seconds), click on text of the loaded label."
    )
    @allure.severity("normal")
    def test_page_client_side_delay(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        client_side_delay_page = ClientSideDelayPage(driver)
        client_side_delay_page.trigger_client_logic_request()
        self.assertIsNotNone(
            client_side_delay_page.get_loaded_data()
        ), "Data from client side wasn't download"


if __name__ == "__main__":
    unittest.main()
