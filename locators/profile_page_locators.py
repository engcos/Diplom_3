from selenium.webdriver.common.by import By


class ProfilePageLocators:
    EMAIL_ENTER = By.XPATH, '//input[@name="name"]'
    PASSWORD_ENTER = By.XPATH, '//input[@name="Пароль"]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти")]'
    ORDER_HISTORY_BUTTON = By.XPATH, '//a[contains(text(),"История заказов")]'
    LOGOUT_BUTTON = By.XPATH, '//button[contains(text(),"Выход")]'
    ORDER_NUM = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
