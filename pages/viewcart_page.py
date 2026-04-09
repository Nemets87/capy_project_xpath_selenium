from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ViewcartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    checkmark = (By.XPATH, "//span[@class='checkmark']")
    order_next_stage = (By.XPATH, "//button[@id='js-next-stage']")

    def get_checkmark_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.checkmark))

    def get_order_next_stage(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_next_stage))

    def click_checkmark_button(self):
        self.get_checkmark_button().click()
        print("✅ Выбран способ оплаты")

    def click_order_next_stage(self):
        self.get_order_next_stage().click()
        print("✅ Переход к оформлению")

    def select_checkmark_button(self):
        self.get_current_url()
        self.click_checkmark_button()

    def select_order_next_stag(self):   # сохранено для совместимости
        self.get_current_url()
        self.click_order_next_stage()