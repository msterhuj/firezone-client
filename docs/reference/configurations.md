# Configurations Management

## Object structure

```python
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
```

## Get current configurations of firezone

```python
from firezone_client import FZclient, Configurations

client = FZClient(endpoint, token)

config = client.get(Configurations)

print(config.updated_at)
```

## Update config

```python
# get current config
config = client.get(Configurations)

# for example add new ip to the list for dns
config.default_client_dns.append("1.1.1.1")

# push update
client.update(config)
```
