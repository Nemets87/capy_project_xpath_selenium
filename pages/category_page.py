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
    data_value_low_to_top_price = "//div[@class='item'][1]" # самая дорогая идет первой 
    data_value_low_to_top_price = "//div[@class='item'][2]" # самая дешевая идет первой
    data_value_a_z_text = "//div[text()='Наименование (А—Я)']" # А—Я
    data_value_z_a_text = "//div[text()='Наименование (Я—А)']" # Я-А

    select_product = "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']"

    cart_sender = //span[@class='cart-btn__text product-item__button-text']


    actions = ActionChains(driver)
    slider = driver.find_element(By.XPATH, handle_upper)

    actions.click_and_hold(slider).move_by_offset(5000, 0).release().perform()
  
    # Getters
    def get_sony_playstation_games_button(self): # целимся в выбор кнопки каталог товаров Игры Sony Playstation
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sony_playstation_games_button))) 
    
    def get_sony_playstation_5_games_button(self): # целимся в выбор кнопки каталог товаров Игры Sony Playstation 5
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sony_playstation_5_games_button))) 
    
    def get_sony_playstation_5_new_games_button(self): # целимся в выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sony_playstation_5_new_games_button))) 

                                                                            
    # Actions
    def click_sony_playstation_games_button(self): # кликаем выбор Игры Sony Playstation
       self.get_sony_playstation_games_button().click()
       print("Click get_sony_playstation_games_button")

    def click_sony_playstation_5_games_button(self): # кликаем выбор Игры Sony Playstation 5
       self.get_sony_playstation_5_games_button().click()
       print("Click get_sony_playstation_5_games_button")

    def click_sony_playstation_5_new_games_button(self): # кликаем выбор Игры Sony Playstation 5 новые игры
       self.get_sony_playstation_5_new_games_button().click()
       print("Click get_sony_playstation_5_new_games_button")


    # Mетоды
    def select_sony_playstation_games_button(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 
        self.get_current_url() # Method get current url
        self.click_sony_playstation_games_button()

    def select_sony_playstation_5_games_button(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 
        self.get_current_url() # Method get current url
        self.click_sony_playstation_5_games_button()

    def select_sony_playstation_5_new_games_button(self): # вызываем выбор кнопки каталог товаров Игры Sony Playstation 5 новые игры
        self.get_current_url() # Method get current url
        self.click_sony_playstation_5_new_games_button()


    # Этот блок выполняется только если файл запущен напрямую (не при импорте)
if __name__ == "__main__":
    # Здесь можно написать код для самостоятельного тестирования класса
    pass