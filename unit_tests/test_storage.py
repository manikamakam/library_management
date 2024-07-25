import unittest
import json
import os
from models import Book, User
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage("test_storage.json")
        self.book_data = {
            "1234567890": Book("Test Title", "Test Author", "1234567890")
        }
        self.user_data = {
            "user123": User("Test User", "user123")
        }

    def tearDown(self):
        if os.path.exists("test_storage.json"):
            os.remove("test_storage.json")

    def test_load_data_non_existent_file(self):
        data = self.storage.load_data(Book)
        self.assertEqual(data, {})

    def test_save_load_data_consistency(self):
        self.storage.save_data(self.book_data)
        loaded_data = self.storage.load_data(Book)
        self.assertEqual(self.book_data["1234567890"].to_dict(), loaded_data["1234567890"].to_dict())

    def test_save_data(self):
        self.storage.save_data(self.book_data)
        with open("test_storage.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data["1234567890"]["title"], "Test Title")

    def test_load_data(self):
        with open("test_storage.json", "w") as file:
            json.dump({key: value.to_dict() for key, value in self.book_data.items()}, file)
        data = self.storage.load_data(Book)
        self.assertEqual(data["1234567890"].title, "Test Title")

if __name__ == "__main__":
    unittest.main()
