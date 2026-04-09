from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

fake = Faker('ru_RU') # Русскоязычные даннные


class ClientInformationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    name = (By.XPATH, "//input[@id='name']")
    email = (By.XPATH, "//input[@id='email']")
    phone = (By.XPATH, "//input[@id='phone']")
    check_approval = (By.XPATH, "//div[@class='checkbox-element dynamic-field-checkbox']")
    check_save = (By.XPATH, "//button[@id='js-save-form']")
    check_order = (By.XPATH, "//button[@id='js-order-stage']")
    need_number = (By.XPATH, "//span[@class='js-cart__total']")

    # Геттеры
    def get_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.name))

    def get_email(self):
        return self.wait.until(EC.element_to_be_clickable(self.email))

    def get_phone(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone))

    def get_check_approval(self):
        return self.wait.until(EC.element_to_be_clickable(self.check_approval))

    def get_check_save(self):
        return self.wait.until(EC.element_to_be_clickable(self.check_save))

    def get_check_order(self):
        return self.wait.until(EC.element_to_be_clickable(self.check_order))

    def get_need_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.need_number))

    # Действия
    def input_name(self, name_text):
        self.get_name().send_keys(name_text)

    def input_email(self, email_text):
        self.get_email().send_keys(email_text)

    def input_phone(self, phone_text):
        self.get_phone().send_keys(phone_text)

    def click_check_approval(self):
        self.get_check_approval().click()
        print("✅ Согласие на обработку данных")

    def click_check_save(self):
        self.get_check_save().click()
        print("✅ Данные сохранены")

    def click_check_order(self):
        self.get_check_order().click()
        print("✅ Заказ оформлен")

    # Получение финальной цены
    def get_need_number_value(self) -> float:
        element = self.get_need_number()
        return self.clean_price_element(element) # возвращает значение

    # Основной метод заполнения
    def input_information(self):
        self.get_current_url()
        # Генерируем случайные имя, email, телефон
        random_name = fake.first_name()
        random_email = fake.email()
        random_phone = fake.msisdn()[:11]   # генерируем номер из 11 цифр == маска (если сайт проверяет формат телефона)

        self.input_name(random_name)
        self.input_email(random_email)
        self.input_phone(random_phone)
        self.click_check_approval()
        self.click_check_save()
        self.click_check_order()

    def input_invalid_information(self):
        """Заполняет поля заведомо неверными данными"""
        self.get_current_url()
        # Имя – цифры
        self.input_name("12345")
        # Email – без @
        self.input_email("test_mail.ru")
        # Телефон – буквы
        self.input_phone("abcdefg")
        self.click_check_approval()
        self.click_check_save()
        self.click_check_order()