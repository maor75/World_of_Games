import random
import time


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_sequence = self.generate_sequence()

    def generate_sequence(self):
        secret_sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        return secret_sequence

    def get_list_from_user(self):
        user_sequence = []
        for i in range(self.difficulty):
            while True:
                try:
                    guess = int(input(f"Enter number {i+1}: "))
                    if guess < 1 or guess > 101:
                        print("Please enter a number between 1 and 101.")
                    else:
                        user_sequence.append(guess)
                        break
                except ValueError:
                    print("Please enter a valid number.")
        return user_sequence

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        print(f"Remember the following {self.difficulty} numbers for 0.7 seconds:")
        print(self.secret_sequence)
        time.sleep(0.7)
        print("\n" * 100)
        user_sequence = self.get_list_from_user()
        if self.is_list_equal(self.secret_sequence, user_sequence):
            print("Congratulations! You remembered all the numbers.")
            return True
        else:
            print("Sorry, you didn't remember all the numbers.")
            return False
