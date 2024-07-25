import unittest
from check import CheckManager
from book import BookManager
from user import UserManager
from models import Book, User
from storage import Storage
import os

class TestCheckManager(unittest.TestCase):
    """
    Unit tests for the CheckManager class.
    """

    def setUp(self):
        """
        Set up BookManager, UserManager, and CheckManager instances and mock storage before each test.
        """
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
        """
        Clean up the test storage files after each test.
        """
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")
        if os.path.exists("test_users.json"):
            os.remove("test_users.json")

    def test_checkout_book(self):
        """
        Test checking out a book to a user.
        """
        self.book_manager.books["1234567890"] = self.test_book
        self.user_manager.users["user123"] = self.test_user
        self.check_manager.check_out_book("user123", "1234567890")
        self.assertEqual(self.book_manager.books["1234567890"].checked_out_to, "user123")

    def test_checkout_already_checked_out_book(self):
        """
        Test checking out a book that is already checked out (should not allow).
        """
        self.book_manager.books["1234567890"] = self.test_book
        self.user_manager.users["user123"] = self.test_user
        self.check_manager.check_out_book("user123", "1234567890")
        initial_checkout = self.book_manager.books["1234567890"].checked_out_to
        self.check_manager.check_out_book("user456", "1234567890")
        self.assertEqual(self.book_manager.books["1234567890"].checked_out_to, initial_checkout)

    def test_checkout_non_existent_book(self):
        """
        Test checking out a non-existent book (should not allow).
        """
        self.user_manager.users["user123"] = self.test_user
        self.check_manager.check_out_book("user123", "nonexistent")
        self.assertNotIn("nonexistent", self.book_manager.books)

    def test_checkout_book_by_non_existent_user(self):
        """
        Test checking out a book by a non-existent user (should not allow).
        """
        self.book_manager.books["1234567890"] = self.test_book
        self.check_manager.check_out_book("nonexistent", "1234567890")
        self.assertIsNone(self.book_manager.books["1234567890"].checked_out_to)

    def test_check_in_book(self):
        """
        Test checking in a book.
        """
        self.book_manager.books["1234567890"] = self.test_book
        self.test_book.check_out("user123")
        self.check_manager.check_in_book("1234567890")
        self.assertIsNone(self.book_manager.books["1234567890"].checked_out_to)

    def test_check_in_non_checked_out_book(self):
        """
        Test checking in a book that is not checked out (should not change anything).
        """
        self.book_manager.books["1234567890"] = self.test_book
        initial_checked_out_to = self.book_manager.books["1234567890"].checked_out_to
        self.check_manager.check_in_book("1234567890")
        self.assertEqual(self.book_manager.books["1234567890"].checked_out_to, initial_checked_out_to)

if __name__ == "__main__":
    unittest.main()
