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
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.first_name)))
    
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.last_name)))
    #                                                                                       
    def get_zip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
    
    
# Actions

    def input_first_name(self, first_name):
       self.get_first_name().send_keys(first_name)
       print("input first_name")

    def input_last_name(self, last_name):
       self.get_last_name().send_keys(last_name)
       print("input last_name")

    def input_zip(self, zip):
       self.get_zip().send_keys(zip)
       print("input zip")

    def click_continue_button(self):
       self.get_continue_button().click()
       print("Click continue_button")


# методы
    def input_information(self):
        self.get_current_url() # Method get current url
        self.input_first_name("Ivan")
        self.input_last_name("Fedorov")
        self.input_zip("344038")
        self.click_continue_button()
()
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass