import allure
import pytest

from endpoints.api_responses import missing_required_login_fields, non_existing_account_error
from endpoints.base_steps import send_request_with_request_json, verify_status_code, verify_json_schema_is_valid, \
    verify_json_text_is_valid
from helpers.data import existing_user, users_list_required_login_attributes_empty, \
    users_list_credentials_missmatch
from endpoints.endpoints import login_courier
from endpoints.json_schemas import login_response_schema


class TestLoginCourier:

    @allure.title('Авторизация с валидными данными')
    @allure.description('Тест проверяет статус код и соответствие ответа json-схеме при авторизации курьера с валидными данными')
    def test_login_courier_with_valid_data(self):
        payload = {'login': existing_user['login'], 'password': existing_user['password']}

        response = send_request_with_request_json(login_courier, payload)

        verify_status_code(response, 200)
        verify_json_schema_is_valid(response, login_response_schema)

    @allure.title('Попытка авторизации пользователя с пустыми обязательными полями')
    @allure.description('Тест проверяет статус код и текст ответа при попытке авторизации с пустыми обязательными полями')
    @pytest.mark.parametrize('user_data', users_list_required_login_attributes_empty)
    def test_attempt_to_login_with_empty_required_fields(self, user_data):
        response = send_request_with_request_json(login_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, missing_required_login_fields)

    @allure.title('Попытка авторизации пользователя с отсутствующими обязательными полями')
    @allure.description('Тест проверяет статус код и текст ответа при попытке авторизации без указания обязательных полей')
    @pytest.mark.parametrize('user_data', users_list_required_login_attributes_empty)
    def test_attempt_to_login_with_missing_required_fields(self, user_data):
        response = send_request_with_request_json(login_courier, user_data)

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, missing_required_login_fields)

    @allure.title('Попытка авторизации пользователя с невалидной связкой логина и пароля')
    @allure.description('Тест проверяет статус код и текст ответа при попытке авторизации с неправильными логином/паролем')
    @pytest.mark.parametrize('user_data', users_list_credentials_missmatch)
    def test_attempt_to_login_with_invalid_password(self, user_data):
        response = send_request_with_request_json(login_courier, user_data)

        verify_status_code(response, 404)
        verify_json_text_is_valid(response, non_existing_account_error)
