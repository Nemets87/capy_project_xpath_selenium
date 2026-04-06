import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
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

    
    item_active_selected = "//div[@class='item active selected']"
    data_value_top_low_price = "//div[@class='item'][1]" # самая дорогая идет первой 
    data_value_low_to_top_price = "//div[@class='item'][2]" # самая дешевая идет первой
    data_value_a_z_text = "//div[text()='Наименование (А—Я)']" # А—Я
    data_value_z_a_text = "//div[text()='Наименование (Я—А)']" # Я-А

    select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']" # отправляем первый продукт в корзину

    
    cart_sender = "//span[@class='cart-btn__text product-item__button-text']" # таргет на товар
    cart = "//span[@class='top-cart__notification top-cart__notification--round-3 quantity-items']" # корзина 
    cart_offer_order = "//a[@class='button button_for_top-cart-drop-down']" # оформить заказ
    choise_add = "//span[@class='checkmark']"
    go_to_buy = "//button[@id='js-next-stage']"


    actions = ActionChains(driver)
    slider = driver.find_element(By.XPATH, handle_upper)

    actions.click_and_hold(slider).move_by_offset(5000, 0).release().perform()
  
    # Getters
    def get_sort_dropdo_button(self): # целимся в выбор кнопки критерия цены и порядка по алфовиту 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_dropdo_button))) 
    
    def get_item_active_selected(self): # целимся в выбор критерия без сортировки товаров 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_active_selected))) 
    
    def get_data_value_top_low_price(self): # целимся в выбор критерия где самая дорогая идет первой 
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_top_low_price))) 
    
    def get_data_value_low_to_top_price(self): # целимся в выбор критерия где самая дешевая идет первой
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_value_low_to_top_price))) 
    
    def get_select_product(self): # целимся в выбор кнопки и отправляем первый продукт в корзину
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product))) 
    
    def get_cart(self): # целимся в выбор кнопки и отправляем первый продукт в корзину
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart))) 

                                                                            
    # Actions
    def click_sort_dropdo_button(self): # кликаем выбор кнопки критерия цены и порядка по алфовиту 
       self.get_sort_dropdo_button().click()
       print("Click get_sony_playstation_games_button")

    def click_item_active_selected(self): # кликаем выбор критерия без сортировки товаров 
       self.get_item_active_selected().click()
       print("Click get_item_active_selected")

    def click_data_value_top_low_price(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_data_value_top_low_price().click()
       print("Click get_sony_playstation_5_new_games_button")

    def click_get_select_product(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_select_product().click()
       print("Click select_product_button")

    def click_get_cart(self): # кликаем выбор критерия где самая дорогая идет первой 
       self.get_cart().click()
       print("Click cart")


    # Mетоды
    def select_click_sort_dropdo_button(self): # вызываем выбор кнопки критерия цены и порядка по алфовиту 
        self.get_current_url() # Method get current url
        self.click_sort_dropdo_button()

    def select_item_active_selected(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 
        self.get_current_url() # Method get current url
        self.click_item_active_selected()

    def select_data_value_top_low_price(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_data_value_top_low_price()

    def select_get_select_product(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_get_select_product()

    def select_click_get_cart(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_get_cart()


    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass