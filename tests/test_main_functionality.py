import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from data import Url
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story('Тесты основного функционала')
class TestMainFunctionality:
    @allure.title('Тест переход по кнопке "Конструктор"')
    def test_transition_to_constructor(self, driver):
        page = MainPage(driver)
        page.open(Url.ORDER_PAGE)
        page.click_constructor_button()
        assert (page.get_url() == Url.BASE_PAGE and
                page.get_text_from_login_button() == 'Войти в аккаунт')

    @allure.title('Тест переход по кнопке "Лента Заказов"')
    def test_transition_to_order_list(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_order_list_button()
        assert (page.get_url() == Url.ORDER_PAGE and
                page.get_text_from_order_list() == 'Лента заказов')

    @allure.title('Тест всплывающего окна ингредиента')
    def test_ingredient_popup(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_ingredient_button()
        assert page.get_text_from_ingredients_details() == 'Детали ингредиента'

    @allure.title('Тест кнопки закрытия всплывающего окна')
    def test_ingredient_popup_close_button(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_ingredient_button()
        page.click_close_popup_window_button()
        page.wait_for_order_details_disappear()
        assert not page.check_ingredients_details_on_screen()

    @allure.title('Тест счетчика ингредиентов')
    def test_ingredient_counter(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        initial_count = int(page.get_text_from_ingredient_counter())
        page.add_ingredient_to_constructor()
        try:
            WebDriverWait(driver, 15).until(
                lambda d: int(page.get_text_from_ingredient_counter()) > initial_count
            )
        except TimeoutException as e:
            page.driver.save_screenshot("ingredient_counter_timeout.png")
            raise e

        new_count = int(page.get_text_from_ingredient_counter())
        assert new_count > initial_count, f"Expected counter to be greater than {initial_count}, but got {new_count}"

    @allure.title('Тест оформления заказа авторизованным пользователем')
    def test_successful_order(self, driver, user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open(Url.LOGIN_PAGE)
        profile_page.login(user)
        main_page.wait_url_change(Url.BASE_PAGE)
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.find_order_number()
        assert main_page.get_text_from_order() == 'идентификатор заказа'
