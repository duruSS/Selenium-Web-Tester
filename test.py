from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class Test:
    driver = webdriver.Chrome()
    def __init__(self, domain):
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(domain)
            print("[!] Chrome driver initiated...")
        except TimeoutException as te:
            print("Error:", te)

    def __del__(self):
        self.driver.quit()
        print("[!] Chrome driver stopped...")

    def test_login(self, email, password):
        time.sleep(2)
        try:
            email_input = self.driver.find_element(By.ID, "email_or_phone")
            email_input.click()
            email_input.clear()
            email_input.send_keys(email)
            print("[+] Test email entered.")
            time.sleep(1)
        except NoSuchElementException as nsee:
            print("Error:", nsee)

        try:
            password_input = self.driver.find_element(By.ID, "password")
            password_input.click()
            password_input.clear()
            password_input.send_keys(password)
            print("[+] Test password entered.")
            time.sleep(1)
        except NoSuchElementException as nsee:
            print("Error:", nsee)

        try:
            self.driver.find_element(By.ID, "submit").click()
            print("[+] Test submission made.")
            time.sleep(1)
        except NoSuchElementException as nsee:
            print("Error:", nsee)