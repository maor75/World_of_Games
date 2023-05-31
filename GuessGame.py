import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print("Invalid input, please enter a number between 1 and {self.difficulty}")
            except ValueError:
                print("Invalid input, please enter a number")

    def compare_results(self, guess):
        if guess == self.secret_number:
            print("Congratulations, you guessed the secret number!")
            return True
        else:
            print(f"Sorry, the secret number was {self.secret_number}")
            return False

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        return self.compare_results(guess)
