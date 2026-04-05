import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base.base_class import Base


class User_agreement_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 

    products_button = "//a[@href='/products']" # локатор на каталог товаров
  
    # Getters

    def get_products_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products_button))) # целимся в выбор кнопки каталог товаров
                                                                            
    # Actions

    def click_products_button(self): # кликаем выбор кнопки каталог товаров
       self.get_products_button().click()
       print("Click products_button")

    # Mетоды
    def select_products_button(self): # вызываем выбор кнопки каталог товаров
        self.get_current_url() # Method get current url
        self.click_products_button()
        

    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass