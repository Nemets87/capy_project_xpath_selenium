import allure
import pytest
from pages.category_page import CatalogPage


@allure.feature("Корзина проверка")
@allure.story("Покупка товаров")
@pytest.mark.order(3)
class TestBuyAllProducts:
      print("Start Test_3")

    @allure.title("Добавление всех товаров на странице в корзину")
    def test_add_all_products_to_cart(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open("https://капибара161.рф/products/category/5382072")
        catalog_page.add_all_products_to_cart()
        cart_page = catalog_page.go_to_cart()
        cart_page.take_screenshot("cart_with_all_products")

