import unittest
from check import CheckManager
from book import BookManager
from user import UserManager
from models import Book, User
from storage import Storage
import os

class TestCheckManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.check_manager = CheckManager(self.book_manager, self.user_manager)
        self.book_storage = Storage("test_books.json")
        self.user_storage = Storage("test_users.json")
        self.book_manager.storage = self.book_storage
        self.user_manager.storage = self.user_storage
        self.book_manager.books = {}
        self.user_manager.users = {}
        self.test_book = Book("Test Title", "Test Author", "1234567890")
        self.test_user = User("Test User", "user123")

    def tearDown(self):
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")
        if os.path.exists("test_users.json"):
            os.remove("test_users.json")

    def test_checkout_book(self):
        self.book_manager.books["1234567890"] = self.test_book
        self.user_manager.users["user123"] = self.test_user
        self.check_manager.check_out_book("user123", "1234567890")
        self.assertEqual(self.book_manager.books["1234567890"].checked_out_to, "user123")

    def test_checkout_already_checked_out_book(self):
        self.book_manager.books["1234567890"] = self.test_book
        self.user_manager.users["user123"] = self.test_user
        self.check_manager.check_out_book("user123", "1234567890")
        # self.book_manager.update_book("1234567890", "Test Title", "Test Author")
    # with self.assertRaises(ValueError):
        self.check_manager.check_out_book("user456", "1234567890")
        self.assertEqual(self.book_manager.books["1234567890"].checked_out_to, "user123")

    def test_checkout_non_existent_book(self):
        self.user_manager.users["user123"] = self.test_user
        # with self.assertRaises(KeyError):
        self.check_manager.check_out_book("user123", "nonexistent")
        self.assertFalse("nonexistent" in self.book_manager.books)

    def test_checkout_book_by_non_existent_user(self):
        self.book_manager.books["1234567890"] = self.test_book
        # with self.assertRaises(KeyError):
        self.check_manager.check_out_book("nonexistent", "1234567890")
        self.assertIsNone(self.book_manager.books["1234567890"].checked_out_to)

    def test_check_in_book(self):
        self.book_manager.books["1234567890"] = self.test_book
        self.test_book.check_out("user123")
        # self.book_manager.update_book("1234567890", "Test Title", "Test Author")
        self.check_manager.check_in_book("1234567890")
        self.assertIsNone(self.book_manager.books["1234567890"].checked_out_to)

    def test_check_in_non_checked_out_book(self):
        self.book_manager.books["1234567890"] = self.test_book
        # with self.assertRaises(ValueError):
        self.check_manager.check_in_book("1234567890")
        self.assertIsNone(self.book_manager.books["1234567890"].checked_out_to)

if __name__ == "__main__":
    unittest.main()
