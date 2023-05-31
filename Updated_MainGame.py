from GuessGame import GuessGame
from MainScores import app
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import ScoreManager


def load_game(user_won=None):
    global game
    print("Please choose a game to play:")
    print("1. Memory Game")
    print("2. Guess Game")
    print("3. Currency Roulette")

    while True:
        try:
            game_choice = int(input("Enter your choice (1-3): "))
            if game_choice < 1 or game_choice > 3:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid choice (1-3).")

    while True:
        try:
            difficulty = int(input("choose game difficulty:1,2,3,4,5 ( 1 = easy, 5 = hard ):"))
            if difficulty < 1 or difficulty > 5:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid difficulty level (1-5).")

    if game_choice == 1:
        game = MemoryGame(difficulty)
    elif game_choice == 2:
        game = GuessGame(difficulty)
    elif game_choice == 3:
        print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
        game = CurrencyRouletteGame(difficulty)
    game.play()

    if user_won:
        ScoreManager.add_score(difficulty)
    if __name__ == '__main__':
        app.run()



