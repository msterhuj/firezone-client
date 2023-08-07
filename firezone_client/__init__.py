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


class Configurations:
    allow_unprivileged_device_configuration: bool
    allow_unprivileged_device_management: bool
    default_client_allowed_ips: list
    default_client_dns: list
    default_client_endpoint: str
    default_client_mtu: int
    default_client_persistent_keepalive: int
    disable_vpn_on_oidc_error: bool
    id: str
    inserted_at: datetime
    local_auth_enabled: bool
    logo: dict
    openid_connect_providers: list
    saml_identity_providers: list
    updated_at: datetime
    vpn_session_duration: int

    @staticmethod
    def __init_from_dict__(data: dict) -> 'Configurations':
        configurations = Configurations()
        configurations.__dict__.update(data)
        return configurations
    
    @staticmethod
    def get(client) -> 'Configurations':
        return Configurations.__init_from_dict__(client.__get__("/configuration")["data"])

    def patch(self, client):
        data = {
            "configuration": {
                "allow_unprivileged_device_configuration": self.allow_unprivileged_device_configuration,
                "allow_unprivileged_device_management": self.allow_unprivileged_device_management,
                "default_client_allowed_ips": self.default_client_allowed_ips,
                "default_client_dns": self.default_client_dns,
                "default_client_endpoint": self.default_client_endpoint,
                "default_client_mtu": self.default_client_mtu,
                "default_client_persistent_keepalive": self.default_client_persistent_keepalive,
                "disable_vpn_on_oidc_error": self.disable_vpn_on_oidc_error,
                "local_auth_enabled": self.local_auth_enabled,
                "openid_connect_providers": self.openid_connect_providers,
                "saml_identity_providers": self.saml_identity_providers,
                "vpn_session_duration": self.vpn_session_duration
            }
        }
        client.__patch__("/configuration", data)

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
    
    def __patch__(self, url: str, body) -> json:
        reply = requests.patch(url=self.endpoint + url, headers=self.headers, verify=self.ssl_verify, json=body)
        if reply.status_code == 500:
            raise Exception("Error for request API")
        return reply.json()
    
    def list(self, obj: object) -> object:
        return obj.list(self)
    
    def get(self, obj: object) -> object:
        return obj.get(self)

    def get_users(self) -> List[User]:
        return [
            User().__init_from_dict__(user_json)
            for user_json in self.__get__("/users")["data"]
        ]