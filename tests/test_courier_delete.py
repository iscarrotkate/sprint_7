import allure

from endpoints.base_steps import send_request_by_address, verify_status_code, verify_json_text_is_valid
from endpoints.endpoints import delete_courier
from helpers.courier_helpers import register_new_courier_and_return_login_password, login_as_exiting_user_and_get_id

class TestDeleteCourier:

    @allure.title('Удаление курьера')
    @allure.description('Тест проверяет статус код и текст ответа при удалении существующего курьера')
    def test_delete_courier(self):
        user = register_new_courier_and_return_login_password()
        user_id = login_as_exiting_user_and_get_id(user)

        response = send_request_by_address(delete_courier, user_id)
        verify_status_code(response, 200)
        verify_json_text_is_valid(response, '{"ok":true}')


    @allure.title('Попытка удаления курьера с пустым id')
    @allure.description('Тест проверяет статус код и текст ответа при попытке удаления курьера с пустым id')
    def test_attempt_to_delete_courier_with_empty_id(self):
        response = send_request_by_address(delete_courier, '')

        verify_status_code(response, 404)
        verify_json_text_is_valid(response, '"message":  "Недостаточно данных для удаления курьера"')


    @allure.title('Попытка удаления курьера без id')
    @allure.description('Тест проверяет статус код и текст ответа при попытке удаления пользователя без указания id')
    def test_attempt_to_delete_courier_without_id(self):
        response = send_request_by_address(delete_courier, '')

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, '"message":  "Недостаточно данных для удаления курьера"')


    @allure.title('Попытка удаления курьера с несуществующим id')
    @allure.description('Тест проверяет статус код и текст ответа при попытке удаления пользователя с несуществующим id')
    def test_attempt_to_delete_courier_without_id(self):
        user = register_new_courier_and_return_login_password()
        user_id = login_as_exiting_user_and_get_id(user)

        send_request_by_address(delete_courier, user_id)
        response = send_request_by_address(delete_courier, user_id)

        verify_status_code(response, 404)
        verify_json_text_is_valid(response, '"message": "Курьера с таким id нет"')
