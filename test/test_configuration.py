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

    def test_update_config(self):
        config: Configuration = self.client.get(Configuration)
        dns_total = len(config.default_client_dns)
        print(f"Current number of dns server: {dns_total}")
        config.default_client_dns.append("0.0.0.0")
        config.default_client_allowed_ips.append("10.0.0.0/24")
        self.client.update(config)
        print(f"Updated number of dns server: {len(config.default_client_dns)}")

        new_config: Configuration = self.client.get(Configuration)
        self.assertIn("0.0.0.0", new_config.default_client_dns)
        self.assertIn("10.0.0.0/24", new_config.default_client_allowed_ips)

    def tearDown(self) -> None:
        config: Configuration = self.client.get(Configuration)
        config.default_client_dns = ["1.1.1.1", "1.0.0.1"]
        config.default_client_allowed_ips = ["0.0.0.0/0", "::/0"]
        self.client.update(config)
