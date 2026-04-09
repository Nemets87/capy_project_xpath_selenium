from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    main_word = (By.XPATH, "//div[@class='cart__checkout-custom-text text-center']")

    def get_main_word(self):
        return self.wait.until(EC.element_to_be_clickable(self.main_word))

    def finish(self, expected_price: float = None, actual_price: float = None):
        """Завершение теста: проверка текста благодарности и опциональная проверка цены"""
        final_page_true = "https://xn--161-5cdaaf9cq5co.xn--p1ai/products/viewcart"
        self.get_current_url()
        self.assert_url(final_page_true)
        self.assert_word(self.get_main_word(), 'Спасибо за заказ. Мы свяжемся с Вами в ближайшее время.')
        self.take_screenshot("finish_success")

        if expected_price is not None and actual_price is not None:
            self.assert_price_match(expected_price, actual_price)
            print(f"✅ Цена в корзине {actual_price} соответствует ожидаемой {expected_price}")
            self.take_screenshot("price_check")