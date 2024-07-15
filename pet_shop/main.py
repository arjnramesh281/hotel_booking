import user_management
import admin_management
import admin_menu
import user_menu

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                print(user_management.register_user(username, password))
            except Exception as e:
                print(e)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                print(user_management.login_user(username, password))
                user_menu.user_menu(username)
            except Exception as e:
                print(e)
        elif choice == "3":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            try:
                print(admin_management.login_admin(username, password))
                admin_menu.admin_menu()
            except Exception as e:
                print(e)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
