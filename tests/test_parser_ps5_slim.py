import requests
from bs4 import BeautifulSoup
import re
import os

# --- Настройки ---
URL = "https://капибара161.рф/products/59830628"
CACHE_FILE = "price_cache.txt"

# Заголовки, чтобы имитировать браузер
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_current_price():
    """Получает цену товара со страницы. Возвращает float или None при ошибке."""
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()  # выбросит исключение при HTTP-ошибке
        response.encoding = 'utf-8'  # явно указываем кодировку

        soup = BeautifulSoup(response.text, 'html.parser')
        # Ищем элемент с классом product-price-data
        price_elem = soup.find('span', class_='product-price-data')
        if not price_elem:
            print("❌ Элемент с ценой не найден на странице.")
            return None

        price_text = price_elem.get_text(strip=True)
        # Убираем всё, кроме цифр, точки и запятой
        clean_price = re.sub(r'[^\d.,]', '', price_text)
        # Заменяем запятую на точку для float
        clean_price = clean_price.replace(',', '.')
        # Убираем возможные лишние точки
        if clean_price.count('.') > 1:
            # Оставляем только последнюю точку (если в цене есть тысячи через точку)
            parts = clean_price.split('.')
            clean_price = ''.join(parts[:-1]) + '.' + parts[-1]
        price = float(clean_price)
        return price
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при запросе страницы: {e}")
        return None
    except Exception as e:
        print(f"❌ Непредвиденная ошибка при парсинге: {e}")
        return None

def save_price(price):
    """Сохраняет цену в файл."""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        f.write(str(price))

def read_old_price():
    """Читает сохранённую цену из файла. Если файла нет – возвращает None."""
    if not os.path.exists(CACHE_FILE):
        return None
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return float(f.read().strip())
    except (ValueError, IOError):
        return None

def main():
    print("🔄 Проверяем цену...")
    current_price = get_current_price()
    if current_price is None:
        print("⚠️ Не удалось получить цену. Завершаем.")
        return

    old_price = read_old_price()
    print(f"Текущая цена: {current_price}")

    if old_price is None:
        print("📁 Сохраняем начальную цену.")
        save_price(current_price)
        return

    print(f"Старая цена: {old_price}")

    if current_price < old_price:
        print(f"🎉 Цена упала! Было: {old_price}, стало: {current_price}. Надо покупать!")
    elif current_price > old_price:
        print(f"📈 Цена выросла! Было: {old_price}, стало: {current_price}. Нужно ждать.")
    else:
        print("🔄 Цена не изменилась.")

    # Обновляем сохранённую цену
    save_price(current_price)

if __name__ == "__main__":
    main()