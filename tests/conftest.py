import pytest

from endpoints.base_steps import send_request_with_request_json, send_request_by_address
from endpoints.endpoints import login_courier, delete_courier, create_courier
from helpers.helpers import generate_random_string, generate_string_based_on_timestamp


@pytest.fixture
def registration_data():
    login = f'{generate_random_string(10)}{generate_string_based_on_timestamp()}'
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    payload = {'login': login, 'password': password}

    login_response = send_request_with_request_json(login_courier, payload)

    if login_response.status_code == 200:
        user_id = login_response.json()['id']
        send_request_by_address(delete_courier, user_id)


@pytest.fixture
def registered_user_id():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    send_request_with_request_json(create_courier, payload)

    payload = {'login': login, 'password': password}

    login_response = send_request_with_request_json(login_courier, payload)
    user_id = login_response.json()['id']

    yield user_id

    delete_user_response = send_request_by_address(delete_courier, user_id)

    if delete_user_response.status_code != 200:
        print(f'Ошибка при удалении пользователя')
