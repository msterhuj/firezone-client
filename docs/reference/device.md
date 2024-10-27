# Device Management

## Object structure

```python
class Device:

    # required fields
    user_id: str | User
    public_key: str

    # optional fields
    allowed_ips: list
    description: str
    dns: list
    endpoint: str
    ipv4: str
    ipv6: str
    mtu: int
    name: str
    persistent_keepalive: int
    preshared_key: str
    use_default_allowed_ips: bool
    use_default_dns: bool
    use_default_endpoint: bool
    use_default_mtu: bool
    use_default_persistent_keepalive: bool

    # read-only fields
    id: str
    server_public_key: str
    inserted_at: datetime
    updated_at: datetime
    remote_ip: str | None
    latest_handshake: datetime | None
    rx_bytes: int | None
    tx_bytes: int | None

    # minimal required fields for creation or update
    required_fields = [ "user_id", "public_key" ]

    # optional fields for creation or update
    optional_fields = [ "allowed_ips", "description", "dns", "endpoint",
                        "ipv4", "ipv6", "mtu", "name", "persistent_keepalive",
                        "preshared_key", "use_default_allowed_ips", "use_default_dns",
                        "use_default_endpoint", "use_default_mtu",
                        "use_default_persistent_keepalive", "user_id" ]
```

## List Devices

```python
from firezone_client import FZClient, Device

client = FZClient(endpoint, token)

device = client.list(Device)
```

## Get Device

```python
from firezone_client import FZClient, Device

client = FZClient(endpoint, token)

# set to variable id the id of the Device or the email
device = client.get(Device, id="aa113452-9f07-4cef-8b57-dc9f38c64312")
```

## Create Device

```python
from firezone_client import FZClient, Device, generate_key_pair

client = FZClient(endpoint, token)

priv, pub = generate_key_pair()
device: Device = Device(
    user_id="user@local",
    public_key=pub,
    allowedsd_ips=["0.0.0.0/0"],
    use_default_allowed_ips=False
)

client.create(device)
```

## Update Device

> This function is not implemented yet

## Delete Device

```python
from firezone_client import FZClient, Device

client = FZClient(endpoint, token)

device = client.get(device, id="aa113452-9f07-4cef-8b57-dc9f38c64312")

client.delete(Device)
```
