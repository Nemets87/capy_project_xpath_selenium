import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_agreement_page import UserAgreementPage
from pages.products_page import ProductsPage
from pages.category_page import CatalogPage
from pages.to_cart_page import ToCartPage
from pages.viewcart_page import ViewcartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage


@allure.feature("Покупка товаров")
class TestBuyProduct:

    @allure.story("Самый дорогой товар")
    @allure.title("Покупка товара с максимальной ценой")
    @pytest.mark.order(1)
    def test_buy_product_1(self, driver, set_up, set_group):
        print("Start Test_1")
        print(f"✅ Страница загружена: {driver.title}")

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
        cp.select_click_sort_dropdo_button()
        cp.select_data_value_top_low_price()   # сортируем по убыванию цены
        cp.select_get_select_product()         # добавляем первый товар в корзину
        expected_price = cp.get_first_product_price()   # берём цену этого первого товара

        tcp = ToCartPage(driver)
        tcp.select_cart_offer_order()

        vp = ViewcartPage(driver)
        vp.select_checkmark_button()
        vp.select_order_next_stag()

        cip = ClientInformationPage(driver)
        actual_price = cip.get_need_number_value()   # метод должен вернуть цену
        cip.input_information()

        f = FinishPage(driver)
        f.finish(expected_price=expected_price, actual_price=actual_price)


    @allure.story("Самый дешёвый товар")
    @allure.title("Покупка товара с минимальной ценой")
    @pytest.mark.order(2)
    def test_buy_product_2(self, driver, set_up, set_group):
        print("Start Test_2")
        print(f"✅ Страница загружена: {driver.title}")

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
        cp.select_click_sort_dropdo_button()
        cp.select_data_value_low_to_top_price()   # сортируем по возрастанию цены
        cp.select_get_select_product()            # добавляем первый товар в корзину
        expected_price = cp.get_first_product_price()   

        tcp = ToCartPage(driver)
        tcp.select_cart_offer_order()

        vp = ViewcartPage(driver)
        vp.select_checkmark_button()
        vp.select_order_next_stag()

        cip = ClientInformationPage(driver)
        actual_price = cip.get_need_number_value()   # метод должен вернуть цену
        cip.input_information()
        
        f = FinishPage(driver)
        f.finish(expected_price=expected_price, actual_price=actual_price)
