import sys
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Добавляем корневую папку в пути поиска
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.client_information_page import Client_information__page

from pages.finish_page import Finish_page

from pages.login_page import Login_page
from pages.main_page import Main_page # вызов метода главное страницы (страницы загрузки)
from pages.user_agreement_page import User_agreement_page
from pages.products_page import Products_page
from pages.category_page import Category_page
from pages.to_cart_page import To_cart_page
from pages.viewcart_page import Viewcart_page

from tests.conftest import set_up
from tests.conftest import set_group

@pytest.mark.order(3)
def test_buy_product_3():
    driver = webdriver.Firefox()

    print("Start Test_3")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_cookies_notice_button()
    mp.select_burger_button()

    ug = User_agreement_page(driver)
    ug.select_products_button()

    pp = Products_page(driver)
    pp.select_sony_playstation_games_button()
    pp.select_sony_playstation_5_games_button()
    pp.select_sony_playstation_5_new_games_button()

    cp = Category_page(driver)
    cp.select_click_sort_dropdo_button()
    cp.select_data_value_a_z_text()
    cp.select_get_select_product()

    tcp = To_cart_page(driver)
    tcp.select_cart_offer_order()

    vp = Viewcart_page(driver)
    vp.select_checkmark_button()
    vp.select_order_next_stag()

    cip = Client_information__page(driver)
    cip.input_information()

    f = Finish_page(driver)
    f.finish()

@pytest.mark.order(4)
def test_buy_product_4():
    driver = webdriver.Firefox()

    print("Start Test_4")
    print(f"✅ Страница загружена: {driver.title}")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_cookies_notice_button()
    mp.select_burger_button()

    ug = User_agreement_page(driver)
    ug.select_products_button()

    pp = Products_page(driver)
    pp.select_sony_playstation_games_button()
    pp.select_sony_playstation_5_games_button()
    pp.select_sony_playstation_5_new_games_button()

    cp = Category_page(driver)
    cp.select_click_sort_dropdo_button()
    cp.select_data_value_z_a_text()
    cp.select_get_select_product()

    tcp = To_cart_page(driver)
    tcp.select_cart_offer_order()

    vp = Viewcart_page(driver)
    vp.select_checkmark_button()
    vp.select_order_next_stag()

    cip = Client_information__page(driver)
    cip.input_information()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)
    driver.quit()
    print("✅ Все тесты пройдены успешно!")

if __name__ == "__main__":
    # test_buy_product_3()
    test_buy_product_4()
   