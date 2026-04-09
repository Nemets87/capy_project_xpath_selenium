import allure
import pytest
import requests
from bs4 import BeautifulSoup
import re
import os

URL = "https://капибара161.рф/products/59830628"
CACHE_FILE = "price_cache.txt"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_current_price() -> float | None:
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        price_elem = soup.find('span', class_='product-price-data')
        if not price_elem:
            return None
        price_text = price_elem.get_text(strip=True)
        clean_price = re.sub(r'[^\d.,]', '', price_text.replace(' ', ''))
        clean_price = clean_price.replace(',', '.')
        if clean_price.count('.') > 1:
            parts = clean_price.split('.')
            clean_price = ''.join(parts[:-1]) + '.' + parts[-1]
        return float(clean_price)
    except Exception:
        return None

def save_price(price: float):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        f.write(str(price))

def read_old_price() -> float | None:
    if not os.path.exists(CACHE_FILE):
        return None
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return float(f.read().strip())
    except:
        return None

@allure.feature("Мониторинг цены")
@allure.story("PS5 Slim")
class TestPriceMonitor:
    @allure.title("Проверка наличия товара и изменения цены")
    def test_price_change(self):
        with allure.step("Получить текущую цену со страницы"):
            current_price = get_current_price()
            # Если цена не найдена, тест падает с рекомендацией
            assert current_price is not None, (
                f"❌ Товар снят с продажи или цена не найдена на странице {URL}. "
                "Ищите в другом магазине или ждите появления."
            )
            allure.attach(str(current_price), name="Текущая цена", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Прочитать сохранённую цену"):
            old_price = read_old_price()
            if old_price is None:
                allure.attach("Первый запуск: цена сохранена", name="Инфо", attachment_type=allure.attachment_type.TEXT)
                save_price(current_price)
                pytest.skip("Первый запуск: нет данных для сравнения")
            allure.attach(str(old_price), name="Старая цена", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Сравнить цены"):
            if current_price < old_price:
                message = f"🎉 Цена упала: {old_price} → {current_price}. Надо покупать!"
            elif current_price > old_price:
                message = f"📈 Цена выросла: {old_price} → {current_price}. Нужно ждать."
            else:
                message = "🔄 Цена не изменилась."
            allure.attach(message, name="Решение", attachment_type=allure.attachment_type.TEXT)
            print(message)

        with allure.step("Обновить кэш цены"):
            save_price(current_price)