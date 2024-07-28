import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class ProfilePage(BasePage):
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_pa_button(self):
        self.move_to_element_and_click(MainPageLocators.PA_BUTTON)

    @allure.step('Логин на ACCOUNT')
    def login(self, data):
        self.send_input(ProfilePageLocators.EMAIL_ENTER, data['email'])
        self.send_input(ProfilePageLocators.PASSWORD_ENTER, data['password'])
        self.move_to_element_and_click(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_order_history_button(self):
        self.move_to_element_and_click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_logout_button(self):
        self.move_to_element_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Собираем текст с кнопки "Восстановить пароль"')
    def get_text_password_recovery_button(self):
        return self.get_text(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Собираем текст с кнопки "Войти"')
    def get_text_login_button(self):
        return self.get_text(ProfilePageLocators.LOGIN_BUTTON)
