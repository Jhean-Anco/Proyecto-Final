class User:
    def __init__(self, dni, username, password, email=None, phone=None, age=None):
        self.dni = dni
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age
