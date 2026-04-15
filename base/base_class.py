import allure
import re
import time
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from utils.logger import Logger


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = Logger()
        

    # ---------- Базовые методы с защитой от StaleElement ----------
    def _safe_action(self, locator, action, *args, retries=3):
        """Универсальный метод для выполнения действия с повтором при StaleElement"""
        for attempt in range(retries):
            try:
                if action == "click":
                    element = self.wait.until(EC.element_to_be_clickable(locator))
                    element.click()
                    self.logger.add_end_step(self.driver.current_url, "click")
                    return
                elif action == "send_keys":
                    element = self.wait.until(EC.visibility_of_element_located(locator))
                    element.clear()
                    element.send_keys(*args)
                    return
                elif action == "get_text":
                    element = self.wait.until(EC.visibility_of_element_located(locator))
                    return element.text
                elif action == "get_attribute":
                    element = self.wait.until(EC.visibility_of_element_located(locator))
                    return element.get_attribute(*args)
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise
                time.sleep(0.5)
        return None

    def open(self, url):
        with allure.step(f"Открыть страницу: {url}"):
            self.driver.get(url)
            self.logger.add_start_step(url)
    
    def double_click(self, locator, retries=3):
        """Выполнить двойной клик по элементу с повторными попытками"""
        with allure.step(f"Двойной клик по элементу: {locator}"):
            for attempt in range(retries):
                try:
                
                    element = self.wait.until(EC.element_to_be_clickable(locator))
                    ActionChains(self.driver).click(element).click(element).perform()
                    # element = self.wait.until(EC.element_to_be_clickable(locator))
                    # ActionChains(self.driver).double_click(element).perform()
                    # self.logger.add_end_step(self.driver.current_url, "double_click")
                    return
                except StaleElementReferenceException:
                    if attempt == retries - 1:
                        raise
                    time.sleep(0.5)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        with allure.step(f"Кликнуть по элементу: {locator}"):
            self._safe_action(locator, "click")

    def send_keys(self, locator, text):
        with allure.step(f"Ввести '{text}' в поле: {locator}"):
            self._safe_action(locator, "send_keys", text)

    def get_text(self, locator):
        return self._safe_action(locator, "get_text")

    def get_attribute(self, locator, attribute):
        return self._safe_action(locator, "get_attribute", attribute)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def take_screenshot(self, name="screenshot"):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=AttachmentType.PNG)

    # ---------- Проверки ----------
    def assert_url(self, expected_substring: str):
        actual = self.driver.current_url
        assert expected_substring in actual, f"URL не содержит '{expected_substring}': {actual}"

    def assert_word(self, element, expected_text):
        actual = element.text
        assert actual == expected_text, f"Текст не совпадает: '{actual}' != '{expected_text}'"
        print("✅ Текст верен")

    @staticmethod
    def extract_float(text: str) -> float:
        text = re.sub(r'\s', '', text)
        text = text.replace(',', '.')
        matches = re.findall(r'\d+(?:\.\d+)?', text)
        return float(matches[0]) if matches else 0.0

    @staticmethod
    def clean_price_element(element) -> float:
        return Base.extract_float(element.text)

    def assert_price_match(self, expected_price: float, actual_price: float, tolerance: float = 0.01):
        diff = abs(expected_price - actual_price)
        assert diff <= tolerance, f"Цена не совпадает: ожидалось {expected_price}, получено {actual_price}"
        print(f"✅ Цена корректна: {actual_price} (ожидалось {expected_price})")