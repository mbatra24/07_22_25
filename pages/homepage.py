import time



from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def homepage(self):
        time.sleep(2)
        # print(f"Page (homepage.py): {self.driver.current_url}")
        ele = self.driver.find_elements(By.TAG_NAME, "p")
        for e in ele:
            print(e.text)








