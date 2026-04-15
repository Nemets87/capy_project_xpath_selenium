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


@allure.feature("Негативные сценарии оформления заказа")
class TestNegative:

    @allure.title("Попытка оформления заказа с невалидными данными")
    @pytest.mark.order(9)
    def test_invalid_checkout_data(self, driver):
        print("✅Start Test_9")
        print(f"✅ Страница загружена: {driver.title}")
        # 1. Добавляем любой товар в корзину
        login = LoginPage(driver)
        login.autorization()

        main_page = MainPage(driver)
        main_page.select_cookies_notice_button()
        main_page.select_burger_button()

        user_agreement = UserAgreementPage(driver)
        user_agreement.select_products_button()

        products_page = ProductsPage(driver)
        products_page.select_sony_playstation_games_button()
        products_page.select_sony_playstation_5_games_button()
        products_page.select_sony_playstation_5_new_games_button()

        catalog_page = CatalogPage(driver)
        catalog_page.select_click_sort_dropdo_button()
        catalog_page.select_data_value_low_to_top_price()  # берём самый дешёвый
        catalog_page.select_get_select_product()

        to_cart_page = ToCartPage(driver)
        to_cart_page.select_cart_offer_order()

        viewcart_page = ViewcartPage(driver)
        viewcart_page.select_checkmark_button()
        viewcart_page.select_order_next_stag()

        # 2. Заполняем форму невалидными данными
        checkout_page = ClientInformationPage(driver)
        checkout_page.input_invalid_information()

        # 3. Проверяем, что заказ не ушёл (остались на той же странице или появилась ошибка)
        # Ожидаем, что URL не изменился на страницу подтверждения
        assert "viewcart" in driver.current_url, "Произошёл переход на финальную страницу, хотя данные невалидны"
        
        # Дополнительно можно проверить наличие сообщения об ошибке (если сайт его выводит)
        # Пример: assert checkout_page.is_error_message_displayed(), "Сообщение об ошибке не появилось"
        
        checkout_page.take_screenshot("invalid_data_error")
