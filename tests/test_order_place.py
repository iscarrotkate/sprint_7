import allure
import pytest

from endpoints.base_steps import send_request_with_request_json, verify_status_code, verify_json_schema_is_valid, \
    send_request_without_request_json, send_request_by_address_with_params, verify_json_text_is_valid
from endpoints.endpoints import create_order, get_orders_list, assign_courier
from endpoints.json_schemas import place_order_response_schema, orders_list_response_schema
from helpers.data import existing_user
from helpers.order_helpers import generate_order_data_json, place_order_and_get_order_id


class TestPlaceOrders:

    @allure.title('Размещение заказа с разными выбранными цветами')
    @allure.description('Тест проверяет статус код соответствие ответа json-схеме при выборе разных цветов')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_with_valid_color(self, color):
        order_json = generate_order_data_json()
        order_json.update({'color': color})

        response = send_request_with_request_json(create_order, order_json)

        verify_status_code(response, 201)
        verify_json_schema_is_valid(response, place_order_response_schema)
