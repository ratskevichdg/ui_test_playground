from .base_page import BasePage
from selenium.webdriver.common.by import By

class VerifyTextPage(BasePage):

    DESIRED_TEXT = "//span[normalize-space(.)='Welcome UserName!']"
    
    
    def find_desird_text(self):
        return self.driver.find_element(By.XPATH, self.DESIRED_TEXT).text

        
    
    # def find_answer(self):
    #     self.driver.find_element(Byself.HIDDING_BUTTON)
        
        # sleep(5)
        # text = verify_table_page.find_desird_text()
        # sleep(5)
        # print(text)
        # # assert (1 == 1)