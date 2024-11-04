import unittest

from firezone_client import FZClient, User, Device, generate_key_pair
from scripts.token_reader import get_token, api_endpoint
from random import randint

USERNAME = "admin@localhost"


class TestRule(unittest.TestCase):

    def setUp(self):
        self.client: FZClient = FZClient(api_endpoint, get_token())
        self.user: User = self.client.get(User, id=USERNAME)

    def test_create_rule(self):
        priv, pub = generate_key_pair()
        device: Device = Device(
            user_id=self.user.id,
            public_key=pub,
            allowedsd_ips=["0.0.0.0/0"],
            use_default_allowed_ips=False
        )
        device_reply = self.client.create(device)
        self.assertIsInstance(device_reply, Device)
        self.assertIsInstance(device_reply.id, str)

    def test_list_rules(self):
        priv, pub = generate_key_pair()
        device: Device = Device(
            user_id=self.user.id,
            public_key=pub,
            allowedsd_ips=["0.0.0.0/0"],
            use_default_allowed_ips=False
        )
        self.client.create(device)
        devices = Device.list(self.client)
        self.assertIsInstance(devices, list)
        self.assertIsInstance(devices[0], Device)
        self.assertIsInstance(devices[0].id, str)

    def test_delete_rule(self):
        priv, pub = generate_key_pair()
        device: Device = Device(
            user_id=self.user.id,
            public_key=pub,
        )
        device_reply = self.client.create(device)
        self.assertIsInstance(device_reply, Device)


    def tearDown(self) -> None:
        devices = Device.list(self.client)
        for device in devices:
            self.client.delete(device)