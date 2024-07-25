class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, title, author, isbn, checked_out_to=None):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            checked_out_to (str, optional): User ID of the person who checked out the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out_to = checked_out_to

    def is_available(self):
        """
        Checks if the book is available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return self.checked_out_to is None

    def check_out(self, user_id):
        """
        Marks the book as checked out to a user.

        Args:
            user_id (str): The ID of the user checking out the book.
        """
        self.checked_out_to = user_id

    def check_in(self):
        """
        Marks the book as returned.
        """
        self.checked_out_to = None

    def to_dict(self):
        """
        Converts the Book instance to a dictionary.

        Returns:
            dict: Dictionary representation of the Book.
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'checked_out_to': self.checked_out_to
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Book instance from a dictionary.

        Args:
            data (dict): Dictionary with book data.

        Returns:
            Book: A Book instance.
        """
        return cls(data['title'], data['author'], data['isbn'], data.get('checked_out_to'))

    def __repr__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: String representation of the book.
        """

        status = "Available" if self.is_available() else f"Checked out to {self.checked_out_to}"
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status})"

class User:
    """
    Represents a user in the library.
    """
    def __init__(self, name, user_id):
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """
        Converts the User instance to a dictionary.

        Returns:
            dict: Dictionary representation of the User.
        """
        return {
            'name': self.name,
            'user_id': self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a User instance from a dictionary.

        Args:
            data (dict): Dictionary with user data.

        Returns:
            User: A User instance.
        """
        return cls(data['name'], data['user_id'])

    def __repr__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: String representation of the user.
        """
        return f"User(Name: {self.name}, ID: {self.user_id})"
