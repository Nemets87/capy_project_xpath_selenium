import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType


# @pytest.fixture(autouse=True)
# def log_test_name(request):
#     """Автоматически логирует начало и конец каждого теста"""
#     test_name = request.node.name
#     Logger.add_start_step(test_name)
#     yield
#     Logger.add_end_step(url="", method=test_name)  # URL можно получать из драйвера


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def set_up():
    """Фикстура для начала теста (совместимость со старыми тестами)"""
    print("\n✅ Start test setup")
    yield
    print("\n✅ Test teardown")


@pytest.fixture(scope="module")
def set_group():
    """Фикстура для группы тестов"""
    print("\n✅ Enter system")
    yield
    print("\n✅ Exit system")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для добавления скриншота при падении теста"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot_on_failure",
                          attachment_type=AttachmentType.PNG)