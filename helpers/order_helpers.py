import allure

from endpoints.base_steps import send_request_with_request_json, send_request_with_params
import random
from endpoints.endpoints import create_order, get_orders_by_track

from faker import Faker

fake = Faker("ru_RU")

@allure.step('Сгенерировать JSON с уникальными данными для оформления заказа')
def generate_order_data_json():

    return {"firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": random.randint(0,224),
    "phone": fake.phone_number(),
    "rentTime": random.randint(0,6),
    "deliveryDate": fake.future_date(),
    "comment": fake.text(25),
    "color": ['BLACK', 'GREY']}

@allure.step('Разместить заказ и получить id')
def place_order_and_get_order_id():
    order_json = generate_order_data_json()

    response = send_request_with_request_json(create_order, order_json)
    track = response.json()["track"]

    return get_order_id_by_track(track)

@allure.step('Получить id заказа по track')
def get_order_id_by_track(track):

    params = {'t': track}

    response = send_request_with_params(get_orders_by_track, params)

    return response.json()["order"]["id"]
