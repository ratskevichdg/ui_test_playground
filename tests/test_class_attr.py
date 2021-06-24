import sys
import os.path

libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from base_test_class import BaseTestClass
import unittest
import allure

from page_objects.class_atrr_page import ClassAttributePage


class ClassAttribute(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/classattr"

    @allure.feature("Check that class attribute based XPath is well formed")
    @allure.story("Record primary (blue) button click and press ok in alert popup.")
    @allure.severity("normal")
    def test_button_by_class_attr(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        cls_attr_page = ClassAttributePage(driver)
        cls_attr_page.click_to_primary_button()
        alert_text = cls_attr_page.get_alert_text()
        cls_attr_page.accept_alert()
        print(alert_text)
        self.assertEqual(alert_text, cls_attr_page.ALERT_TEXT), "Texts didn't match"
        cls_attr_page.click_to_success_button()
        cls_attr_page.click_to_warning_button()


if __name__ == "__main__":
    unittest.main()
