from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_LINK = By.XPATH, ".//a[text()='Профиль']"
    ORDER_HISTORY_LINK = By.XPATH, ".//a[text()='История заказов']"
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ORDER_BY_NUMBER = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem') and contains(., '{}')]"
