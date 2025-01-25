from selenium import webdriver
from time import sleep

# import time
# time.sleep(3)

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
sleep(2)
driver.find_element('id','L2AGLb').click()
sleep(2)
# button_accept = driver.find_element('id','L2AGLb')
# button_accept.click()
search_field = driver.find_element('name', 'q')
search_field.send_keys('Kto gra na narodowym?')
sleep(2)
search_button = driver.find_element('name', 'btnK')
search_button.click()
sleep(2)
driver.quit()

