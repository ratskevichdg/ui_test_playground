from .base_page import BasePage
from selenium.webdriver.common.by import By

class DynamicTablePage(BasePage):

    TABLE_COLUMN_HEADER = (By.XPATH, "/html/body/section/div/div/div[2]/div")
    ANSWER = (By.XPATH, "/html/body/section/div/p[2]")
    # TABLE_ROWS = (By.XPATH, "/html/body/section/div/div/div[3]")
    # ROW = (By.XPATH, "//*[@role='row']")
    CELL = (By.XPATH, "//*[@role='cell']")
    
    def find_cpu_value(self):
        column_headers = self.driver.find_element(*self.TABLE_COLUMN_HEADER).text.split()
        cpu_value_index = column_headers.index("CPU")
        cells = [cell.text for cell in self.driver.find_elements(*self.CELL)]
        return cells[cells.index("Chrome") + cpu_value_index]



    
    def find_answer(self):
        return self.driver.find_element(*self.ANSWER).text
        
