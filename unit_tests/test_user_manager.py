import unittest
from user import UserManager
from models import User
from storage import Storage
import os

class TestUserManager(unittest.TestCase):
    """
    Unit tests for the UserManager class.
    """

    def setUp(self):
        """
        Set up a UserManager instance and mock storage before each test.
        """
        self.user_manager = UserManager()
        self.storage = Storage("test_users.json")
        self.user_manager.storage = self.storage
        self.user_manager.users = {}
        self.test_user = User("Test User", "1")

    def tearDown(self):
        """
        Clean up the test storage file after each test.
        """
        if os.path.exists("test_users.json"):
            os.remove("test_users.json")

    def test_add_user(self):
        """
        Test adding a user to the user manager.
        """
        self.user_manager.add_user("Test User", "1")
        self.assertIn("1", self.user_manager.users)

    def test_add_user_with_existing_id(self):
        """
        Test adding a user with an existing ID (should not be allowed).
        """
        self.user_manager.users["1"] = self.test_user
        initial_users = self.user_manager.users.copy()
        self.user_manager.add_user("Test User", "1")
        self.assertEqual(initial_users, self.user_manager.users)

    def test_update_user(self):
        """
        Test updating a user's details.
        """
        self.user_manager.users["1"] = self.test_user
        self.user_manager.update_user("1", "Updated Test User")
        self.assertEqual(self.user_manager.users["1"].name, "Updated Test User")

    def test_update_non_existent_user(self):
        """
        Test updating a non-existent user (should not change anything).
        """
        user_id = "nonexistent"
        initial_users = self.user_manager.users.copy()
        self.user_manager.update_user(user_id, "Updated Test User")
        self.assertEqual(initial_users, self.user_manager.users)

    def test_delete_user(self):
        """
        Test deleting a user.
        """
        self.user_manager.users["1"] = self.test_user
        self.user_manager.delete_user("1")
        self.assertNotIn("1", self.user_manager.users)

    def test_delete_non_existent_user(self):
        """
        Test deleting a non-existent user (should not change anything).
        """
        user_id = "nonexistent"
        initial_users = self.user_manager.users.copy()
        self.user_manager.delete_user(user_id)
        self.assertEqual(initial_users, self.user_manager.users)

    def test_list_users(self):
        """
        Test listing all users.
        """
        self.user_manager.users["1"] = self.test_user
        users = list(self.user_manager.users.values())
        self.assertEqual(len(users), 1)

    def test_search_user_by_id(self):
        """
        Test searching for a user by ID.
        """
        self.user_manager.users["1"] = self.test_user
        user = self.user_manager.get_user_by_id("1")
        self.assertEqual(user.name, "Test User")

    def test_search_user_by_name(self):
        """
        Test searching for a user by name.
        """
        self.user_manager.users["1"] = self.test_user
        users = self.user_manager.get_users_by_name("Test User")
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Test User")

    def test_search_non_existent_user(self):
        """
        Test searching for a non-existent user.
        """
        user = self.user_manager.get_user_by_id("nonexistent")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
