import unittest
from book import BookManager
from models import Book
from storage import Storage
import os

class TestBookManager(unittest.TestCase):
    """
    Unit tests for the BookManager class.
    """

    def setUp(self):
        """
        Set up a BookManager instance and mock storage before each test.
        """
        self.book_manager = BookManager()
        self.storage = Storage("test_books.json")
        self.book_manager.storage = self.storage
        self.book_manager.books = {}
        self.test_book = Book("Test Title", "Test Author", "1")

    def tearDown(self):
        """
        Clean up the test storage file after each test.
        """
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")

    def test_add_book(self):
        """
        Test adding a book to the book manager.
        """
        self.book_manager.add_book("Test Title", "Test Author", "1")
        self.assertIn("1", self.book_manager.books)

    def test_add_book_with_existing_isbn(self):
        """
        Test adding a book with an existing ISBN (should not be allowed).
        """
        self.book_manager.books["1"] = self.test_book
        initial_books = self.book_manager.books.copy()
        self.book_manager.add_book("Random Title", "Random Author", "1")
        self.assertEqual(initial_books, self.book_manager.books)

    def test_update_book(self):
        """
        Test updating a book's details.
        """
        self.book_manager.books["1"] = self.test_book
        self.book_manager.update_book("1", "Updated Title", "Updated Author")
        self.assertEqual(self.book_manager.books["1"].title, "Updated Title")
        self.assertEqual(self.book_manager.books["1"].author, "Updated Author")

    def test_update_non_existent_book(self):
        """
        Test updating a non-existent book (should not change anything).
        """
        isbn = "nonexistent"
        initial_books = self.book_manager.books.copy()
        self.book_manager.update_book(isbn, "Updated Title", "Updated Author")
        self.assertEqual(initial_books, self.book_manager.books)

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        self.book_manager.books["1"] = self.test_book
        self.book_manager.delete_book("1")
        self.assertNotIn("1", self.book_manager.books)

    def test_delete_non_existent_book(self):
        """
        Test deleting a non-existent book (should not change anything).
        """
        isbn = "nonexistent"
        initial_books = self.book_manager.books.copy()
        self.book_manager.delete_book(isbn)
        self.assertEqual(initial_books, self.book_manager.books)

    def test_list_books(self):
        """
        Test listing all books.
        """
        self.book_manager.books["1"] = self.test_book
        books = list(self.book_manager.books.values())
        self.assertEqual(len(books), 1)

    def test_search_book_by_isbn(self):
        """
        Test searching for a book by ISBN.
        """
        self.book_manager.books["1"] = self.test_book
        book = self.book_manager.get_book_by_isbn("1")
        self.assertEqual(book.title, "Test Title")

    def test_search_book_by_title(self):
        """
        Test searching for a book by title.
        """
        self.book_manager.books["1"] = self.test_book
        books = self.book_manager.get_books_by_title("Test Title")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Title")

    def test_search_book_by_author(self):
        """
        Test searching for a book by author.
        """
        self.book_manager.books["1"] = self.test_book
        books = self.book_manager.get_books_by_author("Test Author")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].author, "Test Author")

    def test_search_non_existent_book(self):
        """
        Test searching for a non-existent book.
        """
        book = self.book_manager.get_book_by_isbn("nonexistent")
        self.assertIsNone(book)

if __name__ == "__main__":
    unittest.main()
