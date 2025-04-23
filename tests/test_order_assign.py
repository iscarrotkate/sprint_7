import allure

from endpoints.api_responses import successful_operation_message
from endpoints.base_steps import send_request_by_address_with_params, verify_status_code, verify_json_text_is_valid
from endpoints.endpoints import assign_courier
from helpers.order_helpers import place_order_and_get_order_id


class TestAssignOrder:
    @allure.title('Принятие заказа')
    @allure.description('Тест проверяет статус код и текст ответа при назначении существующего курьера новому заказу')
    def test_assign_order_with_valid_data(self, registered_user_id):
        order_id = place_order_and_get_order_id()
        params = {"courierId": registered_user_id}

        response = send_request_by_address_with_params(assign_courier, order_id, params)

        verify_status_code(response, 200)
        verify_json_text_is_valid(response, successful_operation_message)
