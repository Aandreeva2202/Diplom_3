from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = By.XPATH, ".//p[text()='Конструктор']/parent::a"
    ORDER_FEED_LINK = By.XPATH, ".//p[text()='Лента Заказов']/parent::a"
    PERSONAL_ACCOUNT_LINK = By.XPATH, ".//p[text()='Личный Кабинет']/parent::a"

    BURGER_HEADER = By.XPATH, ".//h1[text()='Соберите бургер']"
    INGREDIENT = By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{}']]"
    INGREDIENT_COUNTER = By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{}']]//p[contains(@class, 'counter_counter__num')]"
    CONSTRUCTOR_BASKET = By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"
    PLACE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"

    INGREDIENT_MODAL_TITLE = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']"
    INGREDIENT_MODAL_NAME = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[contains(@class, 'text_type_main-medium')]"
    MODAL_CLOSE_BUTTON = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"

    ORDER_MODAL_ID_TEXT = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"
    # до ответа сервера в окне стоит номер-заглушка 9999, ждём реальный номер
    ORDER_MODAL_NUMBER = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large') and text()!='9999']"
    ORDER_MODAL_STATUS = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='Ваш заказ начали готовить']"
    ORDER_MODAL_CLOSE_BUTTON = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened') and .//p[text()='идентификатор заказа']]//button[contains(@class, 'Modal_modal__close')]"
