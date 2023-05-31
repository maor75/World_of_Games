def welcome ():
  name =input("Enter your name:")
  print(f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")

def load_game():
    game = ["1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
    "2. Guess Game - guess a number and see if you chose like the computer",
    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"]
    for i in range (len(game)):
        print(game[i])

    the_number = int(input("Enter the number of the game you want to play 1, 2 , 3:"))
    print("you choose the number ", the_number)
    if the_number == 1:
        print("you choose the game Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back" )
    if the_number == 2:
        print("you choose the game Guess Game - Guess Game - guess a number and see if you chose like the computer")
    if the_number == 3:
        print("you choose the game Currency Roulette - Currency Roulette - try and guess the value of a random amount of USD in ILS ")

def game_difficulty():
    difficulty = int(input("choose game difficulty:1,2,3,4,5( 1 = easy 5 = hard ):"))
    print(difficulty)

