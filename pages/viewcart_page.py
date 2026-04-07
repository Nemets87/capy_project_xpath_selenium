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
    checkmark = "//span[@class='checkmark']"
    order_next_stage = "//button[@id='js-next-stage']" # финал оформления заказа

    # name = "//input[@id='name']" # имя
    # email = "//input[@id='email']" # мыло 
    # phone = "//input[@id='phone']" # телефон
    # check_approval = "//label[@class='inline-block -mg-l-10 -mg-r-10']"  # or //label[@for='field1'] # согласие на обработку данных
    # approval_confirmation = "//button[@class='cart__button new-cart-recipient-data__button']" # сохранить данные
    # place_an_order = "//button[@class='cart__button new-cart-recipient-data__button']" # оформить заказ


    # Getters
    def get_checkmark_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkmark)))
    #   забили имя 

    def get_order_next_stage(self):       
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_next_stage)))
                                                                       
    # def get_phone(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    # #   забили телефон      
    # def get_check_approval (self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_approval)))
    # # дали согласие на обработку данных
    
    # Actions
    def click_checkmark_button(self):
       self.get_checkmark_button().click()
       print("Click checkmark_button")

    def click_order_next_stag(self):
       self.get_order_next_stage().click()
       print("input user_name")

    # def input_user_password(self, password):
    #    self.get_password().send_keys(password)
    #    print("input password")

    # методы
    # def autorization(self):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.get_current_url() # Method get current url
        # self.input_user_name("standard_user")
        # self.input_user_password("secret_sauce")
        # self.click_login_button()
        # self.assert_word(self.get_main_word(), "Products") # Method assert word

    def select_checkmark_button(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_checkmark_button()

    def select_order_next_stag(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_order_next_stag()
   
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass