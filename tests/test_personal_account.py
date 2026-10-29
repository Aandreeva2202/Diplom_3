import allure

from urls import URL_LOGIN_PAGE, URL_ORDER_HISTORY_PAGE, URL_PROFILE_PAGE


@allure.title('Тесты на проверку личного кабинета')
class TestPersonalAccount:

    @allure.title('Переход в личный кабинет по клику на «Личный Кабинет»')
    def test_personal_account_link_opens_profile(self, authorized_user, main_page, account_page):
        main_page.click_to_personal_account()
        account_page.wait_for_profile_page()
        assert account_page.get_current_url() == URL_PROFILE_PAGE and account_page.is_profile_link_displayed()

    @allure.title('Переход в раздел «История заказов»')
    def test_order_history_link_opens_order_history(self, authorized_user, main_page, account_page):
        main_page.click_to_personal_account()
        account_page.wait_for_profile_page()
        account_page.click_to_order_history()
        account_page.wait_for_order_history_page()
        assert account_page.get_current_url() == URL_ORDER_HISTORY_PAGE

    @allure.title('Выход из аккаунта')
    def test_logout_opens_login_page(self, authorized_user, main_page, account_page, login_page):
        main_page.click_to_personal_account()
        account_page.wait_for_profile_page()
        account_page.click_to_logout()
        login_page.wait_for_login_page()
        assert login_page.get_current_url() == URL_LOGIN_PAGE
