from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = By.XPATH, ".//input[@name='Введите новый пароль']/following-sibling::div[contains(@class, 'input__icon')]"
    PASSWORD_FIELD_ACTIVE = By.XPATH, ".//input[@name='Введите новый пароль']/parent::div[contains(@class, 'input_status_active')]"
    SAVE_BUTTON = By.XPATH, ".//button[text()='Сохранить']"
