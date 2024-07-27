# library_management

This repository is designed for a library management system which will handle below functionalities 
1. Manage books
  - Add a book (title, author and ISBN)
  - Update a book (Look up an existing book by ISBN and update it's title or author)
  - Delete a book
  - List all books
  - Search a book (by title, author and ISBN)
2. Manage users
  - Add a user (name, user ID)
  - Update a user (Look up an existing user by ID and update name)
  - Delete a user
  - List all users
  - Search a user (by name and ID)
3. Check out book
  - Check out an available book to a user
4. Check in book
  - Check in a book and make it available

## Instructions to run 

1. git  clone the repository
```
https://github.com/manikamakam/library_management.git
```
2. Go into the directory
```
cd library_management
```
3. Run the main.py
```
python3 main.py
```
You will be presented a menu with above functionalities, provide the required inputs.

4. All the books added are stored in "books.json" and all the users are stored in "users.json". Sample json files are provided in the repository. If needed, can delete these files and run main.py. 

## Testing 
1. All unit cases are in the "unit_tests" folder.
2. Instructions to run
```
export PYTHONPATH = "/path/to/library_management"
python3 unit_tests/test_book_manager.py
python3 unit_tests/test_check_manager.py
python3 unit_tests/test_check_manager.py
python3 unit_tests/test_storage.py
```

3. All unit tests will be passed which verifies all functionalities

## Overview of code
Code is structured in a way that it is modular, easy to add functionalities, easy to maintain and easy for understanding. 
1. book.py provides a BookManager class that has all the functions to manage the books and provides all functionalities like add, update, list, delete and search books. 
2. user.py provide a UserManager class that has all the functions to manage the users and provides all functionalities like add, update, list, delete and search users. 
3. models.py has a Book class and User class which represent a book and user respectively in the library.
4. check.py handles the functionalities of checking in and checking out the books and tracks the availablity of books.
5. storage.py provides functionality to store and load the data from books.json and users.json
6. main.py is the main fucntion to run which provides a menu of all functionalities and invokes the necessary function to activate the desried action.

In future, the code could be extended to add more details for book like check out date and time, location of book in the library. More details could be added to user as well like late fees, date of birth etc. More functionalities could also be added accordingly. 

