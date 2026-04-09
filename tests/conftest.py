import pytest
from utilites.logger import Logger


@pytest.fixture(autouse=True)
def log_test_name(request):
    """Автоматически логирует начало и конец каждого теста"""
    test_name = request.node.name
    Logger.add_start_step(test_name)
    yield
    Logger.add_end_step(url="", method=test_name)  # URL можно получать из драйвера


@pytest.fixture()
def set_up():
    print("✅Start X test")
    yield
    # driver.quit()
    print("✅X")
    print("✅Finish XXX test")


@pytest.fixture(scope="module")
def set_group():
    print("✅Enter the System")
    yield
    # driver.quit()
    print("✅Y")
    print("✅Exit the System")