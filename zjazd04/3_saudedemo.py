from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
username_field = driver.find_element(By.ID, 'user-name')

username_field.send_keys('standard_user')
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('secret_sauce')
sleep(2)
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)
driver.get_screenshot_as_file('screen1.png')