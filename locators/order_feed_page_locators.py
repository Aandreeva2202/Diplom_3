from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_LINK_ACTIVE = By.XPATH, ".//a[contains(@class, 'link_active') and .//p[text()='Лента Заказов']]"
    FIRST_ORDER = By.XPATH, "(.//a[contains(@class, 'OrderHistory_link')])[1]"
    ORDER_BY_NUMBER = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem') and contains(., '{}')]"
    ORDER_MODAL = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]"
    DONE_ALL_TIME_COUNTER = By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"
    DONE_TODAY_COUNTER = By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"
    # счётчик со значением больше заданного: пустой счётчик (данные ещё не пришли) не подходит
    DONE_ALL_TIME_COUNTER_GREATER = By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[number(text()) > {}]"
    DONE_TODAY_COUNTER_GREATER = By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[number(text()) > {}]"
    IN_PROGRESS_ORDER = By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(., '{}')]"
