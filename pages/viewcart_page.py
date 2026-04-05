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

"""Страница Оформление заказа и класс Viewcart_pag ее курирует"""
class Viewcart_page(Base):

    url = 'https://капибара161.рф/products/viewcart' # страница подтверждения заказа

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    name = "//input[@id='name']" # имя
    email = "//input[@id='email']" # мыло 
    phone = "//input[@id='phone']" # телефон
    check_approval = "//label[@class='inline-block -mg-l-10 -mg-r-10']"  # or //label[@for='field1'] # согласие на обработку данных
    approval_confirmation = "//button[@class='cart__button new-cart-recipient-data__button']" # сохранить данные
    place_an_order = "//button[@class='cart__button new-cart-recipient-data__button']" # оформить заказ
    order_stage = "//button[@id='js-order-stage']" # финал оформления заказа

    # Getters
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))
    #   забили имя 
    def get_email(self):       
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.email)))
    #   забили мыло                                                                         
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    #   забили телефон      
    def get_check_approval (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_approval)))
    # дали согласие на обработку данных
    
    
# Actions

    def input_user_name(self, user_name):
       self.get_user_name().send_keys(user_name)
       print("input user_name")

    def input_user_password(self, password):
       self.get_password().send_keys(password)
       print("input password")

    def click_login_button(self):
       self.get_login_button().click()
       print("Click login_button")


# методы
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url() # Method get current url
        self.input_user_name("standard_user")
        self.input_user_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products") # Method assert word
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass