from pom import LoginPage
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
strona = LoginPage(driver)
strona.open()
strona.enter_username('Kamil')
strona.enter_password()
strona.print_page_info()
strona.click_login()
sleep(3)
