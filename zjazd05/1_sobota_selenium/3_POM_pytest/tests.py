import pytest
from pom import LoginPage
from time import sleep
from selenium import webdriver

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('standard_user', 'XX', 'https://www.saucedemo.com/'),
    ('locked_out_user', 'XX', 'https://www.saucedemo.com/'),
    ('problem_user', 'XX', 'https://www.saucedemo.com/'),
    ('performance_glitch_user', 'XX', 'https://www.saucedemo.com/')
]
@pytest.mark.skip(reason='Bo tak')
@pytest.mark.parametrize('username, passwd, url', test_data)
def test_login_page_standard_user(username, passwd, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)
    page.enter_password(passwd)
    page.click_login()
    sleep(3)
    try:
        assert page.current_url() == url
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

@pytest.mark.skipif(len('piesek') == 5, reason='piesek jeszcze za mały')
def test1():
    assert 2 + 3 == 5

@pytest.mark.xfail(reason='nie nasz dział')
def test2():
    assert 2 + 3 == 5

import sys
if sys.platform.startswith('win'):
    @pytest.mark.skip('Linux-only tests')
    def test3():
        assert 2 + 3 == 5
