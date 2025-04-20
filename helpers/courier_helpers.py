import allure

from endpoints.base_steps import send_request_with_request_json
from endpoints.endpoints import create_courier, login_courier
from helpers.helpers import generate_random_string, generate_string_based_on_timestamp


@allure.step('Создать пользователя')
def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = send_request_with_request_json(create_courier, payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@allure.step('Авторизоваться как существующий пользователь')
def login_as_exiting_user_and_get_id(credentials):
    payload = {
        "login": credentials[0],
        "password": credentials[1]
    }

    response = send_request_with_request_json(login_courier, payload)

    return response.json()["id"]

@allure.step('Сгенерировать JSON с уникальными регистрационными данными')
def generate_unique_user_data_json():

    login = f'{generate_random_string(10)}{generate_string_based_on_timestamp()}'
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }
