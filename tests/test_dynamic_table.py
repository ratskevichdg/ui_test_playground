import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.dynamic_table_page import DynamicTablePage

class DynamicTable(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/dynamictable"

    def test_find_cpu_data(self):
        driver = self.driver
        driver.get(self.base_url)
        dynamic_table_page = DynamicTablePage(driver)
        self.assertIn(
            dynamic_table_page.find_cpu_value(),
            dynamic_table_page.find_answer()
        ), "Values doesn't match"
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
