import pytest
import requests
from faker import Faker

@pytest.fixture
def set_url():
    return "http://5.63.153.31:5051/v1/account"


@pytest.fixture
def headers():
    return {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }

fake = Faker("ru_RU")
for_data = [
    # Короткий логин
    {
        "login": "l",
        "email": fake.email(),
        "password": fake.password()
    },
    # Невалидный email
    {
        "login": fake.user_name(),
        "email": "login_useremail.ru",
        "password": fake.password()
    },
    # Короткий пароль
    {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": "1"
    }
]


@pytest.mark.parametrize('data', for_data)
def test_post_v1_account_negative(set_url, headers, data):
    print(data)
    response = requests.request("POST", set_url, headers=headers, json=data)
    print(response.text)
