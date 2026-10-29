import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from urls import URL_FEED_PAGE


class OrderFeedPage(BasePage):

    @allure.step('Открываем ленту заказов')
    def open_order_feed_page(self):
        self.go_to_url(URL_FEED_PAGE)
        self.find_element_with_wait(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step('Ждём открытия ленты заказов')
    def wait_for_order_feed_page(self):
        self.wait_for_url(URL_FEED_PAGE)
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_LINK_ACTIVE)
        self.find_element_with_wait(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step('Клик на первый заказ в ленте')
    def click_to_first_order(self):
        self.click_to_element(OrderFeedPageLocators.FIRST_ORDER)
        self.wait_for_url(f'{URL_FEED_PAGE}/')

    @allure.step('Проверяем, что открыто окно с деталями заказа')
    def is_order_modal_displayed(self):
        return self.is_element_displayed(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step('Проверяем, что заказ {number} есть в ленте')
    def is_order_in_feed(self, number):
        return self.is_element_displayed(self.format_locators(OrderFeedPageLocators.ORDER_BY_NUMBER, number))

    @allure.step('Получаем счётчик «Выполнено за все время»')
    def get_done_all_time_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.DONE_ALL_TIME_COUNTER))

    @allure.step('Получаем счётчик «Выполнено за сегодня»')
    def get_done_today_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.DONE_TODAY_COUNTER))

    @allure.step('Ждём увеличения счётчика «Выполнено за все время»')
    def wait_for_done_all_time_counter_increased(self, counter_before):
        locator = self.format_locators(OrderFeedPageLocators.DONE_ALL_TIME_COUNTER_GREATER, counter_before)
        return int(self.get_text_from_element(locator))

    @allure.step('Ждём увеличения счётчика «Выполнено за сегодня»')
    def wait_for_done_today_counter_increased(self, counter_before):
        locator = self.format_locators(OrderFeedPageLocators.DONE_TODAY_COUNTER_GREATER, counter_before)
        return int(self.get_text_from_element(locator))

    @allure.step('Проверяем, что заказ {number} есть в разделе «В работе»')
    def is_order_in_progress(self, number):
        return self.is_element_displayed(self.format_locators(OrderFeedPageLocators.IN_PROGRESS_ORDER, number))
