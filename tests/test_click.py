import sys
import os.path

libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from base_test_class import BaseTestClass
from time import sleep
import unittest
import allure

from page_objects.click_page import ClickPage


class ClickData(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/click"

    @allure.feature("Event based click on an element may not always work")
    @allure.story("Record button click. The button becomes green after clicking")
    @allure.severity("normal")
    def test_button_colors(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        click_page = ClickPage(driver)
        initial_color = click_page.get_button_color()
        click_page.click_the_button()
        # Enter a 0.5 sec sleep to give a time to response
        sleep(0.5)
        color_after_clicking = click_page.get_button_color()
        self.assertNotEqual(
            initial_color, color_after_clicking
        ), "Button didn't change the color"


if __name__ == "__main__":
    unittest.main()
