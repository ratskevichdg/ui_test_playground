import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
        
capabilities = {
    "browserName": "chrome",
    "browserVersion": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

class BaseTestClass(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities
        )
        self.driver.implicitly_wait(16)


    def tearDown(self):
        self.driver.quit()
