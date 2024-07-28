import allure
import helpers
from data import Url
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage


@allure.story('Тесты ленты заказов')
class TestOrderFeed:
    @allure.title('Тест всплывающего окна с деталями заказа')
    def test_order_details_popup(self, driver):
        order_page = OrderPage(driver)
        order_page.open(Url.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_page.click_order()
        assert order_page.get_text_from_consist() == 'Cостав'

    @allure.title('Тест наличия созданных заказов в истории заказов и в ленте заказов')
    def test_user_order_displayed_in_order_list(self, driver, user):
        order_page = OrderPage(driver)
        order_page.open(Url.LOGIN_PAGE)
        response = helpers.create_order(user)
        order_number = response.json()['order']['number']
        profile_page = ProfilePage(driver)
        profile_page.login(user)
        profile_page.wait_url_change(Url.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_page.search_element_by_order_number(order_number)
        profile_page.click_pa_button()
        profile_page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        profile_page.click_order_history_button()
        assert str(order_number) in order_page.get_text_from_order_number()

    @allure.title('Тест счетчика "Выполнено за все время"')
    def test_all_time_counter(self, driver, user):
        page = OrderPage(driver)
        page.open(Url.ORDER_PAGE)
        old_number = page.get_all_time_counter()
        helpers.create_order(user)
        assert int(page.get_all_time_counter()) >= int(old_number) + 1

    @allure.title('Тест счетчика "Выполнено за сегодня"')
    def test_today_counter(self, driver, user):
        page = OrderPage(driver)
        page.open(Url.ORDER_PAGE)
        old_number = page.get_today_counter()
        helpers.create_order(user)
        assert int(page.get_today_counter()) >= int(old_number) + 1

    @allure.title('Тест раздела "В работе"')
    def test_in_work_list(self, driver, user):
        page = OrderPage(driver)
        page.open(Url.ORDER_PAGE)
        response = helpers.create_order(user)
        order_number = response.json()['order']['number']
        assert str(order_number) >= page.get_in_work_order_number()
