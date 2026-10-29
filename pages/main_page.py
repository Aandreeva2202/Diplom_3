import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import URL_CONSTRUCTOR_PAGE


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.go_to_url(URL_CONSTRUCTOR_PAGE)
        self.find_element_with_wait(MainPageLocators.BURGER_HEADER)

    @allure.step('Ждём открытия конструктора')
    def wait_for_constructor_page(self):
        self.find_element_with_wait(MainPageLocators.BURGER_HEADER)

    @allure.step('Ждём загрузки главной страницы авторизованного пользователя')
    def wait_for_authorized_main_page(self):
        self.find_element_with_wait(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Клик на «Конструктор»')
    def click_to_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Клик на «Лента Заказов»')
    def click_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Клик на «Личный Кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Клик на ингредиент «{name}»')
    def click_to_ingredient(self, name):
        self.click_to_element(self.format_locators(MainPageLocators.INGREDIENT, name))

    @allure.step('Проверяем, что открыто окно с деталями ингредиента')
    def is_ingredient_modal_displayed(self):
        return self.is_element_displayed(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Получаем название ингредиента в окне с деталями')
    def get_ingredient_modal_name(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_MODAL_NAME)

    @allure.step('Закрываем окно с деталями ингредиента крестиком')
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    def is_ingredient_modal_closed(self):
        return not self.driver.find_elements(*MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Получаем счётчик ингредиента «{name}»')
    def get_ingredient_counter(self, name):
        return int(self.get_text_from_element(self.format_locators(MainPageLocators.INGREDIENT_COUNTER, name)))

    @allure.step('Перетаскиваем ингредиент «{name}» в конструктор')
    def add_ingredient_to_constructor(self, name):
        self.drag_and_drop_element(
            self.format_locators(MainPageLocators.INGREDIENT, name),
            MainPageLocators.CONSTRUCTOR_BASKET,
        )

    @allure.step('Клик на «Оформить заказ»')
    def click_to_place_order(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получаем номер созданного заказа')
    def get_order_number(self):
        self.find_element_with_wait(MainPageLocators.ORDER_MODAL_ID_TEXT)
        return self.get_text_from_element(MainPageLocators.ORDER_MODAL_NUMBER)

    @allure.step('Закрываем окно с номером заказа')
    def close_order_modal(self):
        self.click_to_element(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisible(MainPageLocators.ORDER_MODAL_ID_TEXT)

    @allure.step('Оформляем заказ из булки и получаем его номер')
    def place_order_with_bun(self, bun_name):
        self.add_ingredient_to_constructor(bun_name)
        self.click_to_place_order()
        number = self.get_order_number()
        self.close_order_modal()
        return number

    @allure.step('Проверяем, что заказ начали готовить')
    def is_order_status_displayed(self):
        return self.is_element_displayed(MainPageLocators.ORDER_MODAL_STATUS)
