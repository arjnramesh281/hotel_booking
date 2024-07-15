admin_credentials = {"admin": "admin123"}

def login_admin(username, password):
    if username in admin_credentials and admin_credentials[username] == password:
        return "Admin login successful."
    else:
        raise Exception("Invalid admin credentials.")
