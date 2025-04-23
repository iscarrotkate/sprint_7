import allure

from endpoints.api_responses import successful_operation_message, non_existing_courier_error, \
    missing_required_removal_fields
from endpoints.base_steps import send_request_by_address, verify_status_code, verify_json_text_is_valid
from endpoints.endpoints import delete_courier


class TestDeleteCourier:

    @allure.title('Удаление курьера')
    @allure.description('Тест проверяет статус код и текст ответа при удалении существующего курьера')
    def test_delete_courier(self, registered_user_id):
        response = send_request_by_address(delete_courier, registered_user_id)
        verify_status_code(response, 200)
        verify_json_text_is_valid(response, successful_operation_message)

    @allure.title('Попытка удаления курьера без id')
    @allure.description('Тест проверяет статус код и текст ответа при попытке удаления пользователя без указания id')
    def test_attempt_to_delete_courier_without_id(self):
        response = send_request_by_address(delete_courier, '')

        verify_status_code(response, 400)
        verify_json_text_is_valid(response, missing_required_removal_fields)

    @allure.title('Попытка удаления курьера с несуществующим id')
    @allure.description(
        'Тест проверяет статус код и текст ответа при попытке удаления пользователя с несуществующим id')
    def test_attempt_to_delete_courier_with_non_existing_id(self, registered_user_id):
        send_request_by_address(delete_courier, registered_user_id)
        response = send_request_by_address(delete_courier, registered_user_id)

        verify_status_code(response, 404)
        verify_json_text_is_valid(response, non_existing_courier_error)
