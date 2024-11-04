import unittest
import string
import random

from datetime import datetime

from firezone_client import FZClient, User, Rule
from scripts.token_reader import get_token, api_endpoint
from random import randint

def random_24_subnet():
    return ".".join([str(randint(0, 255)) for _ in range(3)]) + ".0/24"

USERNAME = "admin@localhost"

class TestRule(unittest.TestCase):

    def setUp(self):
        self.client: FZClient = FZClient(api_endpoint, get_token())
        self.user: User = self.client.get(User, id=USERNAME)

    def test_create_rule(self):
        rule: Rule = Rule(
            user_id=self.user,
            destination=random_24_subnet(),
            action="accept",
        )
        rule_reply = self.client.create(rule)
        self.assertIsInstance(rule_reply, Rule)
        self.assertIsInstance(rule_reply.id, str)

    def test_list_rules(self):
        rule: Rule = Rule(
            user_id=self.user,
            destination=random_24_subnet(),
            action="accept",
        )
        self.client.create(rule)
        rules = Rule.list(self.client)
        self.assertIsInstance(rules, list)
        self.assertIsInstance(rules[0], Rule)
        self.assertIsInstance(rules[0].id, str)

    #def test_update_rule(self):
    #    rule: Rule = Rule(
    #        user_id=User.get(self.client, id=USERNAME),
    #        destination=random_24_subnet(),
    #        action="accept",
    #    )
    #    rule_reply = self.client.create(rule)
    #    rule_reply.action = "drop"
    #    rule_reply_updated = self.client.update(rule_reply)

    def test_delete_rule(self):
        rule: Rule = Rule(
            user_id=self.user,
            destination=random_24_subnet(),
            action="accept",
        )
        rule_reply = self.client.create(rule)
        self.client.delete(rule_reply)


    def tearDown(self) -> None:
        for rule in Rule.list(self.client):
            self.client.delete(rule)
