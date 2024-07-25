from models import Book
from storage import Storage

class BookManager:
    def __init__(self, storage_file="books.json"):
        self.storage = Storage(storage_file)
        self.books = self.storage.load_data(Book)

    def manage_books(self):
        while True:
            print("````````````````````````````````````````````````````````````````````````")
            print("Book Management")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Book")
            print("6. Back")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                self.add_book(title, author, isbn)
            elif choice == '2':
                isbn = input("Enter book ISBN to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                self.update_book(isbn, title, author)
            elif choice == '3':
                isbn = input("Enter book ISBN to delete: ")
                self.delete_book(isbn)
            elif choice == '4':
                self.list_books()
            elif choice == '5':
                search_term = input("Enter book ISBN, title, or author to search: ")
                self.search_book(search_term)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print("Book with this ISBN already exists. Please choose a different ISBN.")
            return
        book = Book(title, author, isbn)
        self.books[isbn] = book
        self.storage.save_data(self.books)
        print("Book added successfully.")

    def update_book(self, isbn, title=None, author=None):
        book = self.get_book_by_isbn(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            self.books[isbn] = book
            self.storage.save_data(self.books)
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            self.storage.save_data(self.books)
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def list_books(self):
        for book in self.books.values():
            print(book)

    def search_book(self, search_term):
        book = self.get_book_by_isbn(search_term)
        if book:
            print(book)
        else:
            books_by_title = self.get_books_by_title(search_term)
            books_by_author = self.get_books_by_author(search_term)
            if books_by_title or books_by_author:
                for book in books_by_title + books_by_author:
                    print(book)
            else:
                print("Book not found.")

    def get_book_by_isbn(self, isbn):
        return self.books.get(isbn)

    def get_books_by_title(self, title):
        return [book for book in self.books.values() if book.title.lower() == title.lower()]

    def get_books_by_author(self, author):
        return [book for book in self.books.values() if book.author.lower() == author.lower()]

