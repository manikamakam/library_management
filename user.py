# from models import User
# from storage import Storage

# class UserManager:
#     def __init__(self):
#         self.storage = Storage("users.json")
#         self.users = self.storage.load_data(User)

#     def manage_users(self):
#         while True:
#             print("````````````````````````````````````````````````````````````````````````")
#             print("User Management")
#             print("1. Add User")
#             print("2. Update User")
#             print("3. Delete User")
#             print("4. List Users")
#             print("5. Search User")
#             print("6. Back")
#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 name = input("Enter user name: ")
#                 user_id = input("Enter user ID: ")
#                 self.add_user(name,user_id)
#             elif choice == '2':
#                 self.update_user()
#             elif choice == '3':
#                 self.delete_user()
#             elif choice == '4':
#                 self.list_users()
#             elif choice == '5':
#                 self.search_user()
#             elif choice == '6':
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

#     def add_user(self, name, user_id):
#         if user_id in self.users:
#             print("User ID already exists. Please choose a different ID.")
#             return
#         user = User(name, user_id)
#         self.users[user_id] = user
#         self.storage.save_data(self.users)
#         print("User added successfully.")

#     def update_user(self):
#         user_id = input("Enter user ID to update: ")
#         user = self.get_user_by_id(user_id)

#         if user:
#             name = input(f"Enter new name for {user.name} (leave blank to keep current): ")
#             if name:
#                 user.name = name
#             self.users[user_id] = user
#             self.storage.save_data(self.users)
#             print("User updated successfully.")
#         else:
#             print("User not found.")

#     def delete_user(self):
#         user_id = input("Enter user ID to delete: ")
#         if user_id in self.users:
#             del self.users[user_id]
#             self.storage.save_data(self.users)
#             print("User deleted successfully.")
#         else:
#             print("User not found.")

#     def list_users(self):
#         for user in self.users.values():
#             print(user)

#     def search_user(self):
#         search_term = input("Enter user ID or name to search: ")
#         user = self.get_user_by_id(search_term)
#         if user:
#             print(user)
#         else:
#             users_by_name = self.get_users_by_name(search_term)
#             if users_by_name:
#                 for user in users_by_name:
#                     print(user)
#             else:
#                 print("User not found.")

#     def get_user_by_id(self, user_id):
#         return self.users.get(user_id)

#     def get_users_by_name(self, name):
#         return [user for user in self.users.values() if user.name.lower() == name.lower()]

from models import User
from storage import Storage

class UserManager:
    def __init__(self):
        self.storage = Storage("users.json")
        self.users = self.storage.load_data(User)

    def manage_users(self):
        while True:
            print("````````````````````````````````````````````````````````````````````````")
            print("User Management")
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. List Users")
            print("5. Search User")
            print("6. Back")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.add_user(name, user_id)
            elif choice == '2':
                user_id = input("Enter user ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                self.update_user(user_id, name)
            elif choice == '3':
                user_id = input("Enter user ID to delete: ")
                self.delete_user(user_id)
            elif choice == '4':
                self.list_users()
            elif choice == '5':
                search_term = input("Enter user ID or name to search: ")
                self.search_user(search_term)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_user(self, name, user_id):
        if user_id in self.users:
            print("User with this ID already exists. Please choose a different ID.")
            return
        user = User(name, user_id)
        self.users[user_id] = user
        self.storage.save_data(self.users)
        print("User added successfully.")

    def update_user(self, user_id, name=None):
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            self.users[user_id] = user
            self.storage.save_data(self.users)
            print("User updated successfully.")
        else:
            print("User not found.")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            self.storage.save_data(self.users)
            print("User deleted successfully.")
        else:
            print("User not found.")

    def list_users(self):
        for user in self.users.values():
            print(user)

    def search_user(self, search_term):
        user = self.get_user_by_id(search_term)
        if user:
            print(user)
        else:
            users_by_name = self.get_users_by_name(search_term)
            if users_by_name:
                for user in users_by_name:
                    print(user)
            else:
                print("User not found.")

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)

    def get_users_by_name(self, name):
        return [user for user in self.users.values() if user.name.lower() == name.lower()]
