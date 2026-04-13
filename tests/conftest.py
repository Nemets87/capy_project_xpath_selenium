import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from allure_commons.types import AttachmentType

@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    # Определяем, запущены ли мы в CI (GitHub Actions)
    if os.environ.get('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        # Критические настройки для Firefox в headless-режиме
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.download.dir", "/tmp")
        options.set_preference("pdfjs.disabled", True)
        options.set_preference("media.volume_scale", "0.0")
        options.set_preference("dom.webnotifications.enabled", False)
        # Ускоряем загрузку
        options.set_preference("browser.startup.page", 0)
        options.set_preference("browser.offline", True)
    else:
        # Локально можно без headless, но для единообразия оставим как есть
        pass
    
    # Путь к geckodriver (в GitHub Actions он будет в /usr/local/bin)
    geckodriver_path = "/usr/local/bin/geckodriver" if os.environ.get('CI') else None
    if geckodriver_path and os.path.exists(geckodriver_path):
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
    else:
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