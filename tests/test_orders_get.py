import allure

from endpoints.base_steps import send_request_without_request_json, verify_json_schema_is_valid, verify_status_code
from endpoints.endpoints import get_orders_list
from endpoints.json_schemas import orders_list_response_schema

class TestOrders:
    @allure.title('Получение списка заказов')
    @allure.description(
        'Тест проверяет статус код и соответствие ответа json-схеме при запросе списка заказов')
    def test_get_orders_list(self):
        response = send_request_without_request_json(get_orders_list)

        verify_status_code(response, 200)
        verify_json_schema_is_valid(response, orders_list_response_schema)
