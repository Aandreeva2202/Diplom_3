import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
from urls import URL_RESET_PASSWORD_PAGE


class ResetPasswordPage(BasePage):

    @allure.step('Ждём открытия страницы сброса пароля')
    def wait_for_reset_password_page(self):
        self.wait_for_url(URL_RESET_PASSWORD_PAGE)
        self.find_element_with_wait(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_to_show_password_button(self):
        self.click_to_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем, что кнопка «Сохранить» отображается')
    def is_save_button_displayed(self):
        return self.is_element_displayed(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Проверяем, что поле пароля активно')
    def is_password_field_active(self):
        return self.is_element_displayed(ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
