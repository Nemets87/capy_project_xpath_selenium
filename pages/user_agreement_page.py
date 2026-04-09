from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class UserAgreementPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    products_button = (By.XPATH, "//a[@href='/products']")

    def get_products_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.products_button))

    def click_products_button(self):
        self.get_products_button().click()
        print("✅ Переход в каталог товаров")

    def select_products_button(self):
        self.get_current_url()
        self.click_products_button()