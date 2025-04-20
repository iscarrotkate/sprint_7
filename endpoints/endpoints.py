base_url = 'https://qa-scooter.praktikum-services.ru'

#Couriers
create_courier = {'method': 'POST', 'endpoint': '/api/v1/courier'}
login_courier = {'method': 'POST', 'endpoint': '/api/v1/courier/login'}
delete_courier = {'method': 'DELETE', 'endpoint': '/api/v1/courier'}

#Orders
create_order = {'method': 'POST', 'endpoint': '/api/v1/orders'}
get_orders_list = {'method': 'GET', 'endpoint': '/api/v1/orders'}
get_orders_by_track = {'method': 'GET', 'endpoint': '/api/v1/orders/track'}
assign_courier = {'method': 'PUT', 'endpoint': '/api/v1/orders/accept'}