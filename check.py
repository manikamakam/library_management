class CheckManager:
    """
    Manages the checking in and out of books.
    """
    def __init__(self, book_manager, user_manager):
        """
        Initializes CheckManager with book and user managers.

        Args:
            book_manager (BookManager): Instance of BookManager.
            user_manager (UserManager): Instance of UserManager.
        """
        self.book_manager = book_manager
        self.user_manager = user_manager

    def check_out_book(self, user_id, book_isbn):
        """
        Checks out a book to a user and updates the book availability in books.json.
        """
        user = self.user_manager.get_user_by_id(user_id)
        book = self.book_manager.get_book_by_isbn(book_isbn)

        if user and book and book.is_available():
            book.check_out(user_id)
            self.book_manager.books[book_isbn] = book
            self.book_manager.storage.save_data(self.book_manager.books)
            print(f"Book '{book.title}' checked out to {user.name}")
        else:
            print("Cannot check out book. Either user or book is invalid, or book is not available.")

    def check_in_book(self, book_isbn):
        """
        Checks in a book and updates the book availability in books.json.
        """
        book = self.book_manager.get_book_by_isbn(book_isbn)

        if book and not book.is_available():
            book.check_in()
            self.book_manager.books[book_isbn] = book
            self.book_manager.storage.save_data(self.book_manager.books)
            print(f"Book '{book.title}' checked in.")
        else:
            print("Cannot check in book. Book is either invalid or already checked in.")
