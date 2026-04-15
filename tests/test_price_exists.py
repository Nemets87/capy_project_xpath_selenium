import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.category_page import CatalogPage
from pages.cart_page import CartPage
from pages.to_cart_page import ToCartPage


class PriceCheckPage(Base):
    PRICE_LOCATOR = (By.XPATH, "//div[@class='product-item-price']")

    def check_price_exists(self, url: str):
        self.open(url)
        try:
            price_element = self.wait.until(EC.presence_of_element_located(self.PRICE_LOCATOR))
            price_text = price_element.text
            assert price_text, f"Цена отсутствует (пустой текст) на странице {url}"
            price_value = self.extract_float(price_text)
            assert price_value > 0, f"Цена {price_value} не может быть <= 0 на странице {url}"
            print(f"✅ Цена найдена: {price_value} на {url}")
        except Exception as e:
            raise AssertionError(f"Товар вероятно пропал: {e}")


@allure.feature("Мониторинг наличия товара и корзины")
@pytest.mark.order(10)
class TestPriceExists:

    @allure.title("Цена товара присутствует (товар в наличии)")
    def test_price_exists_on_category_page(self, driver):
        page = PriceCheckPage(driver)
        page.check_price_exists("https://капибара161.рф/products/category/5382072")
        page.take_screenshot("price_found")

    @allure.title("Цена конкретного товара")
    def test_price_exists_for_single_product(self, driver):
        page = PriceCheckPage(driver)
        page.check_price_exists("https://капибара161.рф/products/category/5458999")
        page.take_screenshot("single_price_found")

    @allure.title("Удаление товара из корзины перед оформлением")
    def test_remove_from_cart(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open("https://капибара161.рф/products/category/5382072")
        catalog_page.select_click_sort_dropdo_button()
        catalog_page.select_data_value_low_to_top_price()
        catalog_page.select_get_select_product()
        print("✅ Товар добавлен в корзину")

        cart_page = catalog_page.go_to_cart()

        # Удаляем товар и подтверждаем
        cart_page.delete_item()
        cart_page.confirm_delete()

        # Ждём, пока корзина станет пустой (исчезнут товары или появится сообщение)
        WebDriverWait(driver, 10).until(lambda d: cart_page.is_cart_empty())
        assert cart_page.is_cart_empty(), "Корзина не стала пустой после удаления"
        print("✅ Корзина пуста")

        cart_page.take_screenshot("empty_cart_after_delete")

    @allure.title("Попытка оформления заказа с пустой корзиной")
    def test_empty_cart_checkout(self, driver):
        driver.get("https://капибара161.рф/products/viewcart")
        cart_page = CartPage(driver)
        # Проверяем, что корзина пуста
        assert cart_page.is_cart_empty(), "Корзина не пуста, а должна быть"
        # Проверяем, что кнопка оформления отсутствует
        checkout_button = (By.XPATH, "//a[contains(@class, 'checkout')]")
        assert not driver.find_elements(*checkout_button), "Кнопка оформления присутствует при пустой корзине"
        driver.save_screenshot("empty_cart_checkout.png")


