import random
from storage.file_storage import FileStorage


class GuessGame:
    def __init__(self):
        self.storage = FileStorage("scores.json")

    def play(self):
        print("\n Guess Number Game (1-50)")

        number = random.randint(1, 50)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Enter valid number!")
                continue

            attempts += 1

            if guess > number:
                print("Too high!")

            elif guess < number:
                print("Too low!")

            else:
                print(" Correct!")

                score = max(1, 10 - attempts)

                scores = self.storage.load()
                scores.append({"score": score})

                self.storage.save(scores)

                print(f" Your score: {score}")
                break