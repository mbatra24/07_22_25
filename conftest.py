import pytest

from function.function import app_launch, login, closedriver


@pytest.fixture
def setup():
    # below driver is a variable
    driver = app_launch("chrome")
    login(driver)
    yield driver
    closedriver(driver)
