import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])  


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from page_objects.verify_text import VerifyTextPage

class VerifyText(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://uitestingplayground.com/verifytext"

    def test_text_finding(self):
        driver = self.driver
        driver.get(self.base_url)
        verify_text_page = VerifyTextPage(driver)
        
        self.assertIn(
            "Welcome", verify_text_page.find_desird_text()
        ), "Texts didn't match"
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()