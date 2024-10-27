import json
from datetime import datetime
from typing import List

import requests

from firezone_client.models import Configuration, User, Device


class FZClient:
    endpoint: str
    ssl_verify: bool = True
    token: str
    headers = {
        "Content-Type": "application/json",
    }

    def __init__(self, endpoint, token, ssl_verify=True) -> None:
        self.endpoint = endpoint
        self.token = token
        self.ssl_verify = ssl_verify
        self.headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def __get__(self, url: str) -> json:
        reply = requests.get(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.json()

    def __post__(self, url: str, body) -> json:
        reply = requests.post(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify, json=body)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.json()

    def __patch__(self, url: str, body) -> json:
        reply = requests.patch(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify, json=body)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.json()

    def __delete__(self, url: str) -> json:
        reply = requests.delete(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.status_code

    def list(self, obj: object) -> List[Device | Configuration | User]:
        return obj.list(self)

    def get(self, obj: object, *args, **kwargs) -> object:
        return obj.get(self, *args, **kwargs)

    def create(self, obj: object) -> object:
        return obj.create(self)

    def update(self, obj: object) -> object:
        return obj.update(self)

    def delete(self, obj: object) -> object:
        return obj.delete(self)
