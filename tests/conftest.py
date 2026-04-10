import pytest
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from allure_commons.types import AttachmentType
import os

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    # В GitHub Actions geckodriver уже в PATH, можно просто вызвать webdriver.Firefox()
    # Для локальной разработки можно использовать webdriver-manager, но чтобы не было rate limit,
    # лучше один раз установить geckodriver вручную и прописать путь.
    
    # Пытаемся найти geckodriver в стандартных местах
    geckodriver_path = None
    if os.path.exists("/usr/local/bin/geckodriver"):  # GitHub Actions
        geckodriver_path = "/usr/local/bin/geckodriver"
    elif os.path.exists("/usr/bin/geckodriver"):
        geckodriver_path = "/usr/bin/geckodriver"
    else:
        # Если не нашли, пробуем через webdriver-manager (но может быть rate limit)
        try:
            from webdriver_manager.firefox import GeckoDriverManager
            geckodriver_path = GeckoDriverManager().install()
        except:
            pass
    
    if geckodriver_path:
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service)
    else:
        # Надеемся, что geckodriver просто в PATH
        driver = webdriver.Firefox()
    
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot_on_failure",
                          attachment_type=AttachmentType.PNG)