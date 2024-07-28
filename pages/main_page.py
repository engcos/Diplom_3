from telnetlib import EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    ADD_TO_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".counter")

    @allure.step("Добавляем ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ADD_TO_CONSTRUCTOR_BUTTON)
        ).click()

    @allure.step("Получаем текст из счетчика ингредиентов")
    def get_text_from_ingredient_counter(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.INGREDIENT_COUNTER)
        ).text

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на кнопку "Лента Заказов"')
    def click_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient_button(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT)

    @allure.step('Нажимаем на кнопку закрытия')
    def click_close_popup_window_button(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Проверяем наличие элемента на экране')
    def check_ingredients_details_on_screen(self):
        return self.presence_element(MainPageLocators.INGREDIENT_DETAILS).is_displayed()

    @allure.step('Дождаемся исчезновения деталей заказа')
    def wait_for_order_details_disappear(self):
        self.wait_element_disappear(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Нажимаем на кнопку "Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавляем ингридиент в констуктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.find_element(MainPageLocators.INGREDIENT),
                           self.find_element(MainPageLocators.BURGER_CONSTRUCTOR))

    @allure.step('Ищем номер заказа во всплывающем окне')
    def find_order_number(self):
        self.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Собираем текст с кнопки логин')
    def get_text_from_login_button(self):
        return self.get_text(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Собираем текст с листа заказов')
    def get_text_from_order_list(self):
        return self.get_text(OrderPageLocators.ORDER_LIST_TEXT)

    @allure.step('Собираем текст с окна ингредиентов')
    def get_text_from_ingredients_details(self):
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Собираем текст со счетчика ингредиентов')
    def get_text_from_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Собираем текст с заказа')
    def get_text_from_order(self):
        return self.get_text(MainPageLocators.ORDER_TEXT)
