import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.cart_page import CartPage   # мы создадим cart_page.py позже
import time
import re


class CatalogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # ---------- Локаторы ----------
    sort_dropdo_button = (By.XPATH, "//div[@class='sort ui dropdown small-12 selection']")
    upper = (By.XPATH, "//input[@name='max_cost']")
    lower = (By.XPATH, "//input[@name='min_cost']")
    data_value_top_low_price = (By.XPATH, "//div[text()='Цена (по убыванию)']")
    data_value_low_to_top_price = (By.XPATH, "//div[text()='Цена (по возрастанию)']")
    data_value_a_z_text = (By.XPATH, "//div[text()='Наименование (А—Я)']")
    data_value_z_a_text = (By.XPATH, "//div[text()='Наименование (Я—А)']")
    select_product = (By.XPATH, "//button[@class='button product-item__button button_for_product-card cart-btn js-order-product js-cart-btn']")
    cart = (By.XPATH, "//span[@class='top-cart__notification top-cart__notification--round-3 quantity-items']")
    cart_offer_order = (By.XPATH, "//a[@class='button button_for_top-cart-drop-down']")
    checkmark = (By.XPATH, "//span[@class='checkmark']")
    go_to_buy = (By.XPATH, "//button[@id='js-next-stage']")

    # Для теста "купить все товары"
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(@class, 'cart-btn')]")

    first_product_price_locator = (By.XPATH, "(//div[@class='product-item-price'])[1]") 

    # ---------- Геттеры ----------
    def get_sort_dropdo_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sort_dropdo_button))

    def get_data_value_a_z_text(self):
        return self.wait.until(EC.element_to_be_clickable(self.data_value_a_z_text))

    def get_data_value_z_a_text(self):
        return self.wait.until(EC.element_to_be_clickable(self.data_value_z_a_text))

    def get_data_value_top_low_price(self):
        return self.wait.until(EC.element_to_be_clickable(self.data_value_top_low_price))

    def get_data_value_low_to_top_price(self):
        return self.wait.until(EC.element_to_be_clickable(self.data_value_low_to_top_price))

    def get_upper(self):
        return self.wait.until(EC.presence_of_element_located(self.upper))

    def get_lower(self):
        return self.wait.until(EC.presence_of_element_located(self.lower))

    def get_select_product(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_product))

    def get_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart))

    # ---------- Действия ----------
    def click_sort_dropdo_button(self):
        self.get_sort_dropdo_button().click()
        print("✅ Меню сортировки открыто")

    def click_data_value_a_z_text(self):
        self.get_data_value_a_z_text().click()
        print("✅ Сортировка А-Я")

    def click_data_value_z_a_text(self):
        self.get_data_value_z_a_text().click()
        print("✅ Сортировка Я-А")

    def click_data_value_top_low_price(self):
        self.get_data_value_top_low_price().click()
        print("✅ Сортировка: дорогие первыми")

    def click_data_value_low_to_top_price(self):
        self.get_data_value_low_to_top_price().click()
        print("✅ Сортировка: дешёвые первыми")

    def click_get_select_product(self):
        self.get_select_product().click()
        print("✅ Товар добавлен в корзину")

    def click_get_cart(self):
        self.get_cart().click()
        print("✅ Переход в корзину")

    # ---------- Методы для получения цен ----------
    """Возвращает числовое значение максимальной цены из поля max_cost"""
    def get_upper_price(self) -> float:
        element = self.get_upper()
        value_str = element.get_attribute("value") # у input value
        return self.extract_float(value_str) # используем статический метод
    """Возвращает числовое значение минимальной цены из поля min_cost"""
    def get_lower_price(self) -> float:
        element = self.get_lower()
        value_str = element.get_attribute("value") # у input value
        return self.extract_float(value_str) # используем статический метод

    # ---------- Методы для тестов (старые наименования) ----------
    def select_click_sort_dropdo_button(self):
        self.get_current_url()
        self.click_sort_dropdo_button()

    def select_data_value_a_z_text(self):
        self.get_current_url()
        self.click_data_value_a_z_text()

    def select_data_value_z_a_text(self):
        self.get_current_url()
        self.click_data_value_z_a_text()

    def select_data_value_top_low_price(self):
        self.get_current_url()
        self.click_data_value_top_low_price()

    def select_data_value_low_to_top_price(self):
        self.get_current_url()
        self.click_data_value_low_to_top_price()

    def select_get_select_product(self):
        self.get_current_url()
        self.click_get_select_product()

    def select_click_get_cart(self):
        self.get_current_url()
        self.click_get_cart()

    # ---------- Метод для покупки всех товаров ----------

    def get_first_product_price(self) -> float:
        """Возвращает цену первого товара в списке (после сортировки)"""
        price_element = self.wait.until(EC.presence_of_element_located(self.first_product_price_locator))
        price_text = price_element.text
        # Убираем пробелы, символы валют, оставляем только цифры и точку
        clean_price = re.sub(r'[^\d.]', '', price_text.replace(' ', ''))
        return float(clean_price) if clean_price else 0.0


    def add_all_products_to_cart(self):
        with allure.step("Добавить все товары на странице в корзину"):
            add_buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
            for button in add_buttons:
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(0.5)

    def go_to_cart(self):
        cart_link = (By.XPATH, "//a[contains(@href, 'viewcart')]")
        self.click(cart_link)
        return CartPage(self.driver)