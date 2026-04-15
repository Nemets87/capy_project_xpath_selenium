import time
import sys
import os
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    finish_button = "//button[@id='finish']"
        
    item_active_selected = "//div[@class='item active selected']"
    data_value_top_low_price = "//div[@class='item'][1]" # самая дорогая идет первой 
    data_value_low_to_top_price = "//div[@class='item'][2]" # самая дешевая идет первой
    data_value_a_z_text = "//div[text()='Наименование (А—Я)']" # А—Я
    data_value_z_a_text = "//div[text()='Наименование (Я—А)']" # Я-А

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.finish_button)))
                                                                               
   # Actions
    def click_finish_button(self):
       self.get_finish_button().click()
       print("click_finish_button")

    # методы
    def payment(self):
        self.get_current_url() # Method get current url
        self.click_finish_button()

   # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass