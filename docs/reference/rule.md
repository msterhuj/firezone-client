# Rules Management

## Object structure

```python
class Rule:

    # required fields
    user_id: str | User
    destination: str

    # this field need to be both set or equal to None
    port_range: str | None = None
    port_type: str | None = None

    # optional fields
    action: str  # default is drop if not specified

    # read-only fields
    id: str
    inserted_at: datetime
    updated_at: datetime
```

## List Rules

```python
from typing import List
from firezone_client import FZClient, Rule

client = FZClient(endpoint, token)

rules: List[Rule] = client.list(Rule)
```

## Get Rule

```python
from firezone_client import FZClient, Rule

client = FZClient(endpoint, token)

rule: Rule = client.get(Rule, id="0000-0000-0000")
```

## Create Rule

```python
from firezone_client import FZClient, Rule

client = FZClient(endpoint, token)

rule = Rule(
    user_id="0000-0000-0000", # you can pass the user object directly
    destination="0.0.0.0/0",
    action="accept",
)

clien.create(rule)
```

## Update Rule

```python
from firezone_client import FZClient, Rule

client = FZClient(endpoint, token)

rule = client.get(Rule, id="0000-0000-0000")

rule.action = "drop"

client.update(rule)
```

## Delete Rule

```python
from firezone_client import FZClient, Rule

client = FZClient(endpoint, token)

rule = client.get(Rule, id="0000-0000-0000")

client.delete(rule)
```
