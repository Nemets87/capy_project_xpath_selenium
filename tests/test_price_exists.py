import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PriceCheckPage(Base):
    # Локатор цены товара (тот же, что использовали ранее)
    PRICE_LOCATOR = (By.XPATH, "//div[@class='product-item-price']")  # если на странице каталога
    # Для конкретной карточки товара локатор может быть другим. Например:
    # SINGLE_PRICE_LOCATOR = (By.XPATH, "//span[@class='product-price-data']")

    def check_price_exists(self, url: str):
        self.open(url)
        try:
            price_element = self.wait.until(EC.presence_of_element_located(self.PRICE_LOCATOR))
            price_text = price_element.text
            assert price_text, f"Цена отсутствует (пустой текст) на странице {url}"
            # Извлекаем число и проверяем, что оно > 0
            price_value = self.extract_float(price_text)
            assert price_value > 0, f"Цена {price_value} не может быть <= 0 на странице {url}"
            print(f"✅ Цена найдена: {price_value} на {url}")
        except Exception as e:
            raise AssertionError(f"Товар вероятно пропал: {e}")


@allure.feature("Мониторинг наличия товара")
class TestPriceExists:

    @allure.title("Цена товара присутствует (товар в наличии)")
    def test_price_exists_on_category_page(self, driver):
        # Проверяем первый товар в категории новых игр
        page = PriceCheckPage(driver)
        page.check_price_exists("https://капибара161.рф/products/category/5382072")
        page.take_screenshot("price_found")

    # Можно добавить проверку конкретного товара по его URL
    @allure.title("Цена конкретного товара")
    def test_price_exists_for_single_product(self, driver):
        page = PriceCheckPage(driver)
        # Замените на реальный URL товара, который хотите мониторить
        page.check_price_exists("https://капибара161.рф/products/category/5458999")
        page.take_screenshot("single_price_found")