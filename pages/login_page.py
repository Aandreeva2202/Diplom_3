import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import URL_LOGIN_PAGE


class LoginPage(BasePage):

    @allure.step('Открываем страницу входа')
    def open_login_page(self):
        self.go_to_url(URL_LOGIN_PAGE)
        self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ждём открытия страницы входа')
    def wait_for_login_page(self):
        self.wait_for_url(URL_LOGIN_PAGE)
        self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Клик на ссылку «Восстановить пароль»')
    def click_to_forgot_password_link(self):
        self.click_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Авторизуемся пользователем')
    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)
