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

    # """Method assert number"""
    # def assert_number(self,max, number):
    #     assert value_upper() == write_need_number() if test_buy_product_1
    #     assert value_lower() == write_need_number() if test_buy_product_1
    #     print("Good value number")
