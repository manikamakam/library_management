class Book:
    def __init__(self, title, author, isbn, checked_out_to=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out_to = checked_out_to

    def is_available(self):
        return self.checked_out_to is None

    def check_out(self, user_id):
        self.checked_out_to = user_id

    def check_in(self):
        self.checked_out_to = None

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'checked_out_to': self.checked_out_to
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'], data['isbn'], data.get('checked_out_to'))

    def __repr__(self):
        status = "Available" if self.is_available() else f"Checked out to {self.checked_out_to}"
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status})"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            'name': self.name,
            'user_id': self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['user_id'])

    def __repr__(self):
        return f"User(Name: {self.name}, ID: {self.user_id})"
