import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Добавляем корневую папку в пути поиска
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.client_information_page import Client_information__page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
from pages.viewcart_page import Login_page
from pages.cart_page import Cart_page
from pages.main_page import Main_page


def test_link_about():
    driver = webdriver.Firefox()

    print("Start Test")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    # Закрываем браузер
    driver.quit()
    print("✅ Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_link_about()


