from function.function import login
from pages.homepage import HomePage


class TestLogin:

    # def test_loginpage(setup):
    #     driver = setup
    #     # driver.save_screenshot("Reports/inventory.png")
    #     # login(driver)


    def test_login(self,setup):
        self.driver = setup
        hp = HomePage(self.driver)
        hp.homepage()
        # driver.save_screenshot("Reports/inventory.png")
        # login(driver)

