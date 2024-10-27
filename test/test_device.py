import unittest
import string
import random

from datetime import datetime

from firezone_client import FZClient, User, Device, generate_key_pair
from scripts.token_reader import get_token, api_endpoint
from random import randint

USERNAME = "admin@localhost"


class TestRule(unittest.TestCase):

    def setUp(self):
        self.client: FZClient = FZClient(api_endpoint, get_token())

    def test_create_rule(self):
        user = User.get(self.client, id=USERNAME)
        priv, pub = generate_key_pair()
        device: Device = Device(
            user_id=user.id,
            public_key=pub,
            allowedsd_ips=["0.0.0.0/0"],
            use_default_allowed_ips=False
        )
        device_reply = self.client.create(device)
        self.assertIsInstance(device_reply, Device)
        self.assertIsInstance(device_reply.id, str)

    def test_list_rules(self):
        devices = Device.list(self.client)
        self.assertIsInstance(devices, list)
        self.assertIsInstance(devices[0], Device)
        self.assertIsInstance(devices[0].id, str)

    def test_delete_rule(self):
        user = User.get(self.client, id=USERNAME)
        priv, pub = generate_key_pair()
        device: Device = Device(
            user_id=user.id,
            public_key=pub,
        )
        device_reply = self.client.create(device)
        self.assertIsInstance(device_reply, Device)


    def tearDown(self) -> None:
        ...