from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    cookies_notice_button = (By.XPATH, "//button[@id='client-cookies-notice-button']")
    burger_button = (By.XPATH, "//span[@id='burger-btn-text']")

    # Геттеры
    def get_cookies_notice_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cookies_notice_button))

    def get_burger_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.burger_button))

    # Действия
    def click_cookies_notice_button(self):
        self.get_cookies_notice_button().click()
        print("✅ Куки приняты")

    def click_burger_button(self):
        self.get_burger_button().click()
        print("✅ Меню бургер открыто")

    # Методы для тестов
    def select_cookies_notice_button(self):
        self.get_current_url()
        self.click_cookies_notice_button()

    def select_burger_button(self):
        self.get_current_url()
        self.click_burger_button()