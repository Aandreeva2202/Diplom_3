from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            # в Firefox клик перехватывает прозрачный оверлей модального окна
            self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        scroll_element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    # добавить текст на элемент
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # получение текста с элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, value):
        method, locator = locator_1
        locator = locator.format(value)
        return method, locator

    # перетаскивание элемента
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)
        self.driver.execute_script(
            """
            const [source, target] = arguments;
            const dataTransfer = new DataTransfer();
            const fire = (element, type) => element.dispatchEvent(
                new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer})
            );
            fire(source, 'dragstart');
            fire(target, 'dragenter');
            fire(target, 'dragover');
            fire(target, 'drop');
            fire(source, 'dragend');
            """,
            source, target,
        )

    def wait_for_element_invisible(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    # ожидание, пока текст элемента не станет отличаться от заданного
    def wait_for_text_changed(self, locator, old_text):
        self.wait.until(lambda driver: driver.find_element(*locator).text != old_text)
        return self.get_text_from_element(locator)

    # ожидание перехода на страницу
    def wait_for_url(self, url):
        self.wait.until(expected_conditions.url_contains(url))

    def get_current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()
