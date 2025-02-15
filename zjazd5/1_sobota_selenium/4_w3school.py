from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(1)
driver.find_element(By.ID, 'accept-choices').click()

menu = driver.find_element(By.ID, 'navbtn_tutorials')
HTMLtutorial = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
HTML_forms_attributes.click()
tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
tryityourself.click()
time.sleep(1)



driver.quit()