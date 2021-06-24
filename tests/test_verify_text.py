import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest
import allure

from page_objects.verify_text import VerifyTextPage

class VerifyText(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/verifytext"

    @allure.feature("Finding an element by displayed text has nuances")
    @allure.story("Create a test that finds an element with 'Welcome...' text.")
    @allure.severity("normal")
    def test_text_finding(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        verify_text_page = VerifyTextPage(driver)
        
        self.assertIn(
            "Welcome", verify_text_page.find_desird_text()
        ), "Texts didn't match"

if __name__ == "__main__":
    unittest.main()