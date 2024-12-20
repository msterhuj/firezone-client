# User Management

## Object structure

```python
class User:
    disabled_at: datetime | None
    email: str
    id: str
    inserted_at: datetime
    last_signed_in_at: datetime | None
    last_signed_in_method: datetime | None
    role: str = "unprivileged"
    updated_at: datetime

    # only for setting a password or a new
    password: str | None = None
```

## List Users

```python
from firezone_client import FZClient, User

client = FZClient(endpoint, token)

user = client.list(User)
```

## Get User

```python
from firezone_client import FZClient, User

client = FZClient(endpoint, token)

# set to variable id the id of the user or the email
user = client.get(User, id="user@local")
```

## Create User

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| role | admin or **unprivileged** (default) | No | User role. |
| email | string | Yes | Email which will be used to identify the user. |
| password | string | No | A password that can be used for login-password authentication. |
| password_confirmation | string | -> | Is required when the password is set. |

```python
from firezone_client import FZClient, User

client = FZClient(endpoint, token)

user = User(
    email="user@local",
    password="password",
    role="admin",
)

client.create(user)
```

## Update User

```python
from firezone_client import FZClient, User

client = FZClient(endpoint, token)

user = client.get(User, id="user@local")

user.role = "admin"

client.update(user)
```

## Delete User

```python
from firezone_client import FZClient, User

client = FZClient(endpoint, token)

user = client.get(User, id="user@local")

client.delete(user)
```
