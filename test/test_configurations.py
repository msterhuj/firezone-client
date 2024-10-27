import unittest
from datetime import datetime

from firezone_client import FZClient, Configuration
from scripts.token_reader import get_token, api_endpoint


class TestConfiguration(unittest.TestCase):

    def setUp(self):
        self.client: FZClient = FZClient(api_endpoint, get_token())

    def test_get_config(self):
        config: Configuration = self.client.get(Configuration)
        self.assertIsInstance(config, Configuration)
        self.default_config = config

    #def test_update_config(self):
    #    config: Configuration = self.client.get(Configuration)
    #    dns_total = len(config.default_client_dns)
    #    config.default_client_dns.append("0.0.0.0")
    #    self.client.patch(config)
    #    new_config: Configuration = self.client.get(Configuration)
    #    self.assertEqual(len(new_config.default_client_dns), dns_total + 1)
    #    new_config.default_client_dns.pop(2)
    #    self.client.patch(new_config)

    def tearDown(self) -> None:
        ...
