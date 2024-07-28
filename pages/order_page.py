import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.profile_page_locators import ProfilePageLocators


class OrderPage(BasePage):
    @allure.step('Нажимаем на заказ в листе заказов')
    def click_order(self):
        self.click_element(OrderPageLocators.ORDER)

    @allure.step('Поиск элемента по номеру заказа')
    def search_element_by_order_number(self, num_order):
        str_num_order = OrderPageLocators.ORDERS_LIST
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.find_element(str_num_order)

    @allure.step('Собираем количество заказов за все время')
    def get_all_time_counter(self):
        return self.get_text(OrderPageLocators.ALL_TIME_COUNT)

    @allure.step('Собираем количество заказов за сегодня')
    def get_today_counter(self):
        return self.get_text(OrderPageLocators.TODAY_COUNT)

    @allure.step('Собираем номер заказа в работе')
    def get_in_work_order_number(self):
        return self.get_text(OrderPageLocators.ORDERS_IN_WORK)

    @allure.step('Собираем текст с окна состава')
    def get_text_from_consist(self):
        return self.get_text(OrderPageLocators.CONSIST)

    @allure.step('Собираем текст с номера заказа')
    def get_text_from_order_number(self):
        return self.get_text(ProfilePageLocators.ORDER_NUM)
