import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from variables import variable
from variables.variable import URL, usr, pwd


class FunctionLibrary:

    def app_launch(self,browser_type):
        if browser_type.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_type.lower() == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(URL)
        # navigation(driver, PAGE_URL)
        time.sleep(5)
        return self.driver

    def login(self, driver):
        # driver = app_launch()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usr)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        # wait = WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        # wait = WebDriverWait(driver, 3)
        print(driver.current_url)
        # return driver

    def closedriver(self,driver):
        driver.quit()

