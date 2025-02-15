from pom import LoginPage
from time import sleep
from selenium import webdriver

def test_login_page_standard_user():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username('standard_user')
    page.enter_password()
    page.click_login()
    sleep(3)
    try:
        assert page.current_url() == 'https://www.saucedemo.com/inventory.html'
    except AssertionError:
        page.make_screenshot()
        print('Asercja nie przeszła\nstrona się nie zgadza')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print(f'Jesteś na stronie {page.current_url()}')
        print('Czyszcze dane')
        print('Zamykam stronę')
        page.close()

def test_login_page_locked_out_user():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username('locked_out_user')
    page.enter_password()
    page.click_login()
    sleep(3)
    try:
        assert page.current_url() == 'https://www.saucedemo.com/'
    except AssertionError:
        page.make_screenshot()
        print('Asercja nie przeszła\nstrona się nie zgadza')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print(f'Jesteś na stronie {page.current_url()}')
        print('Czyszcze dane')
        print('Zamykam stronę')
        page.close()