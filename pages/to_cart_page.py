from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ToCartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)



    # Локаторы
    plus_button = (By.XPATH, "//button[@class='cart-item__quantity-btn js-incremental-plus']")
    minus_button = (By.XPATH, "//button[@class='cart-item__quantity-btn js-incremental-minus']")
    cart_offer_order = (By.XPATH, "//a[@class='button button_for_top-cart-drop-down']")
    
    # Геттеры (используют базовые методы)
    def get_plus_button(self):
        return self.find_element(self.plus_button)
    
    def get_minus_button(self):
        return self.find_element(self.minus_button)

    def get_cart_offer_order(self):
        return self.find_element(self.cart_offer_order)

    # Действия
    def click_plus_button(self):
        self.click(self.plus_button)
        print("✅ Увеличели кол-во товаров")

    def click_minus_button(self):
        self.click(self.minus_button)
        print("✅ Уменьшили кол-во товаров")

    def click_cart_offer_order(self):
        # Используем базовый метод click, который автоматически повторяет попытку при StaleElement
        self.click(self.cart_offer_order)
        print("✅ Оформление заказа")


    # Методы для тестов
    def select_plus_button(self):
        self.click_plus_button()

    def select_minus_button(self):
        self.click_minus_button()

    def double_click_plus(self):
        """Двойной клик по кнопке увеличения количества"""
        self.double_click(self.plus_button)
        print("✅ Двойной клик по плюсу (количество увеличено на 2)")

    def double_click_minus(self):
        """Двойной клик по кнопке уменьшения количества"""
        self.double_click(self.minus_button)
        print("✅ Двойной клик по минусу (количество уменьшено на 2)")

    def select_cart_offer_order(self):
        self.get_current_url()
        self.click_cart_offer_order()

