class UserManagement:
    def __init__(self):
        self.users = {}

    def register(self):
        while True:
            username = input("Enter a username: ")
            if username in self.users:
                print("Username already exists. Please choose a different username.\n")
            else:
                password = input("Enter a password: ")
                self.users[username] = password
                print("User registered successfully!\n")
                break

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.users and self.users[username] == password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid username or password. Please try again.\n")
            return False
