import hashlib
from storage.file_storage import FileStorage


class AuthManager:
    def __init__(self):
        self.storage = FileStorage("users.json")
        self.users = self.storage.load()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password, role="user"):
        if not username or not password:
            return False

        for user in self.users:
            if user["username"] == username:
                return False

        self.users.append({
            "username": username,
            "password": self.hash_password(password),
            "role": role
        })

        self.storage.save(self.users)
        return True

    def login(self, username, password):
        hashed = self.hash_password(password)

        for user in self.users:
            if user["username"] == username and user["password"] == hashed:
                return user

        return None