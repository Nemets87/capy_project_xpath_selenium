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

#     # Locators 
#     user_name = "//input[@data-test='username']"
#     password = "#password"
#     button_login = "//*[@id='login-button']"
#     main_word = "//span[@data-test='title']"

#     # Getters
#     def get_user_name(self):
#         return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.user_name)))
#     #          WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@data-test='username']")))  
#     def get_password(self):
#         return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.password)))
#     #          WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))                                                                                 
#     def get_login_button(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))
#     #          WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//*[@id='login-button']")))
#     def get_main_word(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    
    
# # Actions

#     def input_user_name(self, user_name):
#        self.get_user_name().send_keys(user_name)
#        print("input user_name")

#     def input_user_password(self, password):
#        self.get_password().send_keys(password)
#        print("input password")

#     def click_login_button(self):
#        self.get_login_button().click()
#        print("Click login_button")


# методы
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url() # Method get current url
        # self.input_user_name("standard_user")
        # self.input_user_password("secret_sauce")
        # self.click_login_button()
        # self.assert_word(self.get_main_word(), "Products") # Method assert word
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass