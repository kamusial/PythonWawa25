from selenium import webdriver
import time

okno1_chrome = webdriver.Chrome()
okno2_firefox = webdriver.Firefox()
okno1_chrome.get('https://www.google.com/')
okno2_firefox.get('https://allegro.pl')

time.sleep(2)

okno1_chrome.quit()
okno2_firefox.quit()
