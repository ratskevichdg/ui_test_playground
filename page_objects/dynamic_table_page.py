from .base_page import BasePage
from selenium.webdriver.common.by import By

class DynamicTablePage(BasePage):

    TABLE_COLUMN_HEADER = "/html/body/section/div/div/div[2]/div"
    ANSWER = "/html/body/section/div/p[2]"
    
    def find_cpu_value(self):
        return self.driver.find_element(By.XPATH, *self.TABLE_COLUMN_HEADER)

        
    
    # def find_answer(self):
    #     self.driver.find_element(Byself.HIDDING_BUTTON)
        
