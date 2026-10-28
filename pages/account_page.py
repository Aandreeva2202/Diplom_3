import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from urls import URL_ORDER_HISTORY_PAGE, URL_PROFILE_PAGE


class AccountPage(BasePage):

    @allure.step('Ждём открытия профиля в личном кабинете')
    def wait_for_profile_page(self):
        self.wait_for_url(URL_PROFILE_PAGE)
        self.find_element_with_wait(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Ждём открытия истории заказов')
    def wait_for_order_history_page(self):
        self.wait_for_url(URL_ORDER_HISTORY_PAGE)

    @allure.step('Клик на «История заказов»')
    def click_to_order_history(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step('Клик на «Выход»')
    def click_to_logout(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверяем, что заказ {number} есть в истории заказов')
    def is_order_in_history(self, number):
        return self.is_element_displayed(self.format_locators(AccountPageLocators.ORDER_BY_NUMBER, number))

    @allure.step('Проверяем, что ссылка «Профиль» отображается')
    def is_profile_link_displayed(self):
        return self.is_element_displayed(AccountPageLocators.PROFILE_LINK)
