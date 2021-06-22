import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTestClass(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(16)


    def tearDown(self):
        self.driver.quit()
