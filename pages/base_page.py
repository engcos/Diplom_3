import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу в браузере')
    def open(self, url):
        return self.driver.get(url)

    @allure.step('Получаем текущий URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Ожидаем смены URL')
    def wait_url_change(self, url, time=15):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    @allure.step('Ожидаем исчезновения элемента')
    def wait_element_disappear(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element(locator))

    @allure.step('Находим элемент')
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    @allure.step('Проверяем наличие элемента')
    def presence_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    @allure.step('Получаем текст элемента')
    def get_text(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).text

    @allure.step('Кликаем по элементу')
    def click_element(self, locator, time=20):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Перемещаемся к элементу и кликаем')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ac(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Вводим данные в элемент')
    def send_input(self, locator, data, time=15):
        WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(data)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, element, target):
        return ac(self.driver).drag_and_drop(element, target).perform()