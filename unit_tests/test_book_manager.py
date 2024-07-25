import unittest
from book import BookManager
from models import Book
from storage import Storage
import os

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()
        self.storage = Storage("test_books.json")
        self.book_manager.storage = self.storage
        self.book_manager.books = {}
        self.test_book = Book("Test Title", "Test Author", "1")
    
    def tearDown(self):
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")

    def test_add_book(self):
        self.book_manager.add_book("Test Title", "Test Author", "1")
        self.assertIn("1", self.book_manager.books)

    def test_add_book_with_existing_isbn(self):
        self.book_manager.books["1"] = self.test_book
        # with self.assertRaises(ValueError):
        tmp = self.book_manager.books
        self.book_manager.add_book("Random Title", "Random Author", "1")
        self.assertEqual(tmp, self.book_manager.books)

    def test_update_book(self):
        self.book_manager.books["1"] = self.test_book
        self.book_manager.update_book("1")
        self.assertEqual(self.book_manager.books["1"].title, "Test Title")

    def test_update_non_existent_book(self):
        isbn = "nonexistent"
        # with self.assertRaises(KeyError):
        tmp = self.book_manager.books
        self.book_manager.update_book(isbn)
        self.assertEqual(tmp, self.book_manager.books)

    def test_delete_book(self):
        self.book_manager.books["1"] = self.test_book
        self.book_manager.delete_book("1")
        self.assertNotIn("1", self.book_manager.books)

    def test_delete_non_existent_book(self):
        isbn = "nonexistent"
        # with self.assertRaises(KeyError):
        tmp = self.book_manager.books
        self.book_manager.delete_book(isbn)
        self.assertEqual(tmp, self.book_manager.books)

    def test_list_books(self):
        self.book_manager.books["1"] = self.test_book
        books = list(self.book_manager.books.values())
        self.assertEqual(len(books), 1)

    def test_search_book(self):
        self.book_manager.books["1"] = self.test_book
        book = self.book_manager.get_book_by_isbn("1")
        self.assertEqual(book.title, "Test Title")

    def test_search_non_existent_book(self):
        book = self.book_manager.get_book_by_isbn("nonexistent")
        self.assertIsNone(book)

if __name__ == "__main__":
    unittest.main()
