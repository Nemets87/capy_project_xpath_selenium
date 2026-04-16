import allure
import pytest
from utils.price_parser import get_price

@allure.feature("Мониторинг цен")
@allure.story("PS5 Slim")
class TestPriceRange:

    @allure.title("Цена товара положительна (товар в наличии)")
    def test_ps5_price_positive(self):
        with allure.step("Получить текущую цену (requests или Selenium)"):
            price = get_price()
            assert price is not None, "Не удалось получить цену (товар возможно снят с продажи)"

        allure.attach(str(price), name="Текущая цена", attachment_type=allure.attachment_type.TEXT)

        # Тест падает ТОЛЬКО если цена <= 0
        assert price > 0, f"Цена {price} руб. не может быть <= 0. Товар пропал!"

        # Диапазон – просто информационное сообщение, не влияет на результат теста
        if price < 40000:
            message = f"Цена {price} руб. ниже 40000. Возможно, курс доллара упал или акция."
        elif price > 60000:
            message = f"Цена {price} руб. выше 60000. Возможно, подорожали чипы или экстренные меры Sony."
        else:
            message = f"Цена {price} руб. в норме (40000–60000). Рынок стабилен."

        allure.attach(message, name="Информация о рыночной ситуации", attachment_type=allure.attachment_type.TEXT)
        print(message)