import allure


@allure.title('Тесты на проверку ленты заказов')
class TestOrderFeed:

    @allure.title('Клик на заказ открывает окно с деталями')
    def test_click_order_opens_details_modal(self, order_feed_page):
        order_feed_page.open_order_feed_page()
        order_feed_page.click_to_first_order()
        assert order_feed_page.is_order_modal_displayed()

    @allure.title('Заказы пользователя из «Истории заказов» отображаются в «Ленте заказов»')
    def test_user_order_from_history_displayed_in_feed(self, authorized_user, main_page, account_page,
                                                       order_feed_page):
        number = main_page.place_order_with_bun('Краторная булка N-200i')
        main_page.click_to_personal_account()
        account_page.wait_for_profile_page()
        account_page.click_to_order_history()
        account_page.wait_for_order_history_page()
        order_in_history = account_page.is_order_in_history(number)
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        assert order_in_history and order_feed_page.is_order_in_feed(number)

    @allure.title('При создании заказа счётчик «Выполнено за все время» увеличивается')
    def test_new_order_increases_done_all_time_counter(self, authorized_user, main_page, order_feed_page):
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        counter_before = order_feed_page.get_done_all_time_counter()
        main_page.click_to_constructor()
        main_page.wait_for_constructor_page()
        main_page.place_order_with_bun('Краторная булка N-200i')
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        assert order_feed_page.wait_for_done_all_time_counter_increased(counter_before) > counter_before

    @allure.title('При создании заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_new_order_increases_done_today_counter(self, authorized_user, main_page, order_feed_page):
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        counter_before = order_feed_page.get_done_today_counter()
        main_page.click_to_constructor()
        main_page.wait_for_constructor_page()
        main_page.place_order_with_bun('Краторная булка N-200i')
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        assert order_feed_page.wait_for_done_today_counter_increased(counter_before) > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_new_order_number_displayed_in_progress(self, authorized_user, main_page, order_feed_page):
        number = main_page.place_order_with_bun('Краторная булка N-200i')
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        assert order_feed_page.is_order_in_progress(number)
