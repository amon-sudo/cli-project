from auth.auth_manager import AuthManager
from game.guess import GuessGame


class Menu:
    def __init__(self):
        self.auth = AuthManager()
        self.current_user = None

    def start(self):
        while True:
            print("\n===== CLI GAME SYSTEM =====")
            print("1. Register")
            print("2. Login")
            print("3. Play Guess Game")
            print("4. Logout")
            print("5. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.register_ui()

            elif choice == "2":
                self.login_ui()

            elif choice == "3":
                self.play_game()

            elif choice == "4":
                self.logout()

            elif choice == "5":
                break

    def register_ui(self):
        username = input("Username: ")
        password = input("Password: ")

        if self.auth.register(username, password):
            print("Registration successful!")
        else:
            print("Registration failed!")

    def login_ui(self):
        username = input("Username: ")
        password = input("Password: ")

        user = self.auth.login(username, password)

        if user:
            self.current_user = user
            print("Login successful!")
        else:
            print("Invalid credentials!")

    def play_game(self):
        if not self.current_user:
            print("Please login first!")
            return

        game = GuessGame()
        game.play()

    def logout(self):
        self.current_user = None
        print("Logged out!")