import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from variables import variable
from variables.variable import URL, usr, pwd


def app_launch(browser_type):
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)
    # navigation(driver, PAGE_URL)
    time.sleep(5)
    return driver

def login(driver):
    # driver = app_launch()
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usr)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print(driver.current_url)
    time.sleep(5)
    # return driver

def closedriver(driver):
    driver.quit()

