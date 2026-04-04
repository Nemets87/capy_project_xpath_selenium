import pytest


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