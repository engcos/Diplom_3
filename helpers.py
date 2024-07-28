import random
import allure
import string
import requests
import data
from data import Url


@allure.step('Создаем случайную строку')
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step('Создаем случайный email')
def generate_random_email():
    return f'{generate_random_string()}@gmail.com'


@allure.step('Регистрируем нового пользователя и возвращаем данные')
def register_new_user_and_return_user_data():
    user_data = {}
    email = generate_random_email()
    password = generate_random_string()
    name = generate_random_string()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(Url.API_CREATE_USER, data=payload)

    if response.status_code == 200:
        user_data = {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': response.json()
        }

    return user_data


@allure.step('Удаляем пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.API_DELETE_USER, headers=headers)


@allure.step('Создаем заказ')
def create_order(user):
    payload = {
        'ingredients': [data.TestData.INGREDIENTS]
    }
    headers = {'Authorization': user['json']['accessToken']}
    response = requests.post(Url.API_ORDERS, data=payload, headers=headers)
    return response
