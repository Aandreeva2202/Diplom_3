import allure

from helpers import generate_email
from urls import URL_FORGOT_PASSWORD_PAGE, URL_RESET_PASSWORD_PAGE


@allure.title('Тесты на проверку восстановления пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_forgot_password_link_opens_forgot_password_page(self, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_to_forgot_password_link()
        forgot_password_page.wait_for_forgot_password_page()
        assert forgot_password_page.get_current_url() == URL_FORGOT_PASSWORD_PAGE

    @allure.title('Ввод почты и клик по кнопке «Восстановить» открывает страницу сброса пароля')
    def test_recover_button_opens_reset_password_page(self, forgot_password_page, reset_password_page):
        forgot_password_page.recover_password(generate_email())
        reset_password_page.wait_for_reset_password_page()
        assert reset_password_page.get_current_url() == URL_RESET_PASSWORD_PAGE and reset_password_page.is_save_button_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_show_password_button_makes_field_active(self, forgot_password_page, reset_password_page):
        forgot_password_page.recover_password(generate_email())
        reset_password_page.wait_for_reset_password_page()
        reset_password_page.click_to_show_password_button()
        assert reset_password_page.is_password_field_active()
