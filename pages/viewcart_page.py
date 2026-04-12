from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ViewcartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    checkmark = (By.XPATH, "//span[@class='checkmark']")
    order_next_stage = (By.XPATH, "//button[@id='js-next-stage']")

    def click_checkmark_button(self):
        # Используем базовый click с защитой
        self.click(self.checkmark)
        print("✅ Выбран способ оплаты")

    def click_order_next_stage(self):
        self.click(self.order_next_stage)
        print("✅ Переход к оформлению")

    # Методы для тестов
    def select_checkmark_button(self):
        self.get_current_url()
        self.click_checkmark_button()

    def select_order_next_stag(self):
        self.get_current_url()
        self.click_order_next_stage()