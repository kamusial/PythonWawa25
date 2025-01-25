from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
try:
    username_field = driver.find_element(By.ID, 'user-nameA')
except:
    print('Nie znaleziono pola')
    driver.get_screenshot_as_file('error_screen.png')
    driver.quit()
    raise

username_field.send_keys('standard_user')
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('secret_sauce')
sleep(2)
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)
driver.get_screenshot_as_file('screen1.png')
driver.quit()