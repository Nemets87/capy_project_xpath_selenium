from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы (подставьте свои, но вы уже дали)
    DELETE_BUTTON = (By.XPATH, "//button[@class='new-cart-item__actions--button new-cart-item__actions--delete js-delete-cart']")
    CONFIRM_DELETE_BUTTON = (By.ID, "js-modal-delete")   # кнопка "Да, удалить"
    CART_ITEM = (By.XPATH, "//div[contains(@class, 'cart-item')]")   # любой товар в корзине
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[contains(text(), 'Корзина пуста')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@class='num-items cart-item__quantity-input js-cart-bar-input js-incremental-input']")
    PLUS_BUTTON = (By.XPATH, "//button[@class='cart-item__quantity-btn js-incremental-plus']")
    MINUS_BUTTON = (By.XPATH, "//button[@class='cart-item__quantity-btn js-incremental-minus']")
    # DELETE_BUTTON = (By.XPATH, "//div[@class='cart-item__bar-delete js-delete-cart-catalog delete']")
    TOTAL_PRICE = (By.XPATH, "//span[@class='js-cart__total']")  # возможно уже есть
    ITEM_PRICE = (By.XPATH, "//span[@class='cart-item__price js-cart-item-price']")  # цена за единицу

    # Геттеры
    def get_delete_button(self):
        return self.find_element(self.DELETE_BUTTON)

    def get_confirm_delete_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))

    def get_quantity(self):
        """Вернуть количество товара (целое число)"""
        value = self.get_attribute(self.QUANTITY_INPUT, "value")
        return int(value) if value else 0

    def click_plus(self):
        self.click(self.PLUS_BUTTON)
        print("➕ Количество увеличено")

    def click_minus(self):
        self.click(self.MINUS_BUTTON)
        print("➖ Количество уменьшено")

    def delete_item(self):
        self.click(self.DELETE_BUTTON)
        print("🗑️ Товар удалён из корзины")

    def get_total_price(self) -> float:
        element = self.find_element(self.TOTAL_PRICE)
        return self.clean_price_element(element)

    def get_item_price(self) -> float:
        element = self.find_element(self.ITEM_PRICE)
        return self.clean_price_element(element)
    
    def delete_item(self):
        """Нажать кнопку удаления товара"""
        self.click(self.DELETE_BUTTON)
        print("🗑️ Нажата кнопка удаления товара")

    def confirm_delete(self):
        """Подтвердить удаление в модальном окне"""
        self.click(self.CONFIRM_DELETE_BUTTON)
        print("✅ Удаление подтверждено")

    def is_cart_empty(self) -> bool:
        """Проверить, пуста ли корзина (нет товаров или есть сообщение)"""
        # Если есть сообщение о пустой корзине – пуста
        if self.is_element_present(self.EMPTY_CART_MESSAGE):
            return True
        # Если нет сообщения, проверяем, есть ли хотя бы один товар
        return not self.is_element_present(self.CART_ITEM)

    def get_quantity(self) -> int:
        """Вернуть количество товара (если один товар)"""
        quantity_input = (By.XPATH, "//input[@class='num-items cart-item__quantity-input js-cart-bar-input js-incremental-input']")
        value = self.get_attribute(quantity_input, "value")
        return int(value) if value else 0
