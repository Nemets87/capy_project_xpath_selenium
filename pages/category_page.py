import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base.base_class import Base



"""Класс выбора нужного продукта(товаров)"""
class Category_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators 
 
    sort_dropdo_button = "//div[@class='sort ui dropdown small-12 selection']" # выбор меню сортировки товаров 
    handle_upper = "//div[@class='noUi-handle noUi-handle-upper']" # ползунок

    upper = "//input[@name='max_cost']" # максимальная цена 
    lower = "//input[@name='min_cost']" # минимальная цена

    

    item_active_selected = "//div[@class='item active selected']"

    data_value_top_low_price = "//div[text()='Цена (по убыванию)']" # самая дорогая идет первой //div[text()='Цена (по убыванию)']
    data_value_low_to_top_price = " //div[text()='Цена (по возрастанию)']" # самая дешевая идет первой

    data_value_a_z_text = "//div[text()='Наименование (А—Я)']" # А—Я
    data_value_z_a_text =  "//div[text()='Наименование (Я—А)']" # Я-А

    select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']" # отправляем продукт в корзину

    cart_sender = "//span[@class='cart-btn__text product-item__button-text']" # таргет на товар
    cart = "//span[@class='top-cart__notification top-cart__notification--round-3 quantity-items']" # корзина 
    cart_offer_order = "//a[@class='button button_for_top-cart-drop-down']" # оформить заказ

    choise_add = "//span[@class='checkmark']"
    go_to_buy = "//button[@id='js-next-stage']"


    # Getters

    def get_data_value_a_z_text(self): # целимся в выбор кнопки критерия цены и порядка по алфовиту от а до я
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_a_z_text))) 
    
    def get_data_value_z_a_text(self): # целимся в выбор кнопки критерия цены и порядка по алфовиту от я до а
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_z_a_text))) 


    def get_sort_dropdo_button(self): # выбираем меню бургер для выбора нужного критерия товара 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_dropdo_button))) 
    
    def get_item_active_selected(self): # целимся в выбор критерия сортировки товаров 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_active_selected))) 
    

    def get_data_value_top_low_price(self): # целимся в выбор критерия где самая дорогая идет первой 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_top_low_price))) 
    
    def get_upper(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.upper)))
    
    
    def get_data_value_low_to_top_price(self): # целимся в выбор критерия где самая дешевая идет первой
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_low_to_top_price))) 
    
    def get_lower(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.lower)))
    

    def get_select_product(self): # целимся в выбор кнопки и отправляем продукт в корзину
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product))) 
    
    def get_cart(self): # целимся в выбор кнопки и отправляем первый продукт в корзину
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart))) 

                                                                            
    # Actions
    def click_data_value_a_z_text(self): # кликаем выбор кнопки критерия порядка по алфовиту по алфовиту от а до я
       self.get_data_value_a_z_text().click()
       print("Click  data_value_a_z_text")

    def click_data_value_z_a_text(self): # кликаем выбор кнопки критерия по алфовиту от я до а
       self.get_data_value_z_a_text().click()
       print("Click data_value_z_a_text")


    def click_sort_dropdo_button(self): # кликаем выбор кнопки критерия цены и порядка по алфовиту 
       self.get_sort_dropdo_button().click()
       print("Click get_sony_playstation_games_button")

    def click_item_active_selected(self): # кликаем выбор критерия без сортировки товаров 
       self.get_item_active_selected().click()
       print("Click get_item_active_selected")


    def click_data_value_top_low_price(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_data_value_top_low_price().click()
       print("Click get_sony_playstation_5_new_games_button")

    def click_data_value_low_to_top_price(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_data_value_low_to_top_price().click()
       print("Click get_data_value_low_to_top_price")


    def click_get_select_product(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_select_product().click()
       print("Click select_product_button")

    def click_get_cart(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_cart().click()
       print("Click cart")

    
    # Mетоды
    def select_data_value_a_z_text(self): # вызываем выбор кнопки критерия цены и порядка по алфовиту 
        self.get_current_url() # Method get current url
        self.click_data_value_a_z_text()

    def select_data_value_z_a_text(self): # вызываем выбор кнопки критерия цены и порядка по алфовиту 
        self.get_current_url() # Method get current url
        self.click_data_value_z_a_text()


    def select_click_sort_dropdo_button(self): # выбираем выбор кнопки критерия цены и порядка по алфовиту 
        self.get_current_url() # Method get current url
        self.click_sort_dropdo_button()

    def select_item_active_selected(self): # 
        self.get_current_url() # Method get current url
        self.click_item_active_selected()


    def select_data_value_top_low_price(self): # выбираем самый дорогой товар
        self.get_current_url() # Method get current url
        self.click_data_value_top_low_price()

    
    def select_data_value_low_to_top_price(self): # выбираем самый доступный товар
        self.get_current_url() # Method get current url
        self.click_data_value_low_to_top_price()


    def select_get_select_product(self): # выбираем товар
        self.get_current_url() # Method get current url
        self.click_get_select_product()

    def select_click_get_cart(self): # кликаем корзину
        self.get_current_url() # Method get current url
        self.click_get_cart()

    def value_upper(self):
        self.get_upper().text()

    def value_lower(self):
        self.get_lower().text()

    def get_upper_price(self) -> float:
        """Возвращает числовое значение максимальной цены из поля max_cost"""
        element = self.get_upper()
        return Base.clean_price_element(element)

    def get_lower_price(self) -> float:
        """Возвращает числовое значение минимальной цены из поля min_cost"""
        element = self.get_lower()
        return Base.clean_price_element(element)
    
    def get_upper_price(self) -> float:
        element = self.get_upper()
        value_str = element.get_attribute("value")  # у input value, а не text
        return self.extract_float(value_str)   # используем статический метод
    
    def get_lower_price(self) -> float:
        element = self.get_lower()
        value_str = element.get_attribute("value")  # у input value, а не text
        return self.extract_float(value_str)   # используем статический метод


    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass