from functions.function import FunctionLibrary
from pages.homepage import HomePage


class TestHomepage:
    # def test_loginpage(setup):
    #     driver = setup
    #     # driver.save_screenshot("Reports/inventory.png")
    #     # login(driver)


    def test_homepage(self,setup):
        self.driver = setup
        hp = HomePage(self.driver)
        hp.homepage()
        # driver.save_screenshot("Reports/inventory.png")
        # login(driver)

