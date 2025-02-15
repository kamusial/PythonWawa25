from selenium import webdriver

class LoginPage:

    def open(self, url, browser):
        if browser == 'Firefox' or browser == 'FF':
            driver = webdriver.Firefox()

            driver.get(url)

