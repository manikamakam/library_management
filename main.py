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
