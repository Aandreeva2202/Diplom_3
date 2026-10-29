import allure
import pytest
import requests
from selenium import webdriver

from helpers import generate_user_data
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.reset_password_page import ResetPasswordPage
from urls import URL_API_REGISTER, URL_API_USER


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture(scope="function")
def reset_password_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture(scope="function")
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture(scope="function")
def user():
    user_data = generate_user_data()
    with allure.step('Создаём пользователя через API'):
        response = requests.post(URL_API_REGISTER, json=user_data, timeout=10)
        response.raise_for_status()
        access_token = response.json()['accessToken']
    yield user_data
    with allure.step('Удаляем пользователя через API'):
        requests.delete(URL_API_USER, headers={'Authorization': access_token}, timeout=10)


@pytest.fixture(scope="function")
def authorized_user(user, login_page, main_page):
    login_page.login(user['email'], user['password'])
    main_page.wait_for_authorized_main_page()
    return user
