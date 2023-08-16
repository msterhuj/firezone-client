from datetime import datetime

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