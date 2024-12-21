import requests


class Client:
    def __init__(self, host="http://5.63.153.31:5051", headers=None):
        self.host = host
        self.headers = headers or {
            'accept': '*/*',
            'Content-Type': 'application/json'
        }

    def register_user(self, json):
        path = self.host + "/v1/account"
        response = requests.request(method="POST", url=path, headers=self.headers, json=json)
        return response