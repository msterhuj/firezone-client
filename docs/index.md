# Getting started

## How its works ?

We start by initiating the client with the server url and the token to access it

Then from this client you can perform any action you want

For example, to retrieve the current configuration you need to do a `client.get(Configuration)` configuration which is a defined type that takes the returns of the firezone api as an object


## Installation

```bash
pip install firezone-client
```

## Init client

```python
from firezone_client import FZclient, Configuration

endpoint = "http://localhost:13000/v0"
token = "0123456789abcdef"
client = FZClient(endpoint, token)
```

## Manage firezone !

> Select on the left the part you want to manage :smile:
