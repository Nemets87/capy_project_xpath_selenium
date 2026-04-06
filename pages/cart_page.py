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


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 

    # cart_sender = "//span[@class='cart-btn__text product-item__button-text']" # таргет на товар
    # cart = "//span[@class='top-cart__notification top-cart__notification--round-3 quantity-items']" # корзина 
    cart_offer_order = "//a[@class='button button_for_top-cart-drop-down']" # оформить заказ
    # choise_add = "//span[@class='checkmark']"
    # go_to_buy = "//button[@id='js-next-stage']"

    # Getters
    def get_cart_offer_ordert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_offer_order)))
                                                                               
    # Actions
    def click_cart_offer_order(self):
        self.get_cart_offer_ordert().click()
        print("checkout_button")

    # методы
    def select_cart_offer_order(self):
        self.get_current_url() # Method get current url
        self.click_cart_offer_order()
        
  
# Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass