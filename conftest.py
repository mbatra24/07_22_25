import pytest


from functions.function import FunctionLibrary


@pytest.fixture
def setup():
    # below driver is a variable
    fl = FunctionLibrary()
    driver = fl.app_launch("chrome")
    fl.login(driver)
    yield driver
    fl.closedriver(driver)
