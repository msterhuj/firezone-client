import json
from datetime import datetime
from typing import List

import requests

class User:
    disabled_at: datetime | None
    email: str
    id: str
    inserted_at: datetime
    last_signed_in_at: datetime | None
    last_signed_in_method: datetime | None
    role: str
    updated_at: datetime

    @staticmethod
    def __init_from_dict__(data: dict) -> 'User':
        user = User()
        user.__dict__.update(data)
        return user


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

    def __get__(self, url: str)-> json:
        reply = requests.get(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.json()

    def get_users(self) -> List[User]:
        return [
            User().__init_from_dict__(user_json)
            for user_json in self.__get__("/users")["data"]
        ]