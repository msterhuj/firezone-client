from datetime import datetime
from typing import List

from firezone_client.models import User

class Devices:
    allowed_ips: list
    description: str
    dns: list
    endpoint: str
    id: str
    inserted_at: datetime
    ipv4: str
    ipv6: str
    latest_handshake: datetime | None
    mtu: int
    name: str
    persistent_keepalive: int
    preshared_key: str
    public_key: str
    remote_ip: str | None
    rx_bytes: int | None
    server_public_key: str
    tx_bytes: int | None
    updated_at: datetime
    use_default_allowed_ips: bool
    use_default_dns: bool
    use_default_endpoint: bool
    use_default_mtu: bool
    use_default_persistent_keepalive: bool
    user_id: str | User

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @staticmethod
    def list(client) -> List['Devices']:
        return [
            Devices().__init_from_dict__(devices_json)
            for devices_json in client.__get__("/devices")["data"]
        ]
    
    def get(client, **kwargs) -> 'Devices':
        devices_id = kwargs.get("id")

        if devices_id is None:
            raise Exception("id is required")

        server_reply = client.__get__(f"/devices/{devices_id}")

        if server_reply.get("errors"):
            raise Exception(server_reply.get("errors"))

        return Devices(server_reply.get("data"))
    
    def create(self, client) -> 'Devices':
        data = {
            "device": { 
                "allowed_ips": self.allowed_ips,
                "description": self.description,
                "dns": self.dns,
                "endpoint": self.endpoint,
                "inserted_at": self.inserted_at,
                "ipv4": self.ipv4,
                "ipv6": self.ipv6,
                "latest_handshake": self.latest_handshake,
                "mtu": self.mtu,
                "name": self.name,
                "persistent_keepalive": self.persistent_keepalive,
                "preshared_key": self.preshared_key,
                "public_key": self.public_key,
                "server_public_key": self.server_public_key,
                "use_default_allowed_ips": self.use_default_allowed_ips,
                "use_default_dns": self.use_default_dns,
                "use_default_endpoint": self.use_default_endpoint,
                "use_default_mtu": self.use_default_mtu,
                "use_default_persistent_keepalive": self.use_default_persistent_keepalive,
                "user_id": self.user_id,
            }
        }
        if isinstance(self.user_id, User):
            data["device"]["user_id"] = self.user_id.id
        
        server_reply = client.__post__("/devices", data)
        if server_reply.get("errors"):
            raise Exception(server_reply.get("errors"))
        
        return Devices(**server_reply.get("data"))
