import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from variables.variable import pim_firstname, admin_username, pim_lastname


class Adminpage:
    def __init__(self, driver):
        self.driver = driver

    def admin_page(self):
        WebDriverWait(self.driver, 5).until(element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
        # self.driver.find_element(By.LINK_TEXT, "Admin").click()
        print(self.driver.current_url)
        time.sleep(2)

    def add_user(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(2)
        print(self.driver.current_url)
        # selecting role
        ele = self.driver.find_element(By.XPATH, "(//div[@class= 'oxd-select-text-input'])[1]")
        ele.click()
        ele.send_keys(keys.Keys.ARROW_DOWN+keys.Keys.ARROW_DOWN+keys.Keys.ENTER)
        time.sleep(3)
        # entering emp name
        emp_name = self.driver.find_element(By.CSS_SELECTOR, "form input:nth-child(2)")
        emp_name.send_keys(pim_firstname + " " + pim_lastname)
        time.sleep(2)
        emp_name.send_keys(keys.Keys.ARROW_DOWN + keys.Keys.ENTER)
        time.sleep(2)
        # form = self.driver.find_element(By.TAG_NAME, "form")
        # form.send_keys(keys.Keys.TAB)
        # form.send_keys("Gary likes dicks")
        # time.sleep(10)

        # selecting status
        ele1 = self.driver.find_element(By.XPATH, "(//div[@class= 'oxd-select-text-input'])[2]")
        ele1.click()
        ele1.send_keys(keys.Keys.ARROW_DOWN+keys.Keys.ENTER)

        # entering usr
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(admin_username)
        time.sleep(3)
        self.driver.save_screenshot("screenshots/possibleerror.png")

        # entering pwd
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("1234gjedatt!")

        # entering pwd2
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("1234gjedatt!")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        print(self.driver.current_url)
        time.sleep(10)


    def search_user(self):
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--active:nth-child(1)").send_keys(admin_username)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(2)
        # search_item = self.driver.find_element(By.XPATH, "//span[normalize-space()='(1) Record Found']").text
        search_item = self.driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--span:nth-child(1)").text
        print(search_item)
        assert "(" in search_item, "record not found"


    def delete_user(self):
        time.sleep(3)
        # Find all data rows (skipping the header)
        rows = self.driver.find_elements(By.XPATH, "//div[@role='row' and not(contains(@class,'header'))]")

        # # Search for a specific name
        # target_name = "jtratest1234!"
        #
        # for row in rows:
        #     if target_name in row.text:
        #         print("✅ Found:", row.text)
        #         # Optional: click or extract other info from `row`
        #         break
        # else:
        #     print("❌ Name not found.")

        # Get all data rows (excluding header row)

        print("Usernames:")
        for row in rows:
            # Get all columns (cells) within the row
            cells = row.find_elements(By.CLASS_NAME, "oxd-table-cell")
            if len(cells) > 1:
                username = cells[1].text.strip()
                if username == admin_username:
                    cb = cells[0].find_element(By.CSS_SELECTOR,"i")
                    cb.click()
                    print(username)
                    time.sleep(10)
                    delb = cells[5].find_element(By.CSS_SELECTOR,"button")
                    delb.click()
                    time.sleep(5)
                    self.driver.find_element(By.CSS_SELECTOR, ".oxd-icon.bi-trash.oxd-button-icon").click()
                    time.sleep(5)
                    self.driver.save_screenshot("screenshots/userdeleted.png")
        # self.driver.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > div > div > label > span > i:nth-child(1)").click()
























