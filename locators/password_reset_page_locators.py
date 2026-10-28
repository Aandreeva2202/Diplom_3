from selenium.webdriver.common.by import By

class PasswordResetPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, "h2")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Введите новый пароль']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Подтвердите новый пароль']")
    SAVE_BTN = (By.CSS_SELECTOR, "button.button_button_type_primary_107Bx")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.input_error")
    FORM_CONTAINER = (By.CSS_SELECTOR, "form.Auth_form_3qKeq")
