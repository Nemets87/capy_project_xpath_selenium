import allure
import re
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class Base:
    """Базовый класс для всех страниц (исправленная версия)"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger()

    # ---------- Базовые методы работы с браузером ----------
    def open(self, url):
        """Открыть страницу"""
        with allure.step(f"Открыть страницу: {url}"):
            self.driver.get(url)
            self.logger.add_start_step(url)

    def get_current_url(self):
        """Вернуть текущий URL"""
        return self.driver.current_url

    def find_element(self, locator):
        """Найти один элемент с ожиданием видимости"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """Найти все элементы по локатору"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Кликнуть по элементу"""
        with allure.step(f"Кликнуть по элементу: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.add_end_step(self.driver.current_url, "click")

    def send_keys(self, locator, text):
        """Ввести текст в поле"""
        with allure.step(f"Ввести '{text}' в поле: {locator}"):
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text

    def is_element_present(self, locator):
        """Проверить наличие элемента без ожидания"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к Allure"""
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=AttachmentType.PNG)

    # ---------- Методы проверок (assert) ----------
    def assert_url(self, expected_url):
        actual = self.driver.current_url
        assert actual == expected_url, f"URL не совпадает: {actual} != {expected_url}"

    def assert_word(self, element, expected_text):
        actual = element.text
        assert actual == expected_text, f"Текст не совпадает: '{actual}' != '{expected_text}'"
        print("✅ Текст верен")

    @staticmethod
    def extract_float(text: str) -> float:
        # Удаляем все пробелы (в том числе неразрывные) и заменяем запятую на точку
        text = re.sub(r'\s', '', text)          # убираем пробелы
        text = text.replace(',', '.')           # запятую на точку
        matches = re.findall(r'\d+(?:\.\d+)?', text)
        return float(matches[0]) if matches else 0.0

    @staticmethod
    def clean_price_element(element) -> float:
        """Очищает цену из WebElement"""
        return Base.extract_float(element.text)

    # Принимать ожидаемую цену (из фильтра) и фактическую (из корзины).
    """
    Проверяет соответствие цены с заданной погрешностью.
    :param expected_price: ожидаемая цена (из фильтра)
    :param actual_price: фактическая цена (в корзине)
    :param tolerance: допустимая разница (по умолчанию 0.01)
                                                            """
    def assert_price_match(self, expected_price: float, actual_price: float, tolerance: float = 0.01): # погрешность 0.01
        """Сравнивает цены с учётом погрешности"""
        diff = abs(expected_price - actual_price)
        assert diff <= tolerance, f"Цена не совпадает: ожидалось {expected_price}, получено {actual_price}"
        print(f"✅ Цена корректна: {actual_price} (ожидалось {expected_price})")

    # Проверка суммы upper + lower
    def assert_sum_prices(self, price1: float, price2: float, total: float, tolerance: float = 0.01):
        """Проверяет, что сумма двух цен равна общей (например, фильтр min+max = что-то)"""
        assert abs((price1 + price2) - total) <= tolerance, f"Сумма {price1}+{price2} = {price1+price2} не равна {total}"
        print(f"✅ Сумма цен корректна: {price1} + {price2} = {price1+price2}")