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


class Client_information__page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    name = "//input[@id='name']" # имя
    email = "//input[@id='email']" # мыло 
    phone = "//input[@id='phone']" # телефон
    check_approval = "//div[@class='checkbox-element dynamic-field-checkbox']" # "//label[@class='inline-block -mg-l-10 -mg-r-10']"  # or //input[@id='field1'] # согласие на обработку данных
    

    # Getters
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))
    #   забили имя 
    def get_email(self):       
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    #   забили мыло                                                                         
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    #   забили телефон      
    def get_check_approval(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_approval)))
    # дали согласие на обработку данных
    
    # Actions
    def input_name(self, name):
       self.get_name().send_keys(name)
       print("input name")

    def input_email(self, email):
       self.get_email().send_keys(email)
       print("input last_name")

    def input_phone(self, phone):
       self.get_phone().send_keys(phone)
       print("input phone")

    def click_check_approval(self):
       self.get_check_approval().click()
       print("Click get_check_approval")

   # Methods
    def input_information(self):
        self.get_current_url() # Method get current url
        self.input_name("Ivan")
        self.input_email("bonustime161@yandex.ru")
        self.input_phone("89614201118")
        self.click_check_approval()
()
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass