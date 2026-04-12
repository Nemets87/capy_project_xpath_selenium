from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    cookies_notice_button = (By.XPATH, "//button[@id='client-cookies-notice-button']")
    burger_button = (By.XPATH, "//span[@id='burger-btn-text']")

    def click_cookies_notice_button(self):
        self.click(self.cookies_notice_button)
        print("✅ Куки приняты")
        # Добавляем небольшую задержку, чтобы страница стабилизировалась
        time.sleep(1)

    def click_burger_button(self):
        # Явное ожидание кликабельности с увеличенным таймаутом
        self.wait.until(EC.element_to_be_clickable(self.burger_button)).click()
        print("✅ Меню бургер открыто")

    def select_cookies_notice_button(self):
        self.get_current_url()
        self.click_cookies_notice_button()

    def select_burger_button(self):
        self.get_current_url()
        self.click_burger_button()