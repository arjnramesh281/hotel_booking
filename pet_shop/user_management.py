users = {}

def register_user(username, password):
    if username in users:
        raise Exception("Username already exists.")
    users[username] = password
    return "User registered successfully."

def login_user(username, password):
    if username not in users:
        raise Exception("User does not exist.")
    if users[username] == password:
        return "Login successful."
    else:
        raise Exception("Invalid credentials.")
