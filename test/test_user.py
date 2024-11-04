import unittest
import string
import random

from datetime import datetime

from firezone_client import FZClient, User, generate_password
from scripts.token_reader import get_token, api_endpoint

def generate_username() -> str:
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
    return username

USERNAME = generate_username() + "@localhost"

class TestUser(unittest.TestCase):

    def setUp(self):
        self.username = USERNAME
        self.user: User = None
        self.client: FZClient = FZClient(api_endpoint, get_token())
        print("Setup test for user")
        print(f"Using username: {self.username}")

    def test_create_user(self):
        user = User(
            email=self.username,
            password=generate_password(12),
            role="admin",
        )
        self.user = self.client.create(user)
        self.assertIsInstance(self.user, User)

    def test_list_users(self):
        user = User(
            email=self.username,
            password=generate_password(12),
            role="admin",
        )
        self.user = self.client.create(user)
        users: list[User] = self.client.list(User)
        self.assertIsInstance(users, list)
        self.assertTrue(len(users) > 0)
        self.assertIsInstance(users[0], User)

    def test_get_user(self):
        user = User(
            email=self.username,
            password=generate_password(12),
            role="admin",
        )
        self.user = self.client.create(user)
        print("Getting user by email")
        user_by_email: User = self.client.get(User, id=self.username)
        self.assertIsInstance(user_by_email, User)
        print(f"Fetched user {self.username} id is {user_by_email.id}")
        print("Getting user by id")
        user_by_id: User = self.client.get(User, id=user_by_email.id)
        self.assertIsInstance(user_by_id, User)

    def test_update_user(self):
        user = User(
            email=self.username,
            password=generate_password(12),
            role="admin",
        )
        self.user = self.client.create(user)
        print("Get user to update")
        user: User = self.client.get(User, id=self.username)
        user.role = "unprivileged"
        print("Apply user update")
        self.client.update(user)
        print("User role updated checking")
        user: User = self.client.get(User, id=self.username)
        self.assertEqual(user.role, "unprivileged")

    def test_delete_user(self):
        new_user = User(
            email=generate_username() + generate_username() + "@localhost",
            password=generate_password(12),
            role="admin",
        )
        print("Create delete account " + new_user.email)
        self.client.create(new_user)
        user: User = self.client.get(User, id=new_user.email)
        self.client.delete(user)

    def tearDown(self) -> None:
        if self.user:
            self.client.delete(self.user)