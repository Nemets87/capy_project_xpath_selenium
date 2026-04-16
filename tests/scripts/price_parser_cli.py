# scripts/price_parser_cli.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.price_parser import get_price, get_price_requests, get_price_selenium

def main():
    print("🔄 Проверяем цену...")
    price = get_price()
    if price is None:
        print("❌ Не удалось получить цену ни через requests, ни через Selenium")
        return
    print(f"Текущая цена: {price}")
    # остальная логика сравнения с кэшем 

if __name__ == "__main__":
    main()