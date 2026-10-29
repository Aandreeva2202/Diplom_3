import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import URL_FORGOT_PASSWORD_PAGE


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        self.go_to_url(URL_FORGOT_PASSWORD_PAGE)
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Ждём открытия страницы восстановления пароля')
    def wait_for_forgot_password_page(self):
        self.wait_for_url(URL_FORGOT_PASSWORD_PAGE)
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Вводим email')
    def set_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик на кнопку «Восстановить»')
    def click_to_recover_button(self):
        self.click_to_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Запрашиваем восстановление пароля')
    def recover_password(self, email):
        self.open_forgot_password_page()
        self.set_email(email)
        self.click_to_recover_button()
