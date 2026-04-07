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


class Login_page(Base):

    url = "https://капибара161.рф/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# методы
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url() # Method get current url
       
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass