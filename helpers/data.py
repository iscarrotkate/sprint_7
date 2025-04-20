from helpers.helpers import generate_random_string

users_list_required_registration_attributes_empty = [
        {
            "login": '',
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        },
        {
            "login": generate_random_string(10),
            "password": '',
            "firstName": generate_random_string(10)
        },
        {
            "login": '',
            "password": '',
            "firstName": generate_random_string(10)
        },
        {
            "login": '',
            "password": '',
            "firstName": ''
        }
]

users_list_required_login_attributes_empty = [
    {"login": 'ebaranova-qa-python-19', "password": ''},
    {"login": '', "password": 'qwerty123'},
    {"login": '', "password": ''}
]

existing_user = {
    "login": 'ebaranova-qa-python-19',
    "password": 'qwerty123',
    "firstName": 'Ekaterina',
    "id": 505830
}

users_list_credentials_missmatch = [
    {
        "login": 'ebaranova-qa-python-19',
        "password": 'ytrewq321'},
    {
        "login": 'ebaranova-qa-python-000',
        "password": 'qwerty123'
    },
    {
        "login": 'ebaranova-qa-python-000',
        "password": 'ytrewq321'
    }
]

users_list_login_invalid_json = [
    {"password": 'qwerty123'},
    {"login": 'ebaranova-qa-python-19'},
    {}
    ]

users_list_registration_invalid_json = [
    {"password": generate_random_string(10), "firstName": generate_random_string(10)},
    {"login": generate_random_string(10), "firstName": generate_random_string(10)},
    {"firstName": generate_random_string(10)},
    {}
]