import allure
import pytest

from urls import URL_CONSTRUCTOR_PAGE, URL_FEED_PAGE


@allure.title('Тесты на проверку основного функционала')
class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_constructor_link_opens_constructor(self, main_page, order_feed_page):
        main_page.open_main_page()
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        main_page.click_to_constructor()
        main_page.wait_for_constructor_page()
        assert main_page.get_current_url() == URL_CONSTRUCTOR_PAGE

    @allure.title('Переход по клику на «Лента Заказов»')
    def test_order_feed_link_opens_order_feed(self, main_page, order_feed_page):
        main_page.open_main_page()
        main_page.click_to_order_feed()
        order_feed_page.wait_for_order_feed_page()
        assert order_feed_page.get_current_url() == URL_FEED_PAGE

    @allure.title('Клик на ингредиент открывает окно с деталями')
    def test_click_ingredient_opens_details_modal(self, main_page):
        main_page.open_main_page()
        main_page.click_to_ingredient('Соус фирменный Space Sauce')
        assert main_page.is_ingredient_modal_displayed() and main_page.get_ingredient_modal_name() == 'Соус фирменный Space Sauce'

    @allure.title('Окно с деталями ингредиента закрывается кликом по крестику')
    def test_close_button_closes_details_modal(self, main_page):
        main_page.open_main_page()
        main_page.click_to_ingredient('Соус фирменный Space Sauce')
        main_page.is_ingredient_modal_displayed()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title('Добавление ингредиента в заказ увеличивает его счётчик')
    @pytest.mark.parametrize(
        'name, expected_increase',
        [
            ('Краторная булка N-200i', 2),
            ('Флюоресцентная булка R2-D3', 2),
            ('Соус фирменный Space Sauce', 1),
            ('Соус традиционный галактический', 1),
        ]
    )
    def test_add_ingredient_increases_counter(self, main_page, name, expected_increase):
        main_page.open_main_page()
        counter_before = main_page.get_ingredient_counter(name)
        main_page.add_ingredient_to_constructor(name)
        assert main_page.get_ingredient_counter(name) == counter_before + expected_increase

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, authorized_user, main_page):
        main_page.add_ingredient_to_constructor('Краторная булка N-200i')
        main_page.add_ingredient_to_constructor('Соус фирменный Space Sauce')
        main_page.click_to_place_order()
        assert main_page.get_order_number().isdigit() and main_page.is_order_status_displayed()
