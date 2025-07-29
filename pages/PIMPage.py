import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from variables.variable import pim_firstname, pim_lastname


def pim_add_employee(driver):
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    # wait = WebDriverWait(driver, 3)
    print(driver.current_url)
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "firstName").send_keys(pim_firstname)
    driver.find_element(By.NAME, "lastName").send_keys(pim_lastname)
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    print(driver.current_url)
    time.sleep(5)

def pim_search_employee(driver):
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(6)
    print(driver.current_url)
    driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys(pim_firstname)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    empname = driver.find_element(By.XPATH, "//div[contains(text(),'Gary A')]").text
    print(empname)
    # Scroll to the bottom
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshots/empname3.png")
    # driver.save_screenshot("screenshots/empname.png")
    assert empname == pim_firstname, "comparison failed"











