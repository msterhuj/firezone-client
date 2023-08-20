import unittest
from datetime import datetime

from firezone_client import FZClient, Configurations
from token_reader import get_token, api_endpoint


class TestConfigurations(unittest.TestCase):

    def setUp(self):
        self.client: FZClient = FZClient(api_endpoint, get_token())

    def test_get_config(self):
        config: Configurations = self.client.get(Configurations)
        self.assertIsInstance(config, Configurations)
        self.default_config = config

    def test_update_config(self):
        config: Configurations = self.client.get(Configurations)
        dns_total = len(config.default_client_dns)
        config.default_client_dns.append("0.0.0.0")
        self.client.patch(config)
        new_config: Configurations = self.client.get(Configurations)
        self.assertEqual(len(new_config.default_client_dns), dns_total + 1)
        new_config.default_client_dns.pop(2)
        self.client.patch(new_config)

    def tearDown(self) -> None:
        ...
