from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ProductsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    sony_playstation_games_button = (By.XPATH, "//a[text()='Игры Sony Playstation']")
    sony_playstation_5_games_button = (By.XPATH, "//a[text()='Игры Sony Playstation 5']")
    sony_playstation_5_new_games_button = (By.XPATH, "//a[text()='New']")

    # Геттеры
    def get_sony_playstation_games_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sony_playstation_games_button))

    def get_sony_playstation_5_games_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sony_playstation_5_games_button))

    def get_sony_playstation_5_new_games_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sony_playstation_5_new_games_button))

    # Действия
    def click_sony_playstation_games_button(self):
        self.get_sony_playstation_games_button().click()
        print("✅ Выбраны игры Sony Playstation")

    def click_sony_playstation_5_games_button(self):
        self.get_sony_playstation_5_games_button().click()
        print("✅ Выбраны игры Sony Playstation 5")

    def click_sony_playstation_5_new_games_button(self):
        self.get_sony_playstation_5_new_games_button().click()
        print("✅ Выбраны новые игры")

    # Методы для тестов
    def select_sony_playstation_games_button(self):
        self.get_current_url()
        self.click_sony_playstation_games_button()

    def select_sony_playstation_5_games_button(self):
        self.get_current_url()
        self.click_sony_playstation_5_games_button()

    def select_sony_playstation_5_new_games_button(self):
        self.get_current_url()
        self.click_sony_playstation_5_new_games_button()