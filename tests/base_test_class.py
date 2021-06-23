import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
        
# capabilities = {
#     "browserName": "chrome",
#     "browserVersion": "91.0",
#     "selenoid:options": {
#         "enableVNC": True,
#         "enableVideo": False
#     }
# }




class BaseTestClass(unittest.TestCase):

    _multiprocess_can_split_ = True
    DRIVER_LOCATION = "/usr/bin/chromedriver" 
    BINARY_LOCATION = "/usr/bin/google-chrome"

    def setUp(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Remote(
        #     command_executor="http://localhost:4444/wd/hub",
        #     desired_capabilities=capabilities
        # )
        self.options = webdriver.ChromeOptions() 
        self.options.binary_location = self.BINARY_LOCATION 
        self.driver = webdriver.Chrome(
            executable_path=self.DRIVER_LOCATION,
            options=self.options
        ) 
        self.driver.implicitly_wait(16)


    def tearDown(self):
        self.driver.quit()
