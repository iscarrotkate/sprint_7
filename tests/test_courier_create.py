import allure
import pytest

from endpoints.api_responses import non_unique_courier_error, successful_operation_message, \
    missing_required_registration_fields
from endpoints.base_steps import send_request_with_request_json, verify_status_code, verify_json_text_is_valid
from helpers.data import users_list_required_registration_attributes_empty, existing_user, \
    users_list_registration_invalid_json
from endpoints.endpoints import create_courier


class TestCreateCourier:

    @allure.title('Создание пользователя с уникальными данными')
    @allure.description('Тест проверяет статус код и текст ответа при создании курьера с валидными данными')
    def test_create_unique_courier(self, registration_data):
        response = send_request_with_request_json(create_courier, registration_data)

        verify_status_code(response, 201)
        verify_json_text_is_valid(response, successful_operation_message)

    @allure.title('Попытка создания пользователя с неуникальными данными')
    @allure.description('Тест проверяет статус код и текст ответа при попытке создания неуникального пользователя')
    def test_attempt_to_create_non_unique_courier(self):
        payload = {'login': existing_user['login'], 'password': existing_user['password']}
        response = send_request_with_request_json(create_courier, payload)

        verify_status_code(response, 409)
        verify_json_text_is_valid(response, non_unique_courier_error)

    @allure.title('Попытка создания пользователя с пустыми обязательными полями')
    @allure.description(
        'Тест проверяет статус код и текст ответа при попытке создания пользователя с пустыми обязательными полями')
    @pytest.mark.parametrize('user_data', users_list_required_registration_attributes_empty)
    def test_attempt_to_create_courier_with_empty_required_fields(self, user_data):
        response = send_request_with_request_json(create_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, missing_required_registration_fields)

    @allure.title('Попытка создания пользователя с отсутствующими обязательными полями')
    @allure.description(
        'Тест проверяет статус код и текст ответа при попытке создания пользователя с отсутствующими обязательными полями в JSON')
    @pytest.mark.parametrize('user_data', users_list_registration_invalid_json)
    def test_attempt_to_create_courier_with_missing_required_fields(self, user_data):
        response = send_request_with_request_json(create_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, missing_required_registration_fields)
