# Utils

Some utility functions that are available in the `firezone_client` package.

## Wireguard Key Pair generator

```python 
from firezone_client import generate_key_pair

private_key, public_key = generate_key_pair()
```

## Basic password generator

Take as an argument the length of the password to generate.
Default length is 8.

```python
from firezone_client.password_generator import generate_password

password = generate_password()
```
