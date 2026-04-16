# utils/price_parser.py
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

URL = "https://капибара161.рф/products/59830628"
PRICE_LOCATOR = (By.XPATH, "//span[@class='product-price-data']")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def _clean_price(text: str) -> float:
    text = re.sub(r'\s', '', text)
    text = text.replace(',', '.')
    matches = re.findall(r'\d+(?:\.\d+)?', text)
    return float(matches[0]) if matches else 0.0

def get_price_requests() -> float | None:
    try:
        resp = requests.get(URL, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        elem = soup.find('span', class_='product-price-data')
        if not elem:
            return None
        return _clean_price(elem.text)
    except Exception:
        return None

def get_price_selenium() -> float | None:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(URL)
        elem = driver.find_element(*PRICE_LOCATOR)
        price_text = elem.text
        return _clean_price(price_text)
    except Exception:
        return None
    finally:
        driver.quit()

def get_price() -> float | None:
    """Сначала requests, если не удалось – Selenium."""
    price = get_price_requests()
    if price is not None:
        return price
    # fallback через Selenium
    return get_price_selenium()