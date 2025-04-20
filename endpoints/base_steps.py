import allure
from jsonschema import validate
import requests

from endpoints.endpoints import base_url

@allure.step('Проверить код ответа')
def verify_status_code(response, status_code):
    actual = response.status_code
    assert actual == status_code, f'Ожидался статус-код {status_code}, но был получен статус-код {actual}'

@allure.step('Проверить соответствие тела ответа JSON-схеме')
def verify_json_schema_is_valid(response, schema):
    try:
        validate(instance=response.json(), schema=schema)
        assert True
    except:
        assert False, f'Тело ответа не соответствует JSON-схеме'

@allure.step('Проверить соответствие тела ответа JSON-схеме')
def verify_json_text_is_valid(response, expected):
    response_text = response.text
    assert response_text == expected, f'Ожидался текст ответа {expected}, но был получен {response_text}'

@allure.step('Отправить запрос с телом запроса')
def send_request_with_request_json(request_data, data_json):
    if request_data['method'] == 'POST':
        return requests.post(f"{base_url}{request_data['endpoint']}", data=data_json)

@allure.step('Отправить запрос без тела запроса')
def send_request_without_request_json(request_data):
    if request_data['method'] == 'GET':
        return requests.get(f"{base_url}{request_data['endpoint']}")

@allure.step('Отправить запрос по адресу')
def send_request_by_address(request_data, address):
    request_url = f"{base_url}{request_data['endpoint']}/{address}"
    if request_data['method'] == 'DELETE':
        return requests.delete(request_url)

@allure.step('Отправить запрос с параметром')
def send_request_with_params(request_data, params):
    request_url = f"{base_url}{request_data['endpoint']}"
    if request_data['method'] == 'GET':
        return requests.get(request_url, params=params)

@allure.step('Отправить запрос по адресу с параметром')
def send_request_by_address_with_params(request_data, address, params):
    request_url = f"{base_url}{request_data['endpoint']}/{address}"
    if request_data['method'] == 'PUT':
        return requests.put(request_url, params=params)