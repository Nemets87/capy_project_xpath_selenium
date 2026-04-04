import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Добавляем корневую папку в пути поиска
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.client_information_page import Client_information__page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from tests.conftest import set_up
from tests.conftest import set_group

@pytest.mark.order(1)
def test_buy_product_1(set_group,set_up):
    driver = webdriver.Firefox()

    print("Start Test_1")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information__page(driver)
    cip.input_information()
    
    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

@pytest.mark.order(2)
def test_buy_product_2(set_up,set_group):
    driver = webdriver.Firefox()

    print("Start Test_2")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    # Закрываем браузер

@pytest.mark.order(3)
def test_buy_product_3(set_up):
    driver = webdriver.Firefox()

    print("Start Test_3")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    driver.quit()
    print("✅ Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_buy_product_1()
    test_buy_product_2()
    test_buy_product_3()