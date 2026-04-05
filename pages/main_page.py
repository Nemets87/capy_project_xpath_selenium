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

    cookies_notice_button = "//button[@id='client-cookies-notice-button']" # локатор кукис на старте страницы 
    products = "//a[@href='/products']"
    

    sort_dropdo_button = "//div[@class='sort ui dropdown small-12 selection']" # выбор меню сортировки товаров 
    data_value_low_to_top_price = "//div[@class='item'][3]" # самая дешевая идет первой
    data_value_top_to_low_price = "//div[@class='item'][2]" # самая дорогая идет первой 
    data_value_a_z_text = "//div[text()='Наименование (А—Я)']"

    sony_games_locator = "//a[@href='/products/category/5374852']"


    select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']" # локатор товара 
    # select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    # select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"


    
    menu ="//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"
    url_main_page = "https://капибара161.рф/"
    shop_url = "https://капибара161.рф/products"
    about_url = "https://капибара161.рф/"
    sony_games = "https://капибара161.рф/products/category/5374852"
    sony_games_ps5 = "https://капибара161.рф/products/category/5382071"
    sony_new_games_ps5 = "https://капибара161.рф/products/category/5382072"


    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    
    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    
    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))
                                                                               
    # Actions

    def click_select_product_1(self):
       self.get_select_product_1().click()
       print("Click select_product_1")

    def click_select_product_2(self):
       self.get_select_product_2().click()
       print("Click select_product_2")

    def click_select_product_3(self):
       self.get_select_product_3().click()
       print("Click select_product_3")


    def click_cart(self):
       self.get_cart().click()
       print("Click cart")

    def click_menu(self):
       self.get_menu().click()
       print("Click burger_menu")

    def click_link_about(self):
       self.get_link_about().click()
       print("Click about")


    # методы
    def select_products_1(self):
        self.get_current_url() # Method get current url
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):
        self.get_current_url() # Method get current url
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url() # Method get current url
        self.click_select_product_3()
        self.click_cart()


    def select_menu_about(self):
        self.get_current_url() # Method get current url
        self.click_menu()
        self.click_link_about()
        self.assert_url(self.about_url)
       
    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass