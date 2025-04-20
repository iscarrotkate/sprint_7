import allure
import pytest

from endpoints.base_steps import send_request_with_request_json, verify_status_code, verify_json_text_is_valid
from helpers.courier_helpers import generate_unique_user_data_json
from helpers.data import users_list_required_registration_attributes_empty, existing_user, \
    users_list_registration_invalid_json
from endpoints.endpoints import create_courier


class TestCreateCourier:

    @allure.title('Создание пользователя с уникальными данными')
    @allure.description('Тест проверяет статус код и текст ответа при создании курьера с валидными данными')
    def test_create_unique_courier(self):
        response = send_request_with_request_json(create_courier, generate_unique_user_data_json())

        verify_status_code(response, 201)
        verify_json_text_is_valid(response, '{"ok":true}')

    @allure.title('Попытка создания пользователя с неуникальными данными')
    @allure.description('Тест проверяет статус код и текст ответа при попытке создания неуникального пользователя')
    def test_attempt_to_create_non_unique_courier(self):
        payload = {'login': existing_user['login'], 'password': existing_user['password']}
        response = send_request_with_request_json(create_courier, payload)

        verify_status_code(response, 409)
        verify_json_text_is_valid(response, '{"message": "Этот логин уже используется"}')

    @allure.title('Попытка создания пользователя с пустыми обязательными полями')
    @allure.description('Тест проверяет статус код и текст ответа при попытке создания пользователя с пустыми обязательными полями')
    @pytest.mark.parametrize('user_data', users_list_required_registration_attributes_empty)
    def test_attempt_to_create_courier_with_missing_required_fields(self, user_data):
        response = send_request_with_request_json(create_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, '{"message": "Недостаточно данных для создания учетной записи"}')

    @allure.title('Попытка создания пользователя с отсутствующими обязательными полями')
    @allure.description('Тест проверяет статус код и текст ответа при попытке создания пользователя с отсутствующими обязательными полями в JSON')
    @pytest.mark.parametrize('user_data', users_list_registration_invalid_json)
    def test_attempt_to_create_courier_with_missing_required_fields(self, user_data):
        response = send_request_with_request_json(create_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, '{"message": "Недостаточно данных для создания учетной записи"}')
