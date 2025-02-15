import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, moj_driver):
        self.driver = moj_driver


    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def print_page_info(self):
        print('Nazwa strony', self.driver.title)
        print('adres', self.driver.current_url)

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, 'user-name')
        field.clear()
        field.send_keys(username)

    def enter_password(self, passwd='secret_sauce'):
        field = self.driver.find_element(By.ID, 'password')
        field.clear()
        field.send_keys(passwd)
    def click_login(self):
        field = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        field.click()

    def make_screenshot(self):
        teraz = datetime.datetime.now()
        filename = teraz.strftime('screens\\screenshot_%H_%M_%S.png')
        self.driver.get_screenshot_as_file(filename)

    def close(self):
        self.driver.quit()