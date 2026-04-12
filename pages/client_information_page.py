from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

fake = Faker('ru_RU')


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

    # Действия
    def input_name(self, name_text):
        self.send_keys(self.name, name_text)

    def input_email(self, email_text):
        self.send_keys(self.email, email_text)

    def input_phone(self, phone_text):
        self.send_keys(self.phone, phone_text)

    def click_check_approval(self):
        self.click(self.check_approval)
        print("✅ Согласие на обработку данных")

    def click_check_save(self):
        self.click(self.check_save)
        print("✅ Данные сохранены")

    def click_check_order(self):
        self.click(self.check_order)
        print("✅ Заказ оформлен")

    # Получение финальной цены
    def get_need_number_value(self) -> float:
        element = self.find_element(self.need_number)
        return self.clean_price_element(element)

    # Основной метод заполнения
    def input_information(self):
        self.get_current_url()
        random_name = fake.first_name()
        random_email = fake.email()
        random_phone = fake.msisdn()[:11]

        self.input_name(random_name)
        self.input_email(random_email)
        self.input_phone(random_phone)
        self.click_check_approval()
        self.click_check_save()
        self.click_check_order()

    def input_invalid_information(self):
        self.get_current_url()
        self.input_name("12345")
        self.input_email("test_mail.ru")
        self.input_phone("abcdefg")
        self.click_check_approval()
        self.click_check_save()
        self.click_check_order()