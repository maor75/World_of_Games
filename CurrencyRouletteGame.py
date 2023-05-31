import requests
from bs4 import BeautifulSoup
import random
import re


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = random.randint(1, 100)

    def get_money_interval(self):
        URL = "https://www.globes.co.il/portal/instrument.aspx?InstrumentID=10463"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="bgLastDeal")
        num = re.findall(r'\d+\.\d+', results.text)[0]
        a = float(num)
        type(a)
        interval =(a * self.difficulty)
        return interval

    def get_guess_from_user(self):
        while True:
            try:
                guess = float(input(f"Guess the value of {self.secret_number}$ in ILS (to two decimal places): "))
                break
            except ValueError:
                print("Invalid input, please enter a number")
        return guess

    def play(self):
        interval = self.get_money_interval()
        guess = self.get_guess_from_user()
        if interval <= guess <= interval:
            print(f"Congratulations! Your guess of {guess} ILS is correct")
            return True
        else:
            print(f"Sorry, the correct answer was {interval} ILS")
            return False
