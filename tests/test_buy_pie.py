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




@allure.feature("Покупка товаров +-")
class TestBuyProduct:

    @allure.story("Покупаем на кол-во с плюсом")
    @allure.title("Покупка товара сперва проверяем + потом -")
    @pytest.mark.order(1)
    def test_buy_product_plus_minus(self, driver):
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
 
        cp.select_get_select_product() # добавляем первый товар в корзину
        expected_price = cp.get_first_product_price()   # берём цену этого первого товара

        tcp = ToCartPage(driver)
        tcp.select_plus_button()
        tcp.double_click_plus()
        tcp.double_click_plus()
        tcp.double_click_plus()
        time.sleep(3)
        tcp.select_minus_button()
        tcp.double_click_minus()
        tcp.double_click_minus()
        tcp.double_click_minus()
        time.sleep(3)
     
        tcp.select_cart_offer_order()
       
        vp = ViewcartPage(driver)
        vp.select_checkmark_button()
        vp.select_order_next_stag()

        cip = ClientInformationPage(driver)
        actual_price = cip.get_need_number_value()   # метод должен вернуть цену
        cip.input_information()

        f = FinishPage(driver)
        f.finish(expected_price=expected_price, actual_price=actual_price)


    @allure.story("Покупаем на кол-во с минус")
    @allure.title("Покупка товара сперва проверяем - потом +")
    @pytest.mark.order(2)
    def test_buy_product_minus_plus(self, driver):
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
 
        cp.select_get_select_product() # добавляем первый товар в корзину
        expected_price = cp.get_first_product_price()   # берём цену этого первого товара

        tcp = ToCartPage(driver)
       

        tcp.select_minus_button()
        time.sleep(3)

        tcp.select_plus_button()
        time.sleep(3)
     
        tcp.select_cart_offer_order()
       
        vp = ViewcartPage(driver)
        vp.select_checkmark_button()
        vp.select_order_next_stag()

        cip = ClientInformationPage(driver)
        actual_price = cip.get_need_number_value()   # метод должен вернуть цену
        cip.input_information()

        f = FinishPage(driver)
        print("✅ Минус не отнял последний товар и не удалил из корзины")
        f.finish(expected_price=expected_price*2, actual_price=actual_price)
        print("✅ X2 стоимость товара ибо минус не убирает с корзины в 0")
    
