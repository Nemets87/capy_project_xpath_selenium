import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from allure_commons.types import AttachmentType

@pytest.fixture(scope="function")
def driver():
    browser = os.environ.get('BROWSER', 'firefox').lower()  # по умолчанию Firefox
    
    if browser == 'chrome':
        options = ChromeOptions()
        if os.environ.get('CI'):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(options=options)
    else:  # firefox
        options = FirefoxOptions()
        if os.environ.get('CI'):
            # Для Firefox в CI нужны дополнительные настройки
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.download.dir", "/tmp")
            options.set_preference("pdfjs.disabled", True)
            options.set_preference("media.volume_scale", "0.0")
            options.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(options=options)
    
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