import pytest
from faker import Faker
from client import Client

@pytest.fixture
def client():
    return Client()

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
def test_post_v1_account_negative(data, client):
    response = client.register_user(data)
