import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest
import allure
from time import sleep

from page_objects.scrollbars_page import ScrollbarsPage

class Scrollbars(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/scrollbars"

    @allure.feature("Scrolling an element into view may be a tricky task")
    @allure.story(
        "Find a button in the scroll view and record button click.\n",
        "Update your test to automatically scroll the button into a visible area."
    )
    @allure.severity("normal")
    def test_find_a_button(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        scrollbars_page = ScrollbarsPage(driver)
        scrollbars_page.execute_js_script()
        sleep(1)

if __name__ == "__main__":
    unittest.main()