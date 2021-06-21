import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.class_atrr_page import ClassAttributePage

class ClassAttribute(unittest.TestCase):

    _multiprocess_can_split_ = True
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/classattr"

    def test_button_by_class_attr(self):
        driver = self.driver
        driver.get(self.base_url)
        cls_attr_page = ClassAttributePage(driver)
        cls_attr_page.click_to_primary_button()
        alert_text = cls_attr_page.get_alert_text()
        cls_attr_page.accept_alert()
        print(alert_text)
        self.assertEqual(alert_text, cls_attr_page.ALERT_TEXT), "Texts didn't match"
        cls_attr_page.click_to_success_button()
        cls_attr_page.click_to_warning_button()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    