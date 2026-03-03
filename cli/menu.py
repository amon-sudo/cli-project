from game.guess import GuessGame


class Menu:
    def start(self):
        game = GuessGame()

        while True:
            print("\n CLI GAME ")
            print("1. Play Guess Game")
            print("2. Exit")

            choice = input("Choice: ")

            if choice == "1":
                game.play()

            elif choice == "2":
                print("Goodbye!")
                break