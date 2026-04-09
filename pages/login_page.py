import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class LoginPage(Base):
    # Локаторы
    USERNAME_INPUT = (By.XPATH, "//input[@data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//button[@class='error-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url="https://капибара161.рф/"):
        """Открыть главную страницу"""
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        """Выполнить вход с указанными данными"""
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Проверить, появилось ли сообщение об ошибке"""
        return self.is_element_present(self.ERROR_MESSAGE)

    def autorization(self):
        """Метод для открытия главной страницы (совместимость со старыми тестами)"""
        self.open()
        self.get_current_url()