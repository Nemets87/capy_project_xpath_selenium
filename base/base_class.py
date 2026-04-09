import datetime
import time
import re

from tests.conftest import set_up

# Класс лучше расположить ВЫШЕ всего основного кода - это правильная архитектура
class Base():
    def __init__(self, driver):
        self.driver = driver

        """Method get price"""
    @staticmethod
    def extract_float(text: str) -> float:
        matches = re.findall(r'\d+(?:\.\d+)?', text)
        
        if matches:
            return float(matches[0])  # Берём первое найденное число
        return 0.0  # Возвращаем 0 если чисел не найдено
    
    @staticmethod
    def clean_price_element(element) -> float:
        text = element.text
        return Base.extract_float(text)

        """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(" Current url " + get_url)

        """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

        """Method Screen_shot"""
    def get_screenshot(self):
        # Создание скриншота
        now_date = datetime.datetime.now().strftime("P1 %Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        # ./Screen - точка указывает на текущий каталог, то есть найти в этом проекте папку Screen
        self.driver.save_screenshot(f"./screen/{name_screenshot}")
        print("Screenshot done")

        """Method assert url"""
    def assert_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()
        Logger.write_log_to_file(f"Клик по элементу {locator}")


    def assert_price_match(self, expected_price: float, actual_price: float, tolerance: float = 0.01):
        """
        Проверяет соответствие цены с заданной погрешностью.
        :param expected_price: ожидаемая цена (из фильтра)
        :param actual_price: фактическая цена (в корзине)
        :param tolerance: допустимая разница (по умолчанию 0.01)
        """
        diff = abs(expected_price - actual_price)
        assert diff <= tolerance, f"Цена не совпадает! Ожидалось {expected_price}, получено {actual_price}, разница {diff}"
        print(f"✅ Цена корректна: {actual_price} (ожидалось {expected_price})")


    def assert_sum_prices(self, price1: float, price2: float, total: float, tolerance: float = 0.01):
        """Проверяет, что сумма двух цен равна общей (например, фильтр min+max = что-то)"""
        assert abs((price1 + price2) - total) <= tolerance, f"Сумма {price1}+{price2} = {price1+price2} не равна {total}"
        print(f"✅ Сумма цен корректна: {price1} + {price2} = {price1+price2}")
