import allure
import pytest
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_agreement_page import UserAgreementPage
from pages.products_page import ProductsPage
from pages.category_page import CatalogPage
from pages.to_cart_page import ToCartPage
from pages.viewcart_page import ViewcartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




@allure.feature("Покупка нескольких товаров")
@allure.story("Суммирование самого дорогого и самого дешёвого")
class TestBuyProductSum:

    @allure.title("Проверка суммы двух товаров в корзине и после оформления")
    def test_sum_prices(self, driver):
        # 1. Открыть главную страницу и пройти по всем пунктам меню до каталога новых игр
        login = LoginPage(driver)
        login.autorization()

        mp = MainPage(driver)
        mp.select_cookies_notice_button()
        mp.select_burger_button()

        ug = UserAgreementPage(driver)
        ug.select_products_button()

        pp = ProductsPage(driver)
        pp.select_sony_playstation_games_button()
        pp.select_sony_playstation_5_games_button()
        pp.select_sony_playstation_5_new_games_button()

        cp = CatalogPage(driver)

        # 2. Добавить самый дорогой товар
        cp.select_click_sort_dropdo_button()
        cp.select_data_value_top_low_price()           # сортировка по убыванию
        expensive_price = cp.get_first_product_price() # запоминаем цену
        cp.select_get_select_product()                 # добавляем в корзину
        print(f"Самый дорогой товар: {expensive_price}")

        # 3. Вернуться в каталог (нажать на логотип или кнопку "Назад")
        # Проще всего перезагрузить страницу каталога, но можно кликнуть по логотипу.
        # Для простоты: снова открыть нужную категорию (но чтобы не усложнять, используем прямой переход)
        driver.get("https://капибара161.рф/products/category/5382072")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='sort ui dropdown small-12 selection']"))) 
        # Небольшая пауза для загрузки
       
        time.sleep(1)

        # 4. Добавить самый дешёвый товар
        cp = CatalogPage(driver)  # создаём заново, т.к. страница перезагружена
        cp.select_click_sort_dropdo_button()
        cp.select_data_value_low_to_top_price()        # сортировка по возрастанию
        cheap_price = cp.get_first_product_price()    # запоминаем цену
        cp.select_get_select_product()                # добавляем в корзину
        print(f"Самый дешёвый товар: {cheap_price}")

        # 5. Перейти в корзину и проверить общую сумму
        tcp = ToCartPage(driver)
        tcp.select_cart_offer_order()

        vp = ViewcartPage(driver)
        vp.select_checkmark_button()
        vp.select_order_next_stag()

        cip = ClientInformationPage(driver)
        actual_sum = cip.get_need_number_value()      # общая сумма в корзине
        expected_sum = expensive_price + cheap_price
        print(f"Ожидаемая сумма: {expected_sum}, Фактическая: {actual_sum}")

        assert abs(expected_sum - actual_sum) < 0.01, f"Сумма не совпадает: {expected_sum} != {actual_sum}"

        # 6. Оформить заказ и на финише снова проверить сумму (если нужно)
        cip.input_information()

        f = FinishPage(driver)
        f.finish(expected_price=expected_sum, actual_price=actual_sum)  # передаём ожидаемую и фактическую сумму