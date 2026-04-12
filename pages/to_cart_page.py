from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ToCartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    cart_offer_order = (By.XPATH, "//a[@class='button button_for_top-cart-drop-down']")

    def click_cart_offer_order(self):
        # Используем базовый метод click, который автоматически повторяет попытку при StaleElement
        self.click(self.cart_offer_order)
        print("✅ Оформление заказа")

    def select_cart_offer_order(self):
        self.get_current_url()
        self.click_cart_offer_order()