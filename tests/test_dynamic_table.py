import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  
from base_test_class import BaseTestClass
import unittest

from page_objects.dynamic_table_page import DynamicTablePage

class DynamicTable(BaseTestClass):

    BASE_URL = "http://uitestingplayground.com/dynamictable"

    def test_find_cpu_data(self):
        driver = self.driver
        driver.get(self.BASE_URL)
        dynamic_table_page = DynamicTablePage(driver)
        self.assertIn(
            dynamic_table_page.find_cpu_value(),
            dynamic_table_page.find_answer()
        ), "Values doesn't match"

if __name__ == "__main__":
    unittest.main()
