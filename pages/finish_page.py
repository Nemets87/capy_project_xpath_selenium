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


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    main_word = "//div[@class='cart__checkout-custom-text text-center']"
 

    # Getters
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
 

    # методы
    def finish(self):
        final_page_true = "https://xn--161-5cdaaf9cq5co.xn--p1ai/products/viewcart"
        self.get_current_url() # Method get current url
        self.assert_url(final_page_true)
        self.assert_word(self.get_main_word(), 'Спасибо за заказ. Мы свяжемся с Вами в ближайшее время.') # Method assert word
        self.get_screenshot()
    

   # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass