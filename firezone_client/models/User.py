from typing import List
from datetime import datetime

class User:
    disabled_at: datetime | None
    email: str
    id: str
    inserted_at: datetime
    last_signed_in_at: datetime | None
    last_signed_in_method: datetime | None
    role: str = "unprivileged"
    updated_at: datetime

    password: str | None = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @staticmethod
    def __init_from_dict__(data: dict) -> 'User':
        user = User()
        user.__dict__.update(data)
        return user
    
    @staticmethod
    def list(client) -> List['User']:
        return [
            User().__init_from_dict__(user_json)
            for user_json in client.__get__("/users")["data"]
        ]

    def get(client, *args, **kwargs) -> 'User':
        user_id = kwargs.get("id")

        if user_id is None:
            raise Exception("id is required")

        server_reply = client.__get__(f"/users/{user_id}")

        if server_reply.get("errors"):
            raise Exception(server_reply.get("errors"))

        return User().__init_from_dict__(server_reply.get("data"))

    def create(self, client) -> 'User':
        data = {
            "user": {
                "email": self.email,
                "role": self.role
            }
        }
        if self.password:
            data["user"]["password"] = self.password
            data["user"]["password_confirmation"] = self.password

        server_reply = client.__post__("/users", data)
        if server_reply.get("errors"):
            raise Exception(server_reply.get("errors"))

        return User(**server_reply.get("data"))
    
    def delete(self, client):
        return client.__delete__(f"/users/{self.id}")
