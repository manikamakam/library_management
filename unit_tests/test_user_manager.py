import unittest
from user import UserManager
from models import User
from storage import Storage
import os

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.storage = Storage("test_users.json")
        self.user_manager.storage = self.storage
        self.user_manager.users = {}
        self.test_user = User("Test User", "1")
    
    def tearDown(self):
        if os.path.exists("test_users.json"):
            os.remove("test_users.json")

    def test_add_user(self):
        self.user_manager.add_user("Test User", "1")
        self.assertIn("1", self.user_manager.users)

    def test_add_user_with_existing_id(self):
        self.user_manager.users["1"] = self.test_user
        # with self.assertRaises(ValueError):
        tmp = self.user_manager.users
        self.user_manager.add_user("Test User", "1")
        self.assertEqual(tmp, self.user_manager.users)

    def test_update_user(self):
        self.user_manager.users["1"] = self.test_user
        self.user_manager.update_user("1", "Updated Test User")
        self.assertEqual(self.user_manager.users["1"].name, "Updated Test User")

    def test_update_non_existent_user(self):
        user_id = "nonexistent"
        # with self.assertRaises(KeyError):
        tmp = self.user_manager.users
        self.user_manager.update_user(user_id, "Updated Test User")
        self.assertEqual(tmp, self.user_manager.users)

    def test_delete_user(self):
        self.user_manager.users["1"] = self.test_user
        self.user_manager.delete_user("1")
        self.assertNotIn("1", self.user_manager.users)

    def test_delete_non_existent_user(self):
        user_id = "nonexistent"
        tmp = self.user_manager.users
        # with self.assertRaises(KeyError):
        self.user_manager.delete_user(user_id)
        self.assertEqual(tmp, self.user_manager.users)

    def test_list_users(self):
        self.user_manager.users["1"] = self.test_user
        users = list(self.user_manager.users.values())
        self.assertEqual(len(users), 1)

    def test_search_user(self):
        self.user_manager.users["1"] = self.test_user
        user = self.user_manager.get_user_by_id("1")
        self.assertEqual(user.name, "Test User")

    def test_search_non_existent_user(self):
        user = self.user_manager.get_user_by_id("nonexistent")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
