# This is a deliberately poorly implemented main script for a Library Management System.

# import book_management
# import user_management
# import checkout_management

# def main_menu():
#     print("\nLibrary Management System")
#     print("1. Add Book")
#     print("2. List Books")
#     print("3. Add User")
#     print("4. Checkout Book")
#     print("5. Exit")
#     choice = input("Enter choice: ")
#     return choice

# def main():
#     while True:
#         choice = main_menu()
#         if choice == '1':
#             title = input("Enter title: ")
#             author = input("Enter author: ")
#             isbn = input("Enter ISBN: ")
#             book_management.add_book(title, author, isbn)
#             print("Book added.")
#         elif choice == '2':
#             book_management.list_books()
#         elif choice == '3':
#             name = input("Enter user name: ")
#             user_id = input("Enter user ID: ")
#             user_management.add_user(name, user_id)
#             print("User added.")
#         elif choice == '4':
#             user_id = input("Enter user ID: ")
#             isbn = input("Enter ISBN of the book to checkout: ")
#             checkout_management.checkout_book(user_id, isbn)
#             print("Book checked out.")
#         elif choice == '5':
#             print("Exiting.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()



from book import BookManager
from user import UserManager
from check import CheckManager

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    check_manager = CheckManager(book_manager, user_manager)

    while True:
        print("````````````````````````````````````````````````````````````````````````")
        print("Library Management System")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_manager.manage_books()
        elif choice == '2':
            user_manager.manage_users()
        elif choice == '3':
            user_id = input("Enter user ID: ")
            book_isbn = input("Enter book ISBN: ")
            check_manager.check_out_book(user_id, book_isbn)
        elif choice == '4':
            book_isbn = input("Enter book ISBN: ")
            check_manager.check_in_book(book_isbn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose valid input from the list.")

if __name__ == "__main__":
    main()
