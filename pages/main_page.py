import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    # //button[@id='client-cookies-notice-button']
    cookies_notice_button = "//button[@id='client-cookies-notice-button']" # локатор кукис на старте страницы 
    burger_button = "//span[@id='burger-btn-text']" # выбор кнопки hellow (меню бургер справа)
    products = "//a[@href='/products']"
    
    # Getters
    def get_cookies_notice_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cookies_notice_button)))

    def get_burger_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_button))) # целимся в выбор кнопки hellow (меню бургер справа)
                                                                      
    # Actions
    def click_cookies_notice_button(self): # кликаем выбор кукис на старте страницы 
       self.cookies_notice_button().click()
       print("Click get_burger_butto")

    def click_burger_button(self): # кликаем выбор кнопки hellow (меню бургер справа)
       self.get_burger_button().click()
       print("Click get_burger_butto")

    # методы
    def select_cookies_notice_button(self):
        self.get_current_url() # Method get current url
        self.click_cookies_notice_button()

    def select_burger_button(self):
        self.get_current_url() # Method get current url
        self.click_burger_button()
       
    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass




    # sort_dropdo_button = "//div[@class='sort ui dropdown small-12 selection']" # выбор меню сортировки товаров 

    # item_active_selected = "//div[@class='item active selected']"
    # data_value_low_to_top_price = "//div[@class='item'][1]" # самая дорогая идет первой 
    # data_value_low_to_top_price = "//div[@class='item'][2]" # самая дешевая идет первой
    # data_value_a_z_text = "//div[text()='Наименование (А—Я)']" # А—Я
    # data_value_z_a_text = "//div[text()='Наименование (Я—А)']" # Я-А

    # select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']" # локатор товара 

    # # sony_games_locator = "//a[@href='/products/category/5374852']"


    # select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']" # локатор товара 
 

    # menu ="//button[@id='react-burger-menu-btn']"
    # link_about = "//a[@id='about_sidebar_link']"

    # main_page_url = "https://капибара161.рф/"
    # shop_url = "https://капибара161.рф/products"
    # about_url = "https://капибара161.рф/"
    # sony_games = "https://капибара161.рф/products/category/5374852"
    # sony_games_ps5 = "https://капибара161.рф/products/category/5382071"
    # sony_new_games_ps5 = "https://капибара161.рф/products/category/5382072"