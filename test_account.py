import requests
import json


def test_one():
  url = "http://5.63.153.31:5051/v1/account"

  payload = json.dumps({
    "login": "login1238765435",
    "email": "login1238765435@mail.ru",
    "password": "passwordlogin1238765435"
  })
  headers = {
    'accept': '*/*',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
